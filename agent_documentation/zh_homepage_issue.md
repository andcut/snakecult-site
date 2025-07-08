# Debugging Guide: Chinese Homepage Post-Listing Issue

This document outlines the investigation into why the Chinese language (`zh`) homepage of the Hugo site fails to display a list of posts, even though the individual post pages are being built correctly and are accessible via direct URLs.

## 1. Problem Description

The primary issue is that the homepage for the Chinese version of the site (`/zh/`) is not rendering the list of articles from the `content/zh/posts/` directory.

- **Symptom**: The "Research Articles" (研究文章) section is present, but it's empty.
- **Verification**:
    - Individual Chinese post URLs (e.g., `/zh/posts/some-article/`) work correctly when navigated to directly.
    - Running `hugo` shows that over 148 individual HTML files for Chinese posts are generated in the `public/zh/posts/` directory.
    - Hugo's build statistics are misleading, often reporting only "10 pages" for `zh`. This has been identified as a statistical quirk and not the root cause, as the files are indeed being created.

## 2. Investigation Summary & Fixes Attempted

Several issues were identified and fixed in the Chinese content files, which were thought to be the cause. While fixing them was necessary for content correctness, they did not resolve the homepage listing problem.

### Fixes Implemented:

1.  **Corrected Corrupted Front Matter (Titles)**: Many Chinese posts had their entire body content incorrectly placed inside the `title` field in the front matter. A script was used to parse these files and correct the titles.
2.  **Corrected Front Matter (Dates)**: The `date` and `lastmod` fields in all Chinese posts were enclosed in quotes (e.g., `date: '2025-07-04'`), which prevented Hugo from correctly parsing them as dates. A script was run to remove the quotes.

After these fixes, `hugo list published` confirms that Hugo now recognizes all Chinese posts with the correct dates and metadata. However, they are still not listed on the homepage.

## 3. Current Hypothesis

The issue likely lies within the **Hugo templates** responsible for rendering the homepage. Since the content itself is now correctly formatted and Hugo is processing it, the template logic that fetches and loops through the posts for the `zh` language section is failing or not executing as expected.

The problem is specific to how the list of posts is being generated for the main index page, not with the generation of the individual post pages themselves.

## 4. Recommended Next Steps & Helpful Tools

The next step is to debug the template files.

1.  **Examine `layouts/index.html`**: This is the primary template for the homepage. The logic for ranging over pages needs to be checked. Look for `range where .Site.RegularPages "Type" "in" .Site.Params.mainSections`. The `mainSections` parameter in the `config.toml` might be incorrect for the Chinese language configuration.
2.  **Check Language Configuration**: Review `config/_default/config.toml` and any language-specific configurations (e.g., `config/_default/languages.toml`) to ensure that the `zh` language is configured correctly and specifies `posts` as a main section.
3.  **Inspect Page Variables**: Use Hugo's debugging functions within the template to inspect variables. For example, you can print the count of pages being found: `{{ len (where .Site.RegularPages "Type" "in" .Site.Params.mainSections) }}`. This can help determine if the template is finding any posts at all.

### Helpful Commands & Tools:

-   **`hugo server -D`**: Runs the development server with draft content included. Essential for live testing.
-   **`hugo list all` / `hugo list published`**: Lists all content files as Hugo sees them, showing their path, title, date, and publish status. Useful for verifying front matter parsing.
-   **`curl http://localhost:1313/zh/`**: Fetches the raw HTML of the homepage to inspect its contents without browser rendering.
-   **`grep -r "pattern" .`**: Searches recursively for text patterns within the project, invaluable for finding where specific variables or strings are used in templates.
-   **File System Checks**:
    -   `ls -R content/zh/posts/`: Verify file existence.
    -   `find public/zh -name "*.html" | wc -l`: Count the number of generated HTML files to confirm the build process is working. 