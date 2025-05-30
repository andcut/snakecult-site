import os
import re
import json
from collections import Counter
import sys

# --- Configuration ---
CONTENT_DIR = "content"
OUTPUT_FILE = "data/tags.json"
# --- End Configuration ---

def extract_tags_from_frontmatter(content):
    """Extracts tags from TOML or YAML front matter using basic string parsing."""
    tags = []
    front_matter_lines = []
    front_matter_type = None # 'toml' or 'yaml'
    
    lines = content.splitlines()
    
    if not lines:
        return []

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
        return [] # No front matter detected

    # Extract front matter lines
    try:
        end_marker_index = lines.index(end_marker, start_line)
        front_matter_lines = lines[start_line:end_marker_index]
    except ValueError:
        # print(f"Warning: Could not find end marker '{end_marker}' for front matter.", file=sys.stderr)
        return [] # Malformed front matter
    
    if not front_matter_lines:
        return [] 

    tag_line_found = False
    if front_matter_type == 'toml':
        # Basic TOML parsing for tags = ["tag1", "tag2"]
        for line in front_matter_lines:
            line = line.strip()
            if line.startswith('tags') and '=' in line and '[' in line and ']' in line:
                try:
                    # Extract the list content, remove quotes, split
                    tag_string = line[line.find('[')+1:line.rfind(']')].strip()
                    if tag_string: # Handle empty tags list
                        tags = [t.strip().strip('"').strip("'") for t in tag_string.split(',')]
                    tag_line_found = True
                    break
                except Exception as e:
                    print(f"Warning: Could not parse TOML tags line: {line} - {e}", file=sys.stderr)
                    return [] # Return empty list on parsing error
    elif front_matter_type == 'yaml':
        # Basic YAML parsing for tags: [tag1, tag2] or tags:
        #  - tag1
        #  - tag2
        in_tags_block = False
        for i, line in enumerate(front_matter_lines):
            stripped_line = line.strip()
            
            if stripped_line.startswith('tags:'):
                tag_line_found = True
                # Check for inline list: tags: [tag1, tag2]
                if '[' in stripped_line and ']' in stripped_line:
                    try:
                        tag_string = stripped_line[stripped_line.find('[')+1:stripped_line.rfind(']')].strip()
                        if tag_string:
                            tags = [t.strip().strip('"').strip("'") for t in tag_string.split(',')]
                        break # Found inline list, exit loop for this file
                    except Exception as e:
                        print(f"Warning: Could not parse YAML inline tags line: {line} - {e}", file=sys.stderr)
                        return [] # Return empty list on parsing error
                # Check for block list starting on the same line: tags:
                elif stripped_line == 'tags:':
                     in_tags_block = True
                # Continue to next line after finding 'tags:' to process items
                continue 

            if in_tags_block:
                # Check for list item
                if stripped_line.startswith('- '):
                    tags.append(stripped_line[2:].strip().strip('"').strip("'"))
                # If indentation decreases or line doesn't start appropriately, assume block ended
                # This basic check assumes consistent indentation for the block
                elif not line.startswith((' ', '\t')): 
                    in_tags_block = False
                    # Don't break here, might be other fields after tags block

    # Clean up empty strings that might result from parsing errors or empty tags
    tags = [tag for tag in tags if tag]
    # if not tag_line_found:
        # print(f"Warning: 'tags' key not found in front matter.", file=sys.stderr)
        
    return tags

def find_markdown_files(root_dir):
    """Recursively finds all .md files in the given directory."""
    md_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        # Skip hidden directories like .git
        if any(part.startswith('.') for part in dirpath.split(os.sep)):
            continue
            
        for f in filenames:
            if f.lower().endswith('.md'):
                md_files.append(os.path.join(dirpath, f))
    return md_files

def tally_tags(content_dir):
    """Finds markdown files, extracts tags, and returns a frequency counter."""
    all_tags = []
    md_files = find_markdown_files(content_dir)
    print(f"Found {len(md_files)} markdown files in '{content_dir}'.")

    if not md_files:
        print("No markdown files found.")
        return Counter()

    files_processed = 0
    files_with_tags = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            tags = extract_tags_from_frontmatter(content)
            files_processed += 1
            if tags:
                # print(f"  Found tags {tags} in {md_file}") # Debugging
                all_tags.extend(tags)
                files_with_tags += 1
            # else: # Debugging
                # print(f"  No tags found in {md_file}") # Debugging
        except Exception as e:
            print(f"Error processing file {md_file}: {e}", file=sys.stderr)
    
    print(f"Processed {files_processed} files, found tags in {files_with_tags} files.")
            
    # Normalize tags (lowercase, remove extra spaces)
    normalized_tags = [tag.lower().strip() for tag in all_tags]
    
    return Counter(normalized_tags)

def save_unique_tags(tag_counter, output_file):
    """Saves the unique tags (sorted) to a JSON file."""
    unique_tags = sorted(list(tag_counter.keys()))
    
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        try:
            print(f"Creating directory: {output_dir}")
            os.makedirs(output_dir)
        except OSError as e:
             print(f"Error creating directory {output_dir}: {e}", file=sys.stderr)
             # Decide if we should exit or try saving to root? For now, let it fail later.
             pass 
        
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(unique_tags, f, indent=2)
        print(f"Unique tags list saved to {output_file}")
    except Exception as e:
        print(f"Error saving tags to {output_file}: {e}", file=sys.stderr)

def main():
    print(f"Starting tag analysis in '{CONTENT_DIR}'...")
    tag_counts = tally_tags(CONTENT_DIR)

    if not tag_counts:
        print("No tags found to analyze.")
        return

    print("\n--- Tag Frequencies ---")
    if tag_counts:
        # Sort by frequency descending, then alphabetically
        sorted_tags = sorted(tag_counts.items(), key=lambda item: (-item[1], item[0]))
        for tag, count in sorted_tags:
            print(f"- {tag}: {count}")
    else:
        print("No tags found.")
        
    print("\n-----------------------")

    save_unique_tags(tag_counts, OUTPUT_FILE)
    print("Tag analysis complete.")

if __name__ == "__main__":
    main() 