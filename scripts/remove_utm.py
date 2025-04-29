#!/usr/bin/env python3
import os
import re
from pathlib import Path

def remove_utm_from_url(url):
    """Remove UTM parameters from a URL."""
    # Split the URL into base and parameters
    if '?' in url:
        base, params = url.split('?', 1)
        # Remove UTM parameters
        params = '&'.join(p for p in params.split('&') if not p.startswith('utm_'))
        # Reconstruct URL
        return base + ('?' + params if params else '')
    return url

def process_markdown_file(file_path):
    """Process a markdown file to remove UTM parameters from links."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all markdown links
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    
    def replace_link(match):
        text = match.group(1)
        url = match.group(2)
        clean_url = remove_utm_from_url(url)
        return f'[{text}]({clean_url})'
    
    # Replace all links with cleaned versions
    new_content = re.sub(link_pattern, replace_link, content)
    
    # Only write if changes were made
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Cleaned UTM parameters from {file_path}")
    else:
        print(f"No UTM parameters found in {file_path}")

def main():
    # Get the project root directory
    project_root = Path(__file__).parent.parent
    posts_dir = project_root / 'content' / 'posts'
    
    # Process all markdown files in the posts directory
    for file_path in posts_dir.glob('*.md'):
        process_markdown_file(file_path)

if __name__ == '__main__':
    main() 