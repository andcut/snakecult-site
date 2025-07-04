# Vectors of Mind to Snakecult.org Conversion Guide

This guide explains how to use the `convert_vom_posts.py` script to convert your Vectors of Mind blog posts to the snakecult.org format.

## What the Script Does

The script converts HTML files from your Vectors of Mind blog export into markdown files with proper frontmatter for Hugo/snakecult.org. It:

1. **Separates published vs draft posts** - Posts with analytics CSV files go to `published/`, others go to `drafts/`
2. **Extracts content** from HTML files
3. **Converts HTML to markdown** using either html2text or basic regex
4. **Handles images** by replacing them with descriptive placeholders
5. **Generates frontmatter** with metadata like title, date, keywords, etc.
6. **Uses keywords instead of tags** - `vectors-of-mind` is added as a keyword for SEO, not as a browseable tag
7. **Adds attribution** with a link back to the original Vectors of Mind post
8. **Creates clean filenames** based on the post title

## Installation

1. Make sure you have Python 3.6+ installed
2. Install optional dependencies for better conversion:
   ```bash
   pip install beautifulsoup4 html2text
   ```

## Usage

1. Place your HTML files in the `vom_posts` directory
2. Run the conversion script:
   ```bash
   python convert_vom_posts.py
   ```
3. Find converted files in the `converted_posts` directory

## Output Structure

Each converted post includes:

### Frontmatter
- `title`: Extracted from filename or HTML content
- `date`: Current date (you may want to update with actual post dates)
- `lastmod`: Current date
- `slug`: URL-friendly version of the title
- `description`: First paragraph excerpt
- `keywords`: Extracted from content
- `about`: `["vectors-of-mind", "blog-archive"]`
- `tags`: `[]` (empty - vectors-of-mind moved to keywords)
- `author`: "Andrew Cutler"
- `license`: Creative Commons license
- `draft`: false
- `quality`: 7 (default)
- `original_id`: Numeric ID from filename
- `original_url`: Link to original Substack post

### Content
- Attribution header linking to original post
- Markdown-formatted content
- Images replaced with `*[Image: description]*` placeholders

## Results Summary

From the recent conversion run:
- **Total files**: 165 HTML files found
- **Published**: 81 files (had analytics CSV data)
- **Drafts**: 77 files (no analytics CSV data)  
- **Skipped**: 7 files (too small, likely placeholders)
- **Errors**: 0 files failed to convert

### Published vs Draft Detection

The script determines if a post was published by checking for associated analytics CSV files:
- `{post_id}.delivers.csv` - email delivery data
- `{post_id}.opens.csv` - email open data  
- `{post_id}.clicks.csv` - link click data

If any of these files exist for a post, it's considered published and goes to `converted_posts/published/`. Otherwise, it's treated as a draft and goes to `converted_posts/drafts/`.

## File Examples

**Input**: `64772741.is-personality-hyperbolic.html`
**Output**: `is-personality-hyperbolic.md`

**Input**: `65111001.did-eve-have-blue-eyes.html`
**Output**: `bringing-back-greek-gnosticism.md` (title from content)

## What You May Want to Adjust

1. **Dates**: The script uses current date - you may want to update with actual publication dates
2. **Slugs**: Some generated slugs may need manual adjustment
3. **Tags**: Currently all posts have empty tags array - you may want to add specific browseable tags
4. **Keywords**: `vectors-of-mind` is added automatically - you may want to add more specific keywords
5. **Quality scores**: All posts default to quality 7 - you may want to adjust based on post importance
6. **Draft status**: Review which posts should actually be published vs kept as drafts
7. **Images**: Review image placeholders and add descriptions where helpful

## File Locations

- **Source**: `vom_posts/` (your HTML files + CSV analytics files)
- **Published Output**: `converted_posts/published/` (posts with analytics data)
- **Draft Output**: `converted_posts/drafts/` (posts without analytics data)
- **Logs**: `converted_posts/conversion_log.txt`
- **Stats**: `converted_posts/conversion_summary.json`

## Moving Files to Hugo

To add these to your actual Hugo site:

1. Review the converted files in `converted_posts/published/` and `converted_posts/drafts/`
2. Make any necessary adjustments (dates, tags, keywords, draft status, etc.)
3. Move desired `.md` files to your Hugo `content/posts/` directory
   - Published posts can be moved directly (they have `draft: false`)
   - Draft posts have `draft: true` - change to `false` when ready to publish
4. Run `hugo server` to preview
5. Build and deploy as usual

## Troubleshooting

- If conversion fails, check the log file for error details
- Very small files are automatically skipped (likely placeholders)
- Missing dependencies will cause fallback to basic HTML parsing
- Complex HTML structures may need manual review

## Notes

- The script preserves all text content while replacing images with placeholders
- Original HTML structure is converted to markdown (headers, lists, links, etc.)
- Blockquotes and emphasis are preserved
- All posts get a header linking back to the original Vectors of Mind post
- The script handles both UTF-8 content and HTML entities properly

This creates a complete archive of your Vectors of Mind content in a format suitable for snakecult.org! 