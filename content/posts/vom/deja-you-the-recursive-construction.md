---
title: "Deja You The Recursive Construction"
date: "2025-07-04"
lastmod: "2025-07-04"
slug: "deja-you-the-recursive-construction"
description: "\"Who looks outside, dreams; who looks inside, awakes.\" -Carl Jung"
keywords:
  - "vectors-of-mind"
  - "deja"
  - "recursive"
  - "construction"
about: ['vectors-of-mind', 'blog-archive']
tags: []
author: "Andrew Cutler"
license: "https://creativecommons.org/licenses/by-sa/4.0/"
draft: False
quality: 6
original_id: "114599293"
original_url: "https://www.vectorsofmind.com/p/deja-you-the-recursive-construction"
---
*From [Vectors of Mind](https://www.vectorsofmind.com/p/deja-you-the-recursive-construction) - images at original.*

---

"Who looks outside, dreams; who looks inside, awakes." -Carl Jung

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!yd8k!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Facfafcba-f620-4405-85ac-cd814afd48c1_1000x582.png)_Echo And Narcissus_ , John William Waterhouse

The unexamined life is not worth living, and yet, there be dragons. The seer Tiresias warned that Narcissus would live a long life if "he never knows himself." Indeed, he died doing what he loved, looking at his beautiful reflection and being doted on by a lover. Moderation in all things, I suppose.

What makes us human has been debated by philosophers for millennia, with introspection remaining a strong candidate. Peering inward requires the mathematical principle of recursion; the self perceives the self. More recently, linguists have entered the ring, bringing insights from computer science in tow. Surprisingly, their very different approach to the question of humanness produced the same answer. Recursion allows us to imagine a future and then work towards it. With it, we can build castles in the sky and on earth as well. By entering the memetic niche, we have come to dominate all species that live solely in the material world. 

It is rare that such divergent approaches converge or that one property can explain so much. As such, this series will adopt a maximalist position on the role of recursion in human evolution. It is well-trod ground, and the first two posts will review other people's work: what is recursion, and when did it evolve. I have theorized that recursion can be taught to an extent. The subsequent posts will discuss how this idea suggests a timeline that better synchronizes the evolutionary and archeological evidence. Finally, I explore the possibility that self-awareness was initially gendered. Women discovered inner life, and men followed.

### Computer Science


 _"Money for nothing, chicks for free"_ ~the Dire Straits

With age one realizes that there's no free lunch. Everything costs; there's always a catch. Relatedly, computer scientists can sometimes seem naive. The cause is their failure to internalize the free lunch principle, having learned about recursion. They know one can get computations for free; they've seen it!

A recursive function applies itself to its own output. Often, each successive application will be a sub-routine, where the input gets simpler and simpler until reaching some stop condition. Algorithmically, it is a superpower. Consider the fractal below. The obvious way to save the image is to enumerate the color of each pixel. Alternatively, one could compress it as a JPEG. [Under the hood JPEG uses recursion](https://qr.ae/prJyDe) to compute the Fast Fourier Transform. Without recursion, it would be [orders of magnitude slower](https://arxiv.org/html/math/0302212#:~:text=Graphical%20explanation%20for%20the%20speed%20of%20the%20Fast%20Fourier%20Transform&text=For%20a%20sample%20set%20of,of%20the%20Cooley%2DTukey%20algorithm.).

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!dOxu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2ff23125-7299-4679-b999-af6e51c20a23_1140x890.png)_"Fractals are the architecture of nature, revealing the underlying recursive patterns that shape our world."_ \- Benoît Mandelbrot

One can go one step further for this image because it is generated with a recursive process. Therefore, the image can be losslessly encoded with the few bytes required to write the recursive algorithm—[a few lines of code](https://en.scratch-wiki.info/wiki/Recursion_and_Fractals). Not only that, but the representation would extend into infinity, for one can zoom in to any edge and see the fractal recapitulate itself forever on increasingly finer scales. Recursion is almost alchemical in producing so much from so little. In the words of legendary programmer Niklaus Wirth:

> _The power of recursion evidently lies in the possibility of defining an infinite set of objects by a finite statement. In the same manner, an infinite number of computations can be described by a finite recursive program, even if this program contains no explicit repetitions._

My field of Natural Language Processing also uses recursion. Until recently, Recurrent Neural Networks were the model of choice for language. As their name suggests, RNNs process sentences recursively, one word at a time[^1]. This sequential processing represents timing information for free, a word's place in a sentence is known by the order it is received. Since 2018, almost all language models have been a type of feedforward network called a Transformer. However, one must append timing information to each word when using a feedforward network. In the end, computers are powerful enough not to worry about the inefficiency, but we will return to the idea that recursion automatically represents time. When implemented in the brain, it would have been a phenomenological leap.

### **Philosophy**


To be self-aware, the self must be aware of itself. Its own internal processes take itself as input. This is recursion. 

I think of it like this. Imagine a primordial self, unable to perceive itself. Written as a function: _self(perceptions)_. This would have been your own model of your own mind or interests. As input, it would receive all that you perceive. Introspection would necessarily produce recursion; the self would receive itself as input: self(self, perceptions). Two time steps of introspection could be written

[^2]:

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!31ID!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F243087e5-033e-4e36-9c6e-ba24939efa4c_1215x73.png)

From the example of RNNs, imagine how this recursion could change our perception and experience of time. It would be a new way to represent this dimension for free, a radical transformation to living in a particular moment.

It is also fruitful to imagine the rocky beginning of this function. Recursive programs are prone to blow up, and this one is running in your head. Take, for example, the most simple f(x) = x+1. If you recursively feed the output as input each time step, that function will grow to infinity. It's doubtful that the chain of consciousness was initially unbroken or pleasant. It would have begun in fits and bursts, the self rearing up for a moment only to be smothered by its own exponential increase. Neurons can only handle so much excitement. The function would need some sort of control system to stabilize recursion and refrain from hitting biological limits. There must have been more split personalities and inner voices with whom we did not identify. Apart from hallucinations, it also seems likely that exploding recursion could produce other side effects like excruciating headaches. Evolving recursion would have broken a few eggs.

There are reasons to believe that the self is recursive even when we are not peering inward. That is the position of the paper [Consciousness as recursive, spatiotemporal self-location](https://pubmed.ncbi.nlm.nih.gov/19763611/) and Douglas Hofstadter's _[I Am a Strange Loop](https://en.wikipedia.org/wiki/I_Am_a_Strange_Loop)_[^3]. However, there is much debate on this point.

[Subscribe now](https://www.vectorsofmind.com/subscribe?)

### **Linguistics**


Descartes equated subjectivity with self-awareness[^4]. Animals, lacking the requisite language and general intelligence to produce _"I think therefore I am,"_ were automata–meat machines. Linguists make no claims about the subjective experience of animals[^5], but they have converged on recursion as the dividing line between man and beast. This was Chomsky's significant contribution: that all languages are recursive in nature, which endows humans with unique abilities.

To learn more recursion in linguistics, I recommend Corballis's [article](https://www.americanscientist.org/article/the-uniqueness-of-human-recursive-thinking) or the footnote[^6]. But for this post, it suffices to know that linguists widely accept recursion as essential for a language with grammar.

### **Psychology**


Astute readers may be reeling at the potential bait and switch. Just because we use _recursion_ to describe all these things doesn't mean they are the same! And that's fair. There probably are some differences. But it's entirely in the mainstream to lump many types of recursion. The psychologist and linguist Michael Corballis adds several other psychological superpowers in his book[ The Recursive Mind](https://www.amazon.com/Recursive-Mind-Origins-Language-Civilization/dp/0691160945), including mental time travel and the ability to count. Mental time travel refers to projecting oneself into the past or future. As this is an imagined future, it also implies the ability to create fiction, worlds that do not exist. This separation produces the mind-body problem, where "I" first becomes distinct from the material world. Once we had recursion, many systems put it to use.

### How did it evolve?


Pinker and Jackendoff write in [The Faculty of Language](https://www.sciencedirect.com/science/article/abs/pii/S0010027704001763):

> _"The only reason language needs to be recursive is because its function is to express recursive thoughts. If there were not any recursive thoughts, the means of expression would not need recursion either."_

That is, recursion could have evolved separately from language and then been transplanted into our communication system after it sprung up. Communication itself doesn't require recursion. Given so many abilities require recursion, why did it first evolve? That is the million-dollar question! Nobody knows.

> _"Here the problem is not a paucity of candidates for evolutionary antecedents but a surfeit. As Herbert Simon has pointed out, probably all complex systems are characterized by hierarchical organization. So if "recursion" is identified with hierarchical decomposition and used as a criterion for identifying some pre-existing cognitive function as a source for exaptation to language, speculations can proliferate unconstrained." ~_ Pinker and Jackendoff

They also offer some possibilities: music, social cognition, the decomposition of objects into parts, and the formulation of complex action sequences.

#### The Case for Theory of Mind


[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!NjWR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4eff3129-d607-485c-bac7-9370716b2018_1024x1024.png)Before casting out an unclean spirit, Jesus asked its name. "Legion, for we are many," they said. Likewise, you contain multitudes.

Among these antecedents, social cognition stands out. Recursion is clearly useful when modeling other minds. Consider the basic moral rule: _do unto others as you would have them do unto you_. This is a recursive model of right behavior. To use even rough versions of it, one would be inching towards recursion. Darwin wrote that reputation management would be the primary selection factor on humans:

> _After the power of language had been acquired, and the wishes of the community could be expressed, the common opinion of how each member ought to act for the public good, would naturally become in a paramount degree the guide to action. ~The Descent of Man_

This is actually the[ insight that lured me into this rabbit hole in the first place](https://vectors.substack.com/p/consequences-of-conscience). I noticed that in personality models the[ dominant factor is essentially the Golden Rule](https://vectors.substack.com/p/primary-factor-of-personality-part). So modern language modeling supports Darwin on this.

Similarly, Dunbar put forth the[ Social Brain Hypothesis](https://onlinelibrary.wiley.com/doi/abs/10.1002/\(SICI\)1520-6505\(1998\)6:5%3C178::AID-EVAN5%3E3.0.CO;2-8), which says selection for intelligence was primarily about solving social problems. More directly, the paper[ Recursion: what is it, who has it, and how did it evolve?](https://www.academia.edu/6885660/Recursion_what_is_it_who_has_it_and_how_did_it_evolve_INTRODUCTION) takes ToM seriously as a path to recursion. At a certain threshold of sophistication, a phase change in ToM could produce recursion. I offered one path above, where the model of self was jerry-rigged to take itself as input.

So, it's unclear where recursion came from, but social cognition is a good place to look. Incidentally, if linguistic recursion is the same as the recursion required for self-awareness, this succinctly explains what language has to do with consciousness. Self-awareness requires recursion. In turn, recursion allows full syntactic language.

### Conclusion


[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!BPnn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6e29fae1-f7b3-46a4-86b9-0c0c9dbfe873_1024x1024.png)The Birth of ~~Venus~~ Recursion

If the evolution of the eye allowed us to see the electromagnetic spectrum, the evolution of recursion would have been a "third eye,"[^7] allowing us to look inward at ourselves and the symbolic world. With it, we saw imagined futures and entered the memetic niche. You could not teach a pre-recursive human the Pythagorean theorem or possibly even how to count[^8]. Further, recursion provided a natural way to represent time, unveiling an entirely new phenomenological dimension[^9]. We looked inward and have been living there ever since.

Recursion is, by definition, required for self-awareness. It allows realizations such as _"I think therefore I am"_ and likely much else. Many experts argue subjectivity, language, counting, and mental time travel also require recursion. Multiple lines of evidence suggest that only humans possess this ability, which is the key to our success.

In this post, we've explored the components of the recursive toolkit. The [next installment](https://vectors.substack.com/p/when-did-recursion-evolve) will delve into various attempts to date when it evolved. As a teaser, imagine the first self-aware individual. What would that have been like? Were they a child or an adult? Male or female? A crustacean? Chimp? Human? There is a huge range of answers in the literature.

[Share](https://www.vectorsofmind.com/p/deja-you-the-recursive-construction?action=share)

[^1]: For example with the cat chased the rat the RNN will first receive "the" as input and produce a context vector, a sort of memory of everything the network has seen so far. This context vector will be received as input in the next stage, along with the next word. So when "cat" is processed, it will be with reference to the context vector. The context vector is then updated, and "chased" is processed with it. This process recurs until the final word. At each step the context vector is updated, then fed to the next stage.

[^2]: There would have been intermediate steps. Imagine these almost-recursive calls: self(rival(self)) or mother(self(mother)). In fact, you can make the argument these are recursive, but it's just not standardized how many time steps are between, or what information will make it through each function. There must have been a lot of modules, and information hopping between them. If self() was called often, there may have been advantages to standardizing how often and in what way the info about self would get back to self. One solution is constant recursion.

[^3]: Also see Nick Humphrey's work: "An evolutionary approach to consciousness can resolve the 'hard problem' – with radical implications for animal sentience"

[^4]: Well, there were several steps. He was a substance dualist and believed in distinct spirit and material types of matter. General intelligence and introspection were evidence of the former variety.

[^5]: Why would they? For linguists, this connection is an unnecessary can of worms. They have plenty of evidence that recursion is important for humans, why also argue that without it animals are automata?

[^6]: Linguistic recursion, as in other domains, means that sentences may be parsed via self-referential subroutines. For example the sentence Watson wrote that Holmes deduced the body was in the shed can be divided into three parts:X1 = Watson wroteX2 = Holmes deducedX3 = the body was in the shedTo parse X2, you must first parse X3. Together this would be P(P(X3), X2). The result in turn can be combined with X1: P(P(P(X3), X2) X1). The meaning of the sentence completely changes with each additional clause, and this can go on indefinitely. We can prepend Jane said that John said that Harold said that… to X1 + X2 + X3 forever. Even though there are a finite set of words there is no longest grammatical sentence. Through the alchemical process of recursion, we pry infinity out of finite building blocks.

[^7]: In science, connotations are considered baggage and there is a race to find words unsullied by any sort of emotional valence. Hence the first personality factor is called "social self-regulation". I prefer connecting it to the Golden Rule, and the thousands of years of religious and philosophical debate that produced it. Likewise, I find "third eye" to be a good way to describe our ability to introspect, even if it has been used by religions, including most recently the New Age movement.

[^8]: Interesting to me how much mysticism was involved in even the discovery of the Pythagorean Rule.

[^9]: Obviously, animals exist in time as well. The argument is that recursion could have been phenomenological important.
