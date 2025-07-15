# Hugo Translation Makefile

.PHONY: help translate-one translate-all translate-dry-run build install-deps dev

help:
	@echo "Available commands:"
	@echo "  install-deps     Install Python dependencies"
	@echo "  translate-dry-run Test what would be translated"
	@echo "  translate-one FILE=path/to/file.md  Translate single file"
	@echo "  translate-all    Translate all English posts to Spanish"
	@echo "  build           Build Hugo site"
	@echo "  build-test      Test build with both languages"
	@echo "  dev             Start fast Hugo server (English-only)"
	@echo "  dev-full        Start Hugo server with all languages"

install-deps:
	pip install -r requirements.txt

translate-dry-run:
	python translate_batch.py --dry-run

translate-one:
	@if [ -z "$(FILE)" ]; then echo "Usage: make translate-one FILE=content/posts/example.md"; exit 1; fi
	python translate_one.py "$(FILE)"

translate-all:
	python translate_batch.py --lang es

build:
	hugo --minify

build-test:
	hugo --minify --destination public_test && rm -rf public_test

dev:
	HUGO_NUMWORKERMULTIPLIER=2 \
	HUGO_SKIP_SASS=true \
	hugo server -D \
	  --environment dev \
	  --disableKinds taxonomy,RSS,sitemap

dev-full:
	HUGO_NUMWORKERMULTIPLIER=2 \
	HUGO_SKIP_SASS=true \
	hugo server -D \
	  --disableKinds taxonomy,RSS,sitemap

# Example: translate a small file for testing
translate-test:
	python translate_one.py content/posts/consider-the-chicken.md 