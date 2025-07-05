---
date: 2024-01-01
description: Showcase of small CSS animations used around the site
draft: false
lang: es
lastmod: '2025-07-04'
slug: effects-gallery
title: Galería de Efectos
translation_model: gpt-4o
---

Below is a collection of small effects inspired by other parts of the site. Each block loads minimal CSS so the rest of the site remains snappy.

<!-- Load page-specific CSS -->
{{ $style := resources.Get "css/effects-gallery.css" | resources.Minify }}
<link rel="stylesheet" href="{{ $style.RelPermalink }}">

<div class="effects-container">

<div class="effect-box">
  <h3>Texto Ojo de Ra</h3>
  <p class="eye-of-ra-text">*<span data-char="C" style="--char-index:0">C</span><span data-char="o" style="--char-index:1">o</span><span data-char="i" style="--char-index:2">i</span><span data-char="l" style="--char-index:3">l</span>*</p>
</div>

<div class="effect-box">
  <h3>Serpiente Mini Rastreo</h3>
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
  <h3>Divisor Glitch</h3>
  {{< glitch-divider >}}
</div>

<div class="effect-box">
  <h3>Divisor Terminal</h3>
  {{< terminal-divider >}}
</div>

<div class="effect-box">
  <h3>Pulso Neón</h3>
  <p class="neon-pulse">Ouroboros</p>
</div>

<div class="effect-box">
  <h3>Texto Parpadeante</h3>
  <p class="flicker">Ritual de la Serpiente</p>
</div>

<div class="effect-box">
  <h3>Ojo Giratorio</h3>
  <div class="rotate-slow">𓂀</div>
</div>

<div class="effect-box">
  <h3>Texto Ondulante</h3>
  <p class="wave-text"><span>S</span><span>N</span><span>A</span><span>K</span><span>E</span></p>
</div>

<div class="effect-box">
  <h3>Resaltado de Escaneo</h3>
  <div class="scan-highlight">A través del Abismo</div>
</div>

<div class="effect-box">
  <h3>Caja Brillante</h3>
  <div class="shimmer" style="padding:0.5rem;">Luz Arcana</div>
</div>

<div class="effect-box">
  <h3>Letras Emergentes</h3>
  <div class="pop-letters"><span>C</span><span>U</span><span>L</span><span>T</span></div>
</div>

<div class="effect-box">
  <h3>Marquesina</h3>
  <div class="marquee"><span>🐍 serpentum semper 🐍 serpentum semper 🐍 serpentum semper </span></div>
</div>

</div>