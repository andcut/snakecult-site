# SnakeCult.net Research Site

This repository contains the source code and content for the SnakeCult.net website, built with Hugo.

The site serves as a research dump exploring the Eve Theory of Consciousness and related topics in gene-culture coevolution.

Generated pages are precompressed with Brotli to maximize transfer speed, including all SVG assets.

See `docs/project-charter.md` for project goals and details.

## Testing

Run `npm test` to ensure Hugo can build the site without errors.

## Development

To spin up a lightning-fast local server (English-only), run:

```bash
make dev
```

The make target bundles several speed optimisations:

* Disables non-English languages via `config/dev/languages.toml`
* Skips taxonomy/RSS/sitemap kinds
* Skips the SASS/Tailwind pipeline (`HUGO_SKIP_SASS=true`)
* Doubles Hugo worker threads

For a full multi-language preview you can still use:

```bash
hugo server -D
```

## Setup

This project uses Hugo themes as Git submodules. After cloning the repository,
run the following command to initialize the `hugo-theme-terminal` theme:

```bash
git submodule update --init --recursive
```

Without the submodule the site will fail to build.

## 🏷️ Tag Translation System

### Overview

Our multilingual site uses a **template-level translation system** for tags:
- **URLs in English**: `/tags/mythology/` (consistent across all languages)
- **Display in local language**: "Mythology" → "Mitología" (Spanish), "神话学" (Chinese)
- **Zero taxonomy explosion**: One tag concept = one URL across all languages

### Writing Articles

Just use English tags in your content - the system handles everything automatically:

```yaml
---
title: "My Article"
tags: ["Mythology", "Consciousness", "New-Tag"]
---
```

**Result:**
- ✅ English site: Shows "Mythology", "Consciousness", "New-Tag"
- ✅ Spanish site: Shows "Mitología", "Conciencia", "New-Tag" 
- ✅ URLs: `/tags/mythology/`, `/tags/consciousness/`, `/tags/new-tag/`

### Translation Management

**Check what needs translation** (optional):
```bash
make check-translations
```

**Auto-translate common tags** (optional):
```bash
make auto-translate-tags
```

**Manual translations**: Add to `i18n/{lang}.toml` files:
```toml
# i18n/es.toml
[tags]
"New-Tag" = "Nueva-Etiqueta"
```

### Benefits

- **Zero maintenance overhead**: New tags work immediately in English
- **SEO consistency**: Same URLs across all language versions
- **UX localization**: Visitors see tags in their language
- **Performance**: 65% faster builds (eliminated tag explosion)
- **LLM friendly**: Consistent tag structure for AI crawlers
