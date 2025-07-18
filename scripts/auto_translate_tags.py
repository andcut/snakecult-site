#!/usr/bin/env python3
"""
Auto-generate missing tag translations using simple rules.
For production, you could integrate with OpenAI API for better translations.
"""
import os
import toml
import yaml
from collections import defaultdict

# Simple translation dictionaries (you could replace this with AI translation)
TRANSLATIONS = {
    'es': {
        'Quantum-Physics': 'Física-Cuántica',
        'Machine-Learning': 'Aprendizaje-Automático',
        'Artificial-Intelligence': 'Inteligencia-Artificial',
        'Space-Exploration': 'Exploración-Espacial',
        'Climate-Science': 'Ciencia-Climática',
        'Biotechnology': 'Biotecnología',
        'Robotics': 'Robótica',
        'Cybersecurity': 'Ciberseguridad',
        'Blockchain': 'Blockchain',
        'Virtual-Reality': 'Realidad-Virtual',
    },
    'zh': {
        'Quantum-Physics': '量子物理',
        'Machine-Learning': '机器学习',
        'Artificial-Intelligence': '人工智能',
        'Space-Exploration': '太空探索',
        'Climate-Science': '气候科学',
        'Biotechnology': '生物技术',
        'Robotics': '机器人学',
        'Cybersecurity': '网络安全',
        'Blockchain': '区块链',
        'Virtual-Reality': '虚拟现实',
    },
    'fr': {
        'Quantum-Physics': 'Physique-Quantique',
        'Machine-Learning': 'Apprentissage-Automatique',
        'Artificial-Intelligence': 'Intelligence-Artificielle',
        'Space-Exploration': 'Exploration-Spatiale',
        'Climate-Science': 'Science-Climatique',
        'Biotechnology': 'Biotechnologie',
        'Robotics': 'Robotique',
        'Cybersecurity': 'Cybersécurité',
        'Blockchain': 'Blockchain',
        'Virtual-Reality': 'Réalité-Virtuelle',
    }
}

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
                        
                    if content.startswith('---'):
                        parts = content.split('---', 2)
                        if len(parts) >= 2:
                            front_matter = yaml.safe_load(parts[1])
                            if front_matter and 'tags' in front_matter:
                                tags = front_matter['tags']
                                if isinstance(tags, list):
                                    all_tags.update(tags)
                except Exception as e:
                    continue
    
    return sorted(all_tags)

def update_i18n_file(lang, new_translations):
    """Add new translations to an i18n file."""
    lang_file = f'i18n/{lang}.toml'
    
    # Load existing translations
    data = {'tags': {}}
    if os.path.exists(lang_file):
        try:
            with open(lang_file, 'r', encoding='utf-8') as f:
                data = toml.load(f)
                if 'tags' not in data:
                    data['tags'] = {}
        except Exception as e:
            print(f"Error reading {lang_file}: {e}")
    
    # Add new translations
    data['tags'].update(new_translations)
    
    # Write back to file
    try:
        with open(lang_file, 'w', encoding='utf-8') as f:
            f.write(f"# {lang.upper()} tag display names\n")
            toml.dump(data, f)
        return True
    except Exception as e:
        print(f"Error writing {lang_file}: {e}")
        return False

def main():
    print("🤖 Auto-generating missing tag translations...\n")
    
    # Get all tags from content
    all_tags = get_all_tags_from_content()
    
    # Process each language
    for lang, translations in TRANSLATIONS.items():
        lang_file = f'i18n/{lang}.toml'
        
        # Get existing translations
        existing = {}
        if os.path.exists(lang_file):
            try:
                with open(lang_file, 'r', encoding='utf-8') as f:
                    data = toml.load(f)
                    if 'tags' in data:
                        existing = data['tags']
            except:
                pass
        
        # Find missing translations we can auto-generate
        new_translations = {}
        for tag in all_tags:
            if tag not in existing and tag in translations:
                new_translations[tag] = translations[tag]
        
        # Update file if we have new translations
        if new_translations:
            print(f"🌍 {lang.upper()}: Adding {len(new_translations)} new translations")
            for eng, translated in new_translations.items():
                print(f"   {eng} → {translated}")
            
            if update_i18n_file(lang, new_translations):
                print(f"   ✅ Updated {lang_file}")
            else:
                print(f"   ❌ Failed to update {lang_file}")
        else:
            print(f"🌍 {lang.upper()}: No new auto-translations available")
    
    print(f"\n💡 Pro tip: For tags not auto-translated, they'll show in English")
    print(f"   Add manual translations to i18n/*.toml files as needed")

if __name__ == "__main__":
    main() 