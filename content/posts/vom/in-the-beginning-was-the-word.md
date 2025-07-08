---
title: "In The Beginning Was The Word"
date: "2025-07-04"
lastmod: "2025-07-04"
slug: "in-the-beginning-was-the-word"
description: "\u201cIn the beginning was the Word, and the Word was with Psychology, and the Word was Psychology\u201d ~New Vector Translation"
keywords:
  - "vectors-of-mind"
  - "beginning"
  - "word"
about: ['vectors-of-mind', 'blog-archive']
tags: []
author: "Andrew Cutler"
license: "https://creativecommons.org/licenses/by-sa/4.0/"
draft: False
quality: 6
original_id: "51210419"
original_url: "https://www.vectorsofmind.com/p/in-the-beginning-was-the-word"
---
*From [Vectors of Mind](https://www.vectorsofmind.com/p/in-the-beginning-was-the-word) - images at original.*

---

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!5qwE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9f7c2505-9587-4daa-aac2-648b8bf16efb_1200x544.png)

_"In the beginning was the Word, and the Word was with Psychology, and the Word was Psychology" ~New Vector Translation_

All personality constructs are first described by words. From Freud's cocaine-fueled models to the staid Big Five, they are all at one point words. Much of academic psychology is concerned with comparing constructs. To do this, they must share a basis, typically a set of subjects. Subjects are given an instrument (usually a survey) which approximates where they live in construct space. Based on how subject responses covary, general claims are then made about the constructs. In this post we explore another way. Advances in NLP allow quantitative comparison of constructs in their natural habitat: language.

### Roadmap


In the [last post](https://vectors.substack.com/p/the-big-five-are-word-vectors?s=w) I argued that the Big Five are word vectors. This post makes the same claim about standalone scales, which then allows constructs to be compared without involving subjects. To demonstrate this, a broad personality model is introduced, as well as a method to represent constructs in word space. The outline follows:

 1. Compare constructs in subject vs word space

 2. Problems with subject space

 3. Relate kin and reciprocal altruism to the Big Five using subjects

 4. The same comparison in word space

 1. Introduce a (temporary) five factor model identified using NLP

 2. Project altruism words into that space

 3. Code available [here](https://colab.research.google.com/drive/13DA2IKQ9zRimGedww_09iGT6ehuYriVz?usp=sharing).

 5. Discussion, limitations, future work




### **A tortuous path**


To compare altruism with the Big Five, signal must travel through many transformations: Altruism (ideal) → described by words → survey developed (and hopefully validated) to approximate this construct → administered to subject who interprets these words and searches their soul → subject altruism score → **correlation in subject space** ← subject Big Five Inventory (BFI) score ← subject interprets BFI items and searches soul ← develop BFI to approximately measure this ← construct defined/communicated by qualitative description ← Big Five (defined by word loadings). Claims are then made about the two ideals, Altruism and the Big Five. 

### **The straight and narrow**


Why not use word vectors as the shared basis instead of subjects? The path is far more direct: Altruism (ideal) → described by words → vectorized to word space → **comparison in word space** ← Big Five, which already exist in word space, as discussed in the [previous post](https://vectors.substack.com/p/the-big-five-are-word-vectors?s=w). For those keeping score, that's 4 vs 10 transformations. (It's scored like golf.)

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!tbb9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb8b6c50-e94e-4462-8772-78359189f70e_1600x1305.png)Statistical realities visiting the field of psychology. It's been a rough few years.

### **Tal the Revelator**


The difficulty of using subjects to make claims about verbal constructs is not secret.

> _"Most theories and hypotheses in psychology are verbal in nature, yet their evaluation overwhelmingly relies on inferential statistical procedures. The validity of the move from qualitative to quantitative analysis depends on the verbal and statistical expressions of a hypothesis being closely aligned – that is, that the two must refer to roughly the same set of hypothetical observations. Here, I argue that many applications of statistical inference in psychology fail to meet this basic condition." ~Tal Yarkoni,_ The [generalizeability crisis](https://psyarxiv.com/jqw35/)

Validity here refers to a score capturing the construct it is intended to measure. It's worth reading the arguments and examples in full. But for us the take home is what can be done, given these realities. He suggests:

 1. Do something else (enter other fields). 

 2. Embrace qualitative research

 3. Adopt better standards (including 7 suggestions). 




> _"One is always free to pretend that small p-values obtained from extremely narrow statistical operationalizations can provide an adequate basis for sweeping verbal inferences about complex psychological constructs. But no one else— not one's peers, not one's funders, not the public, and certainly not the long-term scientific record—is obligated to honor the charade."_

Even if your view of research in psychology is not so dim, surely readers have been burned by papers that make claims but employ experiments that are only tenuously related. All available solutions are painful. The field may have to adopt a narrower view and leave the big questions to those studying history, literature, and linear algebra. I propose another way forward.

### **Convert to wordspace**. 4. Use word vectors as a shared basis

Constructs live together in word space, and yet when comparisons are made we drag them into subject space. This is an enormous, lossy, hassle. What if they could remain safely in word space? The conceit of natural language processing is that words are vectors in continuous space. Analyzing these vectors works well enough to be a [load](https://youtu.be/SGzMElJ11Cc?t=6667) [bearing](https://www.amazon.jobs/en/search?base_query=natural+language+processing&loc_query=&latitude=&longitude=&loc_group_id=&invalid_location=false&country=&city=&region=&county=) [process](https://blog.google/products/search/search-language-understanding-bert/) in trillion dollar industries, and is currently being ([re](https://vectors.substack.com/p/the-big-five-are-word-vectors?s=w))introduced to psychology.

### **Practice what you preach**


Here we will look at a traditional study done in subject space then try to improve it by moving to word space. Hedging against a straw man, the object is [Kin Altruism, Reciprocal Altruism, and the Big Five Personality Factors](https://www.sciencedirect.com/science/article/abs/pii/S1090513898000099?casa_token=05bTreOjGKUAAAAA:nLHTWhK3z45xUbN5nTVd7a3-Qaz9No22rQtVY6vpUjYpeZ1bkPy-cBig9UgRbn-GnqJScTCPpSY) which has been cited hundreds of times and whose first author has an h-index of 70.

Subjects are measured using three instruments: Big Five (via a survey of adjectives), Empathy/Attachment and Forgiveness/Non-Retaliation (survey of phrases), and altruism in a money-divvying game. Because the authors hypothesize that the interstitial space between Agreeableness and Emotional Stability (AKA Neuroticism) differentiates the two altruisms, some words are added to better measure that area. Similarly, a new questionnaire is designed to measure Empathy/Attachment and Forgiveness/Non-Retaliation, which are theorized as related to kin vs reciprocal altruism respectively. Above and beyond for this type of study, a game is used to measure altruism.

> _"In the version of the money allocation task used to measure kin altruism, the other person was described as a close friend—someone with whom the participant had a long history of friendship and with whom the participant had much in common. We hoped that by describing the friendship as an old one and the friend as someone very similar to the participant, the friendship would closely resemble the relationship one has with a relative. The reason why we did not use a relative as the potential object of altruism was to avoid introducing variance in responses due to the particular relative involved; for example, many people might be more willing to behave altruistically toward one sibling than another."_

In other words, as to not sully the data with real world feelings towards kin, reciprocal altruism is measured.

> _"In the version of the money allocation task used to measure reciprocal altruism, the other person was described as a non-cooperator—someone who had been rude, nasty, and inconsiderate toward the participant."_

And to measure reciprocal altruism they measure … non-reciprocated altruism? Naturally there are correlations and the authors conclude:

> _"The results of this study support the suggestion that personality traits involving empathy and attachment facilitate altruism that is primarily directed toward kin (i.e., kin altruism), and that personality traits involving forgiveness and non-retaliation facilitate altruism that is primarily directed toward non-kin (i.e., reciprocal altruism)."_

But if reciprocal altruism was never measured, how can the results support that claim?Statistics in psychology papers are, as Tal points out, often a rhetorical flourish. But we don't have to play along! Let's see what word space has to say.

### **A land of milk and honey (welcome to word space)**


In traditional studies, due to costs of mapping subjects onto personality space, resolution can only be high in a few personality areas at a time. That is why the authors probed Empathy and Non-Retaliation and the space between Agreeableness and Emotional Stability. All of those axes [exist in regular Big Five space](https://psyarxiv.com/vebtm/), but are measured quite granularly. In word space we can compare altruism to the complete Big Five in all their hi-res glory. On my github there are 2819 word vectors factorized down to five PCs. We can use those for convenience. The first order of business is to select word sets that describe each altruism. For kin words I chose those that embody familial roles:_brotherly, sisterly, mothering, motherly, fatherly, grandmotherly, grandfatherly, wifely, maternal, paternal._ For reciprocal altruism, I follow Trivers' definition. 

> _"Regarding human reciprocal altruism, it is shown that the details of the psychological system that regulates this altruism can be explained by the model. Specifically,**friendship, dislike, moralistic aggression, gratitude, sympathy, trust, suspicion, trustworthiness, aspects of guilt, and some forms of dishonesty and hypocrisy** can be explained as important adaptations to regulate the altruistic system. Each individual human is seen as possessing **altruistic and cheating tendencies** , the expression of which is sensitive to developmental variables that were selected to set the tendencies at a balance appropriate to the local social and ecological environment." _[The Evolution of Reciprocal Altruism](https://www.journals.uchicago.edu/doi/abs/10.1086/406755), Robert Trivers (bolding added)

Considering this, I chose:_discriminating, unforgiving, vengeful, loyal, neighborly, cooperative, trustworthy,_ and _fair._ This is about equal on erring towards cooperation but following up with moralistic aggression when things go wrong. Additionally, it tries to capture this altruism as the antithesis of cheating (eg. _fair_ , _trustworthy_).

(For an excellent explanation of the evolution of trust, see [this](https://ncase.me/trust/) interactive demo.)

#### May I introduce you to the unknown Five Factor Model?


Theoretically, we could use Big Five word loadings produced via surveys, but most of these words are rare enough to not be included. This is for the best as one would not get a good estimate of _grandmotherly_ by self-report among psychology students. As such, word vectors computed using the language model RoBERTa. Derived from a large and [well-characterized](https://openpsychologydata.metajnl.com/articles/10.5334/jopd.57/) list of personality words, the resulting Five factors are, in brief:

 1. Affiliation (or Socialization). How much do you want this person on your team? Similar to Agreeableness but precludes being a doormat. _Gullible_ , for example, loads neutrally on Affiliation but positively on Agreeableness.

 2. Dynamism. Quite a close match to Extraversion, but more about a sense of adventure, and less about confidence.

 3. Order. Conscientiousness with an edge. Ability to achieve your own goals. _Exacting_ vs _mushy_.

 4. Emotional Attachment. Whereas Neuroticism is concerned with instability, this is about attachment; both _caring_ and _spiteful_ are highly loaded.

 5. Transcendence. This factor is characterized by _unique, complicated, star-crossed, handicapped, mystical, heartbroken, other-worldly_ vs. u _nphilosophical, fancy-free, pigheaded, boorish, materialistic, self-centered, glib_. It involves looking beyond oneself and the mundane. That process is, apparently, wound up in pain. In fact, "troubled" loads more on Transcendent than Emotional Attachment (the factor related to Neuroticism).




The names for the first three factors are lifted from De Raad's pan cultural [work](https://journals.sagepub.com/doi/10.1002/per.1953) because, qualitatively, the match is closer than with the Big Five. Each factor deserves its own post. (For those in industrial psychology, I suspect that Order is more correlated with business success than Conscientiousness as it's more calculating than showing up on time.) But proposing models is not my forte, and finer language studies are forthcoming which may yield different structure. For now these factors suffice. Here is their correlation with the Big Five: 

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!Sxlw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F63c86f00-e0cc-4854-bd8a-e6ba3fc55449_366x374.png)

#### Results


Altruism word loadings on the first four factors (Transcendence is not important in this study):

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!Q5sr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4efdfb85-197d-4d57-8a8b-3675eaf2b162_955x735.png)It's prosocial to have strong family ties (high Affiliation), if a bit boring (neutral to low Dynamism). All words map to a similar place.

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!f7oe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb08b529e-7443-4f5b-af1e-ce080e36a4b7_961x735.png)Familial words load strongly on emotional attachment. Notice that parent and grandparent relationships are quite gendered. Males are less attached, as Trivers' [theory of parental investment](http://joelvelasco.net/teaching/3330/trivers72-parentalinvestment.pdf) predicts, and [statistics](https://www.pewresearch.org/social-trends/2013/07/02/the-rise-of-single-fathers/) bear out. Brothers and sisters, however, are equally attached, and to a lesser degree than parents. Come to think of it, _wifely_ shouldn't have been included in altruism about blood relatives. In agreement with [day time talk shows](https://www.youtube.com/watch?v=jXZB0FeTyE8), it loads less on attachment than motherly or grandmotherly.

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!FYnd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa40e5562-577f-4b55-bd16-d34ccec1c388_955x735.png)Reciprocal words try to capture ideal tit for tat behavior when a partner is cooperating or cheating. As such, these words are far more spread out, though still mostly positive. Even 'discriminating' is slightly positive, meaning I don't think the word is being coded as something like 'racially discriminatory'—sometimes these language get confused with phonetic similarity (eg. eccentric and ethnocentric).

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!lGox!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6eb4b7d2-4728-4f66-83ce-cd95e2346144_961x735.png)Cooperation and neighborliness slightly imply one's own goals are taking a back seat. Unforgiving and discriminating are for those that mean business.

To compare the altruisms, we would like to collapse each of these word sets down to just one vector. (There is room for debate if that even makes sense given reciprocal—and to a lesser extent kin—requires different responses to different scenarios.) The cheap and dirty solution is to treat each construct as a [Bag of Words](https://en.wikipedia.org/wiki/Bag-of-words_model) and take the average. The mean loadings are:

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!TMN7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe3aaf685-9bb3-4dbf-974f-0ab994f40a88_356x238.png)These are z scored against all 2819 words. On average, kin words are 1-1.5 SD out on both Affiliation and Emotional Attachment.

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!mDHG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fba83d4f1-2f47-42e8-a158-368c7681a2db_356x238.png)Reciprocal altruism also involves Order, accomplishing your own goals.

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!48eW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd912d107-48f4-4d5e-bb23-fe24dd932b78_356x238.png)Difference: Kin minus Reciprocal loadings. Dominated by Order.

### **Discussion**


I don't think the paper in subject space includes a valid measure of kin or reciprocal altruism and as such doesn't add to our understanding of how it relates to personality. This is a surprisingly common failure mode. Word space provides some insurance against invalid comparisons. We have better intuition for where a word should be in word space, than for how subject 112 should answer a survey. It's easier to spot errors. 

From a Bayesian point of view, something different is happening in subject vs word space. Experiments including subjects seek to bring new information to the table. The hope is that will update readers' view of the world. But researchers (and lay folk) have lots of social experience and more acute perception of psychological processes than the snapshot provided by a survey. It's hard to move the needle much. Word space is more akin to visualizing our priors than producing new knowledge. This view is valuable because language is where the rubber meets the road, so to speak. As JL Austin put it:

> _"Our common stock of words embodies all the distinctions men have found worth drawing, and the connections they have found worth marking, in the lifetime of many generations: These surely are likely to be more numerous, more sound, since they have stood up to the long test of survival of the fittest, and more subtle, at least in all ordinary and reasonable practical matters, than any that you or I are likely to think up in our armchair of an afternoon—the most favorite alternative method."[A plea for excuses](https://sites.ualberta.ca/~francisp/NewPhil448/AustinPlea56.pdf)_

Analysis in word space is comparatively straightforward. Rather than tables of correlations and p-values, words are simply plotted on the axes of interest and visual judgements are made. Kin altruism words cluster tightly on both Affiliation and Emotional Attachment, the only two factors with considerable loadings. Fathers, but not brothers, are less attached than their female counterparts, in line with Trivers' theory of parental investment. Brothers and sisters have as much reason to look after their siblings. Fathers, however, have less reason than mothers. Sperm is cheap. Eggs and pregnancy are expensive.

Reciprocal words are more spread out, reflecting traits ideal for responding to different scenarios: partner cooperation or defection. The most salient difference is higher average loading on Order—accomplishing one's own goals. Initially called _delayed return altruism_ , reciprocal altruism is not about sacrificing oneself for a stranger but rather investing in your own future through pro-social means. On the other hand, kin altruism refers to helping family even at your own expense because of the selfish genes tugging at your heart strings. This is apparent in higher loadings of kin altruism words on Emotional Attachment, supporting Ashton's hypothesis. But the main action is on Order, far from where the subject-space instruments were designed to detect. The costs of sampling in subject space make results more dependent on researcher priors.

Interpreting these plots can feel like reading tea leaves, but I'm about 70% sure of what's here. One thing that gives me pause is that the two altruisms are represented in different ways. Kin words all describe relationships (eg. _mother, father, brother_), while reciprocal words are a mix of relationships (eg. _neighbor_) and traits fit in repeated positive-sum games (eg. _vengeful, discriminating, cooperative_). Uncertainty aside, wouldn't it be cool if in an afternoon I ran an experiment that combines the lived altruism experience of millions of people? What generations have agreed makes someone paternal, sisterly, or neighborly. As always with a new source of signal, one starts shooting from the hip. Eventually the Wild West is tamed; methods and heuristics emerge. There is much room for improvement. Readers can tweak the word sets and get new results in a matter of minutes using this [colab notebook](https://colab.research.google.com/drive/13DA2IKQ9zRimGedww_09iGT6ehuYriVz?usp=sharing). Please do so!

#### Advantages of word space


 1. Connected to the Lexical Hypothesis. Grounded in decentralized social reality.

 2. Fewer transformations. Each step is lossy and introduces bias.

 3. Less statistically intensive after the conversion to word space. (Lower barrier to entry.)

 4. Effective sample size (those that contributed to the language model via comments on reddit, writing books, or pubMed articles) is much larger and diverse than most studies.

 5. Better job prospects for psych PhDs who know NLP. 

 6. Easier to do multilingual/multicultural work. Some models are trained on 100 languages simultaneously (which is how Meta trains [hate speech filters](https://ai.facebook.com/blog/how-ai-is-getting-better-at-detecting-hate-speech/) in languages with few examples).

 7. Language models [keep](https://openai.com/blog/introducing-text-and-code-embeddings/) [getting](https://say-can.github.io) [better](https://ai.googleblog.com/2022/04/pathways-language-model-palm-scaling-to.html).

 8. Open science.

 9. [Avoid the IRB](https://slatestarcodex.com/2017/08/29/my-irb-nightmare/).




#### Disadvantages


 1. More moving parts. There are billions of parameters in a language model! However, even billions of neurons and dozens of training decisions can result in a stable representation. Any language model worth its salt can complete the analogy "husband is to wife as king is to ____".

 2. Can't break results down by demographic. Sometimes it's interesting to know the personality of elementary school teachers between 25-30. Or to know how some construct correlates with arrest record. Impossible in word space.

 3. Aren't language models biased? Well, not more than self-report.

 4. Defining altruism as the sum of a bunch of word vectors (ie, a bag of words) is a bit hacky. There is substantial room for improvement here.




[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!ctzj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F455fdb70-3c84-4dfe-81bf-6bf6e676fd44_1600x1128.jpeg)Psychologists happy with another 40 years wandering through subject space.

### **Foreign gods**


 _"I think Kafka was right when he said that, for a modern man, state bureaucracy is the only remaining contact with the dimension of the divine."_ ~Zizek, A Pervert's Guide to Ideology

He's describing here, of course, the transcendent feeling of filing an appeal with the IRB. I have a prediction. Word space is the good and right thing to do from a signal processing perspective, but its adoption will be driven as much by the convenience of not being regulated. The corollary is that the IRB will be the first government body to declare language models sentient.

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!6nGN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fedfc8bac-cf78-40f9-88d3-9a30066ff108_817x1600.jpeg)John spreading the good word space

### **Preparing the way**


We would like to extract relationships between constructs from language models. To do so in a way that adds signal rather than more noise requires a lot of validation work. Initially, this means comparing to well established survey results. Can they be recovered using word vectors? Where do they fail? Once that has been established, every paper that ends "more research needed" should find a way to ask the question in word space. 

I spent more than a year fine-tuning a [method](https://psyarxiv.com/gdm5v/) to extract personality relationships from [RoBERTa](https://arxiv.org/abs/1907.11692), the state of the art model at the time. Soon after GPT-3 was released and it performed better right off the shelf. That compute supersedes domain knowledge is a reoccurring [bitter lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) within AI. Compute increases exponentially. If you can get 30% gains over a general ML solution using domain knowledge, you can also just wait for [compute to catch up](https://twitter.com/russelljkaplan/status/1513128016452337667) and get the same results using general methods. Finding ways to relate psychology questions to off the shelf NLP models is therefore a good way forward. A new model with noticeably better performance is made public every six months or so. Those validating word space are preparing the way for greater intelligences—[PaLM](https://ai.googleblog.com/2022/04/pathways-language-model-palm-scaling-to.html), GPT-7, OSCar (**O** ptimal **S** entience **Car** tography)—to rain down psychological truths. 

Natural language is teeming with shared theories about the world. Now that we can quantify them, can't they be used as evidence?

If you find this interesting, please share!

[Share](https://www.vectorsofmind.com/p/in-the-beginning-was-the-word?action=share)
