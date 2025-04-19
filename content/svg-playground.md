---
title: "SVG Playground"
date: 2024-01-01
draft: true # Keep this page out of production builds
---

## SVG Playground

This page is for testing SVG assets to see how they render with the current site styles.

---

### Custom Eye SVG (`assets/svg/custom-eye.svg`)

{{< svg-inline src="svg/custom-eye.svg" alt="Custom all-seeing eye in triangle" width="100px" >}}

---

### Retarded Snake SVG (`assets/svg/retarded-snake.svg`)

{{< svg-inline src="svg/retarded-snake.svg" alt="Retarded Snake" width="100px" >}}

---

### Usage

To add more SVGs:
1. Place the `.svg` file in the `assets/svg/` directory.
2. Add a new section to this page using the shortcode:
   ```
   {{</* svg-inline src="svg/your-new-file.svg" alt="Description" width="100px" */>}}
   ```
   (Remove the `/*` and `*/`) 