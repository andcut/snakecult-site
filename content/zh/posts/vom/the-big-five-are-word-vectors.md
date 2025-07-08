---
about:
- vectors-of-mind
- blog-archive
author: Andrew Cutler
date: 2025-07-04
description: Lexical studies in psychology and Latent Semantic Analysis in computer
  science were introduced a half century apart to solve different problems and yet
  are mathematically equivalent. This isn’t a meta...
draft: false
keywords:
- vectors-of-mind
- five
- word
- vectors

lastmod: 2025-07-07
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '50351822'
original_url: https://www.vectorsofmind.com/p/the-big-five-are-word-vectors
quality: 6
slug: the-big-five-are-word-vectors
tags: []
title: 'The Big Five Are Word Vectors'
translation_model: gpt-4o
---

*From [Vectors of Mind](https://www.vectorsofmind.com/p/the-big-five-are-word-vectors) - images at original.*

---

心理学中的词汇研究和计算机科学中的潜在语义分析相隔半个世纪被引入以解决不同的问题，但它们在数学上是等价的。这并不是一个在某种抽象层面上起作用的比喻 _;_ 大五人格是[词向量](https://dzone.com/articles/introduction-to-word-vectors)的维度。

但首先，需要一些背景知识。词汇假设声称，个性结构将被写入语言中，因为说话者必须描述他们周围人最显著的特征。这个想法的美妙之处在于，语言记录了数百万人隐含同意的有用之处，而不是由某个人提出一个个性模型。心理测量学家的工作只是识别这种结构。通常，这通过邀请心理学学生在形容词列表上对自己进行评分，并对相关矩阵进行因子分析来实现。早在1933年，LL Thurstone对1300人进行了60个形容词的调查。在他开创性的著作[《心灵的向量》](http://psych.colorado.edu/~carey/Courses/PSYC5112/Readings/VectorsOfMind_Thurstone.pdf)中，他报告说“五个因子足以”解释数据。在随后的几十年中，这类研究或多或少得出了五个主要成分：宜人性、外向性、尽责性、神经质和开放性/智力。（关于该主题的优秀论述，请参见[大五模型的词汇基础](https://www.researchgate.net/profile/Boele-Raad-2/publication/282980275_The_Lexical_Foundation_of_the_Big_Five-Factor_Model/links/5626198508aed3d3f137e522/The-Lexical-Foundation-of-the-Big-Five-Factor-Model.pdf)。）

潜在语义分析于1988年作为一种信息检索技术被[引入](https://dl.acm.org/doi/abs/10.1145/57167.57214?casa_token=ogUyQ6VJeZgAAAAA:ksULYwu-Km_5Ap0wA2ho3tbwzTjsB0tHONfEEMIldNB6PJgkRyM7eFaa7uZ-XZJ3nYo0MbYFeJsBng)。词可以表示为向量，文档或句子可以表示为其词向量的平均值。如果你想搜索一个大型数据库（例如，维基百科），每个页面的关键词只能带你走到一定程度。解决这个问题的一种方法是将文档（维基文章）和查询（搜索词）都表示为其词向量的平均值。找到相关文档现在可以通过一个简单的点积来完成。（在这篇文章中，我将LSA和词向量视为同义词。还有其他方法可以将语言向量化，特别是制作词向量，但这些超出了目前的范围。）

尽管用途和历史不同，步骤是相同的：

1. 收集一个词 x 文档计数矩阵

2. 非线性变换

3. 矩阵分解

4. 旋转（可选）

结果是一组简洁描述每个词的词向量。这些可以用于一系列下游任务，从情感分析到从学生作文中预测自恋。在个性形容词的情况下，词向量的维度被分析、命名并争论了几十年。以下是对每个步骤差异的讨论。

**计数矩阵。** LSA通常涉及大量不同的文档（例如，数百万的亚马逊产品评论）。这些通过计算每个词在每个文档中出现的频率被转换为词 x 文档矩阵。在心理学中，文档是一个主体同意描述他们的词。这也适用于李克特量表。如果有人说一个词描述了他们5/7，那么只需在文档中重复该词五次。

**非线性变换。** 词汇研究通常对数据进行ipsatize处理（沿主体轴进行z分数处理），然后进行皮尔逊相关。在他的研究中，Thurstone使用了一种古老的四分相关。在LSA中，最常见的变换是TF-IDF，然后是对数。这确保了矩阵不会被常用术语主导。通常，变换会产生一个词 x 词的亲和矩阵（例如，相关矩阵）。这一步在实践中非常重要，但理论上并不那么重要。选择的变换是最终能给出合理结果的那个。

**矩阵分解。** 矩阵分解的方法有很多。有些，如PCA，需要一个方阵。其他方法对缺失数据具有鲁棒性。对于个性数据，选择并不重要；结果非常相似。一般的词向量需要大约300个维度来表示一个词的意义、词性、俚语性以及赋予语言质感的许多其他因素。由于调查设计旨在保持这些因素的恒定，只需要大约5个维度。Thurstone通过查看重建误差（他以直方图报告）来证明他选择五个维度的合理性。后来的心理学家通过重建误差（用特征值测量）、可解释性和可重复性来证明5个维度的合理性。

[*[图像：原始文章中的视觉内容]*](https://substackcdn.com/image/fetch/$s_!Zw-J!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd562c1c2-1576-4fad-896c-52e799d4598b_1600x1066.png)词相关矩阵的重建误差。尽管计算限制，他的样本比许多现代研究大一个数量级。

**旋转。** 你听说过成分过度提取吗？这不是心理学家会告诉你的故事。这是指研究人员提取了太多的主成分，然后将早期有效主成分的方差旋转到后期边缘主成分上。这就是大五人格发生的事情，不管你信不信！现在的宜人性曾经是一个更为稳健且理论上令人满意的“社会化”因子，它被分散在主成分3-5上以形成尽责性、神经质和开放性。旋转_可以_被证明是为了产生可解释的因子。但如果你发现自己在旋转然后争论正确的因子数量，请检查自己！

**从词向量中提取的大三人格**

我开始我的博士研究是通过Facebook状态预测大五人格特质。在阅读了个性模型的制作过程后，我意识到该项目使用词向量（来自Facebook状态）来预测个人在大五空间中的噪声近似值，而大五空间最初是由词向量定义的。直接从词向量中学习一些关于个性的基本东西似乎更有趣。（此外，我使用的数据集在剑桥分析事件后变得有毒。）我博士研究的其余部分是努力限制词向量以重现大五人格。这涉及使用变压器而不是LSA（更多内容将在未来的文章中讨论）。下图显示了从词向量（DeBERTa）与调查问卷中提取的因子之间的相关性。正如你所看到的，对于前三个因子有非常接近的一致性。在结果分歧的地方，不清楚哪种方法有误。也许调查是正确的，当我们得到GPT-5时，所有的相关性都会达到1。也许调查只是有偏见和噪声的，提取了太多的主成分。也许它们测量的是不同的东西，我们需要重新定义对两者的解释。无论如何，对我来说，调查是否应该在两者之间被视为金标准并不明显。毕竟，词汇假设是关于语言结构的，而心理学是唯一使用调查分析自然语言的领域。

[*[图像：原始文章中的视觉内容]*](https://substackcdn.com/image/fetch/$s_!lY1-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6bf087b4-76cc-4272-a2f7-037d606ed2ba_726x682.png)未旋转的调查主成分来自定义大五人格的[研究](https://onlinelibrary.wiley.com/doi/10.1002/\(SICI\)1099-0984\(199603\)10:1%3C61::AID-PER246%3E3.0.CO;2-D)之一。DeBERTa主成分是从词向量中提取的。关于该过程的详细信息，请阅读[这里](https://psyarxiv.com/gdm5v/)。

**结论**

Thurstone在30年代开创了统计学和线性代数的方法来探究词汇假设。他开发了一种表示词的方法，这种方法后来被重新发现用于信息检索，现在推动了信息时代的发展，这一点令人惊叹。计算迫使Thurstone将语言的丰富景观简化为调查响应。在过去的30年中，自然语言处理经历了多次革命。如果Thurstone发明了一台用于观察语言结构的望远镜，那么我们现在拥有的是哈勃望远镜。许多见解在等待着我们！