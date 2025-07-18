#!/usr/bin/env python3
"""
Consolidate duplicate and similar tags in English posts to reduce taxonomy explosion.
"""

import os
import re
import yaml
from pathlib import Path

# Tag consolidation mapping: old_tag -> new_tag
TAG_CONSOLIDATION = {
    # Case and format fixes
    "mythology": "Mythology",
    "- mythology": "Mythology", 
    "- Mythology": "Mythology",
    
    "evolution": "Evolution",
    "- Evolution": "Evolution",
    "- evolution": "Evolution",
    
    "consciousness": "Consciousness", 
    "- Consciousness": "Consciousness",
    "- consciousness": "Consciousness",
    
    "archaeology": "Archaeology",
    "- Archaeology": "Archaeology", 
    "- archaeology": "Archaeology",
    
    "Anthropology": "Anthropology",
    "- Anthropology": "Anthropology",
    
    "psychology": "Psychology",
    "Psychology": "Psychology",
    "- psychology": "Psychology",
    "- Psychology": "Psychology",
    
    # Semantic consolidations
    "Deep-Research": "Deep-Research",
    "deep-research": "Deep-Research", 
    "- Deep-Research": "Deep-Research",
    "- deep-research": "Deep-Research",
    
    "human-origins": "Human-Origins",
    "- Human Origins": "Human-Origins",
    "- human origins": "Human-Origins",
    '"human origins"': "Human-Origins",
    "Human Origins": "Human-Origins",
    
    "genetics": "Genetics",
    "Genetics": "Genetics",
    "- Genetics": "Genetics",
    "- Human Genetics": "Human-Genetics",  # Keep this separate as more specific
    
    "Prehistory": "Prehistory", 
    "- Prehistory": "Prehistory",
    "- Paleolithic": "Prehistory",  # Merge into broader category
    
    "Neuroscience": "Neuroscience",
    "- Neuroscience": "Neuroscience",
    
    "Religion": "Religion",
    "- Religion": "Religion",
    
    "History": "History",
    "- History": "History",
    "Ancient History": "Ancient-History",  # Keep specific
    "- Religious History": "Religious-History",  # Keep specific
    "religious history": "Religious-History",
    
    # Remove redundant/overly specific ones
    "- folklore": "Mythology",  # Merge into mythology
    "symbolism": "Symbolism",
    "Symbolism": "Symbolism", 
    "- Symbolism": "Symbolism",
    
    # Standardize format for tools/instruments
    "- Bullroarer": "Bullroarer",
    "- Stone Tools": "Stone-Tools",
    
    # Fix malformed entries
    "**Chronos-Herakles** is the Orphic *macro-myth*: a winged lion-serpent that cracks the world-egg and winds the cosmic clock.": "",  # Remove malformed
    "Fresh synthesis of ~400 diagnosable Upper-Paleolithic human images.": "",  # Remove malformed
    
    # Standardize esoteric topics  
    "- Alchemy": "Alchemy",
    "- Hermeticism": "Hermeticism",
    "- Mysticism": "Mysticism",
    "Gnosticism": "Gnosticism",
    "- Gnosticism": "Gnosticism",
    
    # Consciousness-related (merge some)
    "Cognitive Revolution": "Cognitive-Revolution",
    "cognitive science": "Cognitive-Science",
    "- Cognition": "Cognition",
    "cognition": "Cognition",
    
    # Geographic
    "- Americas": "Americas",
    "- Africa": "Africa", 
    "- Egypt": "Egypt",
    "China": "China",
}

def clean_tag(tag):
    """Clean and normalize a tag string."""
    if not tag or not tag.strip():
        return None
    
    # Remove quotes and extra whitespace
    cleaned = tag.strip().strip('"').strip("'").strip()
    
    # Apply consolidation mapping
    if cleaned in TAG_CONSOLIDATION:
        result = TAG_CONSOLIDATION[cleaned]
        return result if result else None  # Empty string means delete
    
    return cleaned

def process_markdown_file(filepath):
    """Process a single markdown file to consolidate tags."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split front matter and content
        if not content.startswith('---'):
            return False
            
        parts = content.split('---', 2)
        if len(parts) < 3:
            return False
            
        front_matter = parts[1]
        body = parts[2]
        
        # Parse YAML front matter
        try:
            fm_data = yaml.safe_load(front_matter)
        except yaml.YAMLError:
            print(f"Error parsing YAML in {filepath}")
            return False
        
        # Process tags
        if 'tags' in fm_data and fm_data['tags']:
            original_tags = fm_data['tags']
            
            # Clean and consolidate tags
            new_tags = []
            for tag in original_tags:
                cleaned = clean_tag(str(tag))
                if cleaned and cleaned not in new_tags:
                    new_tags.append(cleaned)
            
            # Only update if tags changed
            if new_tags != original_tags:
                fm_data['tags'] = new_tags
                
                # Reconstruct the file
                new_front_matter = yaml.dump(fm_data, default_flow_style=False, allow_unicode=True)
                new_content = f"---\n{new_front_matter}---{body}"
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print(f"Updated tags in {filepath}")
                print(f"  Old: {original_tags}")
                print(f"  New: {new_tags}")
                return True
        
        return False
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    """Main function to process all English posts."""
    posts_dir = Path("content/posts")
    updated_count = 0
    
    for md_file in posts_dir.glob("*.md"):
        if process_markdown_file(md_file):
            updated_count += 1
    
    print(f"\nProcessed {updated_count} files with tag updates")

if __name__ == "__main__":
    main() 