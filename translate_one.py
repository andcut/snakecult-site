#!/usr/bin/env python3
"""
Single-file translation script for Hugo multilingual site.
Translates English markdown posts to Spanish using OpenAI o3 model.
"""

import os
import sys
import argparse
import frontmatter
import yaml
from pathlib import Path
from openai import OpenAI
import tiktoken
import time
import random
import datetime
from dotenv import load_dotenv
from typing import Optional

# Load variables from .env.translation (if present) and from .env.
# These calls return False silently if the file doesn't exist, which is fine.
load_dotenv(dotenv_path=".env.translation", override=False)
# Also look for a generic .env
load_dotenv(override=False)

def count_tokens(text, model="gpt-4"):
    """Estimate token count for text using tiktoken."""
    try:
        encoding = tiktoken.encoding_for_model(model)
        return len(encoding.encode(text))
    except:
        # Fallback approximation if tiktoken fails
        return len(text.split()) * 1.3

def translate_text(client, text, target_lang="es", model="o3", web_format: bool = False, temperature: Optional[float] = None):
    """Translate text using OpenAI API.

    If ``web_format`` is True, use a prompt that additionally breaks up long blocks of text and enriches the Markdown structure for web readability.
    """

    # Language- and style-specific system prompts
    base_prompt = """You are a professional Spanish translator specializing in academic and intellectual content.

Translate the following English text to Mexican Spanish.

MANDATORY GUIDELINES:
1. Do **NOT** omit, shorten, summarise, reorder, or otherwise alter ANY content. The Spanish output must contain every sentence and element present in the original.
2. Preserve all Markdown formatting exactly (headers, links, lists, code blocks, etc.).
3. Maintain the scholarly tone and technical terminology.
4. Keep proper nouns, citations, references, HTML tags, and shortcodes unchanged.

Return only the fully translated text with no additional commentary."""

    web_prompt = """You are a professional Spanish translator.

Translate the text below to accurate Mexican Spanish **without omitting, summarizing, or rearranging any content**.  Preserve *every* Markdown element (headers, links, lists, code, citations, shortcodes, HTML tags) exactly as in the original.

Additional formatting tweaks allowed ONLY when the source paragraph is longer than four sentences:
  • Break that long paragraph into two-to-three shorter paragraphs for mobile readability.
  • Optionally add limited inline emphasis (bold or italics) to highlight key terms; use this sparingly (a handful of times in the whole document).

Do not add new sub-headings, bullet lists, or summaries, and do not remove or change any information.  When in doubt, preserve the original structure.  Output only the translated Markdown text."""

    system_prompt = web_prompt if web_format else base_prompt
    
    try:
        kwargs = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text}
            ]
        }
        # Some models (e.g. o3) currently do not accept custom temperature values
        if temperature is not None:
            if model.startswith("o3") and abs(temperature - 1.0) > 1e-5:
                print(f"⚠️  Model '{model}' ignores non-default temperature; proceeding with default (1.0).")
            else:
                kwargs["temperature"] = temperature

        response = client.chat.completions.create(**kwargs)
        
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        print(f"Translation error: {e}")
        return None

def create_spanish_frontmatter(original_fm, target_lang="es", model_name="o3"):
    """Create Spanish frontmatter from English frontmatter."""
    spanish_fm = original_fm.copy()
    
    # Always set language
    spanish_fm['lang'] = target_lang
    # Record which model performed the translation
    spanish_fm['translation_model'] = model_name
    # Update last modification date to today (ISO-8601)
    spanish_fm['lastmod'] = datetime.date.today().isoformat()
    
    # Keep English slug for now (as discussed)
    # spanish_fm['slug'] stays the same
    
    # Keep other metadata unchanged (date, tags, etc.)
    return spanish_fm

def split_text_into_chunks(text: str, chunk_size_chars: int = 25000):
    """Split *text* into chunks not exceeding *chunk_size_chars* while trying to break on newline.
    Returns a list of chunk strings in order.
    """
    if len(text) <= chunk_size_chars:
        return [text]

    chunks = []
    start = 0
    length = len(text)
    while start < length:
        end = min(start + chunk_size_chars, length)
        # Try to break at last newline before the hard limit to avoid mid-word cuts
        if end < length:
            newline_index = text.rfind('\n', start, end)
            if newline_index != -1 and newline_index > start + int(0.5 * chunk_size_chars):
                end = newline_index + 1  # include the newline char
        chunks.append(text[start:end])
        start = end
    return chunks

def translate_file(src_path, dst_path, target_lang="es", model="o3", api_key=None, web_format: bool = False, temperature: Optional[float] = None, *, chunk: bool = False, chunk_size_chars: int = 25000, auto_model: bool = True):
    """Translate a single markdown file, optionally in chunks and with automatic model selection."""
    
    if not api_key:
        print("Error: OpenAI API key required. Set OPENAI_API_KEY environment variable.")
        return False
    
    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)
    
    # Read source file
    try:
        with open(src_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
    except Exception as e:
        print(f"Error reading {src_path}: {e}")
        return False
    
    print(f"Translating: {src_path}")
    
    # Estimate tokens
    content_tokens = count_tokens(post.content)
    title_tokens = count_tokens(post.metadata.get('title', ''))
    total_tokens = content_tokens + title_tokens
    
    print(f"Estimated tokens: {total_tokens:,}")
    
    # Translate title if present
    translated_title = post.metadata.get('title', '')
    if translated_title:
        print("Translating title...")
        translated_title = translate_text(client, translated_title, target_lang, model, web_format, temperature)
        if not translated_title:
            print("Failed to translate title")
            return False
    
    # Translate main content (with optional chunking)
    if not chunk:
        chosen_model = model
        if auto_model:
            estimated_tokens = count_tokens(post.content)
            if estimated_tokens > 24000:
                chosen_model = "gpt-4o-128k"
        print(f"Translating content using model: {chosen_model} ...")
        translated_content = translate_text(client, post.content, target_lang, chosen_model, web_format, temperature)
        if not translated_content:
            print("Failed to translate content")
            return False
    else:
        print("Chunking enabled – splitting content and translating each chunk…")
        chunks = split_text_into_chunks(post.content, chunk_size_chars)
        translated_chunks = []
        for idx, ch in enumerate(chunks, start=1):
            est_tokens = count_tokens(ch)
            chosen_model = model
            if auto_model and est_tokens > 24000:
                chosen_model = "gpt-4o-128k"
            print(f"  → Chunk {idx}/{len(chunks)} (approx {est_tokens:,} tokens) with model {chosen_model}")
            translated = translate_text(client, ch, target_lang, chosen_model, web_format, temperature)
            if not translated:
                print(f"Failed to translate chunk {idx}")
                return False
            translated_chunks.append(translated)
        # Join the chunks with clear delimiters (HTML comment so it won't show when rendered)
        translated_content = "\n\n<!-- CHUNK BREAK -->\n\n".join(translated_chunks)
    
    # Create Spanish frontmatter
    spanish_fm = create_spanish_frontmatter(post.metadata, target_lang, model)
    if translated_title:
        spanish_fm['title'] = translated_title
    
    # Create new post with translated content
    spanish_post = frontmatter.Post(translated_content, **spanish_fm)
    
    # Ensure destination directory exists
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write translated file
    try:
        with open(dst_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(spanish_post))
        print(f"Saved: {dst_path}")
        return True
    except Exception as e:
        print(f"Error writing {dst_path}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Translate Hugo markdown file to Spanish")
    parser.add_argument("src", help="Source markdown file path")
    parser.add_argument("--lang", default="es", help="Target language (default: es)")
    parser.add_argument("--dst-root", default="content/es", help="Destination root directory (use e.g. 'translation_experiments' for safe testing)")
    parser.add_argument("--model", default="o3", help="OpenAI model to use (default: o3)")
    parser.add_argument("--api-key", help="OpenAI API key (or set OPENAI_API_KEY env var)")
    parser.add_argument("--web-format", action="store_true", help="Apply web-friendly formatting: break paragraphs >4 sentences, subtle emphasis")
    parser.add_argument("--temperature", type=float, default=0.2, help="Sampling temperature for OpenAI completion (default: 0.2; some models like o3 ignore non-1.0 values)")
    parser.add_argument("--chunk", action="store_true", help="Enable automatic chunking for long files (>40k chars)")
    parser.add_argument("--chunk-size-chars", type=int, default=25000, help="Chunk size in characters when --chunk is enabled (default: 25000)")
    parser.add_argument("--no-auto-model", dest="auto_model", action="store_false", help="Disable automatic model switching based on chunk size/token estimate")
    parser.set_defaults(auto_model=True)
    
    args = parser.parse_args()
    
    # Get API key from argument or environment
    api_key = args.api_key or os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("Error: OpenAI API key required. Use --api-key or set OPENAI_API_KEY environment variable.")
        sys.exit(1)
    
    # Parse source path
    src_path = Path(args.src)
    if not src_path.exists():
        print(f"Error: Source file {src_path} does not exist")
        sys.exit(1)
    
    # Construct destination path
    # Example: content/posts/foo.md -> content/es/posts/foo.md
    # Example: content/posts/foo/index.md -> content/es/posts/foo/index.md
    
    src_parts = src_path.parts
    if 'content' in src_parts:
        content_idx = src_parts.index('content')
        # Skip 'content' and rebuild path under dst_root
        rel_path = Path(*src_parts[content_idx + 1:])
        dst_path = Path(args.dst_root) / rel_path
    else:
        # Fallback: just put in dst_root
        dst_path = Path(args.dst_root) / src_path.name
    
    print(f"Source: {src_path}")
    print(f"Destination: {dst_path}")
    print(f"Model: {args.model}")
    print(f"Language: {args.lang}")
    if args.web_format:
        print("Web-formatting: ENABLED (long paragraphs will be split, additional headings/lists may be added)")
    print()
    
    # Translate the file
    success = translate_file(src_path, dst_path, args.lang, args.model, api_key, args.web_format, args.temperature, chunk=args.chunk, chunk_size_chars=args.chunk_size_chars, auto_model=args.auto_model)
    
    if success:
        print("\n✅ Translation completed successfully!")
    else:
        print("\n❌ Translation failed!")
        sys.exit(1)

if __name__ == "__main__":
    main() 