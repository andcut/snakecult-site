---
title: "The Linguistic Hypothesis"
date: "2025-07-04"
lastmod: "2025-07-04"
slug: "the-linguistic-hypothesis"
description: "[intro isn\u2019t that engaging and is too flippant. Just say that psychometrics feels ick because it puts a number on humans. Galton addresses this by arguing against free will. If one can characterize a ..."
keywords:
  - "vectors-of-mind"
  - "linguistic"
  - "hypothesis"
about: ['vectors-of-mind', 'blog-archive']
tags: []
author: "Andrew Cutler"
license: "https://creativecommons.org/licenses/by-sa/4.0/"
draft: True
quality: 1
original_id: "53913156"
original_url: "https://www.vectorsofmind.com/p/the-linguistic-hypothesis"
---
*From [Vectors of Mind](https://www.vectorsofmind.com/p/the-linguistic-hypothesis) - images at original.*

---

[intro isn’t that engaging and is too flippant. Just say that psychometrics feels ick because it puts a number on humans. Galton addresses this by arguing against free will. If one can characterize a motor by horsepower, then one can characterize the character of this habitual machine we call man with a few similar numbers]

In the 1890s progress in science wasn’t the narrow, incremental affair it is now. For example, the paper that lays out the Lexical Hypothesis also argues against free will. Opponents of psychometrics have long gone on about the impossibility of quantifying the infinite depths and heights of a soul. We’re human, you can’t put a number on that. Checkmate, psychometrics. Galton addresses the issue by arguing we don’t even have free will; of course one can take the measure of this habitual machine we call man. He then describes the Lexical Hypothesis, which includes two postulates.

  1. Those personality characteristics that are important to a group of people will eventually become a part of that group's language.

  2. More important personality characteristics are more likely to be encoded into language as a single word.

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!fXSx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F7632794a-3210-4016-aec5-cf2b57cc29a4_500x206.gif)Galton explaining that personality can be measured and time is a flat circle. Papers used to be wild.




Language contains infinite way to evaluate character. Together, these postulates suggest that most of the structure is contained in a much smaller subset: trait adjectives. Speakers mutually agree on which concepts merit lexical real estate. It’s a clever crowdsourced threshold for what counts as important enough for researchers to model. This approach has been enormously successful. Without it, mapping personality structure in language would be have been intractable. However, it leaves a lot of evaluations on the table. What do we get if we include ALL personality descriptions?

### **The Linguistic Hypothesis**


I suggest calling this broader form the Linguistic Hypothesis. Though not as pithy as Galton’s two postulates, three points are salient.

  1. **All personality concepts are contained in linguistic space.** That is, every standalone scale exists within linguistic space, as well as every judgement one makes with words.

  2. **Language is the view from society.** As such, value judgements are inherent to evaluations.

  3. **Linguistic space includes folk explanations**. Personal evaluations embed stories about why someone is a particular way. It’s not a merely descriptive space.




To be clear, I don’t think general linguistic structure will be that different than what is instantiated in the Lexicon. But this does allow very specific evaluations to be mapped onto that general structure. “Defensive when a superior offers constructive criticism” is a particular flavor of defensiveness and ego protection not completely covered by individual words. This unites personality measurement (which uses phrases) with structure discovery (which uses words). It also makes it clear that all personality scales should be subsumed within a general model. Of course, there is a tradeoff between parsimony and descriptive power, but any personality not picked up is due to the choice about how simple to make the model. There isn’t personality information outside linguistic space.

I include 2 and 3 as teasers of subsequent posts, we will spend the remainder here on 1.

#### **1\. Linguistic space is general**


I use linguistic space to mean the quantification speech or text. The current state of the art is to represent a word or phrase as a vector. This is of course a limiting model; it’s not clear how much meaning can be packed into a vector. But it is sufficient for accomplishing increasingly complex tasks in NLP and is likely sufficient to contribute to our understanding of personality structure. Below is a 2D projection of a linguistic neighborhood related to animal sounds from [OpenAI’s website](https://openai.com/blog/introducing-text-and-code-embeddings/). Notice that this space captures the semantic similarity of “moo” and “bovine buddies say” even when “moo” and “woof” are phonetically closer. 

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!yB6S!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F7d0bf7e1-653d-45e5-998d-737ed55532df_1600x1006.png)

In a previous post I used word vectors to explore the difference between reciprocal and kin altruism. The results are more accurate than a well-cited paper that does the same using surveys as the instrument of discovery. The main limitation is that word vectors instead of phrase/paragraph vectors were used. To describe altruism I simply embedded words related to the concept, then analyzed where they landed in word space. It would be better to embed entire passages from the literature that describe or define each altruism. My guess is this is currently feasible, but just needs a year or so concentrated effort to build out a beta version to the standards of skeptical academics (as they should be!). The upside is enormous. It will allow researchers to quickly understanding how constructs relate to one another. It will also make it abundantly clear that we need a better general model of personality. A model that contains any standalone construct.

##### **A theory conspiracy**


It’s not all that controversial to say that linguistic space (and derivative models) should contain all of personality. But it is fraught to say the dominant personality model should. Consider this paper making the rounds. [tweet to paper, explain that it is an excellent question, but frames it a bit off. Of course a subscale of the Big Five is contained within the Big Five. Would be better to frame this as “from a Big Five instrument, how well can one construct each standalone scale”.] 

[#10](https://personalitypsychologypodcast.com/blog/) The past, present and controversies of personality trait psychology with Jeff Mcrae:

“The other striking progress is of course the ffm. And in particular the consensus on ffm. Because the ffm had been discovered over and over by the researchers. And, nothing happened. The reason that it did… there was a sort of conspiracy among five factor enthusiasts to kind of minimize the differences of the lexical model and the questionnaire-based model so that when I edited the 1992 special issue I chose oliver john (goldberg’s student). There are differences between models, but also similarities. And therefore we have a model we can show to developmental psychologists, IO psychologists. …kinda state of the art.” 

To be clear, Vectors of Mind is pro the Big Five conspiracy. It is a fairly reproducible base model that probably could not have escaped the confines of personality psychology without a little ironing over and salesmanship. And it certainly met a need. “‘Big Five’ personality” returns 443,000 results on google scholar. Hard to overstate the impact this has on our understanding of personality as it relates to jobs, romance, and genetics. However, with language models, we can do better.

Some scientists think the ideal format for the discovery of knowledge is preprints + twitter. A sort of public review system that can happen twice as fast. Substack has a part to play as well as it can host interviews and comments. One goal of this blog is to facilitate the rapid exchange of ideas in order to build a better general model.

By the 90s, personality psychologists had produced a fairly reproducible model. Other fields could use this tool, and it makes sense there was some ironing over disagreements as well as salesmanship. It would disrupt IO research if personality psychologists produced an updated general model every five or so years, in addition to not instilling confidence in their previous work. The strategy did, however, stall progress on general personality structure. Now that language can be represented as a vector, we can bring much more data to bear on the question. Can we build a better model now? “‘Big Five’ personality” returns 443,000 results on google scholar. The impact on other fields would be immense.

Reading the genesis of the Big Five as a wide-eyed PhD student I thought surveys of personality adjectives typically produced clean structure. This led to significant consternation when I was unable to reproduce it with NLP data that I hypothesized was of higher quality.

It’s an empirical question as to how well standalone personality constructs can be subsumed by the Big Five. Tweet and paper that try to situate many stand-alone scales in the Big Five: 

[*[Image: Visual content from original post]*Tom Costello @tomstello_It's not just grit: most (read: a vast majority of) highly cited scales in psychology are subsumed by the Big Five. That is, they can probably be considered [sometimes interstitial] facets of the Big Five. (Bainbridge, Ludeke, & Smillie, 2022, JPSP) [psyarxiv.com/vebtm/](https://psyarxiv.com/vebtm/) *[Image: Visual content from original post]**[Image: Visual content from original post]*](https://twitter.com/tomstello_/status/1507069496787361793)[6:59 PM ∙ Mar 24, 2022

* * *

382Likes110Retweets](https://twitter.com/tomstello_/status/1507069496787361793)

The way these numbers are calculated is dumb. As in most methods in psychology everything is done on a factor level. So scores indicate how well a scale can be captured by 

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!u6g8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F2c0d0f5f-32f3-453c-b7df-d34e29199815_500x288.gif)Galton after he finds out how well various scales can be subsumed into the universal model for ‘general’ personality.

Those are rookie numbers. A general model of personality should subsume _any_ scale. Certainly the top 30 standalone scales should be handled no problem. **One of the goals of this blog is to facilitate creating such a general model**. Make the case for the lexical (er… linguistic) hypothesis. That we now have much better language data. And make advances in NLP available to personality researchers.

#### **2\. Values are inherent to language**


The Righteous Mind talks about how we didn’t evolve to reason, but to justify our position to the tribe. Once we could talk, it became a powerful tool to make friends and coordinate shared goals. Those predisposed to use it to get ahead, did. We are their children. The result is that humans are wired to be lawyers more than scientists and the languages that co-evolved with us fill that function.

Language is what makes us human, and it was invented primarily to gossip and form teams. Grooming vs Gossip https://www.amazon.com/Grooming-Gossip-Evolution-Language-Dunbar/dp/0674363361

Because humans are dependent on one another for survival, the evaluations of our tribe constitute a fitness landscape. At the very least it constitutes the direction of social coercion. One needs to be careful with this as we only have access to modern language samples. Since the advent of birth control, natural selection doesn’t primarily happen by calorie count. Who knows what gossip looked like 10k years ago. Will return to the fitness landscape question in another post.

Goldberg is wrong with his 50 word pairs (‘cheap’ vs ‘frugal’). That GFP paper that seeks to remove evaluative content is also bogus. 

#### **3\. Language includes (folk) explanations**


Those studying personality have divided the goals of models into explanatory, descriptive, and predictive. [describe why]. Also note that if a model is explanatory, it is necessarily descriptive and predictive. LSA is a good example of a highly predictive and descriptive model which absolutely mangles the explanation. Language isn’t a bag of words.

In Mexico when a guy sweet talks and buys gifts in order to get laid, it’s called conquistadoring. This turn of phrase relies on a rich shared model of sex, gender, and that it’s okay to joke about tragedy (including your own genocide).

Language isn’t a dry description of the world! Words exist in competition to communicate ideas we value sharing; only the most useful survive the churn of human generations. Because the utility includes communicating explanatory models of the world, personality models built from language should share that property.

Goldberg, one of the fathers of the Big Five, claimed it was just descriptive. 

Make the argument that the Big Two are delightfully theoretical. Digman’s paper was basically ahhhh shiiiieeet, all the theory is right here. What I think is going on is that the Big Two exist in lexical space, but were hidden by varimax rotation. Digman does PCA on Big Five results and arrives at the orthogonal solution, which is a thing of beauty. Big Five is ascendant and his data is quite convoluted; he can’t present (or perhaps even think of) his result as in competition with Big Five. Instead he presents a hierarchical relationship between the Big Two and Big Five.

Read the paper, notice the glee. Now consider the Big Five. Does it fill you with joy? No, because the factors are about as theoretically inspiring as a USB port. Much of the selling point is as a standard that is Good Enough. Have you ever read an empirical paper that triumphantly finds so much theory in an empirically derived construct? Maybe this one from Jordan Peterson and DeYoung… but that’s also the Big Two! I believe there exists a model as theoretical as the Big Two and expressive as the Big Five. I don’t have the psychology chops to propose such a model, but somebody ought to!

Difference between openness and my fifth factor. One of my criticisms of Openness is that it contains a lot of class markers. It is defined by surveys to undergrads in Oregon, after all. Openness implies liking the theater and not believing in God, important parts of the identity of a college student in the 90s but not essential to the human condition. In natural language, PC5 loads heavily on intricate, extraordinary, otherworldly, profound, and serpentine. It also loads on unusual, star-crossed, old, homeless, and cursed. The antithesis is inconsiderate, conceited, snide, bossy, priggish. It’s about transcending the material and social world, often through pain. If this is “seen some shit” then Openness is “seen some shit while studying abroad”. There are also notes of humility, which should excite HEXACO fans. (You can derive this space using code from my paper. In future posts that focus on personality structure I’ll make narrower notebooks to spoon feed people the analysis.)

### **Conclusion**


The Linguistic Hypothesis hypothesis has been used to great effect in developing general models of personality. Many narrower constructs could have been explored in Lexical space as well, and with more treatment as possibly explanatory. But there are limitations to using personality adjectives. Czech and Korean, [for example](https://link.springer.com/article/10.1007/s12124-016-9375-1), use grammar rather than specific words to communicate personal evaluations. Additionally, some psychological constructs are difficult to locate in word space, such as vulnerable narcissism. 

To me language is what makes us human and psychology is the study of that condition (along with history and literature). The beauty of the lexical hypothesis is that the analysis is decentralized to whoever used the language. Workplace gossip, operas, and jokes on reddit all contribute. We can get a long way by letting geniuses like Freud introspect. But they inevitably overstate their own neurosis. The oedipus complex is neither so consuming or universal as Freud imagined. The Lexical hypothesis grounds psychology in shared reality. It is the best insurance to be an empirical science.

This post frames the Lexical Hypothesis as a restricted version of the Linguistic Hypothesis, which also makes claims about the properties of personality in linguistic space. We are at the cusp of meaningfully embedding any personality evaluation into a shared space. There is going to be a lot of cross pollination between ML and psychology. The ML contributions need to be situated theoretically by those that understand psychology. There is also lots of room for ML people who would simply like to apply NLP methods to an interesting problem.

**Cut paragraphs:**

Restricting the analysis to single words is a clever threshold. Because we can’t hope to quantify all possible character descriptions, we limit ourselves to those that win lexical real estate in the brawl of language evolution. This flattens the dizzying complexity of language and results in a model of language that is sufficient to develop general personality models, such as the Big Five. What more personality information do we get if we expand from the lexicon to the language itself?

Language is highly nonlinear and variable (15% of all Google searches are [unique](https://searchengineland.com/google-reaffirms-15-searches-new-never-searched-273786)!), but we are getting better at mapping it to a fairly low dimensional space. This has been done for 30 years with word vectors, and has recently been successfully extended to phrases via Transformer models like GPT-3.

The hope is that any description of personality can be meaningfully mapped to such a space. Consider Vulnerable Narcissism which is defined as: BLAH. This isn’t captured well by any single word in the English Lexicon, even after the colloquialization of Freudian models in terms like egotistic. Therefore it’s hard to define if the only building blocks are word vectors. But it can be described using a string of common words, which transformers can vectorize as one coherent idea. Can GPT-3 accurately disambiguate vulnerable and grandiose narcissism? That remains to be seen. But GPT-10 will certainly be capable.

The Lexical Hypothesis is sufficient to develop general models of personality. It’s true that just a few words pretty much cover the Big Three. The structure I found factorizing just 87 websters words is pretty similar to that produced by 2,700 words. But this does suggest an area of progress in comparing narrower models to each other or the Big Few. They all share a basis in language. 

The Big Few models were developed via the Lexical Hypothesis. Not aware of any other popular model. It’s a shame, nothing says that the Lexicon only contains broad strokes. It’s an analysis decision to only look at general latent factors.

[MBTI gets past the ick factor of assigning people a number by creating cute types like The Governor. My guess is Galton's types would have been less, er, marketable.] 

Let’s look at what is what works most poorly with the big five, meaning making. Hopefully that can be found in the Unknown FFM. Make the claim that, in the future, we will have a replacement for the Big5 that can subsume anything. This might take a few years, and won’t necessarily be a factor structure (not completely normal gaussian structure). But there will be a low-dim model that contains anything significant enough to study. (And we could expand it to include anything that can be described by words). One reason why this may take several years is that words and phrasal evaluations need to be combined. Once you drop the Lexical threshold of the few hundred most common single words, the problem explodes in complexity.
