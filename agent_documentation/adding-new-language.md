# Adding a New Language to Snakecult.net

This guide explains all the steps required to add a new language to the Hugo multilingual site.

## Overview

The site uses Hugo's multilingual capabilities with content organized in language-specific directories under `content/`. Each language needs both configuration and content files to work properly.

## Step 1: Update Hugo Configuration

Add the new language to `config/_default/config.toml` in the `[languages]` section:

```toml
[languages.xx]
  weight = N
  languageName = "Language Name"
  title = "Translated Site Title"
  languageCode = "xx-xx"
```

**Parameters:**
- `xx`: ISO 639-1 language code (e.g., `fr`, `de`, `zh`)
- `N`: Weight determines menu order (increment from existing languages)
- `languageName`: Native language name (e.g., "Français", "Deutsch", "中文")
- `title`: Translated version of the site title
- `languageCode`: Full locale code (e.g., `fr-fr`, `de-de`, `zh-cn`)

**Example:**
```toml
[languages.fr]
  weight = 4
  languageName = "Français"
  title = "Comment les Humains ont Évolué"
  languageCode = "fr-fr"
```

## Step 2: Create Language Content Directory

Create the language directory structure:

```bash
mkdir -p content/xx
mkdir -p content/xx/posts
mkdir -p content/xx/topics
```

## Step 3: Create Essential Pages

The following pages are **required** for Hugo to properly build the language section:

### 3.1 Homepage (`content/xx/_index.md`)

Translate the main homepage from `content/_index.md`. Key elements:
- Front matter with `lang: xx` and `translation_model: gpt-4o`
- Translated title, description, keywords
- Main heading and TL;DR section
- Topics and About sections
- **Important:** Update the relref link to point to the language-specific overview: `{{< relref "/xx/etoc-overview.md" >}}`

### 3.2 About Page (`content/xx/about.md`)

Translate from `content/about.md`:
- Personal bio and research background
- Eve Theory explanation
- All section headings and content
- Preserve external links (vectorsofmind.com, etc.)

### 3.3 Recent Updates Page (`content/xx/recent.md`)

Simple page with layout reference:
```yaml
---
title: "Translated Recent Title"
layout: "recent"
url: "/recent/"
lang: xx
lastmod: '2025-07-07'
translation_model: gpt-4o
---

<!-- Animation comment in target language -->
```

### 3.4 Eve Theory Overview (`content/xx/etoc-overview.md`)

Translate the comprehensive overview from `content/etoc-overview.md`:
- This is a large file (~347 lines)
- Use the translation CLI tool for efficiency
- Contains core theory explanations

### 3.5 Topics Index (`content/xx/topics/_index.md`)

Simple topics listing page:
```yaml
---
title: "Translated Topics Title"
description: "Browse articles by topic"
layout: "topics"
lang: xx
lastmod: '2025-07-07'
translation_model: gpt-4o
---
```

## Step 4: Translate Articles

Use the translation CLI tool to translate individual articles:

```bash
python -m src.snakecult_translate.cli_one content/posts/article-name.md --lang xx --dst-root content/xx --model gpt-4o
```

**Translation Process:**
1. Start with high-priority articles (those with `quality: 6` or higher)
2. The CLI automatically handles:
   - Front matter translation (title, description, keywords, tags)
   - Content translation using appropriate language prompts
   - Markdown structure preservation
   - Citation and link preservation

**Batch Translation:**
For multiple articles, create a script or use the batch translation tools in `src/snakecult_translate/`.

## Step 5: Test the Build

Verify everything works:

```bash
hugo --minify --destination public_test
```

**Expected output:**
- No build errors
- Language shows up in the stats table (e.g., `| XX | 14 |`)
- Check `public_test/xx/` directory exists with content

**Common issues:**
- `REF_NOT_FOUND` errors: Check relref links point to correct language paths
- Missing pages: Ensure all essential pages from Step 3 exist
- Build failures: Verify front matter YAML syntax

## Step 6: Update Translation Prompts (Optional)

If adding a language not covered in `src/snakecult_translate/prompts.py`, add appropriate prompts:

1. Add base prompt constant (e.g., `BASE_PROMPT_XX`)
2. Update `get_system_prompt()` function
3. Add language name to `lang_names` dictionary in `translate_frontmatter_block()`

## Step 7: Quality Check

Verify the new language:

1. **Homepage loads correctly** with translated content
2. **Language selector** shows the new language option
3. **Navigation works** between pages in the target language
4. **Article pages render** with proper formatting
5. **Search and tags** function in the target language
6. **URLs are correct** (e.g., `/xx/article-slug/`)

## Language Priority Order

Current language weights and suggested order for new additions:

1. `en` (English) - weight 1
2. `es` (Spanish) - weight 2  
3. `zh` (Chinese) - weight 3
4. `fr` (French) - weight 4
5. `de` (German) - weight 5
6. `pt` (Portuguese) - weight 6
7. `hi` (Hindi) - weight 7
8. `ar` (Arabic) - weight 8
9. `ru` (Russian) - weight 9

## File Structure Summary

After completing all steps, the language should have this structure:

```
content/xx/
├── _index.md           # Homepage
├── about.md            # About page
├── recent.md           # Recent updates
├── etoc-overview.md    # Theory overview
├── topics/
│   └── _index.md       # Topics index
└── posts/
    ├── article-1.md    # Translated articles
    ├── article-2.md
    └── ...
```

## Troubleshooting

**Build fails with "page not found":**
- Check all relref links use correct language paths
- Ensure all essential pages exist

**Language doesn't appear in selector:**
- Verify config.toml syntax
- Check weight values don't conflict
- Restart Hugo dev server

**Articles missing from language section:**
- Confirm articles have `lang: xx` in front matter
- Check file paths match expected structure
- Verify no draft: true in front matter

**Formatting issues:**
- Review translation prompts for the language
- Check Markdown syntax in translated files
- Verify front matter YAML is valid

## Notes

- Always test builds after adding a new language
- The `lastmod` date should be updated when creating translations
- Keep the `translation_model` field for tracking which AI model was used
- External links (vectorsofmind.com, etc.) should remain in English
- Technical terms and proper nouns should be preserved appropriately for the target language

## Current Status

✅ **Completed Languages:**
- English (en) - 348 pages (original)
- Spanish (es) - 502 pages (full translation)
- Chinese (zh) - 371 pages (full translation)
- French (fr) - 18 pages (essential pages complete)
- German (de) - 18 pages (essential pages complete)
- Portuguese (pt) - 18 pages (essential pages complete)
- Hindi (hi) - 18 pages (essential pages complete)
- Arabic (ar) - 18 pages (essential pages complete)
- Russian (ru) - 18 pages (essential pages complete)

**Total Build:** 1,329 pages across 9 languages

All languages are now configured and have their essential pages created. The site successfully builds with all languages showing in the language selector. Additional article translations can be added incrementally using the CLI tools. 