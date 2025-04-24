---
# -------------- FRONT MATTER -------------- 
# Run snakecult_clean.py before reformatting a raw-test post to .md
# Do not reduce the length of raw-text posts when reformatting them, though do break up long paragraphs and add bolding/emphasis where appropriate for a mobile-friendly reading experience.

# Replace every TODO, then remove these comments.
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
lastmod: {{ .Date }}
slug: {{ .Name }}
description: "TODO: Meta description (≤ 160 chars)."
keywords: # 3–7 items
 - keyword-one
 - keyword-two
about: # high-level topics
 - main-theme
tags: # reader-facing
 - Tag-A
core_entity: ""  # ≤ 3-word noun phrase. Pick the single, concrete thing (object/creature/place/person) that best embodies the post and is easy to illustrate—i.e., what you’d put on the magazine cover.
author: "Andrew Cutler"
license: "https://creativecommons.org/licenses/by-sa/4.0/"
draft: true
---

**TL;DR**  <!-- ≤ 100 words, 3-7 bullets -->

- Replace this bullet list with a *very* tight summary.
- Focus on facts the article supports.

---

## Section Heading One

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse vel risus vitae ipsum fermentum efficitur. Nulla facilisi—see [related internal post](/internal-placeholder/) and compare with the overview on [Example Site](https://example.com/). 

### Subheading A

Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec venenatis, nisl in bibendum tempor, sapien lorem dignissim elit, sed facilisis mauris nunc vel justo.[^1]

### Subheading B

| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data A | Data B | Data C |
| Data D | Data E | Data F |

---

## Section Heading Two

1. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
2. Pellentesque habitant morbi tristique senectus et netus. 
3. Maecenas non tellus sed dolor ultricies pretium. 

---

## FAQ <!-- retains FAQPage schema support -->

**Q 1. Lorem ipsum dolor sit amet?** 
**A.** Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

**Q 2. Ut enim ad minim veniam?** 
**A.** Quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

---

## Footnotes

[^1]: Placeholder citation. Replace with real reference text.

---

## Sources

1. Author A. *Title A*. Publisher, Year. 
2. Author B. *Title B*. Journal **Volume** (Year). 