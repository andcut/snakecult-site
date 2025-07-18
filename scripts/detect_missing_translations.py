#!/usr/bin/env python3
"""
Detect tags that are missing translations in i18n files.
"""
import os
import yaml
import toml
from collections import defaultdict

def get_all_tags_from_content():
    """Extract all unique tags from all content files."""
    all_tags = set()
    
    for root, dirs, files in os.walk('content'):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    # Split front matter and content
                    if content.startswith('---'):
                        parts = content.split('---', 2)
                        if len(parts) >= 2:
                            front_matter = yaml.safe_load(parts[1])
                            if front_matter and 'tags' in front_matter:
                                tags = front_matter['tags']
                                if isinstance(tags, list):
                                    all_tags.update(tags)
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")
                    continue
    
    return sorted(all_tags)

def get_translated_tags(lang_file):
    """Get translated tags from an i18n file."""
    if not os.path.exists(lang_file):
        return set()
    
    try:
        with open(lang_file, 'r', encoding='utf-8') as f:
            data = toml.load(f)
            if 'tags' in data:
                return set(data['tags'].keys())
    except Exception as e:
        print(f"Error reading {lang_file}: {e}")
    
    return set()

def main():
    print("🔍 Detecting missing tag translations...\n")
    
    # Get all tags used in content
    all_tags = get_all_tags_from_content()
    print(f"📊 Found {len(all_tags)} unique tags in content")
    
    # Check each language
    languages = ['en', 'es', 'zh', 'fr', 'de', 'pt', 'hi', 'ar', 'ru']
    
    for lang in languages:
        lang_file = f'i18n/{lang}.toml'
        translated_tags = get_translated_tags(lang_file)
        missing_tags = set(all_tags) - translated_tags
        
        print(f"\n🌍 {lang.upper()}: {len(translated_tags)}/{len(all_tags)} tags translated")
        
        if missing_tags:
            print(f"   Missing: {len(missing_tags)} tags")
            # Show a few examples
            examples = sorted(missing_tags)[:5]
            print(f"   Examples: {', '.join(examples)}")
            if len(missing_tags) > 5:
                print(f"   ... and {len(missing_tags) - 5} more")
        else:
            print("   ✅ All tags translated!")
    
    # Summary
    print(f"\n📋 Most frequently used untranslated tags:")
    tag_counts = defaultdict(int)
    
    # Count tag usage
    for root, dirs, files in os.walk('content'):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    if content.startswith('---'):
                        parts = content.split('---', 2)
                        if len(parts) >= 2:
                            front_matter = yaml.safe_load(parts[1])
                            if front_matter and 'tags' in front_matter:
                                tags = front_matter['tags']
                                if isinstance(tags, list):
                                    for tag in tags:
                                        tag_counts[tag] += 1
                except:
                    continue
    
    # Get English translations to see what's missing
    en_translated = get_translated_tags('i18n/en.toml')
    missing_from_en = set(all_tags) - en_translated
    
    if missing_from_en:
        print("\n🎯 Priority tags to translate (used frequently, not in EN file):")
        frequent_missing = sorted(missing_from_en, key=lambda x: tag_counts[x], reverse=True)[:10]
        for tag in frequent_missing:
            print(f"   {tag} (used {tag_counts[tag]} times)")

if __name__ == "__main__":
    main() 