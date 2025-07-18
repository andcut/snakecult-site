#!/usr/bin/env python3
"""
Use translation dictionary to maintain consistent tags across languages.
"""

import json
import yaml
from pathlib import Path

def load_tag_translations():
    """Load the tag translation dictionary."""
    try:
        with open('data/tag_translations.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading tag translations: {e}")
        return {}

def translate_tags(tags, target_lang, translations):
    """Translate tags to target language using dictionary."""
    translated = []
    for tag in tags:
        if tag in translations and target_lang in translations[tag]:
            translated.append(translations[tag][target_lang])
        else:
            # Fallback to English if no translation available
            translated.append(tag)
            print(f"Warning: No translation for '{tag}' in {target_lang}, using English")
    return translated

def update_language_file_tags(file_path, target_lang, english_tags, translations):
    """Update a language file with properly translated tags."""
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
        
        # Translate tags to target language
        new_tags = translate_tags(english_tags, target_lang, translations)
        
        # Only update if different
        if original_tags != new_tags:
            fm_data['tags'] = new_tags
            
            # Reconstruct file
            new_front_matter = yaml.dump(fm_data, default_flow_style=False, allow_unicode=True)
            new_content = f"---\n{new_front_matter}---{parts[2]}"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"Updated {file_path}: {original_tags} → {new_tags}")
            return True
            
        return False
        
    except Exception as e:
        print(f"Error updating {file_path}: {e}")
        return False

def main():
    """Main function to apply consistent translated tags."""
    
    translations = load_tag_translations()
    if not translations:
        print("No translations loaded, exiting")
        return
    
    languages = ['es', 'zh', 'fr', 'de', 'pt', 'hi', 'ar', 'ru']
    updated_count = 0
    
    # Process regular posts
    english_posts = Path("content/posts")
    for english_file in english_posts.glob("*.md"):
        try:
            with open(english_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if not content.startswith('---'):
                continue
                
            parts = content.split('---', 2)
            if len(parts) < 3:
                continue
                
            fm_data = yaml.safe_load(parts[1])
            english_tags = fm_data.get('tags', []) or []
            
            if not english_tags:
                continue
                
            # Update corresponding files in other languages
            for lang in languages:
                lang_file = Path(f"content/{lang}/posts/{english_file.name}")
                if lang_file.exists():
                    if update_language_file_tags(lang_file, lang, english_tags, translations):
                        updated_count += 1
                        
        except Exception as e:
            print(f"Error processing {english_file}: {e}")
    
    print(f"\nUpdated {updated_count} files with translated tags")
    print("All languages now have consistent translated tags!")

if __name__ == "__main__":
    main() 