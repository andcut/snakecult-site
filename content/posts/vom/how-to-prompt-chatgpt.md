---
title: "How To Prompt Chatgpt"
date: "2025-07-04"
lastmod: "2025-07-04"
slug: "how-to-prompt-chatgpt"
description: "My work has become dangerously close to a Prompt Engineer1. This is fine by me, as it combines my love of writing, psychometrics, and NLP. Here are some of the most overpowered prompting techniques:"
keywords:
  - "vectors-of-mind"
  - "prompt"
  - "chatgpt"
about: ['vectors-of-mind', 'blog-archive']
tags: []
author: "Andrew Cutler"
license: "https://creativecommons.org/licenses/by-sa/4.0/"
draft: False
quality: 6
original_id: "145544092"
original_url: "https://www.vectorsofmind.com/p/how-to-prompt-chatgpt"
---
*From [Vectors of Mind](https://www.vectorsofmind.com/p/how-to-prompt-chatgpt) - images at original.*

---

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!EpIx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F719d87af-7c69-45fd-8c84-595b16af3dae_1024x1024.webp)You after reading this post

My work has become dangerously close to a Prompt Engineer[^1]. This is fine by me, as it combines my love of writing, psychometrics, and NLP. Here are some of the most overpowered prompting techniques:

 1. Use clear and specific instructions

 2. Chain-of-thought reasoning

 3. Collect the required information before doing a task

 4. Break tasks up into steps

 5. Technical terms are your friend

 6. Grab-bag of useful phrases




#### **1\. Clear and specific instructions**


Lawyers and computer scientists are naturally good at this. In fact, one of the joys of prompting is that one can be much less precise compared to regular code, and LLMs often get the gist. However, many requests can be improved by simply being explicit about the task and the format the answer should take. For example, I recently scrounged up this meal:

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!dVwU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F216d83a0-b1be-4f15-877a-bfbb9842c0ed_1284x1253.jpeg)

It tasted great, thanks for asking. Other examples:

 * "Summarize the history of AI in a paragraph."

 * "Create a table of the oldest language families sorted by age. Be exhaustive."[^2]

 * "Rewrite the quoted text in a White and Strunk fashion. Give me three options."

 * "Calculate a Pearson correlation matrix for columns 2-7 of the attached.csv."

 * follow-up: "Write code to display the results as a heat map at high enough resolution it can be used in a poster. Use best practices in aesthetic choices"




Specific instructions often include specific examples. White and Strunk wrote _Elements of Style_. Citing their book is better than using adjectives such as "concise," "professional," or "excellent" writing. In part because LLMs tend to over-deliver, especially on specific adjectives. Hence, if you want the robot to adopt a sassy persona, try telling it to act like Veronica Mars or Regina George from Mean Girls.

#### **2\. Chain of thought reasoning**


LLMs are trained on an enormous text corpus to predict the next word. Surprisingly, this makes them good at approximating reasoning, but it quickly breaks down for complex tasks. Here, "complex" can mean something like "add up the numbers in column 1". This is very hard to 1-shot, and it will spit out some number that seems reasonable and will likely be in the right range but not the correct answer. Appending "think about it in steps" does wonders. Often, you don't even have to specify what the steps are; LLMs can infer that to sum column, the intermediate steps are to write "n1 + n2 + n3 + … + n100 =" It is essentially prompting itself to get a better answer on the right side of that equal sign. Or, by analogy, giving itself time to think about it. For any problem, the phrase "think about it in steps" is your first line of defense in dealing with LLM hallucinations. If that doesn't work, enumerate the steps yourself (a technique we'll return to).

#### **3\. Collect the required information before doing a task**


If you ask chatGPT to write a blog post (I would never) or a Python function (I absolutely would), it will pound it out without asking for the particulars of what you actually want. Much of this can be avoided by saying something like, "I want to write a function that does X; what information do I need to gather before coding?" or "Write a function that does X, but first ask for any required information before writing code." where "X" is some partial description. 

#### 4\. Break tasks up into steps


Whenever chatGPT fails an assignment and chain-of-thought doesn't help, break the task into subtasks. This is often half the work of a task to begin with and, coincidentally, what is (currently) hard for LLMs to do on their own. However, note that you can often outsource this to the LLM as well[^3]. For example, I prompted chatGPT to come up with items for a creativity test (which you can skim):

> I'm trying to come up with more questions similar to the Remote Associates Test (RAT). The RAT requires individuals to find a common word that links three seemingly unrelated words. Here are some example sets of words:
> 
> 1\. Cottage, Swiss, Cake (Answer: Cheese)
> 
> 2\. High, Book, Chair (Answer: School)
> 
> 3\.  Fruit, Gaze, Traffic (Answer: Jam)
> 
> 4\. Cream, Skate, Water (Answer: Ice)
> 
> 5\. Ache, Hunter, Cabbage (Answer: Head)
> 
> 6\. Manners, Round, Tennis (Answer: Table)
> 
> 7\. Falling, Actor, Dust (Answer: Star)
> 
> 8\. Light, Birthday, Stick (Answer: Candle)
> 
> 9\. Salad, Head, Goose (Answer: Egg)
> 
> 10\. Music, Ached, Green (Answer: Apple) 
> 
> What are best practices? How should I think about this in steps?

Like understanding how to sum numbers, chatGPT is great at producing "recipes" for accomplishing tasks. After it delivered, all I had to say was:

> "Great! Now go through that process to produce 5 new questions"

And then five more, and five more. I had previously tried directly asking for new items, and the suggestions were atrocious. For a [much more complicated example](https://redwoodresearch.substack.com/p/getting-50-sota-on-arc-agi-with-gpt), see how an AI safety institute used this technique (among other tricks) to solve a problem that was designed to be impossible for LLMs. 

#### 5\.  Technical terms are your friend


Technical terms are attractor basins for competent LLM behavior. For example, describing an illness and asking what is "indicated" will get you farther than asking, "What should I do?" Using "indicated" tells the LLM to map your symptoms to every medical textbook ever written. The latter maps to asking for medical/life advice, which it has been trained not to give. Using technical or non-colloquial terms moves you out of normie assistant space, which has the most guardrails and Reddit-tier advice.

#### 6\. Grab-bag of useful prompts


Here are a few phrases I find myself using

 * "Is that correct?"

 * Whenever I write a summary of someone else's work or describe an idea I'm not totally familiar with, I copy-paste my writing and ask if it's correct. It's usually quite good about pushing back when parts are debatable

 * "Are you sure?"

 * Similarly, whenever I suspect an LLM is spouting bullshit, I ask if it's sure. If it changes its mind, then take the claim with a huge grain of salt.

 * "Help me brainstorm." "Be creative"

 * One of the best uses of an LLM is to help you explore idea space. Sometimes, it needs encouragement to break away from the modal answers.




If you have any gotos, add them in the comments!

[Share](https://www.vectorsofmind.com/p/how-to-prompt-chatgpt?action=share)

[^1]: It's also become spottier than I'd like, so if you have any contract work in data science, AI, or psychometrics, hit me up!

[^2]: Admittedly, there is no way in hell an LLM will list all 142-420 language families in the world. As this is "impossible" (i.e., too far from its default behavior, past some hard token limit), "exhaustive" serves to fight the gravity of a short response, making the LLM more thorough. This is the downside of prompting, which sometimes degrades into begging, pleading, bribing, and threatening.

[^3]: The fact that you can get help from an LLM in breaking up the subtask indicates that this will also be increasingly automated. Who knows what future generations will be capable of.
