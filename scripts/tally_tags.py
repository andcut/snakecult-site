import os
import re
import json
from collections import Counter
import sys

# --- Configuration ---
CONTENT_DIRS = ["content/posts", "content/posts/vom"]
OUTPUT_FILE = "agent_documentation/all_english_tags.md"
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

def tally_tags(content_dirs):
    """Finds markdown files, extracts tags, and returns a list of unique tags."""
    all_tags = []
    total_files = 0
    
    for content_dir in content_dirs:
        print(f"Processing directory: {content_dir}")
        md_files = find_markdown_files(content_dir)
        print(f"Found {len(md_files)} markdown files in '{content_dir}'.")
        total_files += len(md_files)

        if not md_files:
            print(f"No markdown files found in {content_dir}.")
            continue

        files_processed = 0
        files_with_tags = 0
        for md_file in md_files:
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                tags = extract_tags_from_frontmatter(content)
                files_processed += 1
                if tags:
                    all_tags.extend(tags)
                    files_with_tags += 1
            except Exception as e:
                print(f"Error processing file {md_file}: {e}", file=sys.stderr)
        
        print(f"Processed {files_processed} files, found tags in {files_with_tags} files.")
    
    print(f"Total files processed: {total_files}")
    unique_tags = set(all_tags)
    return list(unique_tags)

def save_all_tags(tags, output_file):
    """Saves the list of all tags to an MD file."""
    tags = sorted(tags)  # Optional: sort alphabetically
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        try:
            print(f"Creating directory: {output_dir}")
            os.makedirs(output_dir)
        except OSError as e:
             print(f"Error creating directory {output_dir}: {e}", file=sys.stderr)
             
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# All English Tags\n\n")
            f.write(f"Total unique English tags: **{len(tags)}**\n\n")
            for tag in tags:
                f.write(f"- {tag}\n")
        print(f"All tags list saved to {output_file}")
    except Exception as e:
        print(f"Error saving tags to {output_file}: {e}", file=sys.stderr)

def main():
    print(f"Starting tag analysis in {CONTENT_DIRS}...")
    tag_list = tally_tags(CONTENT_DIRS)

    if not tag_list:
        print("No tags found to analyze.")
        return

    print(f"\n--- Total Unique English Tags: {len(tag_list)} ---")
        
    print("\n-----------------------")

    save_all_tags(tag_list, OUTPUT_FILE)
    print("Tag analysis complete.")

if __name__ == "__main__":
    main() 