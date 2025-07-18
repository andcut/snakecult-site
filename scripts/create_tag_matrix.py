#!/usr/bin/env python3
"""
Create Tag Matrix Script
Generates a matrix file with all English tags copied to every other language.
"""

import json
import csv
import os

# Configuration
ENGLISH_TAGS_FILE = "agent_documentation/all_english_tags.md"
OUTPUT_JSON = "data/tag_matrix.json"
OUTPUT_CSV = "data/tag_matrix.csv"

# All supported languages (excluding English which is the source)
LANGUAGES = ["en", "es", "zh", "fr", "de", "pt", "hi", "ar", "ru"]

def read_english_tags():
    """Read the English tags from the markdown file."""
    tags = []
    try:
        with open(ENGLISH_TAGS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract tags from the markdown bullet list
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('- '):
                tag = line[2:].strip()
                if tag:  # Only add non-empty tags
                    tags.append(tag)
        
        print(f"Read {len(tags)} English tags from {ENGLISH_TAGS_FILE}")
        return sorted(tags)  # Sort for consistency
        
    except Exception as e:
        print(f"Error reading English tags: {e}")
        return []

def create_tag_matrix(english_tags):
    """Create a matrix with English tags copied to all languages."""
    matrix = {}
    
    for tag in english_tags:
        matrix[tag] = {}
        for lang in LANGUAGES:
            # For now, copy English tag to all languages
            # This will be the basis for future translation
            matrix[tag][lang] = tag
    
    return matrix

def save_json_matrix(matrix, output_file):
    """Save the matrix as JSON."""
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(matrix, f, indent=2, ensure_ascii=False)
        print(f"JSON matrix saved to {output_file}")
        return True
    except Exception as e:
        print(f"Error saving JSON matrix: {e}")
        return False

def save_csv_matrix(matrix, output_file):
    """Save the matrix as CSV."""
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            # Write header
            header = ['english_tag'] + LANGUAGES
            writer.writerow(header)
            
            # Write data rows
            for tag in sorted(matrix.keys()):
                row = [tag]
                for lang in LANGUAGES:
                    row.append(matrix[tag][lang])
                writer.writerow(row)
        
        print(f"CSV matrix saved to {output_file}")
        return True
    except Exception as e:
        print(f"Error saving CSV matrix: {e}")
        return False

def main():
    print("Tag Matrix Creation Script")
    print("=" * 40)
    
    # Read English tags
    english_tags = read_english_tags()
    if not english_tags:
        print("No English tags found. Exiting.")
        return
    
    print(f"Creating matrix for {len(english_tags)} tags across {len(LANGUAGES)} languages")
    
    # Create matrix
    matrix = create_tag_matrix(english_tags)
    
    # Save in both formats
    json_success = save_json_matrix(matrix, OUTPUT_JSON)
    csv_success = save_csv_matrix(matrix, OUTPUT_CSV)
    
    if json_success and csv_success:
        print(f"\n✅ Success! Created {len(english_tags)}×{len(LANGUAGES)} tag matrix")
        print(f"   JSON: {OUTPUT_JSON}")
        print(f"   CSV:  {OUTPUT_CSV}")
    else:
        print("❌ Some files failed to save")

if __name__ == "__main__":
    main() 