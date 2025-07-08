---
title: "Personality Around The World"
date: "2025-07-04"
lastmod: "2025-07-04"
slug: "personality-around-the-world"
description: "Okay, let\u2019s take a little reprieve from the sapience stuff. I actually had a bunch of psychometrics queued up before being pulled in by the clarion call of consciousness. It\u2019s just so hard to look awa..."
keywords:
  - "vectors-of-mind"
  - "personality"
  - "around"
  - "world"
about: ['vectors-of-mind', 'blog-archive']
tags: []
author: "Andrew Cutler"
license: "https://creativecommons.org/licenses/by-sa/4.0/"
draft: False
quality: 6
original_id: "108601152"
original_url: "https://www.vectorsofmind.com/p/personality-around-the-world"
---
*From [Vectors of Mind](https://www.vectorsofmind.com/p/personality-around-the-world) - images at original.*

---

Okay, let's take a little reprieve from the sapience stuff. I actually had a bunch of psychometrics queued up before being pulled in by the clarion call of consciousness. It's just so hard to look away.

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!X2nA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F62106fb3-6e73-444d-96f1-07b95ec828f9_1024x506.jpeg)[Ulysses and the Sirens](https://en.wikipedia.org/wiki/Ulysses_and_the_Sirens_\(Waterhouse\)), painting by [John William Waterhouse](https://en.wikipedia.org/wiki/John_William_Waterhouse)

I started this blog to explore the Lexical Hypothesis from a machine learning perspective. Personality models define the most-gossiped-about traits in a language, and we can measure that much better in the age of GPT. Personality models derived from either word vectors or traditional surveys come back to the same few traits, especially the Big Two: social self-regulation, and dynamism. For a refresher on this check out [The Big Five are Word Vectors](https://vectors.substack.com/p/the-big-five-are-word-vectors) and [The Primary Factor of Personality](https://vectors.substack.com/p/primary-factor-of-personality-part). 

The Big Five has been found in many languages independently, but the comparison between languages is always qualitative. Researchers administer a survey of personality adjectives in Turkish or German, factorize it, and kind of eyeball the factors to see if they are the same. This data can't be used to say "Extraversion is shifted 15 degrees away from Conscientiousness in German compared to English." To be so precise, both languages would have to share some basis. 

If you administer questions in multiple languages you can relate them by 1) finding a bilingual cohort who can answer in both languages or 2) assuming the translations of words are 1:1 (eg. _fun_ is perfectly equivalent to _divertido_ in Spanish). In the former case, there is a strong selection effect. What if bilingual people tend to be better educated? The latter is simply not true. In fact, the reason to factor languages together is to understand how personality structure may diverge between them. Assuming the words are the same defeats the purpose.

**[My research](https://arxiv.org/abs/2203.02092) showed that you can extract personality structure from language models in English. A natural question is how that changes when you add other languages.** With models trained on dozens of languages, this becomes rather painless to explore. You can map any number of languages to the same basis.

## The Big Two, once again


I used [XLM-RoBERTa](https://huggingface.co/xlm-roberta-base) to assign similarity between personality adjectives. Strangely, this model is a result of the genocide in Myanmar. Meta has the unenviable position where they need to remove content in places of which they have very little understanding. Technically, this is what's called a transfer learning problem. They would like to train a hate speech classifier in English (or another well-sourced language), and then have that apply to other languages. In the dark ages of language modeling (2018) this worked very poorly. Colloquial speech in Burmese for "let's round up the gays and kill them" looked to their classifiers like "there should be less rainbows". This, of course, slid past their content moderation. The NYT explained the consequence: _**[A Genocide Incited on Facebook, With Posts From Myanmar's Military](https://www.nytimes.com/2018/10/15/technology/myanmar-facebook-genocide.html)**_

Meta's response was to build a language model that could better map any language (well, 100 languages) to word vectors in the same shared space. That way a hate speech classifier trained in English can better extend to other languages. (Less Burmese is needed to fine tune it.) Using this model, I embedded personality words in four languages: English, Spanish, French, and Turkish. Below are the first two factors:

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!eLVQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd3ff00d-d96d-4e3b-ada4-640e3cd66089_1245x954.png)

These serve to separate the different languages. The first factor distinguishes Turkish from the Indo-European languages. On the second factor, the romance languages are adjacent (though also close to Turkish).

This makes sense. The model is trained to predict the next word of a sentence, so will naturally include language-specific information. If someone is talking in Spanish they do not often switch to Turkish. The hope is that there are also directions in vector-space that correspond to personality information. 

If languages are fairly independent, you need at least 3 dimensions to separate 4 languages in their own non-overlapping groups. Let's check out the next principal components.

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!PRKA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5eb70bd2-8684-4844-94bd-aa12adc030bf_1256x954.png)

Factor 4 is the first factor that wasn't learned to separate the languages, and it's the General Factor of Personality! In English: _domineering, ruthless, compulsive_ and _selfish_ **vs** _generous, gentle,_ and _thoughtful_. [I have argued](https://vectors.substack.com/p/primary-factor-of-personality-part) that this factor is best understood as the tendency to live the Golden Rule. The Eve Theory of Consciousness was actually a result of [wondering what this would select for](https://vectors.substack.com/p/consequences-of-conscience) in our evolutionary history. Factor 5 is also about personality, plotting them together:

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!pD64!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F192dc8f4-db5e-4d96-b8a5-ce16c1cbf1f6_1264x954.png)

We get the Big Two! Factor Five (or two, of the personality factors) is Dynamism: _adventurous, imaginative,_ and _enthusiastic_**vs** _cautious, reserved,_ and _cowardly._ It's amazing that this pops out so regularly. **There are[2,500 citations on the Big Two paper](https://scholar.google.com/scholar?cites=11052969740325606797&as_sdt=2005&sciodt=0,5&hl=en), and still researchers don't realize that they are simply the first two unrotated factors of general personality.** The common belief that they somehow exist in a hierarchical relationship with the Big Five comes from researchers abandoning dealing directly with language shortly after making the Big Five inventories. Since then, any attempt to understand basic or general personality must be done in reference to the Big Five. But words came first, and language models make it easy to analyze language on that fundamental level now.

[Share](https://www.vectorsofmind.com/p/personality-around-the-world?action=share)

## We have to go deeper


Adding Russian and Farsi yields the same factors:

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!IIKx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F976f1c11-fd97-4184-a74a-a384a09b0579_2078x1715.png)To better see the words download the image and zoom in.

By my lazy-ass engineer standards this is fairly labor intensive because it requires finding a good prompt for each language. I worked with Google Translate and native speakers to get this right, and you can see the Farsi distribution is still off on Factor 4. My guess is that my method of ignoring any factor that is not shared is too janky for this many languages. Factor 4 is probably used as the GFP, and also to separate Farsi (just a bit). There is nothing keeping these factors pure, we are really lucky that the distribution is as well-behaved as it is. Doing some preprocessing (like zero-meaning each language cluster) may solve this. 

To my knowledge this is the first time multiple languages have been factorized together. This would be publishable with results on just English and Spanish and here I got up to six, including two non-Indo-European languages. It also sheds light on the nature of the Big Two, one of the most popular—and misunderstood—constructs in psychometrics.

## Shortcomings


I did this research in about the dumbest way possible. I found 100 personality words in an ESL guide, and then translated those to other languages using Google Translate. If there were duplicates, I removed them. This isn't as bad as it seems. The first two factors are virtually unchanged in English whether you use 100 or 500 words. But, if this were a real paper, you would obviously want to develop a set of words in each vocabulary independently. There are several other shortcomings:

**Not enough languages!** If I published this, I would like to add a dozen more languages that are not typically studied in personality science. This is, in fact, why I never got around to publishing it. That's a lot of work and would require native speakers of several Asian languages.

**Multi-lingual models warped by training data.** Language models are trained to predict the next word of a sentence. If you train with multiple languages, the model will try and transfer some of the knowledge. However, for the smaller languages this could look more like their meanings being strong-armed to analogies within the better-sourced languages (English, Chinese, Russian, etc). 

**The queries are a researcher degree of freedom.** The method I use to embed words is "My personality can be described as <mask> and [word]" where [word] is one of the personality words. Because of the way the sentence is written, the model loads pure personality information on the mask token and then embeds it. In my dissertation, I found this worked best. Of course, there are infinite variations to this, and you have to select one. Theoretically a researcher could have a particular result in mind, and then find a query that supports that. IMO it's not too much of a risk, given how similar this result is to what survey methods produce. We have a pretty strong prior about what personality structure we find with factor analysis. This method recapitulating it is evidence the method works.

**Outdated language model.** I did this work over 2 years ago, long before GPT-4 came out. Simpler times.

## Conclusion


If I were still in academia, this would be my research agenda. Add as many languages as possible, and try to understand all the ways the method can be biased. In the end, it may produce a universal model of personality superior to the Big Five. It would help us better understand who we are, and maybe even where we came from. For it is language that defines our species now, and it was language that forged our psyche deep in the past. We are habitually social because thousands of years ago to fail to manage your reputation was to die. Personality models are maps of language; they are vectors in the evolution of our mind.

[Subscribe now](https://www.vectorsofmind.com/subscribe?)

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!MDwl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F935dcb92-8e91-41c3-9630-2a80f2bc9a06_1024x1024.png)
