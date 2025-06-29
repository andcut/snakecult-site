# SnakeCult.net Research Site

This repository contains the source code and content for the SnakeCult.net website, built with Hugo.

The site serves as a research dump exploring the Eve Theory of Consciousness and related topics in gene-culture coevolution.

Generated pages are precompressed with Brotli to maximize transfer speed, including all SVG assets.

See `docs/project-charter.md` for project goals and details.

## Testing

Run `npm test` to ensure Hugo can build the site without errors.

## Setup

This project uses Hugo themes as Git submodules. After cloning the repository,
run the following command to initialize the `hugo-theme-terminal` theme:

```bash
git submodule update --init --recursive
```

Without the submodule the site will fail to build.
