# Speeding up the Hugo build

A full-site build currently takes **≈7 s** on an M2 MacBook Air.  That is decent for a multilingual (~1 000 pages) Hugo site, but you can trim it to the 1–3 s range while developing and keep production builds under 5 s.

Below is a menu of levers, ordered by ease-of-use versus payoff.  Stack as many as you like—zero-cost tweaks first, deeper refactors later.

---

## 1 · Use incremental / partial rebuilds (FREE)

`hugo server` already enables “Fast Render”, yet it still renders every language, alias, and taxonomy page.  Narrow the scope while you work:

| Goal | Command | Typical speed-up |
|------|---------|------------------|
| **English only** | `hugo server -D --environment dev` | 2–3 × |
| **Skip taxonomies & RSS** | `hugo server -D --environment dev --disableKinds taxonomy,taxonomyTerm,RSS,sitemap` | +10–30 % |
| **Skip SASS/Tailwind pipeline** | `HUGO_SKIP_SASS=true hugo server -D --environment dev` | +0.5–1 s |

Combine them in a single alias / Make target (see below).

> Note: The `config/dev/languages.toml` file disables all non-English languages when the environment is set to `dev`, so the single `--environment dev` flag is enough to limit the build to English.

---

## 2 · Turn on Hugo’s build cache (FREE)

We added this to `config/_default/config.toml`:

```toml
[build]
useResourceCacheWhen = "always"
```

Previously-generated resources (minified CSS/JS, processed images) are now reused across runs.  Expect 1.5–2 × speed-ups for repeated full builds.

---

## 3 · Cache expensive partials (MEDIUM effort)

Run once:

```bash
hugo --templateMetrics --templateMetricsHints
```

Wrap slow partials in `partialCached`:

```go-html
{{ partialCached "slow.html" . .Page.File.Path }}
```

Reduces template overhead by 10–50 %.

---

## 4 · Trim taxonomy & alias bloat (SITE ARCHITECTURE)

Every tag/category list is rendered per language **and** per paginator page.

* Merge duplicate / single-use tags (see `data/tags.json`).
* Increase `paginate` to 50–100 to cut the number of pages.
* If you don’t need translated taxonomies, add `disableKinds = ["taxonomy", "taxonomyTerm"]` inside each non-English `[languages.*]` block.

Savings: 15–40 %.

---

## 5 · Run SASS/PostCSS outside Hugo (MEDIUM)

Let a watcher handle CSS:

```bash
npm run watch:css  # dart-sass + postcss --watch
hugo server -D     # no asset pipeline, faster IO
```

Removes 0.5–1 s from every rebuild.

---

## 6 · Turn up parallelism (FREE)

```bash
export HUGO_NUMWORKERMULTIPLIER=2   # or 3 on big CPUs
```

Adds 5–15 % on very large sites.

---

## 7 · Hardware upgrade (COSTLY but linear)

| CPU | Full-build time |
|-----|-----------------|
| M2 MacBook Air | 7 s |
| M3 Pro MacBook Pro | 4–5 s |
| M3 Max | 3–4 s |

---

## Recommended dev command

A convenient Make target that stacks the zero-cost tweaks:

```makefile
dev:
	HUGO_NUMWORKERMULTIPLIER=2 \
	HUGO_SKIP_SASS=true \
	hugo server -D \
	  --environment dev \
	  --disableKinds taxonomy,taxonomyTerm,RSS,sitemap
```

Run it with:

```bash
make dev
```

It usually drops save-to-browser refresh times to **≈2 seconds**.

---

## Recommended production command

```bash
hugo --gc --minify --environment production
```

A clean, minified build that’s still under 5 s on modern Apple silicon. 