#!/usr/bin/env python3
"""
Batch async translation CLI using OpenAI Batch API for 50% discount.
"""

import argparse
import json
import sys
import tempfile
import time
from pathlib import Path
from typing import List, Dict, Any

import frontmatter
from openai import OpenAI

from .core import create_translated_frontmatter, translate_text, translate_frontmatter_block
from .models import supports_batch_api
from .prompts import get_system_prompt
from .utils import discover_markdown_files, load_env_and_key, split_text_into_chunks


def build_request_obj(content: str, model: str, target_lang: str, temperature: float, web_format: bool) -> Dict[str, Any]:
    """Return dict representing one chat/completions request."""
    system_prompt = get_system_prompt(target_lang, web_format)
    
    req: Dict[str, Any] = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": content},
        ],
    }
    
    # Clamp temperature inside [0,1] and add if valid
    if 0.0 <= temperature <= 1.0:
        req["temperature"] = temperature
    
    return req


def poll_batch(client: OpenAI, batch_id: str, interval: int = 30):
    """Poll batch status until completion."""
    while True:
        batch = client.batches.retrieve(batch_id)
        status = batch.status  # "in_progress", "completed", "failed"
        print(f"[poll] Batch {batch_id} → {status}")
        if status in {"completed", "failed"}:
            return batch
        time.sleep(interval)


def assemble_outputs(outputs_jsonl: str, args, mapping_path: Path):
    """Assemble batch outputs into translated Markdown files."""
    with open(mapping_path, "r", encoding="utf-8") as f:
        mapping = json.load(f)

    api_key = load_env_and_key()
    client = OpenAI(api_key=api_key)

    # Process each output line
    print(f"Processing {len(outputs_jsonl.strip().splitlines())} results …")
    
    # Create mapping dict for faster lookup
    mapping_dict = {item["custom_id"]: item for item in mapping}
    
    # Group results by file to handle chunks
    file_results = {}  # file_idx -> {chunks: [], metadata: {}}
    
    for line in outputs_jsonl.strip().splitlines():
        result = json.loads(line)
        
        # Handle potential API errors in batch results
        if "error" in result and result["error"] is not None:
            print(f"❌ Error in batch result {result.get('custom_id', 'unknown')}: {result['error']}")
            continue
            
        # Extract from batch response format
        if "response" in result and "body" in result["response"]:
            response_body = result["response"]["body"]
            translated_content = response_body["choices"][0]["message"]["content"].strip()
        else:
            print(f"❌ Unexpected response format for {result.get('custom_id', 'unknown')}: {result}")
            continue

        mapping_item = mapping_dict[result["custom_id"]]
        file_idx = mapping_item["file_idx"]
        
        if file_idx not in file_results:
            file_results[file_idx] = {
                "chunks": [],
                "metadata": mapping_item
            }
        
        if mapping_item.get("is_chunk", False):
            # Store chunk with its index for proper ordering
            file_results[file_idx]["chunks"].append({
                "chunk_idx": mapping_item["chunk_idx"],
                "content": translated_content
            })
        else:
            # Single file, no chunks
            file_results[file_idx]["chunks"].append({
                "chunk_idx": 0,
                "content": translated_content
            })

    # Now assemble each file
    for file_idx, file_data in file_results.items():
        mapping_item = file_data["metadata"]
        src_path = Path(mapping_item["src"])
        dst_path = Path(mapping_item["dst"])

        # Sort chunks by chunk_idx and combine
        chunks = sorted(file_data["chunks"], key=lambda x: x["chunk_idx"])
        
        if len(chunks) > 1:
            # Multiple chunks - combine with chunk break markers
            translated_content = "\n\n<!-- CHUNK BREAK -->\n\n".join(chunk["content"] for chunk in chunks)
            print(f"Assembled {len(chunks)} chunks for {src_path.name}")
        else:
            # Single chunk
            translated_content = chunks[0]["content"]

        # Reload source to fetch metadata / title
        post = frontmatter.load(src_path)
        translated_title = post.metadata.get("title", "")
        
        if translated_title:
            # Cheap synchronous call for title only (negligible cost)
            translated_title = translate_text(
                client=client,
                text=translated_title,
                target_lang=args.lang,
                model=args.model,
                web_format=args.web_format,
                temperature=args.temperature
            )

        # Build translated front matter
        translated_meta = create_translated_frontmatter(post.metadata, args.lang, args.model)
        if translated_title:
            translated_meta["title"] = translated_title

        # Translate additional front-matter fields (description, keywords, tags, etc.)
        translated_meta = translate_frontmatter_block(
            client=client,
            frontmatter_dict=translated_meta,
            target_lang=args.lang,
            model=args.model,
            web_format=args.web_format,
            temperature=args.temperature,
        )

        translated_post = frontmatter.Post(translated_content, **translated_meta)
        dst_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(dst_path, "w", encoding="utf-8") as f:
            f.write(frontmatter.dumps(translated_post))
        print(f"Saved  → {dst_path}")


def main():
    parser = argparse.ArgumentParser(description="OpenAI Batch API translator (async)")

    parser.add_argument("--lang", default="es", help="Target language (default: es)")
    parser.add_argument("--src-root", default="content", type=Path, help="Root dir with English Markdown")
    parser.add_argument("--dst-root", type=Path, help="Destination root for translations (default: content/<lang>)")
    parser.add_argument("--model", default="gpt-4o", help="OpenAI model (batch pricing supports gpt-4o, gpt-3.5 etc.)")
    parser.add_argument("--temperature", type=float, default=0.2)
    parser.add_argument("--limit", type=int, help="Translate only first N (shortest) files")
    parser.add_argument("--web-format", action="store_true", help="Apply web-friendly formatting")

    parser.add_argument("--batch-id", help="Existing Batch ID to resume / download outputs")
    parser.add_argument("--resume", action="store_true", help="Resume mode: download & assemble outputs of existing batch id")
    parser.add_argument("--no-wait", dest="wait", action="store_false", help="Submit job and exit without waiting")
    parser.add_argument("--chunk", action="store_true", help="Enable automatic chunking for long files")
    parser.add_argument("--chunk-size-chars", type=int, default=25000, help="Chunk size in characters (default: 25000)")

    args = parser.parse_args()

    if args.dst_root is None:
        args.dst_root = Path("content") / args.lang

    api_key = load_env_and_key()
    if not api_key:
        print("OPENAI_API_KEY not found – add to .env.translation or env var.")
        sys.exit(1)

    # Check if model supports batch API
    if not supports_batch_api(args.model):
        print(f"⚠️  Model '{args.model}' does not support Batch API. Consider using gpt-4o or gpt-3.5-turbo.")
        response = input("Continue anyway? (y/N): ")
        if response.strip().lower() != "y":
            sys.exit(1)

    client = OpenAI(api_key=api_key)

    if args.resume:
        if not args.batch_id:
            print("--resume requires --batch-id <id>")
            sys.exit(1)
        batch = poll_batch(client, args.batch_id, interval=30)
        if batch.status != "completed":
            print(f"Batch not completed. Status: {batch.status}")
            if hasattr(batch, 'errors') and batch.errors:
                print(f"Errors: {batch.errors}")
            if hasattr(batch, 'error_file_id') and batch.error_file_id:
                print(f"Error file ID: {batch.error_file_id}")
                try:
                    error_content = client.files.content(batch.error_file_id)
                    print(f"Error details: {error_content.decode()}")
                except Exception as e:
                    print(f"Could not fetch error details: {e}")
            sys.exit(1)
        output_file_id = batch.output_file_id
        print(f"Downloading output file {output_file_id} …")
        output_bytes = client.files.content(output_file_id)
        mapping_path = Path("batch_work") / f"batch_{args.batch_id}_mapping.json"
        assemble_outputs(output_bytes.content.decode(), args, mapping_path)
        print("✅ All translations written.")
        return

    # ---------------- New submission path ----------------
    all_md = discover_markdown_files(args.src_root)
    
    # Remove those already inside dst_root
    all_md = [p for p in all_md if args.dst_root not in p.parents]
    
    # Sort by size and limit
    all_md.sort(key=lambda p: p.stat().st_size, reverse=True)  # Largest first for chunking tests
    if args.limit:
        all_md = all_md[: args.limit]

    print(f"Will translate {len(all_md)} Markdown files using Batch API …")

    # Build JSONL and mapping
    mapping: List[Dict[str, str]] = []
    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".jsonl") as tmp:
        request_id = 0
        for file_idx, src_path in enumerate(all_md):
            with open(src_path, "r", encoding="utf-8") as f:
                post = frontmatter.load(f)
            content = post.content
            
            # Destination path mirrors structure under dst_root
            try:
                rel = src_path.relative_to(args.src_root)
            except ValueError:
                rel = Path(src_path.name)
            dst_path = args.dst_root / rel
            
            # Check if chunking is needed
            if args.chunk and len(content) > args.chunk_size_chars:
                print(f"Chunking {src_path.name} ({len(content):,} chars) into chunks of {args.chunk_size_chars:,} chars")
                chunks = split_text_into_chunks(content, args.chunk_size_chars)
                
                for chunk_idx, chunk in enumerate(chunks):
                    batch_req = {
                        "custom_id": f"translate-{request_id}",
                        "method": "POST",
                        "url": "/v1/chat/completions",
                        "body": build_request_obj(chunk, args.model, args.lang, args.temperature, args.web_format)
                    }
                    tmp.write(json.dumps(batch_req, ensure_ascii=False) + "\n")
                    
                    mapping.append({
                        "custom_id": f"translate-{request_id}",
                        "src": str(src_path), 
                        "dst": str(dst_path),
                        "file_idx": file_idx,
                        "chunk_idx": chunk_idx,
                        "total_chunks": len(chunks),
                        "is_chunk": True
                    })
                    request_id += 1
            else:
                # Single file, no chunking
                batch_req = {
                    "custom_id": f"translate-{request_id}",
                    "method": "POST",
                    "url": "/v1/chat/completions",
                    "body": build_request_obj(content, args.model, args.lang, args.temperature, args.web_format)
                }
                tmp.write(json.dumps(batch_req, ensure_ascii=False) + "\n")
                
                mapping.append({
                    "custom_id": f"translate-{request_id}",
                    "src": str(src_path), 
                    "dst": str(dst_path),
                    "file_idx": file_idx,
                    "is_chunk": False
                })
                request_id += 1
        requests_path = tmp.name

    print(f"JSONL with {len(mapping)} requests written to {requests_path}")

    # Upload file for batch
    uploaded = client.files.create(file=open(requests_path, "rb"), purpose="batch")
    print(f"Uploaded file id: {uploaded.id}")

    # Create 24h batch job
    batch = client.batches.create(
        input_file_id=uploaded.id,
        endpoint="/v1/chat/completions",
        completion_window="24h",
    )
    print(f"Batch submitted. id={batch.id}")

    # Store mapping locally to resume later
    batch_work_dir = Path("batch_work")
    batch_work_dir.mkdir(parents=True, exist_ok=True)
    mapping_file = batch_work_dir / f"batch_{batch.id}_mapping.json"
    with open(mapping_file, "w", encoding="utf-8") as f:
        json.dump(mapping, f, ensure_ascii=False, indent=2)
    print(f"Mapping saved → {mapping_file}")

    if not args.wait:
        print("🏃‍♂️ Not waiting for completion (--no-wait). You can resume later with --batch-id.")
        return

    # Wait for completion
    batch = poll_batch(client, batch.id, interval=60)
    if batch.status != "completed":
        print("Batch failed or cancelled.")
        sys.exit(1)

    # Download & assemble
    output_file_id = batch.output_file_id
    print(f"Downloading output file {output_file_id} …")
    output_bytes = client.files.content(output_file_id)
    assemble_outputs(output_bytes.content.decode(), args, mapping_file)
    print("✅ All translations written.")


if __name__ == "__main__":
    main() 