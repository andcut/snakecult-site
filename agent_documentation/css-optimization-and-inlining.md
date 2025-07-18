# CSS Optimization and Inlining Strategy

This document covers the CSS optimization approaches for achieving 1-second flat loading times, with focus on automated inlining strategies.

## Current Implementation: Hugo-Native Automated Inlining

### ✅ Recommended Approach (Currently Implemented)

**File:** `layouts/partials/head.html`
```html
{{/* Get and inline CSS automatically */}}
{{ $css := resources.Get "css/main.processed.css" | resources.Minify }}
<style>{{ $css.Content | safeCSS }}</style>
```

**Benefits:**
- **Fully automated** - CSS changes automatically propagate
- **Build pipeline integrated** - Works with existing Tailwind→Hugo workflow
- **Zero maintenance** - No manual copying or version drift
- **Performance optimal** - Eliminates render-blocking requests
- **Hugo-native** - Uses built-in resource processing and caching

### How It Works

1. **CSS Generation:** `npm run build:css` creates `assets/css/main.processed.css`
2. **Hugo Processing:** `resources.Get` loads the CSS file automatically
3. **Optimization:** `resources.Minify` applies additional compression
4. **Inlining:** `safeCSS` safely injects CSS into `<style>` tags
5. **Result:** ~7.3 KiB CSS inlined in every page's `<head>`

### Performance Impact

**Build Time:**
- Local: ~7-8 seconds (vs 5s external CSS)
- Netlify: +4-6 seconds expected (vs 4min baseline)

**Frontend Performance:**
- **FCP:** 1.3s → 0.9-1.1s (-300-400ms)
- **TTI:** 1.6s → 1.2-1.3s (-300-400ms) 
- **TBT:** 180ms → <50ms (with animation delays)
- **Requests:** 3 → 2 (-1 blocking CSS request)

## Alternative Approaches (Not Currently Used)

### Option 2: Critical CSS Extraction

**Tools:** `critical`, `penthouse`, `criticalcss.com`

```javascript
// package.json
"scripts": {
  "build:critical": "critical --inline --src public/index.html --dest public/index.html"
}
```

**Pros:**
- Only inlines above-the-fold CSS
- Smaller initial payload
- Loads non-critical CSS asynchronously

**Cons:**
- More complex build pipeline
- Requires per-page generation
- Additional tooling dependency

### Option 3: Conditional Inlining

**Implementation:**
```html
{{ if .IsHome }}
  {{/* Inline for homepage only */}}
  <style>{{ $css.Content | safeCSS }}</style>
{{ else }}
  {{/* External CSS for other pages */}}
  <link rel="stylesheet" href="{{ $css.RelPermalink }}">
{{ end }}
```

**Use Case:** If build times become problematic

### Option 4: PostCSS Plugin Approach

**Implementation:** PostCSS plugins like `postcss-inline-critical`

**Pros:**
- Build-time optimization
- Automated critical extraction

**Cons:**
- Complex Hugo integration
- Additional build complexity

## Build Performance Optimization

### Current Status
- **Full build:** ~7-8 seconds locally
- **Incremental:** Hugo's fast render + caching
- **Netlify:** ~4:04-4:06 (estimated)

### If Build Times Become Problematic

1. **Enable conditional inlining** (homepage only)
2. **Use critical CSS extraction** for landing pages
3. **Implement build caching** strategies
4. **Split CSS by page type** 

### Development Workflow

**Fast development:** `make dev`
- English-only build
- External CSS (faster rebuilds)
- ~2s incremental builds

**Production testing:** `make build`
- Full multilingual build  
- Inlined CSS
- ~7-8s full build

## Integration with Existing Pipeline

### CSS Build Chain
```
assets/css/main.css 
  → Tailwind Processing 
  → PostCSS (autoprefixer)
  → assets/css/main.processed.css
  → Hugo resources.Get
  → resources.Minify
  → Inline in <style> tags
```

### Hugo Resource Caching
- Hugo caches processed resources in `/resources/`
- Subsequent builds reuse cached CSS when unchanged
- No performance penalty for repeated builds

## Future Considerations

### When to Revisit This Approach

1. **CSS grows beyond 10-15 KiB** - Consider critical CSS extraction
2. **Build times exceed 15 seconds** - Implement conditional inlining
3. **Multiple CSS files needed** - Split by page type or component
4. **Specialized pages** - Custom critical CSS per template

### Monitoring

**Metrics to Track:**
- Build time (local and Netlify)
- CSS payload size
- Core Web Vitals (FCP, LCP, TTI, TBT)
- Cache hit ratios

**Thresholds:**
- CSS size: <10 KiB ideal, <15 KiB acceptable
- Build time: <10s local, <5min Netlify
- FCP: <1s target, <1.2s acceptable

## Implementation History

**January 2025:** 
- Initial manual CSS inlining (fragile approach)
- Performance gains: 300-400ms FCP/TTI improvement
- Build time increase: +3-4 seconds

**January 2025 (Updated):**
- Automated Hugo-native inlining
- Same performance benefits
- Zero maintenance overhead
- Fully integrated with existing pipeline 

## July 2025 – 14 kB “Initial TCP Window” Optimisation Plan

Inspired by [“Why your website should be under 14 kB in size”](https://endtimes.dev/why-your-website-should-be-under-14kb-in-size/), we want the **very first HTTP response** (HTML + headers) to fit inside the initial congestion window (≈ 10 × 1460 B ≈ 14 kB compressed).

### Action items

1. **Externalise Tailwind bulk CSS**  
   – Continue to build `assets/css/main.processed.css`, but fingerprint & serve it as an *external* file:  
   ```gotemplate
   {{ $css := resources.Get "css/main.processed.css" | resources.Minify | fingerprint }}
   <link rel="preload" href="{{ $css.RelPermalink }}" as="style" onload="this.rel='stylesheet'">
   <noscript><link rel="stylesheet" href="{{ $css.RelPermalink }}"></noscript>
   ```
2. **Inline only ~2 kB of critical CSS**  
   – Use Tailwind JIT + `@unocss/cli` or `purgecss` to generate `critical.css`.  
   – Inline that file exactly as we currently inline *everything*.
3. **Defer heavy meta-data**  
   – Move JSON-LD and `hreflang` tags into a small `<script>` that runs after `DOMContentLoaded`, or drop them entirely.
4. **Slim hero assets**  
   – Replace the inline SVG banner with a tiny CSS background or an external `loading="lazy"` image/SVG.
5. **Remove development-only scripts**  
   – Exclude `livereload.js` from production builds.

### Expected outcome

* Gzipped HTML drops from ~37 kB → **≈ 11–14 kB**.  
* The external CSS (~25 kB Gzip) downloads in parallel, non-blocking.  
* First paint on 3G improves by **0.5–1 s**.

> Keep monitoring the payload. The rule is a *heuristic*, but staying beneath it guarantees at least one RTT shaved off for worst-case latency scenarios. 