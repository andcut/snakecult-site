---
title: "Cut Text"
date: "2025-07-04"
lastmod: "2025-07-04"
slug: "cut-text"
description: "Though not general, it is singularly important in the landscape of personality. personality concepts have to declare what team they play for (FFP+ or FFP-) before proceeding to describe some other con..."
keywords:
  - "vectors-of-mind"
  - "text"
about: ['vectors-of-mind', 'blog-archive']
tags: []
author: "Andrew Cutler"
license: "https://creativecommons.org/licenses/by-sa/4.0/"
draft: True
quality: 1
original_id: "63959222"
original_url: "https://www.vectorsofmind.com/p/cut-text"
---
*From [Vectors of Mind](https://www.vectorsofmind.com/p/cut-text) - images at original.*

---

## Cut paragraphs


Though not general, it is singularly important in the landscape of personality. personality concepts have to declare what team they play for (FFP+ or FFP-) before proceeding to describe some other concept. High energy…in a good or bad way? Even this neutral description of the second factor can be a devastating critique depending on the context. Just ask Low Energy Jeb! 

[show bimodal distribution.]

This may indeed suggest a hierarchical relationship to the other factors. This would explain why every item seems to load on this factor. Even if orthogonal factors exist (eg dynamism, order, beta) it’s difficult to measure them without also measuring FFP. We are social creatures and can’t help but process social desirability. Hence the persistent criticism that the FFP is _merely_ response bias. Using word vectors addresses this by removing respondents from the equation.

[Implication for psychometrics: Seems we may have to score non-GFP factors as their residuals, after removing the first PC. This makes for a more complicated scoring, but would allow us to much more sensibly discuss factors.]

[one of the things I’m having to decide is the audience. I care about truth and understanding the world. I write because it clarifies my thinking, and opens up doors to finding like-minded people. Like many, I’m interested in people, and I happen to think that there is a lot of low-hanging fruit in this area. However, making technical arguments Personality psychologists, especially, demand history and technical language. MyCertainly far more than building better personality surveys for industrial psychology. 

For clarity of writing (and fun) it’s written in a somewhat polemic style. Some wrinkles are clarified the footnotes.

It has been transformed from social self-regulation to being a door mat. (Gullible loads neutrally on PC1, but strongly on Agreeableness.)

### Statistical artifact?


Obvious by now that PFP is not just bias. We find it in word vectors as well as surveys. On surveys PFP is enormously externally valid. Usually more so than any Big Five factor. Rushton, “the genetics and evolution of GFP” lists X examples of FFP performing better than any of the Big Five. (ctrl-f “Construct validity for the GFP”). 

But to make it clear just what a powerhouse is, compared to other personality signal, look at the eigenvalues.

Below are the eigenvalues for the similarity matrix of 435 common words as measured by survey and NLP.

[new title: eigenvalues of 435 adjectives]

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!DHXT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9263ce31-ae4e-4023-be21-e80c41db5c66_387x307.png)

Structure similar in either method; both suggest a few factor model. In the survey data PFP explains 8 times more variance than the fifth factor, which is claimed to be a fundamental dimension of personality. Further, if one believes this factor doesn’t carry personality information, surely we shouldn’t spread that variance to the other factors via varimax rotation.

### Political neurons (PFP is bimodal)


As noted above, words are bimodally distributed on FFP. It’s almost as if there is a [neuron in the transformer](https://openai.com/blog/unsupervised-sentiment-neuron/) that sorts words into positive or negative camps, as that is of primary importance. I guess social evaluations must be good or bad so to avoid confusion we have few neutral words. Humans, too, may have a neuron sorting words first by valence.

What happens when we factor positive and negative words separately? 

[plot]

The structure is remarkably stable. Even when the data is bifurcated along the axis that would most shrink it’s impact, it is the first PC. 

**Viewing this as language data, what is the rationale to discard the first principal component?** It’s social desirability bias? Yes, the axis is about social desirability, but why is that bias? Social approval is the most salient feature of character descriptions. Language is, after all, gossip++. Further, is this factor simply response bias? Response of whom? Word vectors?

This is in contrast to **social intelligence** , which is more about raw social ability. Napoleon and Hitler certainly had social intelligence, which they used in unapproved ways.

There are of course many people who are well-liked, despite their norm violations. These individuals make the case for themselves using … social intelligence. As such, either term is a fair description. Social intelligence happens to be far catchier and highlight the parallels to _g_.

To be honest, qualitative analysis is not my forte. Luckily, there is a vast literature describing this factor, no need to rely on me!

[dalle: pure social intelligence. Or, know thyself]

How well one can regulate their own desires/beliefs/goals to make life pleasant for others. This list emphasizes politeness. Pinker [notes](https://en.wikipedia.org/wiki/The_Better_Angels_of_Our_Nature) that states now have a monopoly on violence. Historical data and men’s broad shoulders suggest this is a rare situation. My guess is that, anciently, the standard for norm violations was lower and the factor would have emphasized not being violent.
