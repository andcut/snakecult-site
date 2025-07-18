#!/usr/bin/env python3
"""
Tag Consolidation Script
Consolidates duplicate and similar tags across English markdown files.
"""

import os
import re
import sys
from pathlib import Path

# --- Configuration ---
CONTENT_DIRS = ["content/posts", "content/posts/vom"]
DRY_RUN = False  # Set to True to see changes without applying them
# --- End Configuration ---

# Tag consolidation mapping: old_tag -> new_tag
TAG_CONSOLIDATIONS = {
    # Exact duplicates (case normalization)
    "archaeology": "Archaeology",
    "diffusionism": "Diffusionism", 
    "evolution": "Evolution",
    "human origins": "Human Origins",
    "human evolution": "Human Evolution",
    "mythology": "Mythology",
    "psychology": "Psychology",
    "religious history": "Religious History",
    "ritual": "Ritual",
    "symbolism": "Symbolism",
    "deep-research": "Deep Research",
    
    # Semantic duplicates - Ancient History group
    "Ancient Civilizations": "Ancient History",
    "Ancient-History": "Ancient History", 
    "Ancient-Religion": "Ancient History",
    
    # Cognitive Science group
    "Cognitive-Revolution": "Cognitive Science",
    "Cognitive-Science": "Cognitive Science",
    "Cognition": "Cognitive Science",
    
    # Consciousness group
    "Consciousness-Studies": "Consciousness",
    
    # Cultural Diffusion group (excluding Cultural Evolution per user request)
    "Cultural-Diffusion": "Cultural Diffusion",
    "diffusion": "Cultural Diffusion",
    # Note: keeping "Cultural Evolution" separate as requested
    
    # Secret Societies group
    "Secret Knowledge": "Secret Societies",
    "Secret-Societies": "Secret Societies",
    
    # Mythology group
    "Mythic‑Studies": "Mythology",
    "World‑Mythology": "Mythology",
    
    # History of Science normalization
    "History-of-Science": "History of Science",
    
    # Mystery Cults group
    "Mysteries": "Mystery Cults",
    "Mystery-Cults": "Mystery Cults",
    
    # Ritual normalization
    "Ritual‑Practice": "Ritual",
    
    # Overly specific archaeology tags
    "Biblical Archaeology": "Archaeology",
    "Archaeoastronomy": "Archaeology",
    "Archaeological Theory": "Archaeology",
    
    # Paleolithic consolidation
    "Paleolithic-Art": "Paleolithic",
    
    # Human Origins normalization
    "Human-Origins": "Human Origins",
    
    # Deep Research normalization  
    "Deep-Research": "Deep Research",
    
    # Remove problematic tags
    "Health-Disparities": "",  # Remove entirely
    "Tag-A": "",  # Remove placeholder tag
}

def extract_and_update_tags_from_frontmatter(content, file_path):
    """
    Extracts tags from front matter, applies consolidations, and returns updated content.
    """
    lines = content.splitlines()
    
    if not lines:
        return content, False
    
    # Detect front matter type and boundaries
    if lines[0] == '---':
        front_matter_type = 'yaml'
        end_marker = '---'
        start_line = 1
    elif lines[0] == '+++':
        front_matter_type = 'toml'
        end_marker = '+++'
        start_line = 1
    else:
        return content, False  # No front matter detected
    
    try:
        end_marker_index = lines.index(end_marker, start_line)
    except ValueError:
        return content, False  # Malformed front matter
    
    front_matter_lines = lines[start_line:end_marker_index]
    updated_front_matter = []
    tags_updated = False
    
    if front_matter_type == 'yaml':
        in_tags_block = False
        i = 0
        while i < len(front_matter_lines):
            line = front_matter_lines[i]
            stripped_line = line.strip()
            
            if stripped_line.startswith('tags:'):
                # Handle inline list: tags: [tag1, tag2]
                if '[' in stripped_line and ']' in stripped_line:
                    # Extract and process inline tags
                    tag_string = stripped_line[stripped_line.find('[')+1:stripped_line.rfind(']')].strip()
                    if tag_string:
                        old_tags = [t.strip().strip('"').strip("'") for t in tag_string.split(',')]
                        new_tags = []
                        for tag in old_tags:
                            if tag in TAG_CONSOLIDATIONS:
                                new_tag = TAG_CONSOLIDATIONS[tag]
                                if new_tag:  # Only add if not empty (i.e., not being removed)
                                    new_tags.append(new_tag)
                                    if new_tag != tag:
                                        tags_updated = True
                                        print(f"  {file_path}: '{tag}' -> '{new_tag}'")
                                else:
                                    print(f"  {file_path}: Removing tag '{tag}'")
                                    tags_updated = True
                            else:
                                new_tags.append(tag)
                        
                        # Rebuild the line
                        new_tag_string = ', '.join(f'"{tag}"' for tag in new_tags if tag)
                        updated_front_matter.append(f"tags: [{new_tag_string}]")
                    else:
                        updated_front_matter.append(line)
                    
                elif stripped_line == 'tags:':
                    # Block list format
                    updated_front_matter.append(line)
                    in_tags_block = True
                else:
                    updated_front_matter.append(line)
                    
            elif in_tags_block and stripped_line.startswith('- '):
                # Process tag list item
                tag = stripped_line[2:].strip().strip('"').strip("'")
                if tag in TAG_CONSOLIDATIONS:
                    new_tag = TAG_CONSOLIDATIONS[tag]
                    if new_tag:  # Only add if not empty
                        updated_front_matter.append(f"- {new_tag}")
                        if new_tag != tag:
                            tags_updated = True
                            print(f"  {file_path}: '{tag}' -> '{new_tag}'")
                    else:
                        print(f"  {file_path}: Removing tag '{tag}'")
                        tags_updated = True
                        # Don't append the line (effectively removing it)
                else:
                    updated_front_matter.append(line)
                    
            elif in_tags_block and not line.startswith((' ', '\t')):
                # End of tags block
                in_tags_block = False
                updated_front_matter.append(line)
            else:
                updated_front_matter.append(line)
            
            i += 1
    
    else:  # TOML format
        for line in front_matter_lines:
            if line.strip().startswith('tags') and '=' in line and '[' in line and ']' in line:
                # Extract and process TOML tags
                tag_string = line[line.find('[')+1:line.rfind(']')].strip()
                if tag_string:
                    old_tags = [t.strip().strip('"').strip("'") for t in tag_string.split(',')]
                    new_tags = []
                    for tag in old_tags:
                        if tag in TAG_CONSOLIDATIONS:
                            new_tag = TAG_CONSOLIDATIONS[tag]
                            if new_tag:  # Only add if not empty
                                new_tags.append(new_tag)
                                if new_tag != tag:
                                    tags_updated = True
                                    print(f"  {file_path}: '{tag}' -> '{new_tag}'")
                            else:
                                print(f"  {file_path}: Removing tag '{tag}'")
                                tags_updated = True
                        else:
                            new_tags.append(tag)
                    
                    # Rebuild the TOML line
                    new_tag_string = ', '.join(f'"{tag}"' for tag in new_tags if tag)
                    updated_front_matter.append(f'tags = [{new_tag_string}]')
                else:
                    updated_front_matter.append(line)
            else:
                updated_front_matter.append(line)
    
    if tags_updated:
        # Reconstruct the full content
        new_content = lines[0] + '\n'  # Front matter start marker
        new_content += '\n'.join(updated_front_matter) + '\n'
        new_content += lines[end_marker_index] + '\n'  # Front matter end marker
        new_content += '\n'.join(lines[end_marker_index + 1:])  # Rest of content
        return new_content, True
    
    return content, False

def find_markdown_files(root_dirs):
    """Find all .md files in the given directories."""
    md_files = []
    for root_dir in root_dirs:
        for dirpath, _, filenames in os.walk(root_dir):
            # Skip hidden directories
            if any(part.startswith('.') for part in dirpath.split(os.sep)):
                continue
            
            for f in filenames:
                if f.lower().endswith('.md'):
                    md_files.append(os.path.join(dirpath, f))
    return md_files

def main():
    print("Tag Consolidation Script")
    print("=" * 40)
    
    if DRY_RUN:
        print("DRY RUN MODE - No files will be modified")
    
    print(f"Processing directories: {CONTENT_DIRS}")
    print(f"Consolidation rules: {len(TAG_CONSOLIDATIONS)} mappings")
    print()
    
    md_files = find_markdown_files(CONTENT_DIRS)
    print(f"Found {len(md_files)} markdown files")
    
    files_updated = 0
    total_changes = 0
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content, was_updated = extract_and_update_tags_from_frontmatter(content, md_file)
            
            if was_updated:
                files_updated += 1
                if not DRY_RUN:
                    with open(md_file, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                        
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    print()
    print("=" * 40)
    print(f"Summary:")
    print(f"  Files processed: {len(md_files)}")
    print(f"  Files updated: {files_updated}")
    
    if DRY_RUN:
        print("\nRe-run with DRY_RUN = False to apply changes")

if __name__ == "__main__":
    main() 