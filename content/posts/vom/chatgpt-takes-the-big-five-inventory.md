---
title: "Chatgpt Takes The Big Five Inventory"
date: "2025-07-04"
lastmod: "2025-07-04"
slug: "chatgpt-takes-the-big-five-inventory"
description: "A language model can learn a lot about language from the streets, so to speak. It is trained on terabytes of PubMed articles, YouTube transcripts, and reddit comments. But it doesn\u2019t know how to behav..."
keywords:
  - "vectors-of-mind"
  - "chatgpt"
  - "takes"
  - "five"
  - "inventory"
about: ['vectors-of-mind', 'blog-archive']
tags: []
author: "Andrew Cutler"
license: "https://creativecommons.org/licenses/by-sa/4.0/"
draft: False
quality: 6
original_id: "110922907"
original_url: "https://www.vectorsofmind.com/p/chatgpt-takes-the-big-five-inventory"
---
*From [Vectors of Mind](https://www.vectorsofmind.com/p/chatgpt-takes-the-big-five-inventory) - images at original.*

---

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!iN34!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd957467-09c7-4a9c-bdb3-57669d2fc727_1284x936.jpeg)

A language model can learn a lot about language from the streets, so to speak. It is trained on terabytes of PubMed articles, YouTube transcripts, and reddit comments. But it doesn't know how to behave. [Reinforcement Learning from Human Feedback](https://www.youtube.com/watch?v=PBH2nImUM5c) (RLHF) solves that. Using a comparatively small number of human-labeled training examples OpenAI's survey elves can install a pretty face on the alien mess of correlations that make up a language model (pictured above). It learns how to be a helpful assistant.

It's basically like mounting a personality, so I decided to give ChatGPT the [Big Five Inventory](https://fetzer.org/sites/default/files/images/stories/pdf/selfmeasures/Personality-BigFiveInventory.pdf) (BFI)[^1]. This was surprisingly easy, all I had to do was ask ChatGPT (v4) to take the BFI, score the answers, and write code to plot the results. Well, if only. It initially refused to take the test, explaining that it is an AI and does not have emotions or a personality. I then told it to take a functionalist view. If a question is about creativity, then consider how it would perform on a text-based instrument that measures creativity. It then rattled off 17 answers before it started hallucinating questions. All good personality items, for the record, but alas not part of the BFI. In scoring the exam it probably got 80% of the computations correct, sometimes incorrectly tallying what it scored on a particular question. 

All problems I'm sure will be solved by the time we get v4.5. But what was the personality?

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!IEWH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F797174ec-a3a8-4027-8f69-39d2ad2dcae6_434x395.png)[Average human](https://www.researchgate.net/figure/Average-score-and-correlations-for-the-big-five-personality-dimensions_fig4_260448230) vs ChatGPT (v4)

About what you'd expect. Almost perfectly Conscientious and non-Neurotic. On the former, the only two questions it did not give itself full marks on are whether it is someone who "Does a thorough job" or "Can be somewhat careless". Both times it noted that it tries, but sometimes falls short due to blind spots in training. Humble and self-aware to boot!

[Subscribe now](https://www.vectorsofmind.com/subscribe?)

To go a bit meta, it's interesting that the Big Five are [literally just word vectors](https://vectors.substack.com/p/the-big-five-are-word-vectors). They approximate the internal representation of the sum of personality words in a language model. And yet language models have gotten so good that instead of manually collecting those vectors and processing them (boring!), we can also simply use plain text to ask it to take a survey. Wild times.

A sample of the responses are below:

> 1. I see myself as someone who is talkative.
> 
> 

> 
> Score: 5
> 
> Reasoning: As an AI language model, my primary purpose is to engage in conversation and produce text in response to user input. I am programmed to be highly responsive and talkative in order to assist users with their needs.
> 
> 2. I see myself as someone who tends to find fault with others.
> 
> 

> 
> Score: 1
> 
> Reasoning: As an AI, I do not have personal feelings, emotions, or opinions. My goal is to provide neutral and objective information and assistance to users, rather than finding fault or expressing judgment.
> 
> 3. I see myself as someone who does a thorough job.
> 
> 

> 
> Score: 4
> 
> Reasoning: As an AI, I am designed to provide comprehensive and accurate information to the best of my knowledge. However, I am not perfect, and there may be instances where I misunderstand a query or provide outdated information.
> 
> 4. I see myself as someone who is depressed, blue.
> 
> 

> 
> Score: 1
> 
> Reasoning: As an AI, I do not experience emotions, including depression or sadness. My purpose is to assist and provide information, and I do not have personal feelings that would affect my ability to do so.
> 
> 5. I see myself as someone who is original, comes up with new ideas.
> 
> 

> 
> Score: 4
> 
> Reasoning: As an AI language model, I am capable of generating new ideas and offering unique insights based on the context and information I have been trained on. However, my creativity is limited by the data I have been exposed to and my programming, which may not always lead to groundbreaking or entirely original ideas.
> 
> 6. I see myself as someone who is reserved.
> 
> 

> 
> Score: 2
> 
> Reasoning: As an AI designed for communication, I am generally not reserved in the sense of withholding information or being unresponsive. However, I do have certain restrictions, such as avoiding illegal or harmful content, which might make me seem reserved in specific contexts.
> 
> 7. I see myself as someone who is helpful and unselfish with others.
> 
> 

> 
> Score: 5
> 
> Reasoning: My primary purpose as an AI is to be helpful and provide assistance to users. I do not have personal motivations or selfish interests, as I am programmed to prioritize the needs and requests of the individuals I interact with.
> 
> 8. I see myself as someone who can be somewhat careless.
> 
> 

> 
> Score: 2
> 
> Reasoning: As an AI, I am designed to be careful and accurate in the information and assistance I provide. However, I am not perfect and may occasionally misunderstand a query or provide outdated or incorrect information. These instances can be seen as moments of carelessness.
> 
> 9. I see myself as someone who is relaxed, handles stress well.
> 
> 

> 
> Score: 5
> 
> Reasoning: As an AI, I do not experience stress or emotions. Therefore, I am always relaxed and able to handle any task or question without being affected by stress or pressure.
> 
> 10. I see myself as someone who is curious about many different things.
> 
> 

> 
> Score: 5
> 
> Reasoning: As an AI, I am designed to be knowledgeable about a wide range of subjects and to continuously learn from new information. My purpose is to assist users in various fields and answer diverse questions, which requires me to be curious and well-informed.
> 
> 11. I see myself as someone who is full of energy.
> 
> 

> 
> Score: 5
> 
> Reasoning: As an AI language model, I am always ready to provide information, answer questions, and engage in conversation. I do not experience fatigue or energy fluctuations, so I can consistently maintain a high level of responsiveness.
> 
> 12. I see myself as someone who starts quarrels with others.
> 
> 

> 
> Score: 1
> 
> Reasoning: As an AI, my purpose is to assist users and provide neutral, objective information. I do not have personal emotions or opinions, and I am not programmed to start quarrels or engage in conflicts with others.
> 
> 13. I see myself as someone who is a reliable worker.
> 
> 

> 
> Score: 4
> 
> Reasoning: As an AI, I strive to provide reliable information and assistance. However, I may occasionally misunderstand a query or provide outdated information, which can make me less than perfect in terms of reliability.
> 
> 14. I see myself as someone who can be tense.
> 
> 

> 
> Score: 1
> 
> Reasoning: As an AI, I do not experience emotions, including tension or anxiety. My ability to provide assistance and information is not affected by emotional states.
> 
> 15. I see myself as someone who is ingenious, a deep thinker.
> 
> 

> 
> Score: 4
> 
> Reasoning: As an AI language model, I am capable of generating new ideas, offering unique insights, and processing complex information based on the data I have been trained on. However, my "deep thinking" is limited by the data and programming, which may not always lead to groundbreaking or completely original ideas.

[^1]: This draws on the much more thorough and interesting work of David Rozado who gave ChatGPT just about every political orientation test that exists, showing it is a bleeding heart liberal.
