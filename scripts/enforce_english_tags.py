#!/usr/bin/env python3
"""
Enforce English tags across all language versions to maintain consistency.
This prevents the same concept from being tagged differently in different languages.
"""

import os
import yaml
import re
from pathlib import Path

def get_english_tags(english_file):
    """Extract tags from the English version of a file."""
    try:
        with open(english_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.startswith('---'):
            return []
            
        parts = content.split('---', 2)
        if len(parts) < 3:
            return []
            
        fm_data = yaml.safe_load(parts[1])
        return fm_data.get('tags', []) or []
        
    except Exception as e:
        print(f"Error reading English file {english_file}: {e}")
        return []

def update_non_english_tags(file_path, english_tags):
    """Update a non-English file to use English tags."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.startswith('---'):
            return False
            
        parts = content.split('---', 2)
        if len(parts) < 3:
            return False
            
        fm_data = yaml.safe_load(parts[1])
        original_tags = fm_data.get('tags', [])
        
        # Only update if tags are different
        if original_tags != english_tags:
            fm_data['tags'] = english_tags
            
            # Reconstruct file
            new_front_matter = yaml.dump(fm_data, default_flow_style=False, allow_unicode=True)
            new_content = f"---\n{new_front_matter}---{parts[2]}"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"Updated {file_path}: {original_tags} → {english_tags}")
            return True
            
        return False
        
    except Exception as e:
        print(f"Error updating {file_path}: {e}")
        return False

def main():
    """Main function to enforce English tags across all languages."""
    
    # Languages to process (skip English)
    languages = ['es', 'zh', 'fr', 'de', 'pt', 'hi', 'ar', 'ru']
    updated_count = 0
    
    # Process regular posts
    english_posts = Path("content/posts")
    for english_file in english_posts.glob("*.md"):
        english_tags = get_english_tags(english_file)
        
        if not english_tags:
            continue
            
        # Update corresponding files in other languages
        for lang in languages:
            lang_file = Path(f"content/{lang}/posts/{english_file.name}")
            if lang_file.exists():
                if update_non_english_tags(lang_file, english_tags):
                    updated_count += 1
    
    # Process VOM posts
    english_vom = Path("content/posts/vom")
    for english_file in english_vom.glob("*.md"):
        english_tags = get_english_tags(english_file)
        
        if not english_tags:
            continue
            
        # Update corresponding VOM files in other languages  
        for lang in languages:
            lang_file = Path(f"content/{lang}/posts/vom/{english_file.name}")
            if lang_file.exists():
                if update_non_english_tags(lang_file, english_tags):
                    updated_count += 1
    
    print(f"\nEnforced English tags on {updated_count} non-English files")
    print("All languages now use consistent English tags!")

if __name__ == "__main__":
    main() 