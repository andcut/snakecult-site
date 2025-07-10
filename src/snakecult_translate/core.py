"""
Core translation functionality shared across all translation modes.
"""

import datetime
from pathlib import Path
from typing import Optional

import frontmatter
from openai import OpenAI

from .models import choose_model_for_tokens
from .prompts import get_system_prompt
from .utils import count_tokens, split_text_into_chunks


def translate_text(
    client: OpenAI,
    text: str,
    target_lang: str = "es",
    model: str = "gpt-4o",
    web_format: bool = False,
    temperature: Optional[float] = None
) -> Optional[str]:
    """Translate text using OpenAI API."""
    
    system_prompt = get_system_prompt(target_lang, web_format)
    
    try:
        kwargs = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text}
            ]
        }
        
        # Some models (e.g. o3) currently do not accept custom temperature values
        if temperature is not None:
            if model.startswith("o3") and abs(temperature - 1.0) > 1e-5:
                print(f"⚠️  Model '{model}' ignores non-default temperature; proceeding with default (1.0).")
            else:
                kwargs["temperature"] = temperature

        response = client.chat.completions.create(**kwargs)
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        print(f"Translation error: {e}")
        return None


def create_translated_frontmatter(original_fm: dict, target_lang: str, model_name: str = "gpt-4o") -> dict:
    """Return a copy of front-matter with language/meta fields updated for the translation.

    This keeps most keys intact (date, slug, etc.) and only touches:
    • lang – new language code
    • translation_model – which LLM produced the text
    • lastmod – timestamp of translation
    """

    fm = original_fm.copy()

    # Required language metadata
    fm["lang"] = target_lang

    # Track provenance so we can later filter / re-translate if model versions change
    fm["translation_model"] = model_name

    # Always refresh last modified date
    fm["lastmod"] = datetime.date.today().isoformat()

    return fm

# Alias removed; use create_translated_frontmatter everywhere


def translate_file(
    src_path: Path,
    dst_path: Path,
    target_lang: str = "es",
    model: str = "gpt-4o",
    api_key: Optional[str] = None,
    web_format: bool = False,
    temperature: Optional[float] = None,
    *,
    chunk: bool = False,
    chunk_size_chars: int = 25000,
    auto_model: bool = True
) -> bool:
    """Translate a single markdown file, optionally in chunks and with automatic model selection."""
    
    if not api_key:
        print("Error: OpenAI API key required. Set OPENAI_API_KEY environment variable.")
        return False
    
    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)
    
    # Read source file
    try:
        with open(src_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
    except Exception as e:
        print(f"Error reading {src_path}: {e}")
        return False
    
    print(f"Translating: {src_path}")
    
    # Estimate tokens
    content_tokens = count_tokens(post.content)
    title_tokens = count_tokens(post.metadata.get('title', ''))
    total_tokens = content_tokens + title_tokens
    
    print(f"Estimated tokens: {total_tokens:,}")
    
    # Translate title if present
    translated_title = post.metadata.get('title', '')
    if translated_title:
        print("Translating title...")
        translated_title = translate_text(client, translated_title, target_lang, model, web_format, temperature)
        if not translated_title:
            print("Failed to translate title")
            return False
    
    # Translate main content (with optional chunking)
    # Check if content is empty or just whitespace/comments
    content_to_translate = post.content.strip()
    if not content_to_translate or content_to_translate.startswith('<!--') and content_to_translate.endswith('-->'):
        print("Content is empty or just comments - skipping content translation")
        translated_content = post.content  # Keep original content
    elif not chunk:
        chosen_model = choose_model_for_tokens(content_tokens, model, auto_model)
        print(f"Translating content using model: {chosen_model} ...")
        translated_content = translate_text(client, post.content, target_lang, chosen_model, web_format, temperature)
        if not translated_content:
            print("Failed to translate content")
            return False
    else:
        print("Chunking enabled – splitting content and translating each chunk…")
        chunks = split_text_into_chunks(post.content, chunk_size_chars)
        translated_chunks = []
        for idx, ch in enumerate(chunks, start=1):
            est_tokens = count_tokens(ch)
            chosen_model = choose_model_for_tokens(est_tokens, model, auto_model)
            print(f"  → Chunk {idx}/{len(chunks)} (approx {est_tokens:,} tokens) with model {chosen_model}")
            translated = translate_text(client, ch, target_lang, chosen_model, web_format, temperature)
            if not translated:
                print(f"Failed to translate chunk {idx}")
                return False
            translated_chunks.append(translated)
        # Join the chunks with clear delimiters (HTML comment so it won't show when rendered)
        translated_content = "\n\n<!-- CHUNK BREAK -->\n\n".join(translated_chunks)
    
    # Create translated frontmatter
    translated_fm = create_translated_frontmatter(post.metadata, target_lang, model)
    if translated_title:
        translated_fm['title'] = translated_title

    # Translate frontmatter fields in one shot
    translated_fm = translate_frontmatter_block(
        client,
        translated_fm,
        target_lang,
        model,
        web_format,
        temperature
    )

    # Fallback: if certain fields remain identical to English after block translation
    for fld in ["description", "keywords", "tags", "about"]:
        if fld in translated_fm:
            if translated_fm[fld] == post.metadata.get(fld):
                # For lists translate each item; for str translate direct
                if isinstance(translated_fm[fld], list):
                    translated_list = []
                    for item in translated_fm[fld]:
                        trans_item = translate_text(
                            client,
                            item,
                            target_lang,
                            model,
                            web_format,
                            temperature
                        ) or item
                        translated_list.append(trans_item)
                    translated_fm[fld] = translated_list
                elif isinstance(translated_fm[fld], str):
                    trans_val = translate_text(
                        client,
                        translated_fm[fld],
                        target_lang,
                        model,
                        web_format,
                        temperature
                    )
                    if trans_val:
                        translated_fm[fld] = trans_val

    # Fallback: core_entity sometimes remains unchanged because the block translator
    # treats it as a proper noun. If we detect that it's still identical to the
    # English and the target language is not English, attempt a single-field
    # translation.
    if target_lang != "en" and "core_entity" in translated_fm:
        original_core = post.metadata.get("core_entity", "")
        if translated_fm["core_entity"] == original_core and isinstance(original_core, str):
            translated_core = translate_text(
                client,
                original_core,
                target_lang,
                model,
                web_format,
                temperature
            )
            if translated_core:
                translated_fm["core_entity"] = translated_core

    # Create new post with translated content
    translated_post = frontmatter.Post(translated_content, **translated_fm)
    
    # Ensure destination directory exists
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write translated file
    try:
        with open(dst_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(translated_post))
        print(f"Saved: {dst_path}")
        return True
    except Exception as e:
        print(f"Error writing {dst_path}: {e}")
        return False


def translate_frontmatter_block(
    client: OpenAI,
    frontmatter_dict: dict,
    target_lang: str = "es",
    model: str = "gpt-4o",
    web_format: bool = False,
    temperature: Optional[float] = None
) -> dict:
    """Translate entire frontmatter block in one API call."""
    
    # Extract translatable fields
    translatable_fields = {}
    for field in ['title', 'description', 'keywords', 'tags', 'about', 'core_entity']:
        if field in frontmatter_dict and frontmatter_dict[field]:
            translatable_fields[field] = frontmatter_dict[field]
    
    if not translatable_fields:
        return frontmatter_dict
    
    # Build YAML snippet for translation
    import yaml
    yaml_snippet = yaml.dump(translatable_fields, default_flow_style=False, allow_unicode=True)
    
    # Craft prompt for frontmatter translation
    lang_names = {
        "es": "Spanish (Mexican)",
        "zh": "Simplified Chinese",
        "fr": "French",
        "de": "German"
    }
    lang_name = lang_names.get(target_lang, target_lang)
    
    prompt = f"""Translate the following YAML frontmatter fields to {lang_name}:

```yaml
{yaml_snippet}```

RULES:
1. Translate ONLY the values, never the field names (title:, description:, etc.)
2. Keep proper nouns unchanged (names, places like "El Arenal", technical terms like "pharmakon")
3. For list items, translate each item but preserve the YAML list structure
4. Output only the translated YAML block, no explanations
5. Maintain academic/scholarly tone"""

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=temperature or 0.2
        )
        
        translated_yaml = response.choices[0].message.content.strip()
        
        # Clean up markdown code fences if present
        if translated_yaml.startswith('```yaml'):
            translated_yaml = translated_yaml[7:]
        if translated_yaml.endswith('```'):
            translated_yaml = translated_yaml[:-3]
        translated_yaml = translated_yaml.strip()
        
        # Parse translated YAML
        try:
            translated_fields = yaml.safe_load(translated_yaml)
            if not isinstance(translated_fields, dict):
                print("Warning: Translation didn't return a dict, using original frontmatter")
                return frontmatter_dict
                
            # Merge back into original frontmatter
            result_fm = frontmatter_dict.copy()
            result_fm.update(translated_fields)

            # Placeholder cleanup for keywords/tags
            for field in ("keywords", "tags"):
                if field in result_fm and isinstance(result_fm[field], list):
                    cleaned = []
                    for kw in result_fm[field]:
                        if kw.lower() in {"keyword-one", "keyword-two", "main-theme"}:
                            continue
                        # kebab-case normalisation
                        cleaned.append(
                            kw.lower().replace(" ", "-").replace("_", "-")
                        )
                    result_fm[field] = cleaned

            # Ensure title doesn't keep doubled apostrophes
            if "title" in result_fm and isinstance(result_fm["title"], str):
                result_fm["title"] = result_fm["title"].replace("''", "'")

            return result_fm
            
        except yaml.YAMLError as e:
            print(f"Warning: Could not parse translated YAML: {e}")
            print(f"Raw response: {translated_yaml}")
            return frontmatter_dict
            
    except Exception as e:
        print(f"Frontmatter translation error: {e}")
        return frontmatter_dict 