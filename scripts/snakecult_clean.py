#!/usr/bin/env python3
"""
Run this script before the LLM reformats a post. 

Clean Unicode quirks and (optionally) chunk long paragraphs for SnakeCult posts.

Usage will most often be:
  python3 snakecult_clean.py draft.md --inplace

Flags:
  --chunk N      Split paragraphs longer than N words (default: off)
  --no-bold      Do NOT bold topic sentence when chunking
  --inplace      Modify the file in-place instead of writing to stdout
"""
import argparse, re, sys, textwrap, pathlib

RE_MAP = {
    "\u00A0": " ",   # NBSP
    "\u200B": " ",   # ZWSP
    "\u00AD": "",    # SOFT HYPHEN
    "\u2011": "-",   # NON-BREAKING HYPHEN
    "\uFFFD": "",   # REPLACEMENT CHARACTER (often indicates encoding issues)
    "\uFFFC": "",   # OBJECT REPLACEMENT CHARACTER
}

def scrub(text:str)->str:
    for bad, good in RE_MAP.items():
        text = text.replace(bad, good)
    text = re.sub(r"[ ]{2,}", " ", text)
    return text

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
            first_sent = re.split(r"(?<=[.!?])\s+", chunk, maxsplit=1)
            if len(first_sent) > 1:
                chunk = f"**{first_sent[0]}** {first_sent[1]}"
            else:
                chunk = f"**{chunk}**"
        chunks.append(chunk)
        start = end
    return "\n\n".join(chunks)

def autochunk(md:str, limit:int, bold:bool)->str:
    # Ignore code blocks & front-matter
    out, code = [], False
    for line in md.splitlines():
        if line.startswith("```"):
            code = not code
            out.append(line)
            continue
        if code or not line.strip():
            out.append(line)
            continue
        if re.match(r"^#{1,6}\s", line):          # headings untouched
            out.append(line)
            continue
        # accumulate paragraph until blank
        para_lines = [line]
        while out and not out[-1].strip():        # previous blank line?
            break
        out.append("\n".join(para_lines))
    # second pass: chunk paragraphs
    final = []
    for block in "\n".join(out).split("\n\n"):
        if block.strip().startswith("```"):
            final.append(block)
        else:
            final.append(split_para(block, limit, bold))
    return "\n\n".join(final)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("file", type=pathlib.Path)
    p.add_argument("--chunk", type=int, default=0,
                   help="Word limit per paragraph before splitting")
    p.add_argument("--no-bold", action="store_true")
    p.add_argument("--inplace", action="store_true",
                   help="Modify the file in-place instead of writing to stdout")
    args = p.parse_args()

    text = args.file.read_text(encoding="utf-8")
    text = scrub(text)
    if args.chunk:
        text = autochunk(text, args.chunk, not args.no_bold)

    if args.inplace:
        args.file.write_text(text, encoding="utf-8")
        print(f"File '{args.file}' modified in-place.", file=sys.stderr)
    else:
        sys.stdout.write(text)

if __name__ == "__main__":
    main()