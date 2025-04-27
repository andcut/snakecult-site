#!/usr/bin/env python3
"""
Run this script before posting Deep Research reports.

Cleans Unicode quirks, normalizes quotes, lightly de-hyphenates,
fixes space before periods, and adds minor double-spacing after periods,
while preserving URLs, metadata, and code blocks.

Usage:
  python3 snakecult_clean.py draft.md --inplace

Flags:
  --chunk N      Split paragraphs longer than N words (default: off)
  --no-bold      Do NOT bold topic sentence when chunking
  --inplace      Modify the file in-place
"""
import argparse, re, sys, textwrap, pathlib, random

# Regex patterns
URL_PATTERN = re.compile(r'https?://[^\s\)\]]+')
BLOCK_PATTERN = re.compile(r'(?s)(^---.*?---|^\+\+\+.*?\+\+\+|^```.*?```)', re.MULTILINE)

# Unicode fixups
RE_MAP = {
    "\u00A0": " ",   # NBSP (U+00A0)
    "\u200B": " ",   # ZWSP (U+200B)
    "\u00AD": "",    # SOFT HYPHEN (U+00AD)
    "\u2011": "-",   # NON-BREAKING HYPHEN (U+2011)
    "\uFFFD": "",    # REPLACEMENT CHARACTER (U+FFFD)
    "\uFFFC": "",    # OBJECT REPLACEMENT CHARACTER (U+FFFC)
    "“": '"', "”": '"',  # Normalize smart quotes to dumb quotes
    "‘": "'", "’": "'",  # Same for single quotes
}

# Helpers to freeze/thaw blocks
def freeze_special_blocks(text:str):
    blocks = []
    def replacer(match):
        blocks.append(match.group(0))
        return f"__BLOCK{len(blocks)-1}__"
    text = BLOCK_PATTERN.sub(replacer, text)
    return text, blocks

def thaw_special_blocks(text:str, blocks:list):
    for i, block in enumerate(blocks):
        text = text.replace(f"__BLOCK{i}__", block)
    return text

def freeze_urls(text:str):
    urls = []
    def replacer(match):
        urls.append(match.group(0))
        return f"__URL{len(urls)-1}__"
    text = URL_PATTERN.sub(replacer, text)
    return text, urls

def thaw_urls(text:str, urls:list):
    for i, url in enumerate(urls):
        text = text.replace(f"__URL{i}__", url)
    return text

# Core cleaning functions
def scrub(text:str)->str:
    # Debug: Print code points of characters in the first 100 chars
    print("DEBUG - First 100 chars code points:", [ord(c) for c in text[:100]])
    for bad, good in RE_MAP.items():
        text = text.replace(bad, good)
    text = re.sub(r"[ ]{2,}", " ", text)
    return text

def fix_space_before_period(text:str)->str:
    return re.sub(r'\s+\.', '.', text)

def dehyphenate(text:str)->str:
    # NOTE: This function is currently disabled in main() due to over-aggressive behavior
    return re.sub(r'\\b([a-z]+)-([a-z]+)\\b', r'\\1 \\2', text)

def randomize_spacing(text:str)->str:
    def maybe_double_space(match):
        return match.group(1) + ("  " if random.random() < 0.2 else " ")
    return re.sub(r'(\\.)( )', maybe_double_space, text)

# Optional paragraph chunking
def split_para(para:str, limit:int, bold:bool)->str:
    words = para.split()
    if len(words) <= limit: return para
    chunks = []
    start = 0
    while start < len(words):
        end = min(start + limit, len(words))
        chunk_words = words[start:end]
        chunk = " ".join(chunk_words)
        if bold and not chunks:
            first_sent = re.split(r"(?<=[.!?])\\s+", chunk, maxsplit=1)
            if len(first_sent) > 1:
                chunk = f"**{first_sent[0]}** {first_sent[1]}"
            else:
                chunk = f"**{chunk}**"
        chunks.append(chunk)
        start = end
    return "\\n\\n".join(chunks)

def autochunk(md:str, limit:int, bold:bool)->str:
    out, code = [], False
    for line in md.splitlines():
        if line.startswith("```"):
            code = not code
            out.append(line)
            continue
        if code or not line.strip():
            out.append(line)
            continue
        if re.match(r"^#{1,6}\\s", line):
            out.append(line)
            continue
        para_lines = [line]
        while out and not out[-1].strip():
            break
        out.append("\\n".join(para_lines))
    final = []
    for block in "\\n".join(out).split("\\n\\n"):
        if block.strip().startswith("```"):
            final.append(block)
        else:
            final.append(split_para(block, limit, bold))
    return "\\n\\n".join(final)

# Main pipeline
def main():
    p = argparse.ArgumentParser()
    p.add_argument("file", type=pathlib.Path)
    p.add_argument("--chunk", type=int, default=0)
    p.add_argument("--no-bold", action="store_true")
    p.add_argument("--inplace", action="store_true")
    args = p.parse_args()

    # Debug: Print raw bytes
    with open(args.file, 'rb') as f:
        raw_bytes = f.read()
        print("DEBUG - First 100 bytes:", raw_bytes[:100])
        print("DEBUG - Hex representation:", raw_bytes[:100].hex())

    text = args.file.read_text(encoding="utf-8")

    # Freeze dangerous content
    text, blocks = freeze_special_blocks(text)
    text, urls = freeze_urls(text)

    # Clean normal text
    text = scrub(text)
    text = fix_space_before_period(text)
    # text = dehyphenate(text) # Commented out - too aggressive
    text = randomize_spacing(text)

    # Restore frozen content
    text = thaw_urls(text, urls)
    text = thaw_special_blocks(text, blocks)

    # Optionally chunk paragraphs
    if args.chunk:
        text = autochunk(text, args.chunk, not args.no_bold)

    # Output
    if args.inplace:
        args.file.write_text(text, encoding="utf-8")
        print(f"File '{args.file}' modified in-place.", file=sys.stderr)
    else:
        sys.stdout.write(text)

if __name__ == "__main__":
    main()