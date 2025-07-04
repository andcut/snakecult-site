---
title: "The AI Basis Of The Eve Theory Of"
date: "2025-07-04"
lastmod: "2025-07-04"
slug: "the-ai-basis-of-the-eve-theory-of"
description: "The Eve Theory of Consciousness proposes that self-awareness was discovered by women and spread memetically. To make this case I draw on linguistics, archeology, pharmacology, genetics, anthropology, ..."
keywords:
  - "vectors-of-mind"
  - "basis"
about: ['vectors-of-mind', 'blog-archive']
tags: []
author: "Andrew Cutler"
license: "https://creativecommons.org/licenses/by-sa/4.0/"
draft: False
quality: 6
original_id: "121454386"
original_url: "https://www.vectorsofmind.com/p/the-ai-basis-of-the-eve-theory-of"
---
*From [Vectors of Mind](https://www.vectorsofmind.com/p/the-ai-basis-of-the-eve-theory-of) - images at original.*

---

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!0pra!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff5166314-7a08-4939-9b16-2311d6214e87_1456x816.png)

The [Eve Theory of Consciousness](https://vectors.substack.com/p/eve-theory-of-consciousness-v2) proposes that self-awareness was discovered by women and spread memetically. To make this case I draw on [linguistics](https://vectors.substack.com/p/the-unreasonable-effectiveness-of), [archeology](https://vectors.substack.com/i/95941288/the-genesis-of-religion), [pharmacology](https://vectors.substack.com/p/comments-on-snake-venom), [genetics](https://vectors.substack.com/p/y-chromosome-bottleneck), [anthropology](https://vectors.substack.com/p/the-snake-cult-of-consciousness), and [neuroscience](https://vectors.substack.com/i/114650037/women-lead-the-way). And yet, I’m an electrical engineer. How can I have something valuable to say on a topic where so many others have actual training? Well, the idea for EToC actually came out of machine learning. Long-time readers have [watched the blog progress](https://substack.com/profile/31996842-andrew/note/c-16789002?utm_source=notes-share-action) from ML psychometrics to recursion and comparative mythology. Let me explain how I got here.

## Personality structure from words


Psychology has a ground truth problem. One researcher may theorize that there are only a few basic axes on which humans vary, the foremost being Internalizing vs Externalizing. Another may say that there have got to be something like [30 basic factors](https://www.scholars.northwestern.edu/en/publications/exploring-the-persome-the-power-of-the-item-in-understanding-pers) because humans are just that complicated. Who is right? Back in 1890, [Galton](https://astralcodexten.substack.com/p/galton-ehrlich-buck) suggested that instead of psychologists coming up with models of personality based on their pet theories, the best model already lay embedded in language. Every personality adjective exists because millions of people find it useful when they make judgments of others. Surely these words must illuminate all important aspects of personality. Put formally as the Lexical Hypothesis:

  1. Those personality characteristics that are important to a group of people will eventually become a part of that group's language.

  2. More important personality characteristics are more likely to be encoded into language as a single word.




This idea can be used to build a personality model. Simply create a list of personality adjectives, see how they relate, and compress that to a few latent factors[^1]. (LL Thurstone invented factor analysis to do this, and the [paper](https://psycnet.apa.org/record/1934-02322-001) is the namesake of this blog.) Traditionally the relationships between adjectives have been estimated by asking psychology undergrads which words describe them best. Those that say they are _bright_ also tend to say they are _open-minded_. This suggests they both relate to some underlying factor. In my dissertation, [I used language models to estimate word similarity](https://vectors.substack.com/p/the-big-five-are-word-vectors) and produced results similar to the traditional surveys (the first factor of the two methods correlates with r=0.93).

It’s easiest to understand this process with an example. Here are 100 random personality adjectives plotted on the two dimensions that capture the most personality information. Think of these as two of the [Big Five](https://en.wikipedia.org/wiki/Big_Five_personality_traits) (though there [is a difference in how they are rotated](https://vectors.substack.com/i/61936908/relation-to-the-big-five)). One of the jobs of a personality psychologist is to look at such plots and qualitatively describe them. You can practice that exercise in [Guess the Factor](https://vectors.substack.com/p/guess-the-factor), or do so below. How would you sum up Factor 1?

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!N5Ou!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3c50c0d0-6e09-4758-bfad-6c9135f154af_1423x891.png)Factors 1 and 2 are produced using [PCA](https://builtin.com/data-science/step-step-explanation-principal-component-analysis), a method to distill the personality information onto the smallest number of axes. For more information on how to get these from word vectors, see my paper [Deep Lexical Hypothesis](https://arxiv.org/abs/2203.02092). You can also reproduce this result (and much more) using my [code](https://colab.research.google.com/drive/1SXZNVqH0m_Bnd2hvIJFYiKQvHWpGu8ZM?usp=sharing), which runs for free on Google Colab.

From a statistical perspective, Factor 1 has stripped naked and is waving a big flag “I am by far the most important”, as I explain in the [Primary Factor of Personality](https://vectors.substack.com/p/primary-factor-of-personality-part) (PFP). Qualitatively, it is essentially “what society wants from you”. Be considerate and respectful, don’t be snobbish or uncooperative. 

To abstract PFP (Factor 1) another way, it’s useful to go back 2,000 years. The Israelites had libraries devoted to social rules and their proper application. With centuries of debate and interpretation, the letter of the law multiplied. But there was also a movement to distill the spirit of the law. 

According to the traditional narrative, a potential convert approached Rabbi Shammai and asked him to explain the entire Torah while standing on one foot. Rabbi Shammai, known for his strict adherence to Jewish law, found the question disrespectful and rebuffed the convert, dismissing him.

Undeterred, the convert then approached Rabbi Hillel with the same request. Hillel, renowned for his compassion and wisdom, responded in a different manner. Instead of dismissing the convert, Hillel accepted the challenge and provided a concise summary of the Torah while standing on one foot. He said, "What is hateful to you, do not do to your fellow: this is the whole Torah; the rest is the commentary." 

This is also an excellent description of the PFP. One must be able to put oneself in another’s shoes to be considerate or reject intolerance. Darwin, as it turns out, summed up our social instinct the same way in _The Descent of Man_ :

The moral sense perhaps affords the best and highest distinction between man and the lower animals;…the social instincts,—the prime principle of man's moral constitution (50. 'The Thoughts of Marcus Aurelius,' etc., p. 139.)—with the aid of active intellectual powers and the effects of habit, naturally lead to the golden rule, "As ye would that men should do to you, do ye to them likewise;" and this lies at the foundation of morality.

## Gossip as a fitness landscape


[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!urUr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6938214c-6388-43e0-8a75-44821ce23845_1024x1024.png)Mapping the mind

I used ML to distill personality factors from adjectives that were forged through eons of gossip. In fact, judging others is deeply intertwined with our evolution. Once again from Darwin in _The Descent of Man_ :

_After the power of language had been acquired, and the wishes of the community could be expressed, the common opinion of how each member ought to act for the public good, would naturally become in a paramount degree the guide to action._

On the Savannah, your reputation is your life. If others find you lazy or cruel, odds are you will have fewer surviving offspring. The first personality factor reflects this, being defined by words such as _considerate_ and _pleasant_ vs _uncooperative_ and _intolerant_[^2]. **In building a map of personality I also built a map of fitness**. But you don’t have to take my word for it. Scroll up and look at Factor 1. Would you sum it up with something like the Golden Rule? It’s not an accident this keeps popping up, as it is held in place by game theory and enforced via gossip. 

Over the past 200 years, Darwin’s idea has been developed. Consider the 2020 book [Survival of the Friendliest: Understanding Our Origins and Rediscovering Our Common Humanity](https://www.amazon.com/Survival-Friendliest-Understanding-Rediscovering-Humanity/dp/0399590668). The cover reads: 

> _For most of the approximately 300,000 years that Homo sapiens have existed, we have shared the planet with at least four other types of humans. All of these were smart, strong, and inventive. But around 50,000 years ago, Homo sapiens made a cognitive leap that gave us an edge over other species. What happened?  
>   
>  Since Charles Darwin wrote about “evolutionary fitness,” the idea of fitness has been confused with physical strength, tactical brilliance, and aggression. In fact, what made us evolutionarily fit was a remarkable kind of friendliness, a virtuosic ability to coordinate and communicate with others that allowed us to achieve all the cultural and technical marvels in human history. Advancing what they call the “self-domestication theory,” Brian Hare, professor in the department of evolutionary anthropology and the Center for Cognitive Neuroscience at Duke University and his wife, Vanessa Woods, a research scientist and award-winning journalist, shed light on the mysterious leap in human cognition that allowed Homo sapiens to thrive._

The book itself makes it clear that, to Darwin, fitness included cooperation; it pushes back against Darwinists, who equate fitness with ruthlessness. (For more see ’s [interview](https://insitome.libsyn.com/brian-hare-and-survival-of-the-friendliest-understanding-our-origins-and-rediscovering-our-common-humanity) with Brian Hare.) I was pretty sure that the first factor I found had to do with this process. Hence suggesting an additional claim to [Galton](https://www.experimental-history.com/p/how-to-keep-cakes-moist-and-cause)’s Lexical Hypothesis in [Consequences of Conscience](https://vectors.substack.com/p/consequences-of-conscience):

  3. **The primary latent factor represents the direction of social selection that made us human.**




In order to understand personality structure, I connected it to other concepts with which I was familiar. The most important were the Golden Rule and human self-domestication.

## The leap of faith


[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!eHWy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1975779f-d059-4ec4-8845-6ca8d1c618af_800x553.jpeg) **Domenichino:[The Expulsion of Adam and Eve](https://www.wikidata.org/wiki/Q77880823)**

Now, all I had was the fitness map that said the Golden Rule was paramount. What about our psychology could it have caused to evolve? A conscience seems like a pretty obvious bet. Maybe this had to do with the evolution of our inner voice. Let’s say the first inner voice said “ _share your food!_ ”; what would it be like to first identify with this inner voice? Well, I think it would be a lot like Genesis, and that’s the kernel I’ve been chasing ever since. Certainly, it was a leap. The evolution of the inner voice doesn’t necessarily follow from the Golden Rule, nor does our identification with it necessarily produce an inner life. But both seemed plausible and as I studied more they fit very cleanly into our evolutionary timeline.

As for Genesis, three things immediately struck me as plausible: feeling abandoned by god, inventing agriculture, and women leading the way. (The possibility of a [snake-venom ritual](https://vectors.substack.com/p/the-snake-cult-of-consciousness) only came after reading other creation accounts.)

### Abandoned by god


Initially, I was only concerned with where the inner voice came from. My conception was the self kind of absorbing an internal moral voice. This, I figured, would feel a lot like obtaining “knowledge of good and evil” as you took over the role of the hallucinated tutelary spirit. (A spirit I had assumed from the get-go with the thought experiment.) If you were used to outsourcing moral decisions, taking the reins would have felt like leaving a childlike state where you communed directly with god.

With a bit more reading, I realized that this moment of self-awareness was sufficient to produce an “I” in the first place. I make that argument in [Deja-you, the recursive construction of self](https://vectors.substack.com/p/deja-you-the-recursive-construction). It would have been the creation—or rather discovery—of the human condition in a very real way.

### Inventing agriculture


In Genesis agriculture is a consequence of the human condition. The discovery of “I”, it turns out, is also sufficient to explain the Agricultural Revolution. For it is plausibly a [package deal with recursion](https://vectors.substack.com/p/deja-you-the-recursive-construction) and the ability to think flexibly about the future. A general phase change in our planning abilities. 

If you believe that humans have been sapient for 200,000 years, then it is a great mystery why they would invent agriculture 11 times independently in the last 10,000 years. That’s a lot to cram into 10% of our existence. And, if you think your particular theory can explain it, please read [this review](https://www.pnas.org/doi/abs/10.1073/pnas.1323964111) where 25 scholars get together and agree that they cannot agree on what caused the shift.

### Women lead the way


The word vector for “feminine” correlates with the PFP. Even before contemplating a connection to Genesis, I conceived of the first person to identify with their inner voice as a woman. (As you can tell, I’m a true believer in what these word vectors can tell us.)

Genesis is a complex story. Obtaining agency is equated with becoming as gods and is a sin worthy of death. But it is also all part of the plan. Christianity throws in another wrench, where we are instructed to overcome original sin and become like God himself, taking up the cross to live eternal life (once again mixing life and death).

Likewise, Eve initiates death but is given the title Mother of All Living. Nowadays, consider how much effort is put into portraying women as agents in film. And yet, thousands of years ago, Eve is clearly painted as the agent who wrests humanity from its state of innocence. Adam tags along. Eve’s curiosity is portrayed as a bad thing, but it’s still an interesting addition to such a patriarchal text.

Conditioned on self-awareness being discovered, it seems likely that the explorer was a woman. Conditioned on women making the discovery, it seems likely that Adam and Eve are a memory. These, of course, are enormous ifs. But I had a sense they were possible. And enough will to investigate.

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!9mJt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67c3400e-4baf-476a-a8ad-10ad26212f62_843x403.jpeg)Demeter, Goddess of the Harvest and Eleusinean Mysteries

### The Sapient Paradox


The point of this post is to lay out how my work in ML led to the EToC, not to provide evidence. However, I want to briefly point out why it is plausible that self-awareness was discovered and that is recorded in myths. Quite simply, the human condition seems to be a recent phenomenon. Before 50 kya there is not great evidence for inner life, recursion, or any higher-order thinking. You may think that the evidence for anything that far back would not be good, but many archeologists and anthropologists disagree. The crux of the [Sapient Paradox](https://en.wikipedia.org/wiki/Sapient_paradox) is that [Behavioral Modernity](https://en.wikipedia.org/wiki/Behavioral_modernity) is regional before 10kya. That is very recent! And if the was a fundamental change to our psychology after Out of Africa, its diffusion must have been largely memetic rather than genetic. Self-awareness being discovered and spreading follows from (or is at least implied by) these constraints.

It’s a fantastic idea that the human condition could be recent. But it’s also a [fantastic idea that modern psychology was fully in place 200 kya](https://vectors.substack.com/i/114632067/years-ago) and lay fallow for tens of thousands of years before we finally applied it and conquered the world. The Eve Theory of Consciousness solves the problem of diffusion by allowing it to be memetic rather than just genetic. Fundamental changes could have occurred after we left Africa.

## Uncorrelated Truth


I believe the PFP is best described as one’s tendency to live the Golden Rule, the same latent dimension seen by Hillel and Darwin. This is an idiosyncratic view within the psychometric community. For contrast, consider the well-received paper [Two, five, six, eight (thousand): Time to end the dimension reduction debate!](https://psycnet.apa.org/record/2020-64387-036)

> _Lexical analyses and dimensionality-reduction methods are tools to explore rough contours of the personality space. We should not, however, delude ourselves into thinking that we are slicing nature at its joints to discover a “true” structure of personality._

Essentially, the argument is that any old rotation of the data is fine because we can’t plumb the structure for fundamental insights. But, depending on the preprocessing, 80% of all personality information is contained in the first factor. Surely that must be telling us something! And yet, still, researchers [largely believe that this factor is not personality signal at all](https://vectors.substack.com/i/61936908/enter-gfp). A [2013 paper](https://sci-hub.se/10.1016/j.paid.2013.03.002) opens _“The overwhelmingly dominant view of the GFP [the first factor] is that it represents an artefact due either to evaluative bias or responding in a socially desirable manner”. (_ I would note that even while believing this factor to be wholly bias [psychometricians distributed factor 1 to factors 3-5](https://vectors.substack.com/i/61936908/relation-to-the-big-five) in order to construct Conscientiousness, Emotional Stability, and Openness to Experience.)

With views like that one cannot connect lexical data to evolution or begin to hypothesize about the process of self-domestication. Writing my dissertation required spending many hours staring at these factors[^3]. Throughout, I thought they represented a fitness landscape, and would sometimes wonder what that would cause. As an engineer, I was blissfully ignorant of the prevailing view that the structure didn’t really matter. I went in deluded enough to try and slice nature at its joints.

## Conclusion


I hope this makes it clear why an electrical engineer is writing about mythology and consciousness. The idea found me, really. I was making a map of personality and it turned out to be a map of evolution. The connections to the Golden Rule suggested a proto-conscience as a mechanism of self-domestication. This was my first leap. I then speculated that the inner voice may have been involved. What would it be like to first realize the inner voice was “I”? Genesis struck me as a dead ringer[^4]. Further, many experts have argued that human psychology changed in the last 50,000 years often invoking language, religion, or self-domestication as crucial to this shift. In these time scales, it’s possible that such an important story could be preserved in myth. “ _In the beginning was the Word, and the Word was with God, and the Word was God_ ” … or—and don’t take this as blasphemy—possibly it was the inner voice.

Given how recently Behavioral Modernity arose, my contention is that creation myths can inspire [formal models](https://vectors.substack.com/p/eve-theory-of-consciousness-v2) that can then be connected to [philosophy](https://vectors.substack.com/p/deja-you-the-recursive-construction), [psychology](https://vectors.substack.com/p/consequences-of-conscience), [linguistics](https://vectors.substack.com/p/the-unreasonable-effectiveness-of), [archeology](https://vectors.substack.com/i/97498400/evidence-of-anti-venom), and [genetics](https://vectors.substack.com/p/y-chromosome-bottleneck). Perhaps these models can help us understand the myths as well. It is significant to me that Eve became as the gods and this required her separation from God. In Genesis, the explanation is that an often jealous God exercised righteous judgment. To me it makes sense as a natural law; humans and the gods could not dwell together for we fashioned “I” out of their remains. The distance between man and beast is then two steps: evolving a conscience, then rejecting it. Or perhaps that is too dour. It is more that we live in tension, and always have the choice. This epiphany granted [recursion](https://vectors.substack.com/p/deja-you-the-recursive-construction), the key to the backbreaking work of bending nature to our will. If I had to explain this in a way that could last 10,000 years, I would tell the story of Adam and Eve[^5].

Naturally, the journey started in my area of expertise where I had sure footing. It seems very likely to me that my map of personality records evolutionary pressures. Given how recently we have changed, and how long the Golden Rule has been a force, I go as far as adding a third postulate to Galton’s Lexical Hypothesis: **The primary latent factor represents the direction of selection that made us human**. From there, I _did_ make leaps but upon landing found myself in good company, with the likes of Jaynes, Jung, Pinker, Chomsky, and Descartes. This type of exploration is the essence of science; not everything has a p-value.

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!_K5c!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe08ec046-d650-4769-894e-fa1a77837040_1280x1847.jpeg)[Figurine of Isis](https://en.wikipedia.org/wiki/Isis#/media/File:Isis_with_Serpent_Tail_LACMA_M.80.202.222.jpg), Egyptian Goddess of Wisdom, second century CE

[^1]: I was surprised that Jordan Peterson described the derivation of the Big Five as an early form of AI in an interview with Joe Rogan. I made that argument in the first post of this blog and had never heard it before. Whatever you think of his politics, he is quite good on personality psychology.

[^2]: Some may note that being intolerant seems like a recent cardinal sin. Perhaps. It would be interesting to build word vectors on historical text and see how PC1 changes. Given that the latent factor of modern text is a good match for the Golden Rule, my guess is there wouldn’t be that much movement from, say, 1900 language. Hard to move something buttressed by so much game theory, even if the moral circle has expanded.

[^3]: Even though personality adjectives are fundamental to personality models, it is also rare for researchers to deal directly with words. In the 90s, once it was clear that something like the Big Five consistently emerged, researchers began to measure personality with phrase-based surveys designed to approximate the lexical structure (eg. the Big Five Inventory). (Trade secret: the fifth factor Openness/Intellect is not consistently recovered.) This was easier, and since then little work has been done on language. What’s more, my data was better than earlier attempts. If you want to understand how words relate, use a language model, not surveys of undergrads. No one else has spent as much time staring at such an accurate map of personality. (You can practice that exercise in Guess the Factor.)

[^4]: Consider the fact that Adam named the animals while in the Garden of Eden. Even without self-awareness, there would have been non-recursive language. Hunters have an encyclopedic knowledge of plants and animals. It may have been the most important part of language before The Fall. Astounding if that fact survived 10,000 years.

[^5]: I am impressed with Genesis, but that may just be what I know best. If I was Indian I would probably be talking about Saraswati, or if Navajo the role of women in the Emergence myth, or if Egyptian the moment when Atum called himself into being by saying his name (and then fought a primordial serpent). EToC requires these to be different perspectives of the same story. Obviously, that is traditionally shown by building a phylogeny. On these time scales and with my skills that’s not possible. This is why my focus is on the evolution of recursion. I want to show that it’s likely humans recently got recursion and that it diffused. That would radically change our prior on whether creation myths share a root and what the root was like.
