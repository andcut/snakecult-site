"""
merge_duplicate_tags.py
---------------------------------
Normalize and de-duplicate `tags:` front-matter arrays across all Markdown
posts.  The script works in two passes:

1. Scans English (default-language) posts to treat their tags as canonical.
   It builds a mapping of **slug → canonical tag** where the slug is obtained
   with a Hugo-like sanitisation (lower-case, spaces → hyphens, ASCII only).
2. Walks through every Markdown file (both English and Spanish).  For each
   tag it looks up the slug in the canonical map.  If found, it replaces the
   tag with the canonical spelling/casing; otherwise it keeps the original
   tag but still applies slug-level de-duplication.

Only files whose `tags:` list changes are rewritten in-place.
"""

from __future__ import annotations

import re
import unicodedata
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent  # project root
CONTENT_DIR = ROOT / "content"

# ----------------------------------------------------------------------------
# Utility functions
# ----------------------------------------------------------------------------

def slugify(tag: str) -> str:
    """Return a Hugo-style slug for *tag* (simplified)."""
    # 1. Normalise accents → ASCII
    tag = unicodedata.normalize("NFKD", tag).encode("ascii", "ignore").decode()
    # 2. Lower-case
    tag = tag.lower()
    # 3. Only keep alphanumerics, spaces, and hyphens
    tag = re.sub(r"[^a-z0-9\s-]", "", tag)
    # 4. Collapse whitespace → single hyphen
    tag = re.sub(r"\s+", "-", tag.strip())
    # 5. Collapse repeated hyphens
    tag = re.sub(r"-+", "-", tag)
    return tag


def iter_markdown_files() -> list[Path]:
    """Yield every *.md file under /content."""
    return list(CONTENT_DIR.rglob("*.md"))


# ----------------------------------------------------------------------------
# 1. Build canonical tag map from English posts
# ----------------------------------------------------------------------------

def build_canonical_map() -> dict[str, str]:
    canonical: dict[str, str] = {}
    for md in (CONTENT_DIR / "posts").rglob("*.md"):
        meta = read_front_matter(md)
        for tag in meta.get("tags", []) or []:
            slug = slugify(tag)
            # First occurrence establishes the canonical spelling
            canonical.setdefault(slug, tag)
    return canonical


# ----------------------------------------------------------------------------
# Front-matter helpers
# ----------------------------------------------------------------------------

def read_front_matter(path: Path) -> dict:
    """Return YAML front-matter as dict (empty if none)."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    try:
        _sep1, fm, _sep2 = text.split("---", 2)
    except ValueError:
        return {}
    try:
        return yaml.safe_load(fm) or {}
    except yaml.YAMLError:
        return {}


def write_front_matter(path: Path, meta: dict, body: str) -> None:
    """Overwrite *path* with updated front-matter and *body*."""
    new_content = "---\n" + yaml.safe_dump(meta, sort_keys=False, allow_unicode=True) + "---" + body
    path.write_text(new_content, encoding="utf-8")


# ----------------------------------------------------------------------------
# 2. Normalise tags in every post
# ----------------------------------------------------------------------------

def normalise_tags(canonical_map: dict[str, str]) -> None:
    changed_files = 0
    for md in iter_markdown_files():
        text = md.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue  # skip non-front-matter files
        sep1, fm, rest = text.split("---", 2)
        meta = yaml.safe_load(fm) or {}
        tags = meta.get("tags")
        if not tags:
            continue
        # De-duplicate & normalise
        new_tags: list[str] = []
        seen_slugs: set[str] = set()
        for tag in tags:
            slug = slugify(tag)
            slug = slugify(tag)
            canonical = canonical_map.get(slug, tag)
            slug = slugify(canonical)
            if slug not in seen_slugs:
                seen_slugs.add(slug)
                new_tags.append(canonical)
        if new_tags != tags:
            meta["tags"] = new_tags
            write_front_matter(md, meta, rest)
            changed_files += 1
    print(f"Normalised tags in {changed_files} Markdown files.")


if __name__ == "__main__":
    canonical = build_canonical_map()
    normalise_tags(canonical) 