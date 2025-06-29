#!/usr/bin/env python3
"""set_draft_false.py – Batch-update Hugo markdown files.

Searches all *.md files under a given directory (default: content/posts)
and flips `draft: true` to `draft: false` in their YAML front matter.
Run:
    python3 scripts/set_draft_false.py [root_dir]
"""
from __future__ import annotations
import pathlib
import re
import sys

def flip_draft_flag(root: pathlib.Path) -> None:
    md_files = list(root.rglob("*.md"))
    pattern = re.compile(r"^draft:\s*true\s*$", re.MULTILINE)
    for path in md_files:
        try:
            text = path.read_text(encoding="utf-8")
        except Exception as e:
            print(f"! Skipping {path}: {e}")
            continue
        if not pattern.search(text):
            continue  # nothing to change
        new_text = pattern.sub("draft: false", text)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            print(f"✓ Updated draft flag in {path.relative_to(root)}")


def main():
    root_arg = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path("content/posts")
    if not root_arg.is_dir():
        sys.exit(f"Error: {root_arg} is not a directory")
    flip_draft_flag(root_arg)

if __name__ == "__main__":
    main() 