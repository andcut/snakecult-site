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

def remove_utm_params(url:str)->str:
    """Remove UTM parameters from URLs."""
    # Split URL into base and query parts
    if '?' not in url:
        return url
    base, query = url.split('?', 1)
    # Remove UTM parameters from query string
    params = [p for p in query.split('&') if not p.startswith('utm_')]
    # Reconstruct URL
    if params:
        return f"{base}?{'&'.join(params)}"
    return base

def clean_oai_citations(text: str) -> str:
    """
    Clean up oai_citation format links by converting them to footnotes.
    
    Converts patterns like:
    [oai_citation:3‡publishing.cdlib.org](https://publishing.cdlib.org/...)
    [oai_citation_attribution:0‡Wikipedia](https://en.wikipedia.org/...)
    
    To footnote references [^1], [^2], etc. and adds footnote definitions at the end.
    """
    import re
    from urllib.parse import urlparse
    
    # Pattern to match oai_citation links
    # Matches: [oai_citation:N‡domain](url) or [oai_citation_attribution:N‡domain](url)
    pattern = r'\[oai_citation(?:_attribution)?:\d+‡([^\]]+)\]\(([^)]+)\)'
    
    # Find all citations
    citations = []
    
    def collect_citation(match):
        domain_hint = match.group(1).strip()
        url = match.group(2).strip()
        
        # Extract meaningful text from domain hint
        domain_text = domain_hint.lower()
        
        # Map common domains to cleaner names
        domain_mappings = {
            'wikipedia': 'Wikipedia',
            'en.wikipedia.org': 'Wikipedia',
            'pubmed': 'PubMed',
            'pmc': 'PMC',
            'pnas': 'PNAS',
            'sciencedirect': 'ScienceDirect',
            'researchgate': 'ResearchGate',
            'jstor': 'JSTOR',
            'nature': 'Nature',
            'science': 'Science',
            'theoi.com': 'Theoi',
            'topostext.org': 'ToposText',
            'hellenicgods.org': 'Hellenic Gods',
            'atheologica.wordpress.com': 'Atheologica',
            'dainst.blog': 'Tepe Telegrams',
            'scientific american': 'Scientific American',
            'vectors of mind': 'Vectors of Mind',
            'royal society publishing': 'Royal Society',
            'j-stage': 'J-STAGE',
            'berkeley news': 'UC Berkeley News',
            'gmat club': 'GMAT Club',
            'ethnology.pitt.edu': 'Ethnology',
            'bible hub': 'Bible Hub',
            'uc davis': 'UC Davis',
            'smithsonian magazine': 'Smithsonian',
            'norse mythology for smart people': 'Norse Mythology',
            'psymposia': 'Psymposia',
            'amazon': 'Amazon',
            'organism earth': 'Organism Earth',
            'encyclopedia britannica': 'Britannica',
            'aaron cheak': 'Aaron Cheak',
            'bryn mawr classical review': 'Bryn Mawr Classical Review',
            'penelope': 'Penelope (U. Chicago)',
            'semper initiativus unum': 'Semper Initiativus Unum',
            'the guardian': 'The Guardian',
            'wired': 'WIRED',
            'abc': 'ABC News',
            'western australian museum': 'WA Museum',
            'paleoanthro': 'PaleoAnthro',
            'austhrutime': 'AusThruTime',
            'the metropolitan museum of art': 'Met Museum',
            'anu press': 'ANU Press',
            'time': 'Time',
            'unesco world heritage centre': 'UNESCO',
            'national museum of australia': 'National Museum of Australia',
            'sci.news: breaking science news': 'Sci.News',
            'jcu.edu.au': 'JCU',
            'figshare': 'Figshare',
            'au.news.yahoo.com': 'Yahoo News AU'
        }
        
        # Find the best match for domain text
        display_text = domain_mappings.get(domain_text, domain_hint)
        
        # If we couldn't find a mapping, try to extract from the actual URL
        if display_text == domain_hint:
            try:
                parsed = urlparse(url)
                domain = parsed.netloc.lower()
                # Remove www. prefix
                if domain.startswith('www.'):
                    domain = domain[4:]
                
                # Try common domain mappings
                for key, value in domain_mappings.items():
                    if key in domain:
                        display_text = value
                        break
                else:
                    # Fallback: capitalize first letter of domain
                    display_text = domain.split('.')[0].capitalize()
            except:
                # If URL parsing fails, use the domain hint as-is
                display_text = domain_hint
        
        # Check if we already have this exact citation
        citation_entry = (display_text, url)
        if citation_entry not in citations:
            citations.append(citation_entry)
        
        # Return footnote reference
        footnote_num = citations.index(citation_entry) + 1
        return f"[^oai{footnote_num}]"
    
    # Replace all citations with footnote references
    result_text = re.sub(pattern, collect_citation, text)
    
    # If we found citations, add footnotes section
    if citations:
        # Check if there's already a footnotes section
        footnote_section_exists = re.search(r'^\[?\^[^\]]*\]?:', result_text, re.MULTILINE)
        
        # Build footnotes
        footnotes = []
        for i, (display_text, url) in enumerate(citations, 1):
            footnotes.append(f"[^oai{i}]: [{display_text}]({url})")
        
        # Add footnotes to the end of the document
        if footnote_section_exists:
            # Insert before existing footnotes
            result_text = re.sub(r'(\n\[?\^[^\]]*\]?:.*)', r'\n' + '\n'.join(footnotes) + r'\1', result_text, count=1)
        else:
            # Add at the end
            if not result_text.endswith('\n'):
                result_text += '\n'
            result_text += '\n' + '\n'.join(footnotes) + '\n'
    
    return result_text

# Core cleaning functions
def scrub(text:str)->str:
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

    text = args.file.read_text(encoding="utf-8")

    # Clean oai_citation format links BEFORE freezing anything
    text = clean_oai_citations(text)
    
    # Freeze dangerous content
    text, blocks = freeze_special_blocks(text)
    text, urls = freeze_urls(text)

    # Clean normal text
    text = scrub(text)
    text = fix_space_before_period(text)
    # text = dehyphenate(text) # Commented out - too aggressive
    text = randomize_spacing(text)

    # Clean URLs
    urls = [remove_utm_params(url) for url in urls]

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