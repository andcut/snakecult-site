#!/usr/bin/env python3
"""
Tag Propagation Script
Updates tag sections in all non-English content files using the tag matrix.
"""

import json
import os
import re
import sys
from pathlib import Path

# Configuration
TAG_MATRIX_FILE = "data/tag_matrix.json"
CONTENT_DIRS = {
    "es": "content/es",
    "zh": "content/zh", 
    "fr": "content/fr",
    "de": "content/de",
    "pt": "content/pt",
    "hi": "content/hi",
    "ar": "content/ar",
    "ru": "content/ru"
}
ENGLISH_CONTENT_DIRS = ["content/posts", "content/posts/vom"]
DRY_RUN = False  # Set to True to see changes without applying them

def load_tag_matrix():
    """Load the tag matrix from JSON file."""
    try:
        with open(TAG_MATRIX_FILE, 'r', encoding='utf-8') as f:
            matrix = json.load(f)
        print(f"Loaded tag matrix with {len(matrix)} tags")
        return matrix
    except Exception as e:
        print(f"Error loading tag matrix: {e}")
        return {}

def find_corresponding_english_file(non_english_file, english_dirs):
    """Find the corresponding English file for a non-English file."""
    # Extract the relative path from the language directory
    for lang_code, lang_dir in CONTENT_DIRS.items():
        if non_english_file.startswith(lang_dir):
            # Remove the language directory prefix
            relative_path = non_english_file[len(lang_dir):].lstrip('/')
            
            # Handle different directory structures
            if relative_path.startswith('posts/'):
                # For posts, check both content/posts and content/posts/vom
                post_filename = relative_path[6:]  # Remove 'posts/' prefix
                
                # Try content/posts/filename
                english_path = os.path.join("content/posts", post_filename)
                if os.path.exists(english_path):
                    return english_path
                    
                # Try content/posts/vom/filename  
                english_path = os.path.join("content/posts/vom", post_filename)
                if os.path.exists(english_path):
                    return english_path
            else:
                # For non-post files, try to find equivalent in content/
                english_path = os.path.join("content", relative_path)
                if os.path.exists(english_path):
                    return english_path
            break
    return None

def extract_tags_from_english_file(english_file):
    """Extract tags from the corresponding English file."""
    try:
        with open(english_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.splitlines()
        if not lines or lines[0] not in ['---', '+++']:
            return []
        
        front_matter_type = 'yaml' if lines[0] == '---' else 'toml'
        end_marker = '---' if front_matter_type == 'yaml' else '+++'
        
        try:
            end_idx = lines.index(end_marker, 1)
        except ValueError:
            return []
        
        front_matter_lines = lines[1:end_idx]
        tags = []
        
        if front_matter_type == 'yaml':
            in_tags_block = False
            for line in front_matter_lines:
                stripped = line.strip()
                if stripped.startswith('tags:'):
                    if '[' in stripped and ']' in stripped:
                        # Inline list
                        tag_string = stripped[stripped.find('[')+1:stripped.rfind(']')].strip()
                        if tag_string:
                            tags = [t.strip().strip('"').strip("'") for t in tag_string.split(',')]
                        break
                    elif stripped == 'tags:':
                        in_tags_block = True
                elif in_tags_block and stripped.startswith('- '):
                    tags.append(stripped[2:].strip().strip('"').strip("'"))
                elif in_tags_block and not line.startswith((' ', '\t')):
                    break
        else:  # TOML
            for line in front_matter_lines:
                if line.strip().startswith('tags') and '=' in line and '[' in line and ']' in line:
                    tag_string = line[line.find('[')+1:line.rfind(']')].strip()
                    if tag_string:
                        tags = [t.strip().strip('"').strip("'") for t in tag_string.split(',')]
                    break
        
        return [tag for tag in tags if tag]  # Remove empty tags
        
    except Exception as e:
        print(f"Error extracting tags from {english_file}: {e}")
        return []

def translate_tags(english_tags, target_lang, tag_matrix):
    """Translate English tags to target language using the matrix."""
    translated_tags = []
    
    for eng_tag in english_tags:
        if eng_tag in tag_matrix and target_lang in tag_matrix[eng_tag]:
            translated_tag = tag_matrix[eng_tag][target_lang]
            translated_tags.append(translated_tag)
        else:
            # Fallback to English tag if not in matrix
            translated_tags.append(eng_tag)
            print(f"  Warning: Tag '{eng_tag}' not found in matrix, using English")
    
    return translated_tags

def update_tags_in_content(content, new_tags, file_path):
    """Update the tags section in content and return the modified content."""
    lines = content.splitlines()
    
    if not lines or lines[0] not in ['---', '+++']:
        print(f"  Warning: {file_path} has no front matter")
        return content, False
    
    front_matter_type = 'yaml' if lines[0] == '---' else 'toml'
    end_marker = '---' if front_matter_type == 'yaml' else '+++'
    
    try:
        end_idx = lines.index(end_marker, 1)
    except ValueError:
        print(f"  Warning: {file_path} has malformed front matter")
        return content, False
    
    front_matter_lines = lines[1:end_idx]
    updated_front_matter = []
    tags_updated = False
    tags_found = False
    
    if front_matter_type == 'yaml':
        in_tags_block = False
        i = 0
        while i < len(front_matter_lines):
            line = front_matter_lines[i]
            stripped = line.strip()
            
            if stripped.startswith('tags:'):
                tags_found = True
                if '[' in stripped and ']' in stripped:
                    # Replace inline list
                    new_tag_string = ', '.join(f'"{tag}"' for tag in new_tags)
                    updated_front_matter.append(f"tags: [{new_tag_string}]")
                    tags_updated = True
                elif stripped == 'tags:':
                    # Replace block list
                    updated_front_matter.append("tags:")
                    for tag in new_tags:
                        updated_front_matter.append(f" - {tag}")  # Add space for proper YAML indentation
                    tags_updated = True
                    in_tags_block = True
                else:
                    updated_front_matter.append(line)
                    
            elif in_tags_block and stripped.startswith('- '):
                # Skip old tag items (already added new ones)
                pass
            elif in_tags_block and not line.startswith((' ', '\t')):
                # End of tags block
                in_tags_block = False
                updated_front_matter.append(line)
            else:
                updated_front_matter.append(line)
            
            i += 1
    else:  # TOML
        for line in front_matter_lines:
            if line.strip().startswith('tags') and '=' in line:
                tags_found = True
                # Replace TOML tags line
                new_tag_string = ', '.join(f'"{tag}"' for tag in new_tags)
                updated_front_matter.append(f'tags = [{new_tag_string}]')
                tags_updated = True
            else:
                updated_front_matter.append(line)
    
    # If no tags section found, add one
    if not tags_found and new_tags:
        if front_matter_type == 'yaml':
            updated_front_matter.append("tags:")
            for tag in new_tags:
                updated_front_matter.append(f" - {tag}")  # Add space for proper YAML indentation
        else:  # TOML
            new_tag_string = ', '.join(f'"{tag}"' for tag in new_tags)
            updated_front_matter.append(f'tags = [{new_tag_string}]')
        tags_updated = True
    
    if tags_updated:
        # Reconstruct content
        new_content = lines[0] + '\n'  # Start marker
        new_content += '\n'.join(updated_front_matter) + '\n'
        new_content += lines[end_idx] + '\n'  # End marker
        new_content += '\n'.join(lines[end_idx + 1:])  # Rest of content
        return new_content, True
    
    return content, False

def find_markdown_files(directory):
    """Find all .md files in a directory."""
    md_files = []
    if not os.path.exists(directory):
        return md_files
        
    for dirpath, _, filenames in os.walk(directory):
        if any(part.startswith('.') for part in dirpath.split(os.sep)):
            continue
        for f in filenames:
            if f.lower().endswith('.md'):
                md_files.append(os.path.join(dirpath, f))
    return md_files

def main():
    print("Tag Propagation Script")
    print("=" * 50)
    
    if DRY_RUN:
        print("DRY RUN MODE - No files will be modified")
    
    # Load tag matrix
    tag_matrix = load_tag_matrix()
    if not tag_matrix:
        print("Failed to load tag matrix. Exiting.")
        return
    
    total_files_processed = 0
    total_files_updated = 0
    
    # Process each language
    for lang_code, lang_dir in CONTENT_DIRS.items():
        print(f"\n🌍 Processing {lang_code.upper()} ({lang_dir})")
        
        md_files = find_markdown_files(lang_dir)
        print(f"   Found {len(md_files)} markdown files")
        
        files_updated = 0
        files_checked = 0
        
        for md_file in md_files:
            total_files_processed += 1
            files_checked += 1
            
            # Find corresponding English file
            english_file = find_corresponding_english_file(md_file, ENGLISH_CONTENT_DIRS)
            if not english_file:
                if files_checked <= 5:  # Only show first few for debugging
                    print(f"   ⚠ No English counterpart for {os.path.relpath(md_file)}")
                continue
            
            # Extract tags from English file
            english_tags = extract_tags_from_english_file(english_file)
            if not english_tags:
                if files_checked <= 5:  # Only show first few for debugging
                    print(f"   ⚠ No tags in English file {os.path.relpath(english_file)}")
                continue
            
            # Translate tags to target language
            translated_tags = translate_tags(english_tags, lang_code, tag_matrix)
            
            try:
                # Read target file
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Update tags
                new_content, was_updated = update_tags_in_content(content, translated_tags, md_file)
                
                if was_updated:
                    files_updated += 1
                    total_files_updated += 1
                    print(f"   ✓ Updated {os.path.relpath(md_file)} ({len(translated_tags)} tags)")
                    
                    if not DRY_RUN:
                        with open(md_file, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                elif files_checked <= 5:  # Debug info for first few files
                    print(f"   → No update needed for {os.path.relpath(md_file)}")
                            
            except Exception as e:
                print(f"   ❌ Error processing {md_file}: {e}")
        
        print(f"   📊 {lang_code.upper()}: {files_updated}/{len(md_files)} files updated")
    
    print("\n" + "=" * 50)
    print(f"📈 SUMMARY:")
    print(f"   Total files processed: {total_files_processed}")
    print(f"   Total files updated: {total_files_updated}")
    
    if DRY_RUN:
        print(f"\n🔄 Re-run with DRY_RUN = False to apply changes")

if __name__ == "__main__":
    main() 