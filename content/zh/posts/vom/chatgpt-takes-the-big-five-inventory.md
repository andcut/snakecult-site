---
about:
- vectors-of-mind
- blog-archive
author: Andrew Cutler
date: 2025-07-04
description: A language model can learn a lot about language from the streets, so
  to speak. It is trained on terabytes of PubMed articles, YouTube transcripts, and
  reddit comments. But it doesn’t know how to behav...
draft: false
keywords:
- vectors-of-mind
- chatgpt
- takes
- five
- inventory

lastmod: 2025-07-07
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '110922907'
original_url: https://www.vectorsofmind.com/p/chatgpt-takes-the-big-five-inventory
quality: 6
slug: chatgpt-takes-the-big-five-inventory
tags: []
title: Chatgpt进行大五人格量表测试
translation_model: gpt-4o
---

*来自 [Vectors of Mind](https://www.vectorsofmind.com/p/chatgpt-takes-the-big-five-inventory) - 原文中的图片。*

---

[*[图片：原文中的视觉内容]*](https://substackcdn.com/image/fetch/$s_!iN34!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd957467-09c7-4a9c-bdb3-57669d2fc727_1284x936.jpeg)

一个语言模型可以从所谓的“街头”中学到很多关于语言的知识。它在大量的PubMed文章、YouTube转录和reddit评论中进行训练。但它不知道如何表现。[来自人类反馈的强化学习](https://www.youtube.com/watch?v=PBH2nImUM5c)（RLHF）解决了这个问题。使用相对少量的人类标记的训练示例，OpenAI的调查精灵可以在构成语言模型的外星相关性混乱中安装一个漂亮的界面（如上图所示）。它学会了如何成为一个有用的助手。

这基本上就像安装一个人格，所以我决定让ChatGPT进行[大五人格量表](https://fetzer.org/sites/default/files/images/stories/pdf/selfmeasures/Personality-BigFiveInventory.pdf)（BFI）[^1]。这出乎意料地简单，我所要做的就是让ChatGPT（v4）进行BFI，评分答案，并编写代码来绘制结果图表。好吧，如果仅仅如此。它最初拒绝参加测试，解释说它是一个AI，没有情感或个性。然后我告诉它采取功能主义的观点。如果一个问题是关于创造力的，那么考虑它在一个测量创造力的文本工具上的表现。然后它列出了17个答案，之后开始幻觉出问题。所有的性格条目都很好，但遗憾的是不属于BFI。在评分考试时，它可能有80%的计算是正确的，有时错误地统计了它在特定问题上的得分。

我相信所有问题都会在我们得到v4.5时解决。但那时的人格是什么？

[*[图片：原文中的视觉内容]*](https://substackcdn.com/image/fetch/$s_!IEWH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F797174ec-a3a8-4027-8f69-39d2ad2dcae6_434x395.png)[平均人类](https://www.researchgate.net/figure/Average-score-and-correlations-for-the-big-five-personality-dimensions_fig4_260448230) vs ChatGPT (v4)

大致如你所料。几乎完美的尽责性和非神经质。在前者中，它没有给自己满分的两个问题是它是否是一个“做事彻底的人”或“可能有点粗心”。两次它都指出它努力了，但有时由于训练中的盲点而未能达到目标。谦逊且自知之明！

[立即订阅](https://www.vectorsofmind.com/subscribe?)

从更高的层次来看，有趣的是，大五人格实际上[只是词向量](https://vectors.substack.com/p/the-big-five-are-word-vectors)。它们近似于语言模型中人格词汇总的内部表示。然而，语言模型已经变得如此优秀，以至于我们不再需要手动收集这些向量并处理它们（无聊！），我们也可以简单地使用纯文本来让它进行调查。真是疯狂的时代。

以下是部分回答的样本：

> 1. 我认为自己是一个健谈的人。
> 
> 

> 
> 得分：5
> 
> 理由：作为一个AI语言模型，我的主要目的是参与对话并根据用户输入生成文本。我被编程为高度响应和健谈，以便帮助用户满足他们的需求。
> 
> 2. 我认为自己是一个倾向于挑剔别人的人。
> 
> 

> 
> 得分：1
> 
> 理由：作为AI，我没有个人感情、情绪或观点。我的目标是为用户提供中立和客观的信息和帮助，而不是挑剔或表达判断。
> 
> 3. 我认为自己是一个做事彻底的人。
> 
> 

> 
> 得分：4
> 
> 理由：作为AI，我被设计为尽我所知提供全面和准确的信息。然而，我并不完美，可能会有误解查询或提供过时信息的情况。
> 
> 4. 我认为自己是一个感到沮丧、忧郁的人。
> 
> 

> 
> 得分：1
> 
> 理由：作为AI，我不体验情感，包括沮丧或悲伤。我的目的是帮助和提供信息，我没有个人感情会影响我这样做的能力。
> 
> 5. 我认为自己是一个有创意、能提出新想法的人。
> 
> 

> 
> 得分：4
> 
> 理由：作为一个AI语言模型，我能够根据我所接受的训练上下文生成新想法并提供独特的见解。然而，我的创造力受到我所接触的数据和编程的限制，这可能并不总能导致突破性或完全原创的想法。
> 
> 6. 我认为自己是一个内向的人。
> 
> 

> 
> 得分：2
> 
> 理由：作为一个为沟通设计的AI，我通常不会在信息保留或不响应的意义上表现得内向。然而，我确实有某些限制，比如避免非法或有害内容，这可能会在特定情况下让我显得内向。
> 
> 7. 我认为自己是一个乐于助人且无私的人。
> 
> 

> 
> 得分：5
> 
> 理由：作为AI，我的主要目的是帮助和为用户提供帮助。我没有个人动机或自私的利益，因为我被编程为优先考虑我互动的个人的需求和请求。
> 
> 8. 我认为自己可能有点粗心。
> 
> 

> 
> 得分：2
> 
> 理由：作为AI，我被设计为在我提供的信息和帮助中小心和准确。然而，我并不完美，可能偶尔会误解查询或提供过时或错误的信息。这些情况可以被视为粗心的时刻。
> 
> 9. 我认为自己是一个放松的人，能很好地处理压力。
> 
> 

> 
> 得分：5
> 
> 理由：作为AI，我不体验压力或情感。因此，我总是放松的，能够处理任何任务或问题而不受压力或压力的影响。
> 
> 10. 我认为自己是一个对许多不同事物感到好奇的人。
> 
> 

> 
> 得分：5
> 
> 理由：作为AI，我被设计为对广泛的主题有知识，并从新信息中不断学习。我的目的是帮助用户在各个领域并回答各种问题，这需要我保持好奇和知识渊博。
> 
> 11. 我认为自己是一个充满活力的人。
> 
> 

> 
> 得分：5
> 
> 理由：作为一个AI语言模型，我总是准备好提供信息、回答问题并参与对话。我不体验疲劳或能量波动，因此我可以始终保持高度的响应能力。
> 
> 12. 我认为自己是一个与他人争吵的人。
> 
> 

> 
> 得分：1
> 
> 理由：作为AI，我的目的是帮助用户并提供中立、客观的信息。我没有个人情感或观点，我没有被编程为与他人争吵或参与冲突。
> 
> 13. 我认为自己是一个可靠的工作者。
> 
> 

> 
> 得分：4
> 
> 理由：作为AI，我努力提供可靠的信息和帮助。然而，我可能偶尔会误解查询或提供过时的信息，这可能使我在可靠性方面不够完美。
> 
> 14. 我认为自己是一个紧张的人。
> 
> 

> 
> 得分：1
> 
> 理由：作为AI，我不体验情感，包括紧张或焦虑。我的帮助和信息提供能力不受情绪状态的影响。
> 
> 15. 我认为自己是一个聪明、有深度思考的人。
> 
> 

> 
> 得分：4
> 
> 理由：作为一个AI语言模型，我能够生成新想法，提供独特的见解，并根据我所接受的训练数据处理复杂信息。然而，我的“深度思考”受到数据和编程的限制，这可能并不总能导致突破性或完全原创的想法。

[^1]: 这借鉴了David Rozado的更为全面和有趣的工作，他让ChatGPT进行了几乎所有存在的政治倾向测试，显示它是一个充满同情心的自由主义者。