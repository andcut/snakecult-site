---
title: "Effect Gallery"
date: 2024-01-01
slug: effects-gallery
description: "Showcase of small CSS animations used around the site"
draft: false
---

Below is a collection of small effects inspired by other parts of the site. Each block loads minimal CSS so the rest of the site remains snappy.

<!-- Load page-specific CSS -->
{{ $style := resources.Get "css/effects-gallery.css" | resources.Minify }}
<link rel="stylesheet" href="{{ $style.RelPermalink }}">

<div class="effects-container">

<div class="effect-box">
  <h3>Eye of Ra Text</h3>
  <p class="eye-of-ra-text">*<span data-char="C" style="--char-index:0">C</span><span data-char="o" style="--char-index:1">o</span><span data-char="i" style="--char-index:2">i</span><span data-char="l" style="--char-index:3">l</span>*</p>
</div>

<div class="effect-box">
  <h3>Mini Snake Crawl</h3>
  <div style="overflow:hidden;height:2em;position:relative;">
    <div style="display:flex;width:200%;animation:slither-track 12s linear infinite;">
      <div style="width:50%;font-family:monospace;color:var(--retro-accent);white-space:nowrap;">
        <span style="display:inline-block;animation:wiggle 2s ease-in-out infinite;">~</span>≈≈≈≈≈≈≈≈≈≈≈~&lt;:&gt;
      </div>
      <div style="width:50%;font-family:monospace;color:var(--retro-accent);white-space:nowrap;">
        <span style="display:inline-block;animation:wiggle 2s ease-in-out infinite;">~</span>≈≈≈≈≈≈≈≈≈≈≈~&lt;:&gt;
      </div>
    </div>
  </div>
  <style>
    @keyframes slither-track { from{transform:translateX(-50%);} to{transform:translateX(0);} }
    @keyframes wiggle { 0%{transform:rotate(-4deg);}50%{transform:rotate(4deg);}100%{transform:rotate(-4deg);} }
  </style>
</div>

<div class="effect-box">
  <h3>Spinning Swastika</h3>
  {{< spinning_swastika >}}
</div>

<div class="effect-box">
  <h3>Glitch Divider</h3>
  {{< glitch-divider >}}
</div>

<div class="effect-box">
  <h3>Terminal Divider</h3>
  {{< terminal-divider >}}
</div>

<div class="effect-box">
  <h3>Neon Pulse</h3>
  <p class="neon-pulse">Ouroboros</p>
</div>

<div class="effect-box">
  <h3>Flicker Text</h3>
  <p class="flicker">Serpent Ritual</p>
</div>

<div class="effect-box">
  <h3>Rotating Eye</h3>
  <div class="rotate-slow">𓂀</div>
</div>

<div class="effect-box">
  <h3>Wave Text</h3>
  <p class="wave-text"><span>S</span><span>N</span><span>A</span><span>K</span><span>E</span></p>
</div>

<div class="effect-box">
  <h3>Scanning Highlight</h3>
  <div class="scan-highlight">Across the Abyss</div>
</div>

<div class="effect-box">
  <h3>Shimmer Box</h3>
  <div class="shimmer" style="padding:0.5rem;">Arcane Light</div>
</div>

<div class="effect-box">
  <h3>Pop Letters</h3>
  <div class="pop-letters"><span>C</span><span>U</span><span>L</span><span>T</span></div>
</div>

<div class="effect-box">
  <h3>Marquee</h3>
  <div class="marquee"><span>🐍 serpentum semper 🐍 serpentum semper 🐍 serpentum semper </span></div>
</div>

</div>
