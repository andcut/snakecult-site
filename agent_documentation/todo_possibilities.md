# Language Toggle – Option B (Inline "pill" link)

This idea keeps a visible language-switch link on every article without requiring users to open the header menu.

---

## UX sketch
```
<h1>Article Title</h1>  [ES]
                         ↑
                small rounded pill, right-aligned, blends with theme colour
```
Clicking the pill sends the reader to the translation (`.RelPermalink`) of the same page.

## Implementation Steps
1. **Partial** `layouts/partials/other-lang-link.html`
   ```html
   {{ with .Translations }}
     {{ $other := index . 0 }}
     <a class="lang-pill" href="{{ $other.RelPermalink }}">
       {{ upper $other.Language.Lang }}
     </a>
   {{ end }}
   ```
2. **Insert** the partial in `layouts/_default/single.html` just under the `<h1>`:
   ```html
   <h1>{{ .Title }}</h1>
   {{ partial "other-lang-link.html" . }}
   ```
3. **CSS** (can go in `assets/css` or inline):
   ```css
   .lang-pill{
     font-size:0.75rem; padding:2px 6px; margin-left:8px;
     border:1px solid currentColor; border-radius:4px;
     opacity:.7; transition:opacity .15s;
   }
   .lang-pill:hover{ opacity:1; }
   ```
4. **Optional**: hide the pill when no translation exists (the `with .Translations` guard already does this).

---

Advantages
* Always visible; zero clicks to discover alternate language.
* Works on mobile and desktop without JS.
* Minimal template footprint; easy to customise later (flags, tooltips, etc.).

Drawbacks
* Slight visual clutter under the title—needs tasteful styling.
* Only switches between two languages; multi-language sites would want a dropdown instead.

---

Status: *not yet implemented* – kept here as a future enhancement idea. 