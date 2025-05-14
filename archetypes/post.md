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
core_entity: ""  # ≤ 3-word noun phrase. Pick the single, concrete thing (object/creature/place/person) that best embodies the post and is easy to illustrate—i.e., what you'd put on the magazine cover.
quality: 6          # ★ 1‒10 subjective "how good is this?"; 6 = unrated/OK
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

## FAQ <!-- retains FAQPage schema support. Produce 2–5 Q-A pairs. -->

**Q 1. What makes a good question?**  
**A.** Choose "how / what / why" queries that the post already answers and that a curious reader might type verbatim. Include at least one narrowly focused question that drills into a concrete detail or example.

**Q 2. How long should each answer be?**  
**A.** One punchy, self-contained sentence (≈30–50 words) that fully resolves the query, optionally followed by a brief clarifier. Total ≤120 words.

---

## Footnotes

[^1]: Placeholder citation. Replace with real reference text.

---

## Sources

Be source-heavy! Cite liberally from diverse sources including academic papers, books, news articles, websites, and primary sources. Include hyperlinks where available.

1. Smith, John. *The Complete History of Snakes*. Oxford University Press, 2023. [https://example.com/book](https://example.com/book)
2. Johnson, Sarah. "Snake Behavior Patterns." *Journal of Herpetology* **45** (2022): 123-145. [https://doi.org/10.1234/jh.2022.45](https://doi.org/10.1234/jh.2022.45)
3. National Geographic. "The Secret Lives of Pythons." *National Geographic Magazine*, March 2024. [https://natgeo.com/pythons](https://natgeo.com/pythons)
4. World Health Organization. "Snakebite Prevention and Treatment Guidelines." WHO Technical Report Series, 2023. [https://who.int/snakebite](https://who.int/snakebite)
5. The New York Times. "Urban Snakes: A Growing Phenomenon." *The New York Times*, January 15, 2024. [https://nytimes.com/urban-snakes](https://nytimes.com/urban-snakes)
6. Ancient Egyptian Hieroglyphic Text. "The Serpent Cult of Apep." British Museum Collection, 1500 BCE. [https://britishmuseum.org/apep](https://britishmuseum.org/apep)