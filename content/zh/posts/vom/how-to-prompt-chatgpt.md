---
about:
- vectors-of-mind
- blog-archive
author: Andrew Cutler
date: 2025-07-04
description: 'My work has become dangerously close to a Prompt Engineer1. This is
  fine by me, as it combines my love of writing, psychometrics, and NLP. Here are
  some of the most overpowered prompting techniques:'
draft: false
keywords:
- vectors-of-mind
- prompt
- chatgpt

lastmod: 2025-07-07
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '145544092'
original_url: https://www.vectorsofmind.com/p/how-to-prompt-chatgpt
quality: 6
slug: how-to-prompt-chatgpt
tags: []
title: '如何提示ChatGPT'
translation_model: gpt-4o
---

*来自 [Vectors of Mind](https://www.vectorsofmind.com/p/how-to-prompt-chatgpt) - 原文中的图像。*

---

[*[图像：原文中的视觉内容]*](https://substackcdn.com/image/fetch/$s_!EpIx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F719d87af-7c69-45fd-8c84-595b16af3dae_1024x1024.webp)你在阅读完这篇文章后的样子

我的工作已经非常接近于成为一名提示工程师[^1]。这对我来说很好，因为它结合了我对写作、心理测量学和自然语言处理的热爱。以下是一些最强大的提示技术：

1. 使用清晰且具体的指令

2. 连贯的思维推理

3. 在执行任务前收集所需信息

4. 将任务分解为步骤

5. 技术术语是你的朋友

6. 有用短语的杂烩

#### **1\. 清晰且具体的指令**

律师和计算机科学家在这方面天生就很擅长。事实上，提示的乐趣之一在于，与常规代码相比，可以不那么精确，而大型语言模型（LLM）通常能理解要点。然而，许多请求可以通过简单地明确任务和答案的格式来改进。例如，我最近凑出了一顿饭：

[*[图像：原文中的视觉内容]*](https://substackcdn.com/image/fetch/$s_!dVwU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F216d83a0-b1be-4f15-877a-bfbb9842c0ed_1284x1253.jpeg)

味道很好，谢谢你的关心。其他例子：

* “用一段话总结人工智能的历史。”

* “创建一个按年龄排序的最古老语言家族的表格。要详尽。”[^2]

* “以White和Strunk的风格重写引用的文本。给我三个选项。”

* “计算附加.csv文件中第2-7列的皮尔逊相关矩阵。”

  * 后续：“编写代码以高分辨率显示结果为热图，可以用于海报。使用美学选择的最佳实践”

具体的指令通常包括具体的例子。White和Strunk撰写了《风格的要素》。引用他们的书比使用诸如“简洁”、“专业”或“优秀”的形容词更好。部分原因是LLM倾向于过度交付，尤其是在具体形容词上。因此，如果你希望机器人采用一种俏皮的个性，试着告诉它像《美少女的谎言》中的Veronica Mars或《贱女孩》中的Regina George一样行事。

#### **2\. 连贯的思维推理**

LLM是通过一个庞大的文本语料库进行训练，以预测下一个词。令人惊讶的是，这使得它们在近似推理方面表现良好，但在处理复杂任务时很快就会崩溃。在这里，“复杂”可以意味着像“将第1列的数字相加”这样的事情。这很难一次性完成，它会吐出一个看似合理的数字，可能在正确范围内但不是正确答案。附加“分步骤思考”效果显著。通常，你甚至不需要指定步骤是什么；LLM可以推断出要对列求和，中间步骤是写“n1 + n2 + n3 + … + n100 =”。这本质上是在提示自己在等号右侧得到更好的答案。或者，打个比方，给自己时间去思考。对于任何问题，短语“分步骤思考”是你应对LLM幻觉的第一道防线。如果这不起作用，请自己列出步骤（我们将回到这一技术）。

#### **3\. 在执行任务前收集所需信息**

如果你让chatGPT写一篇博客文章（我绝不会）或一个Python函数（我绝对会），它会在不询问你实际想要的细节的情况下完成。很多这种情况可以通过说“我想写一个执行X功能的函数；在编码之前我需要收集哪些信息？”或者“写一个执行X功能的函数，但在编写代码之前先询问任何所需信息。”其中“X”是某种部分描述。

#### **4\. 将任务分解为步骤**

每当chatGPT未能完成任务且连贯思维不起作用时，将任务分解为子任务。这通常是任务开始时的一半工作，巧合的是，这也是（目前）LLM难以自行完成的。然而，请注意，你通常也可以将此外包给LLM[^3]。例如，我提示chatGPT为创造力测试想出项目（你可以浏览）：

> 我正在尝试想出更多类似于远程联想测试（RAT）的题目。RAT要求个人找到一个将三个看似无关的词联系在一起的共同词。以下是一些示例词组：
> 
> 1\. Cottage, Swiss, Cake（答案：Cheese）
> 
> 2\. High, Book, Chair（答案：School）
> 
> 3\. Fruit, Gaze, Traffic（答案：Jam）
> 
> 4\. Cream, Skate, Water（答案：Ice）
> 
> 5\. Ache, Hunter, Cabbage（答案：Head）
> 
> 6\. Manners, Round, Tennis（答案：Table）
> 
> 7\. Falling, Actor, Dust（答案：Star）
> 
> 8\. Light, Birthday, Stick（答案：Candle）
> 
> 9\. Salad, Head, Goose（答案：Egg）
> 
> 10\. Music, Ached, Green（答案：Apple）   
>   
> 最佳实践是什么？我应该如何分步骤思考？

就像理解如何求和一样，chatGPT在生成“食谱”以完成任务方面表现出色。在它交付后，我只需说：

> “太好了！现在通过这个过程再产生5个新问题”

然后再来五个，再来五个。我之前尝试直接要求新项目，建议非常糟糕。对于一个[更复杂的例子](https://redwoodresearch.substack.com/p/getting-50-sota-on-arc-agi-with-gpt)，请参阅一个AI安全研究所如何使用这种技术（以及其他技巧）来解决一个被设计为对LLM不可能的问题。

#### **5\. 技术术语是你的朋友**

技术术语是LLM行为的吸引子。例如，描述一种疾病并询问“指示”会比问“我该怎么办？”走得更远。使用“指示”告诉LLM将你的症状映射到每一本医学教科书。后者则映射到请求医学/生活建议，而它已被训练不提供这些建议。使用技术或非口语化术语将你移出普通助手空间，这里有最多的护栏和Reddit级别的建议。

#### **6\. 有用提示的杂烩**

以下是我经常使用的一些短语

* “这正确吗？”

  * 每当我写别人工作的总结或描述我不太熟悉的想法时，我会复制粘贴我的写作并询问是否正确。它通常在可辩论的部分上表现得很好

* “你确定吗？”

  * 同样，每当我怀疑LLM在胡说八道时，我会问它是否确定。如果它改变了主意，那么对这个说法要持怀疑态度。

* “帮我头脑风暴。” “要有创造力”

  * 使用LLM的最佳用途之一是帮助你探索想法空间。有时，它需要鼓励才能摆脱模式化的答案。

如果你有任何常用的提示，请在评论中添加！

[分享](https://www.vectorsofmind.com/p/how-to-prompt-chatgpt?utm_source=substack&utm_medium=email&utm_content=share&action=share)

[^1]: 它也变得比我想象的更不稳定，所以如果你在数据科学、AI或心理测量学方面有任何合同工作，请联系我！

[^2]: 诚然，LLM不可能列出世界上所有142-420个语言家族。因为这是“不可能的”（即，离其默认行为太远，超过某个硬性令牌限制），“详尽”用于抵抗简短回答的重力，使LLM更为详尽。这是提示的缺点，有时会退化为乞求、恳求、贿赂和威胁。

[^3]: 你可以从LLM中获得帮助以分解子任务这一事实表明，这也将越来越自动化。谁知道未来的世代会有什么能力。