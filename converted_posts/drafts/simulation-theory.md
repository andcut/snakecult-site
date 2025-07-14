---
title: "Simulation Theory"
date: "2025-07-04"
lastmod: "2025-07-04"
slug: "simulation-theory"
description: "This is a less serious piece immortalizing a blazed thought experiment my friend and I devised. He is a math prodigy, and studied optimization. As such, our musings took a technical turn. Readers who ..."
keywords:
  - "vectors-of-mind"
  - "simulation"
about: ['vectors-of-mind', 'blog-archive']
tags: []
author: "Andrew Cutler"
license: "https://creativecommons.org/licenses/by-sa/4.0/"
draft: True
quality: 1
original_id: "119869095"
original_url: "https://www.vectorsofmind.com/p/simulation-theory"
---
*From [Vectors of Mind](https://www.vectorsofmind.com/p/simulation-theory) - images at original.*

---

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!gpiH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a0327c9-aff1-4d91-8092-df6b8555f849_1100x596.jpeg)

This is a less serious piece immortalizing a blazed thought experiment my friend and I devised. He is a math prodigy, and studied optimization. As such, our musings took a technical turn. Readers who have never gotten high with engineers, this is your chance to be a fly on the wall.

Let’s say the universe is simulated. How is that information stored on the cosmic hard drive? The material perspective is to record every particle at every time step. But, with some assumptions, there may be an equivalent “dual” transformation which can equivalently represent the universe. The footnote describes what dual means in optimization which is what we had in mind. Understanding the particulars isn’t important though; it’s just that there are sometimes two very different ways to express something that is mathematically equivalent. Sometimes one version is millions of times better behaved, particularly when you are trying to apply certain operations (like finding a minimum value in the terrain). A more accessible example is how engineers represent sound. There is the time domain, where one represents the sound wave’s amplitude at each moment, and there is the frequency domain, where one represents the amplitude at each frequency. You can losslessly move between these two with the fourier transform. There are loads of explainers on this topic on the internet.

Okay, so let’s take it as a given that sometimes you can represent the same information two ways. Even though the content is the same, the form you choose may have very different properties. The naive way to represent the universe is one particle at a time. But what about Descartes and his radical skepticism? We could be wrong there is a material world at all, but we can’t be wrong that there is an “I”. So maybe the “dual” representation is the duality described by philosophy. Simply record all subjective experiences at each time step. This may also constitute the entire universe. (If a tree falls in the forest and nobody hears it, was that recorded on the cosmic hard drive?) This seems like a vastly reduced amount of data. Maybe one could formalize this in a way that is identical to wave function collapse. The dual includes the experience of all subjective agents defined as all agents that can collapse the wave function. It’s a bit like rendering in a video game. The world contains a whole map, which may be represented statistically, but only the field of view is instantiated. VR takes this a step farther with [foveated rendering](https://www.tobii.com/blog/what-is-foveated-rendering#); it uses eye tracking to increase resolution but only directly where you are focussed. If the universe were like this, how would you know? *Draws another toke* we create the world by perceiving it.

I like this because it is a way to treat subjectivity as “real” even if the material world can completely describe the simulation. Using the analogy of a song, music can be fully represented in the frequency domain. This doesn’t mean that time is an illusion, any more than frequency is.

But from an information theoretical perspective, even the dual is a naive way to store something. Consider Jack’s magnum opus in The Shining. It starts out “all work and no play makes Jack a dull boy” and repeats this page after page. Modulo some interesting typesetting, the entire book can be represented as “All work and no play makes Jack a dull boy” x 3,000. Similarly, if you have a similar experience every day, surely the simulators have some way to compress this. So the experience of having your morning coffee may be a pointer to the platonic morning cup’o’joe, with a few particular modifiers. As good data scientists we were thinking in terms of PCA so, put more technically, is the experience matrix full rank? How many eigenvalues do you need to keep for it to be lossless. And would a bit of loss be so bad? Does god keep jpegs or does he go .raw?

And of course because we were high and everything had meaning we didn’t stop there. What would be the goals of these simulators? Maybe increase information in this space. Data is the new oil, after all. This would mean you can add a byte to the cosmic hard drive every time you have a truly new experience. Kind of a nice thought. There are alien Platonic experiences waiting to be minted. Happy trails, traveler.

footnote: In optimization, one defines a landscape with a loss function as well as constraints. There is a whole literature on when you can find an equivalent “dual” expression of this same landscape. Solving the dual problem will give you the identical answer as the primal. You follow steps to write the constraints as
