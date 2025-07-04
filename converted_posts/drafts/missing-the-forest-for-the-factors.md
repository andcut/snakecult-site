---
title: "Missing The Forest For The Factors"
date: "2025-07-04"
lastmod: "2025-07-04"
slug: "missing-the-forest-for-the-factors"
description: "[say something about goldberg, the words at poles, and interstitial space."
keywords:
  - "vectors-of-mind"
  - "missing"
  - "forest"
  - "factors"
about: ['vectors-of-mind', 'blog-archive']
tags: []
author: "Andrew Cutler"
license: "https://creativecommons.org/licenses/by-sa/4.0/"
draft: True
quality: 1
original_id: "59426140"
original_url: "https://www.vectorsofmind.com/p/missing-the-forest-for-the-factors"
---
*From [Vectors of Mind](https://www.vectorsofmind.com/p/missing-the-forest-for-the-factors) - images at original.*

---

[say something about goldberg, the words at poles, and interstitial space. 

Consider some data we just harvested. Say, a 200 item test taken by thousands of psychology undergrads. By magic, the latent space is essentially two dimensions. Below are two possible distributions of the test items in latent space, what do you think occurs more often in nature?

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!mM2G!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F59e405b5-3b86-474e-a1fe-9eb2ae346e18_1101x547.png)Credit: Jonathan Lansey, author of [matviz](https://github.com/JLansey/matviz)

If you choose to represent the data with a correlated factor model (CFM), you are claiming the distribution on the left. Each data point either loads on a single factor, and there are no interstitial points. Scientists are still trying to find such a distribution in the wild. (There have been scattered reports [not far from the University of Oregon](https://www.arcgis.com/apps/View/index.html?appid=f987f36187c140aeab6eb157e909eb64).)

Let’s see how CFM represents a normal distribution. The data below is a 2 dimensional gaussian. Naturally, the data can be described completely with 2 axes. Because CFM requires data to load on just one factor, more are required to represent the data so we will use 3. Once again, consider this to be high-dimensional data that only has 2 significant eigenvalues; this is latent space.

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!T1H3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F173bb599-75fb-45c2-aaa9-5c1545b83d24_627x467.png)By restricting points to load on a single factor, the axes are forced to spread out, each claiming two opposing pieces of pizza.

You’ve heard of the Spanish Inquisition, but what about the pizza imposition? As you can see, the factors spread out to represent different pizza-shaped neighborhoods. All we know about a point is how much it loads on a single factor. Therefore two points (A and B) may be far from each other but have the exact representation. Neighbors (B and C) may be assigned to completely different neighborhood. 

This is of course a simplification. If there are only 2 significant eigenvalues, a psychometrician would pick up on this and use only 2 factors. There are tests for whether each factor [blah blah]. Over the decades many guard rails have been developed. What I’m trying to build is an intuition for what CFM does when interstitial space is as important.

One can keep adding factors to have arbitrarily good reconstruction loss (cut the pizza finer). And of course there are rules of thumb to say how many should be added. 

Correlated factor analysis really be out there imposing pizzas where they don’t belong. Hard to cut nature at it’s joints when you’re forced to cut it at the crust!

After such a model is fit, the correlation between factors is reported, as well as the top-loading data points on each factor. (there are some statistics of how ‘pure’ each factor is?)

### Understanding people or personality


[These choices are made to produce a simple scoring. Useful to understand people, but we have to understand such modeling decisions confuse our understanding of personality space. Consider the Big Two]

There are psychometric upsides to such models. They lead to simple scoring where an item on a test only loads on one factor. Factors potentially represent a single concept which is easier to communicate and may be theoretically simpler (eg. monocausal). Scoring is only a consideration when we want to place individuals (rather than words/items) on an axes. When doing basic science on the structure of constructs, this is not an issue. As for producing simpler factors, IMO these models usually muddy the conceptual model.

### The spatial view


Once dimensions have been reduced, you can 

### Big Two


Will be covered in the post about GFP, but go over that result. Big Two are obviously PC1 and 2 of general personality. No need to think of them as hierarchically related to the Big Five. This falls from a spatial view. Totally confused by a factor view of personality.

### A factor by any other name


[from there, why do we focus so much on these particular factors?]

My family has eaten many hamburgers, but my sisters couldn’t quite stomach eating Gimpy. Gimpy had three legs, and we had visited him on my grandfather’s ranch. Naming something, brings attachment and one stops acting rationally.

Similarly, psychologists are factor-brained. They have named these axes, built careers on them, loved them, hated them, and sometimes been driven mad by them. 

[*[Image: Visual content from original post]*Sanjay Srivastava @hardsciAnd those “latent variables,” are they in the room with us right now? *[Image: Visual content from original post]*](https://twitter.com/hardsci/status/1446560457796554804?lang=en)[7:37 PM ∙ Oct 8, 2021

* * *

9,051Likes1,109Retweets](https://twitter.com/hardsci/status/1446560457796554804?lang=en)

There is good reason for this. It’s interesting that similar latent factors emerge in dataset after dataset, regardless of particular items. Communicating and understanding that requires describing factors. Doing so over a long period must result in a standard rotation for the same reason we all use the same electrical outlets. But this doesn’t change the nature of the space. Though not named, the interstitial space is as densely populated with concepts as the Big Five. It is largely forgotten and rarely mapped. Additionally, there are many times structure is clear from the item level but confused by dealing with factors. **Sometimes psychologists miss the forest for the factors.**

[ *[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!4ula!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F93db2793-7ab2-444f-b92f-373487cf8b47_500x976.jpeg)Jesse’s dialogue lifted from the abstract of **Higher Order Factors of Personality: Do They Exist?.** Cited hundreds of times, but could have been definitely answered by the 

## Everything below this is about


Problems with factors in general, not correlated factor models. Better to keep the post short and sweet. These are good arguments, move them to the post about FFP

### Big Two


Will be covered in the post about GFP, but go over that result. Big Two are obviously PC1 and 2 of general personality. No need to think of them as hierarchically related to the Big Five. This falls from a spatial view. Totally confused by a factor view of personality.

### A factor by any other name


[from there, why do we focus so much on these particular factors?]

My family has eaten many hamburgers, but my sisters couldn’t quite stomach eating Gimpy. Gimpy had three legs, and we had visited him on my grandfather’s ranch. Naming something, brings attachment and one stops acting rationally.

Similarly, psychologists are factor-brained. They have named these axes, built careers on them, loved them, hated them, and sometimes been driven mad by them. 

[*[Image: Visual content from original post]*Sanjay Srivastava @hardsciAnd those “latent variables,” are they in the room with us right now? *[Image: Visual content from original post]*](https://twitter.com/hardsci/status/1446560457796554804?lang=en)[7:37 PM ∙ Oct 8, 2021

* * *

9,051Likes1,109Retweets](https://twitter.com/hardsci/status/1446560457796554804?lang=en)

There is good reason for this. It’s interesting that similar latent factors emerge in dataset after dataset, regardless of particular items. Communicating and understanding that requires describing factors. Doing so over a long period must result in a standard rotation for the same reason we all use the same electrical outlets. But this doesn’t change the nature of the space. Though not named, the interstitial space is as densely populated with concepts as the Big Five. It is largely forgotten and rarely mapped. Additionally, there are many times structure is clear from the item level but confused by dealing with factors. **Sometimes psychologists miss the forest for the factors.**

[ *[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!4ula!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F93db2793-7ab2-444f-b92f-373487cf8b47_500x976.jpeg)Jesse’s dialogue lifted from the abstract of **Higher Order Factors of Personality: Do They Exist?.** Cited hundreds of times, but could have been definitely answered by the 

### Nature at it’s joints


 _“Lexical analyses and dimensionality-reduction methods are tools to explore rough contours of the personality space. We should not, however, delude ourselves into thinking that we are slicing nature at its joints to discover a “true” structure of personality.” ~Wiernik, et al_

Many wonderful points are made in the response [Two, five, six, eight (thousand): Time to end the dimension reduction debate!](https://psyarxiv.com/d7jye/), but I am more optimistic that we can find simple, general, and meaningful structure in Lexical data. It will at least be “true” in the sense the Lexical Hypothesis claims: the aspects of character that the speakers find useful. Psychometrics is a world without anchors, is there a better standard than utility in everyday life for billions of people? I really do think I’ve answered the GFP question by calling it FFP. It, and indeed alpha, stability, g-PD, p, are all simply the first PC of general personality. The unifying signal overcomes very different modes of data collection: natural language vs surveys, participants in psychology departments vs psych wards, Big Five Inventory vs surveys of drug abuse, PCA vs Network Analysis. They all yield very similar structure. Further, the language data connect the construct to rich theoretical ideas from evolution to consciousness: what it means to be human. Such explanations are what it looks like to slice nature at its joints. 

In the parlance of tech twitter, there is still alpha in Alpha. Psychology focussed far too much on factors that were optimized for scoring individuals, not describing the constructs. Interstitial space was ignored. Simple structure was confused for hierarchy. Data was largely from small samples of WEIRD undergrads. There was a ‘conspiracy’ (their words!) to export this half-baked factor structure to other fields. Now we have terabytes of natural language data from all over the world. We have the compute, models, and method to translate that to personality structure [link to me and david]. We have open science, and we have a more diverse set of voices. The time is ripe for another round of the long debate. Keep reading for front row seats. Share if you think there’s merit!

## Cut paragraphs


### The Big Two


[explain how focusing on factors caused digman to misinterpret the hierarchy. 

Particularly, I went down this road to try to understand how the Big Two could have been interpreted as hierarchically related to the Big Five for so long. Personality latent space indeed has just a few dimensions. Other than the first factor, which is bimodal, factor rotations are an arbitrary choice about how to represent the data. There is just as much density in interstitial space and any rotation produces quite normal loadings. Books have been written about the number of factors and correct rotation, but that shouldn’t obscure the relation of the Big Two and Big Five.

From a spatial view, the observation data (say, items of a survey or a matrix of word correlations) exists in messy high-dimensional space. But it can be explained parsimoniously in low-dimensional space. “Explained parsimoniously” means that we are in the world of reconstruction loss. We are looking for a simple way to explain the data which can roughly reconstruct the original. There are many many ways to do this, depending on the structure of the data. PCA, information theory, clustering. Note that not all of this is geometric, information theory also applies to compressing jpegs or books. Clustering, too, just assigns neighborhood membership (sometimes with 

But, it’s amazing how often psychometric data is roughly a multi-dimensional gaussian and PCA suffices. There is also really interesting work using network analysis to try to understand the structure of data. In this view, each data point is a node connected to every other node to the extent it is ‘similar’. There are then ways to trim this network into its underlying skeletal structure by combining nodes that behave in the same way. This is a great way to handle non-gaussian data. But IMO PCA usually suffices. When it does not perhaps try preprocessing the data to make it behave better rather than using a more complicated model. That is best practices in data science, where it is usually easier to evaluate the usefulness of a model. 

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!nxRo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F3a941d71-3009-4266-998e-d7765766a647_500x976.jpeg)

https://www.frontiersin.org/articles/10.3389/fpsyg.2020.01357/full

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!nQRt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F3d36aead-02c8-4dd9-b7e6-bc4c8f73aab6_1500x2541.jpeg)
