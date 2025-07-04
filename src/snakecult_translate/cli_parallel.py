#!/usr/bin/env python3
"""
Parallel translation CLI using shared core functionality.
Fast, synchronous, multi-threaded translator.
"""

import argparse
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from threading import Lock
from typing import List, Tuple

from .core import translate_file
from .utils import discover_markdown_files, load_env_and_key, log


# Thread-safe progress tracking
progress_lock = Lock()
progress = {
    "completed": 0,
    "failed": 0,
    "skipped": 0,
    "total": 0,
}


def update_progress(kind: str) -> None:
    with progress_lock:
        progress[kind] += 1
        done = progress["completed"] + progress["failed"] + progress["skipped"]
        total = progress["total"]
        print(f"Progress: {done}/{total} | ✅ {progress['completed']}  ❌ {progress['failed']}  ⏭ {progress['skipped']}", end="\r")


def translate_worker(args: Tuple[Path, Path, str, str, str, argparse.Namespace]):
    """Wrapper around translate_file for ThreadPoolExecutor."""
    src_path, dst_path, lang, model, api_key, cli_args = args

    # Skip logic handled here to avoid spinning up translate_file for nothing
    if dst_path.exists() and not cli_args.overwrite:
        update_progress("skipped")
        return True

    try:
        success = translate_file(
            src_path=src_path,
            dst_path=dst_path,
            target_lang=lang,
            model=model,
            api_key=api_key,
            web_format=cli_args.web_format,
            temperature=cli_args.temperature,
            chunk=cli_args.chunk,
            chunk_size_chars=cli_args.chunk_size_chars,
            auto_model=cli_args.auto_model,
        )
        update_progress("completed" if success else "failed")
        return success
    except Exception as exc:
        log(f"Exception while translating {src_path}: {exc}", prefix="ERROR: ")
        update_progress("failed")
        return False


def build_tasks(md_files: List[Path], cli_args: argparse.Namespace) -> List[Tuple[Path, Path, str, str, str, argparse.Namespace]]:
    """Return a list of task tuples for the executor."""
    tasks = []

    for src_path in md_files:
        # Derive destination path preserving sub-directories relative to src_root
        try:
            rel_path = src_path.relative_to(cli_args.src_root)
        except ValueError:
            # src_path is outside src_root – place file directly in dst_root
            rel_path = Path(src_path.name)

        dst_path = Path(cli_args.dst_root) / rel_path
        tasks.append((src_path, dst_path, cli_args.lang, cli_args.model, cli_args.api_key, cli_args))

    return tasks


def main():
    parser = argparse.ArgumentParser(description="Parallel batch translation")
    
    parser.add_argument("--lang", default="es", help="Target language code (default: es)")
    parser.add_argument("--src-root", default="content", type=Path, help="Root of source content tree")
    parser.add_argument("--dst-root", default=None, type=Path, help="Root for translated content (defaults to content/<lang>)")
    parser.add_argument("--model", default="gpt-4o", help="OpenAI model (default: gpt-4o)")
    parser.add_argument("--api-key", help="OpenAI API key (or set OPENAI_API_KEY env var)")

    parser.add_argument("--workers", type=int, default=3, help="Parallel worker threads (default: 3)")
    parser.add_argument("--dry-run", action="store_true", help="List what would be done and exit")
    parser.add_argument("--limit", type=int, help="Translate only the first N discovered files (size-asc)")
    parser.add_argument("--overwrite", action="store_true", help="Re-translate files even if output already exists")

    # Passthrough flags to translate_file
    parser.add_argument("--web-format", action="store_true", help="Ask translator to tweak long paragraphs for web readability")
    parser.add_argument("--temperature", type=float, default=0.2, help="Sampling temperature (some models ignore)")
    parser.add_argument("--chunk", action="store_true", help="Enable automatic chunking for very long docs")
    parser.add_argument("--chunk-size-chars", type=int, default=25_000, help="Chunk size when --chunk is set")
    parser.add_argument("--no-auto-model", dest="auto_model", action="store_false", help="Disable auto model switch for long chunks")
    parser.set_defaults(auto_model=True)

    args = parser.parse_args()

    # Determine default dst_root if not provided
    if args.dst_root is None:
        args.dst_root = Path("content") / args.lang

    # Resolve API key
    args.api_key = args.api_key or load_env_and_key()
    if not args.api_key and not args.dry_run:
        print("Error: OpenAI API key required. Use --api-key or set OPENAI_API_KEY environment variable.")
        sys.exit(1)

    log(f"Scanning for Markdown files under {args.src_root} …")
    all_md = discover_markdown_files(args.src_root)

    # Remove those already inside dst_root (so we don't double-translate Spanish → Spanish etc.)
    all_md = [p for p in all_md if args.dst_root not in p.parents]

    # Sort by file size (ascending) so --limit n picks the shortest posts
    all_md.sort(key=lambda p: p.stat().st_size)

    if args.limit:
        all_md = all_md[: args.limit]

    tasks = build_tasks(all_md, args)
    progress["total"] = len(tasks)

    if not tasks:
        log("No source files found – nothing to do.")
        return

    log(f"Planned translations: {len(tasks)} file(s)")

    if args.dry_run:
        for src, dst, *_ in tasks:
            status = "OVERWRITE" if dst.exists() else "NEW"
            print(f"  {src} -> {dst} [{status}]")
        print("\nDry-run complete.")
        return

    # Interactive safety prompt for full runs
    if not args.overwrite:
        response = input(f"Proceed translating {len(tasks)} file(s)? (y/N): ")
        if response.strip().lower() != "y":
            print("Aborted.")
            return

    log("Starting parallel translation …")
    start_ts = time.time()

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futs = [pool.submit(translate_worker, t) for t in tasks]

        # Force retrieval so exceptions propagate
        for fut in as_completed(futs):
            fut.result()

    duration = time.time() - start_ts

    print("\n\n======= Summary =======")
    print(f"✅  Success : {progress['completed']}")
    print(f"❌  Failed  : {progress['failed']}")
    print(f"⏭  Skipped : {progress['skipped']}")
    print(f"📄  Total   : {progress['total']}")
    print(f"⏱  Time    : {duration:.1f} s")

    if progress["failed"]:
        sys.exit(1)


if __name__ == "__main__":
    main() 