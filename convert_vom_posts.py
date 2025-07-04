#!/usr/bin/env python3
"""
Convert Vectors of Mind blog posts to snakecult.org format.

This script converts HTML files from the vom_posts directory to markdown format
with proper frontmatter for the snakecult.org Hugo site.
"""

import os
import re
import html
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
import json

# Try to import optional dependencies
try:
    from bs4 import BeautifulSoup
    HAS_BEAUTIFULSOUP = True
except ImportError:
    HAS_BEAUTIFULSOUP = False

try:
    import html2text
    HAS_HTML2TEXT = True
except ImportError:
    HAS_HTML2TEXT = False


class VOMPostConverter:
    """Simplified converter for Vectors of Mind blog posts."""
    
    def __init__(self, source_dir: str = "vom_posts", output_dir: str = "converted_posts"):
        self.source_dir = Path(source_dir)
        self.output_dir = Path(output_dir)
        
        # Published posts go to the main content directory
        self.published_dir = Path("content/posts/vom")
        # Drafts go to the converted_posts/drafts directory
        self.drafts_dir = self.output_dir / "drafts"
        
        # Create directories
        self.published_dir.mkdir(parents=True, exist_ok=True)
        self.drafts_dir.mkdir(parents=True, exist_ok=True)
        
        self.stats = {'total': 0, 'published': 0, 'drafts': 0, 'skipped': 0, 'errors': 0}
    
    def is_published_post(self, filename: str) -> bool:
        """Check if a post was published by looking for associated CSV files."""
        post_id = filename.split('.')[0]
        csv_patterns = [f"{post_id}.delivers.csv", f"{post_id}.opens.csv", f"{post_id}.clicks.csv"]
        return any((self.source_dir / pattern).exists() for pattern in csv_patterns)
    
    def extract_title_from_filename(self, filename: str) -> str:
        """Extract title from filename like '64772741.is-personality-hyperbolic.html'."""
        # Remove .html extension
        name = filename.replace('.html', '')
        
        # Split by first dot to separate ID from slug
        parts = name.split('.', 1)
        if len(parts) < 2:
            return name.replace('-', ' ').title()
        
        slug = parts[1]
        # Convert slug to title
        title = slug.replace('-', ' ').title()
        
        # Clean up common issues
        title = title.replace('Etoc', 'EToC')
        title = title.replace('Pfc', 'PFC')
        title = title.replace('Adhd', 'ADHD')
        title = title.replace('Dna', 'DNA')
        title = title.replace('Ai', 'AI')
        
        return title
    
    def extract_title_from_content(self, content: str) -> Optional[str]:
        """Extract title from HTML content."""
        if HAS_BEAUTIFULSOUP:
            soup = BeautifulSoup(content, 'html.parser')
            h1 = soup.find('h1')
            return h1.get_text().strip() if h1 else None
        
        h1_match = re.search(r'<h1[^>]*>([^<]+)</h1>', content, re.IGNORECASE)
        return html.unescape(h1_match.group(1).strip()) if h1_match else None
    
    def generate_slug(self, title: str) -> str:
        """Generate URL-friendly slug from title."""
        slug = title.lower()
        slug = re.sub(r'[^a-z0-9\s-]', '', slug)
        slug = re.sub(r'\s+', '-', slug)
        slug = re.sub(r'-+', '-', slug)
        return slug.strip('-')
    
    def extract_description(self, content: str) -> str:
        """Extract description from first paragraph."""
        if HAS_BEAUTIFULSOUP:
            soup = BeautifulSoup(content, 'html.parser')
            first_p = soup.find('p')
            if first_p:
                text = first_p.get_text().strip()
                return text[:200] + "..." if len(text) > 200 else text
        
        p_match = re.search(r'<p[^>]*>([^<]+)</p>', content, re.IGNORECASE)
        if p_match:
            text = html.unescape(p_match.group(1).strip())
            return text[:200] + "..." if len(text) > 200 else text
        
        return "A blog post from Vectors of Mind."
    
    def extract_keywords(self, title: str) -> List[str]:
        """Extract keywords from title."""
        keywords = ['vectors-of-mind']
        title_words = re.findall(r'\b[a-zA-Z]{4,}\b', title.lower())
        keywords.extend([word for word in title_words if word not in ['theory', 'the', 'and', 'for', 'with', 'from']])
        return keywords[:8]  # Limit to 8 keywords
    
    def handle_images(self, content: str) -> str:
        """Replace images with placeholder text."""
        content = re.sub(r'<img[^>]*>', '*[Image: Visual content from original post]*', content)
        return content
    
    def convert_footnotes(self, content: str) -> str:
        """Convert Substack footnotes to markdown format with proper spacing."""
        if not HAS_BEAUTIFULSOUP:
            # Basic regex-based footnote conversion
            content = re.sub(
                r'<a[^>]*class="footnote-anchor"[^>]*id="footnote-anchor-(\d+)"[^>]*>(\d+)</a>',
                r'[^\1]',
                content
            )
            
            # Convert footnote definitions
            footnote_pattern = r'<div[^>]*class="footnote"[^>]*>.*?<a[^>]*id="footnote-(\d+)"[^>]*>\d+</a>.*?<div[^>]*class="footnote-content"[^>]*>(.*?)</div>.*?</div>'
            footnotes = []
            
            def collect_footnote(match):
                footnote_num = match.group(1)
                footnote_content = re.sub(r'<[^>]+>', '', match.group(2))
                footnote_content = html.unescape(footnote_content.strip())
                footnotes.append(f'[^{footnote_num}]: {footnote_content}')
                return ''
            
            content = re.sub(footnote_pattern, collect_footnote, content, flags=re.DOTALL)
            
            # Add footnotes at the end with proper spacing (double newlines between each)
            if footnotes:
                content += '\n\n' + '\n\n'.join(footnotes)
            
            return content
        
        # BeautifulSoup-based conversion
        soup = BeautifulSoup(content, 'html.parser')
        
        # Convert footnote anchors to markdown references
        for anchor in soup.find_all('a', class_='footnote-anchor'):
            footnote_id = anchor.get('id', '')
            if footnote_id.startswith('footnote-anchor-'):
                footnote_num = footnote_id.replace('footnote-anchor-', '')
                anchor.replace_with(f'[^{footnote_num}]')
        
        # Convert footnote definitions
        footnote_markdown = []
        for footnote_div in soup.find_all('div', class_='footnote'):
            footnote_link = footnote_div.find('a', class_='footnote-number')
            if not footnote_link:
                continue
                
            footnote_id = footnote_link.get('id', '')
            if footnote_id.startswith('footnote-'):
                footnote_num = footnote_id.replace('footnote-', '')
                content_div = footnote_div.find('div', class_='footnote-content')
                if content_div:
                    footnote_text = content_div.get_text().strip()
                    footnote_markdown.append(f'[^{footnote_num}]: {footnote_text}')
            
            footnote_div.decompose()
        
        content_str = str(soup)
        if footnote_markdown:
            # Add footnotes with proper spacing (double newlines between each)
            content_str += '\n\n' + '\n\n'.join(footnote_markdown)
        
        return content_str
    
    def convert_html_to_markdown(self, html_content: str) -> str:
        """Convert HTML to markdown."""
        # Down-rank headers (h1 -> h2, etc.)
        for i in range(5, 0, -1):  # 5 to 1 to avoid double substitution
            html_content = re.sub(f'<h{i}([^>]*)>', f'<h{i+1}\\1>', html_content, flags=re.IGNORECASE)
            html_content = re.sub(f'</h{i}>', f'</h{i+1}>', html_content, flags=re.IGNORECASE)
        
        if HAS_HTML2TEXT:
            h = html2text.HTML2Text()
            h.ignore_links = False
            h.ignore_images = True
            h.body_width = 0
            h.single_line_break = False
            
            markdown_content = h.handle(html_content)
            
            # Fix headers and ensure proper spacing
            markdown_content = re.sub(r'^(#{1,6})\s*(.+)$', r'\1 \2\n', markdown_content, flags=re.MULTILINE)
            
            # Convert Setext-style headings to ATX format
            def setext_to_atx(match):
                title_line = match.group(1).strip()
                underline = match.group(2)
                prefix = '##' if underline.startswith('=') else '###'
                return f"{prefix} {title_line}\n\n"
            
            markdown_content = re.sub(r'^(.*?)\n([=-]{2,})\s*$', setext_to_atx, markdown_content, flags=re.MULTILINE)
            
            return markdown_content
        else:
            # Basic HTML to markdown conversion
            replacements = [
                (r'<h6[^>]*>(.*?)</h6>', r'###### \1\n\n'),
                (r'<h5[^>]*>(.*?)</h5>', r'##### \1\n\n'),
                (r'<h4[^>]*>(.*?)</h4>', r'#### \1\n\n'),
                (r'<h3[^>]*>(.*?)</h3>', r'### \1\n\n'),
                (r'<h2[^>]*>(.*?)</h2>', r'## \1\n\n'),
                (r'<ul[^>]*>', ''),
                (r'</ul>', ''),
                (r'<ol[^>]*>', ''),
                (r'</ol>', ''),
                (r'<li[^>]*>([^<]+)</li>', r'* \1\n'),
                (r'<p[^>]*>([^<]+)</p>', r'\1\n\n'),
                (r'<blockquote[^>]*>([^<]+)</blockquote>', r'> \1\n\n'),
                (r'<a[^>]*href="([^"]*)"[^>]*>([^<]+)</a>', r'[\2](\1)'),
                (r'<em[^>]*>([^<]+)</em>', r'*\1*'),
                (r'<strong[^>]*>([^<]+)</strong>', r'**\1**'),
                (r'<[^>]+>', ''),  # Remove remaining HTML tags
            ]
            
            for pattern, replacement in replacements:
                html_content = re.sub(pattern, replacement, html_content, flags=re.DOTALL)
            
            # Clean up and unescape
            html_content = re.sub(r'\n\n+', '\n\n', html_content)
            return html.unescape(html_content).strip()
    
    def _yaml_str(self, value: str) -> str:
        """Safely wrap a string for YAML front-matter using JSON escaping.

        JSON is a strict subset of YAML 1.2, so json.dumps will produce a
        correctly escaped double-quoted string that YAML can parse. This
        avoids broken front-matter when the string itself contains quotes
        (e.g. a description beginning with a quotation mark)."""
        return json.dumps(value)
    
    def _clean_substack_links(self, text: str) -> str:
        """Replace all vectorsofmind *substack* URLs with the canonical domain."""
        pattern = re.compile(r"https?://vectorsofmind\.substack\.com", re.IGNORECASE)
        return pattern.sub("https://www.vectorsofmind.com", text)
    
    def _ensure_footnote_spacing(self, md: str) -> str:
        """Guarantee that every footnote definition starts on its own line.

        After html2text conversion, newlines inside plain-text segments may be
        collapsed. We detect patterns of a footnote definition (e.g. `[^1]:`)
        that are *not* already at the beginning of a line and prefix them with
        two newlines so that each definition is separated by a blank line.
        """
        return re.sub(r"(?<!\n)\s*(\[\^\d+\]:)", r"\n\n\1", md)
    
    def create_frontmatter(self, filename: str, title: str, content: str, is_published: bool) -> str:
        """Create frontmatter for the post."""
        slug = self.generate_slug(title)
        description = self.extract_description(content)
        keywords = self.extract_keywords(title)
        
        # Extract original ID from filename
        original_id = filename.split('.')[0]
        original_url = f"https://www.vectorsofmind.com/p/{slug}"
        
        frontmatter = {
            'title': self._yaml_str(title),
            'date': self._yaml_str("2025-07-04"),
            'lastmod': self._yaml_str("2025-07-04"),
            'slug': self._yaml_str(slug),
            'description': self._yaml_str(description),
            'keywords': keywords,
            'about': ['vectors-of-mind', 'blog-archive'],
            'tags': '[]',
            'author': self._yaml_str("Andrew Cutler"),
            'license': self._yaml_str("https://creativecommons.org/licenses/by-sa/4.0/"),
            'draft': 'False' if is_published else 'True',
            'quality': 6 if is_published else 1,
            'original_id': self._yaml_str(original_id),
            'original_url': self._yaml_str(original_url)
        }
        
        # Format frontmatter
        lines = ['---']
        for key, value in frontmatter.items():
            if isinstance(value, list):
                if key == 'keywords':
                    lines.append(f'{key}:')
                    for item in value:
                        lines.append(f'  - "{item}"')
                else:
                    lines.append(f'{key}: {value}')
            else:
                lines.append(f'{key}: {value}')
        lines.append('---')
        
        return '\n'.join(lines)
    
    def convert_file(self, filename: str) -> bool:
        """Convert a single HTML file to markdown."""
        try:
            html_file = self.source_dir / filename
            
            # Check if this is a published post or draft
            is_published = self.is_published_post(filename)
            
            # Read HTML content
            with open(html_file, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            # Extract title - prioritize filename over content extraction
            title = self.extract_title_from_filename(filename)
            content_title = self.extract_title_from_content(html_content)
            
            # Only use content title if filename doesn't provide a good title
            # (i.e., if filename is just a number or very short)
            if content_title and (len(title.replace(' ', '')) < 5 or title.isdigit()):
                title = content_title
                print(f"Using content title '{content_title}' for {filename}")
            else:
                print(f"Using filename title '{title}' for {filename}")
            
            # Process content
            content = self.handle_images(html_content)
            content = self.convert_footnotes(content)
            markdown_content = self.convert_html_to_markdown(content)
            
            # Replace substack links with canonical domain
            markdown_content = self._clean_substack_links(markdown_content)
            
            # Ensure footnote definitions have proper spacing
            markdown_content = self._ensure_footnote_spacing(markdown_content)
            
            # Create frontmatter
            frontmatter = self.create_frontmatter(filename, title, html_content, is_published)
            
            # Add VOM header
            original_url_line = frontmatter.split("original_url: ")[1]
            original_url = original_url_line.split('"')[1]
            vom_header = (
                f'*From [Vectors of Mind]({original_url}) - images at original.*\n\n---\n\n'
            )
            
            # Combine everything
            full_content = f"{frontmatter}\n{vom_header}{markdown_content}"
            
            # Generate output filename and directory
            slug = self.generate_slug(title)
            if is_published:
                output_file = self.published_dir / f"{slug}.md"
                self.stats['published'] += 1
            else:
                output_file = self.drafts_dir / f"{slug}.md"
                self.stats['drafts'] += 1
            
            # Write output file
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(full_content)
            
            status = "Published" if is_published else "Draft"
            print(f"Converted {status}: {filename} -> {output_file}")
            return True
            
        except Exception as e:
            print(f"Error converting {filename}: {e}")
            self.stats['errors'] += 1
            return False
    
    def convert_all(self):
        """Convert all HTML files in the source directory."""
        html_files = list(self.source_dir.glob("*.html"))
        self.stats['total'] = len(html_files)
        
        print(f"Found {len(html_files)} HTML files to process")
        
        for html_file in html_files:
            self.convert_file(html_file.name)
        
        print(f"\nConversion complete!")
        print(f"Total: {self.stats['total']}")
        print(f"Published: {self.stats['published']}")
        print(f"Drafts: {self.stats['drafts']}")
        print(f"Skipped: {self.stats['skipped']}")
        print(f"Errors: {self.stats['errors']}")


def main():
    """Main entry point."""
    if not HAS_BEAUTIFULSOUP:
        print("Warning: BeautifulSoup not available. Using basic HTML parsing.")
    if not HAS_HTML2TEXT:
        print("Warning: html2text not available. Using basic HTML-to-markdown conversion.")
    
    converter = VOMPostConverter()
    converter.convert_all()


if __name__ == "__main__":
    main() 