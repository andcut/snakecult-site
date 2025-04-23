import os
import sys
import re
import json # Used only for formatting the output list of tags

# --- Configuration ---
CONTENT_DIR = "content"
# Define the consolidation rules: lowercase 'old_tag': 'new_tag'
CONSOLIDATION_RULES = {
    "deep research": "deep-research",
    "evolution of consciousness": "consciousness",
    "social evolution": "evolution",
    "gene–culture co-evolution": "evolution", # Note: using en dash '–' as seen in the tally output
    "consciousness studies": "consciousness",
    "eve theory of consciousness": "consciousness",
    "hard problem of consciousness": "consciousness",
    "ritual studies": "ritual",
    "ritualised mind hypothesis": "ritual", # Assuming 'ritualised' spelling is consistent
    "comparative mythology": "mythology",
    "creation myths": "mythology",
    "recursive thinking": "recursion",
    "comparative religion": "religion",
    "theology": "religion",
    "gnosticism": "religion",
    "christianity": "religion",
    "ancient history": "prehistory",
    "paleolithic": "prehistory",
    "cultural origins": "human origins",
    "metaphysics": "philosophy",
    "theorists": "philosophy",
    "oral history": "narrative",
    "folklore": "narrative",
    "self-awareness": "psychology",
    "selfhood": "psychology",
    "social brain": "psychology",
    "self-domestication": "psychology",
    "cognitive-science": "cognitive science" # Normalize hyphen
}
# --- End Configuration ---

def find_markdown_files(root_dir):
    """Recursively finds all .md files in the given directory."""
    md_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        # Skip hidden directories like .git
        parts = dirpath.split(os.sep)
        if any(part.startswith('.') for part in parts):
            continue
            
        for f in filenames:
            if f.lower().endswith('.md'):
                md_files.append(os.path.join(dirpath, f))
    return md_files

def apply_consolidation(tags):
    """Applies consolidation rules to a list of tags."""
    updated_tags = set() # Use a set to handle potential duplicates after consolidation
    changed = False
    original_lower_tags = set(t.lower().strip() for t in tags)
    
    for tag in tags:
        original_tag_val = tag # Keep original tag value
        lower_tag = tag.lower().strip()
        
        if lower_tag in CONSOLIDATION_RULES:
            new_tag = CONSOLIDATION_RULES[lower_tag]
            updated_tags.add(new_tag)
            if new_tag != lower_tag: # Check if the rule actually changed the tag
                changed = True
        else:
            updated_tags.add(original_tag_val) # Keep the original tag if no rule matches

    # Sort for consistent output order in files
    final_tags = sorted(list(updated_tags))
    
    # Determine if changes occurred more robustly
    final_lower_tags = set(t.lower().strip() for t in final_tags)
    
    # Changed if the set of lowercased tags is different OR if the number of tags changed (due to duplicates merging)
    if final_lower_tags != original_lower_tags or len(final_tags) != len(tags):
        changed = True
         
    return final_tags, changed

def update_front_matter(lines):
    """Finds the tags line/block, applies consolidation, and returns updated lines."""
    
    if not lines: 
        return lines, False

    front_matter_type = None
    end_marker = None
    start_line = 0
    tags_line_index = -1 # For inline tags: or tags = 
    # For YAML block tags like: tags:
    #   - tag1
    tags_block_start_index = -1 
    tags_block_end_index = -1 # Line index *after* the last tag in a block
    current_tags = []
    original_tags_repr = "" # Store original representation if possible for comparison
    
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
        return lines, False # No front matter

    # Find end marker index
    try:
        end_marker_index = lines.index(end_marker, start_line)
    except ValueError:
        return lines, False # Malformed

    front_matter_lines_indices = range(start_line, end_marker_index)
    
    # --- Locate Existing Tags ---
    if front_matter_type == 'toml':
        # Look for tags = [...]
        tag_re = re.compile(r"^\s*tags\s*=\s*(\[.*\])")
        for i in front_matter_lines_indices:
            match = tag_re.match(lines[i])
            if match:
                tags_line_index = i
                original_tags_repr = match.group(1)
                try:
                    # Use json.loads for robust parsing of the list part
                    current_tags = json.loads(original_tags_repr)
                    if not isinstance(current_tags, list):
                        current_tags = [] # Ensure it's a list
                        raise ValueError("Parsed TOML tags is not a list")
                    # Clean strings just in case
                    current_tags = [str(t).strip() for t in current_tags if str(t).strip()] 
                except Exception as e:
                    print(f"  Warning: Could not json parse existing TOML tags: {original_tags_repr} - {e}", file=sys.stderr)
                    current_tags = [] # Reset if parsing fails
                break # Found the TOML tags line

    elif front_matter_type == 'yaml':
        # Look for tags: [...] (inline) or tags:
        #   - tag1... (block)
        inline_tag_re = re.compile(r"^\s*tags\s*:\s*(\[.*\])")
        block_tag_start_re = re.compile(r"^\s*tags\s*:")
        block_item_re = re.compile(r"^\s*-\s+(.*)")
        
        in_tags_block = False
        for i in front_matter_lines_indices:
            line = lines[i]
            stripped_line = line.strip()
            
            # Check for inline first
            inline_match = inline_tag_re.match(line)
            if inline_match:
                tags_line_index = i
                original_tags_repr = inline_match.group(1)
                try:
                    # Use json.loads for robust parsing of the list part
                    current_tags = json.loads(original_tags_repr)
                    if not isinstance(current_tags, list):
                        current_tags = []
                        raise ValueError("Parsed YAML inline tags is not a list")
                    current_tags = [str(t).strip() for t in current_tags if str(t).strip()]
                except Exception as e:
                    print(f"  Warning: Could not json parse existing YAML inline tags: {original_tags_repr} - {e}", file=sys.stderr)
                    current_tags = []
                break # Found inline list, stop searching

            # Check for block start
            if not in_tags_block and block_tag_start_re.match(line):
                # Ensure it's not the inline match we just handled
                if tags_line_index != i: 
                    in_tags_block = True
                    tags_block_start_index = i
                    current_tags = [] # Reset for block parsing
                    continue # Move to next line for block items

            # Process block items
            if in_tags_block:
                item_match = block_item_re.match(line)
                if item_match:
                    tag_value = item_match.group(1).strip()
                    # Handle potential quotes around the tag
                    if (tag_value.startswith('"') and tag_value.endswith('"')) or \
                       (tag_value.startswith("'") and tag_value.endswith("'")):
                        tag_value = tag_value[1:-1]
                    current_tags.append(tag_value)
                # Block ends if indentation decreases or non-item found
                # Simple check: if line is not indented or not a list item
                elif not line.startswith((' ', '\t')) or not stripped_line.startswith('-'):
                    tags_block_end_index = i # Block ends *before* this line
                    in_tags_block = False
                    # Don't break, need to continue scanning rest of front matter
                    
        # If block was still open at the end of front matter
        if in_tags_block:
            tags_block_end_index = end_marker_index

    # --- Apply Consolidation ---
    if not current_tags and tags_line_index == -1 and tags_block_start_index == -1:
        return lines, False # No tags found

    # print(f"  Found tags: {current_tags}") # Debug
    new_tags, changed = apply_consolidation(current_tags)
    
    if not changed:
        # print(f"  No changes needed for tags.") # Debug
        return lines, False

    print(f"  Updating tags: {current_tags} -> {new_tags}") # Debug/Info

    # --- Reconstruct Front Matter ---
    new_lines = list(lines) # Make a mutable copy

    if tags_line_index != -1: # Handle TOML or YAML inline list update
        indent = lines[tags_line_index][:len(lines[tags_line_index]) - len(lines[tags_line_index].lstrip())]
        # Use json.dumps to create a valid JSON array representation, which works for both TOML and basic YAML inline
        formatted_tags_list = json.dumps(new_tags) 
        
        if front_matter_type == 'toml':
            new_lines[tags_line_index] = f"{indent}tags = {formatted_tags_list}"
        elif front_matter_type == 'yaml':
            new_lines[tags_line_index] = f"{indent}tags: {formatted_tags_list}"

    elif tags_block_start_index != -1: # Handle YAML block list update
        # Get indent from the 'tags:' line itself
        indent = lines[tags_block_start_index][:len(lines[tags_block_start_index]) - len(lines[tags_block_start_index].lstrip())]
        item_indent = indent + '  ' # Standard 2-space indent for YAML list items
        
        # Create new tag lines, quote if necessary (simple check for spaces)
        new_tag_lines = []
        for tag in new_tags:
            # Basic quoting heuristic: quote if space or special chars present
            # A proper YAML library would be better, but avoid dependency for now.
            if ' ' in tag or ':' in tag or '#' in tag: 
                # Use json.dumps for safe quoting
                new_tag_lines.append(f"{item_indent}- {json.dumps(tag)}")
            else:
                new_tag_lines.append(f"{item_indent}- {tag}")

        
        # Replace old block lines with new ones
        # Remove lines from (start_index + 1) up to (but not including) end_index
        del new_lines[tags_block_start_index + 1 : tags_block_end_index]
        # Insert new lines after the 'tags:' line
        new_lines[tags_block_start_index + 1 : tags_block_start_index + 1] = new_tag_lines
        
    else:
        # This case should ideally not be reached if tags were found
        print("  Error: Could not determine how to rewrite tags.", file=sys.stderr)
        return lines, False 

    return new_lines, True


def main():
    print(f"Starting one-off tag consolidation in '{CONTENT_DIR}'...")
    md_files = find_markdown_files(CONTENT_DIR)
    print(f"Found {len(md_files)} markdown files.")

    files_modified = 0
    files_error = 0

    for md_file in md_files:
        # print(f"Processing: {md_file}") # Debug
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                # Read preserving line endings if possible? readlines() might be better but splitlines is simpler
                original_content = f.read()
                original_lines = original_content.splitlines()

            if not original_lines: continue # Skip empty files

            new_lines, modified = update_front_matter(original_lines)

            if modified:
                print(f"  Modified: {md_file}")
                # Determine original line ending (simple check)
                line_ending = '\n'
                if '\r\n' in original_content:
                    line_ending = '\r\n'
                elif '\r' in original_content:
                    line_ending = '\r'

                # Write back the changes using the detected line ending
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(line_ending.join(new_lines) + line_ending) 
                files_modified += 1

        except Exception as e:
            print(f"Error processing file {md_file}: {e}", file=sys.stderr)
            files_error += 1

    print(f"\nConsolidation complete.")
    print(f"Files modified: {files_modified}")
    if files_error > 0:
        print(f"Files with errors: {files_error}")

if __name__ == "__main__":
    main() 