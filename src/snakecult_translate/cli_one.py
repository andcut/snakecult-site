#!/usr/bin/env python3
"""
Single-file translation CLI using shared core functionality.
"""

import argparse
import sys
from pathlib import Path

from .core import translate_file
from .utils import load_env_and_key


def main():
    parser = argparse.ArgumentParser(description="Translate Hugo markdown file")
    parser.add_argument("src", help="Source markdown file path")
    parser.add_argument("--lang", default="es", help="Target language (default: es)")
    parser.add_argument("--dst-root", default="content/es", help="Destination root directory")
    parser.add_argument("--model", default="gpt-4o", help="OpenAI model to use (default: gpt-4o)")
    parser.add_argument("--api-key", help="OpenAI API key (or set OPENAI_API_KEY env var)")
    parser.add_argument("--web-format", action="store_true", help="Apply web-friendly formatting")
    parser.add_argument("--temperature", type=float, default=0.2, help="Sampling temperature (default: 0.2)")
    parser.add_argument("--chunk", action="store_true", help="Enable automatic chunking for long files")
    parser.add_argument("--chunk-size-chars", type=int, default=25000, help="Chunk size in characters (default: 25000)")
    parser.add_argument("--no-auto-model", dest="auto_model", action="store_false", help="Disable automatic model switching")
    parser.set_defaults(auto_model=True)
    
    args = parser.parse_args()
    
    # Get API key from argument or environment
    api_key = args.api_key or load_env_and_key()
    if not api_key:
        print("Error: OpenAI API key required. Use --api-key or set OPENAI_API_KEY environment variable.")
        sys.exit(1)
    
    # Parse source path
    src_path = Path(args.src)
    if not src_path.exists():
        print(f"Error: Source file {src_path} does not exist")
        sys.exit(1)
    
    # Construct destination path
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
        print("Web-formatting: ENABLED")
    print()
    
    # Translate the file
    success = translate_file(
        src_path=src_path,
        dst_path=dst_path,
        target_lang=args.lang,
        model=args.model,
        api_key=api_key,
        web_format=args.web_format,
        temperature=args.temperature,
        chunk=args.chunk,
        chunk_size_chars=args.chunk_size_chars,
        auto_model=args.auto_model
    )
    
    if success:
        print("\n✅ Translation completed successfully!")
    else:
        print("\n❌ Translation failed!")
        sys.exit(1)


if __name__ == "__main__":
    main() 