---
about:
- 心灵向量
- 博客存档
author: Andrew Cutler
date: 2025-07-04
description: 好吧，让我们从智慧的事情中稍作休息。实际上，在被意识的号召吸引之前，我已经准备了一堆心理测量学的内容。实在是很难移开目光……
draft: false
keywords:
- 心灵向量
- 人格
- 周围
- 世界
lang: zh
lastmod: '2025-07-13'
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '108601152'
original_url: https://www.vectorsofmind.com/p/personality-around-the-world
quality: 6
slug: personality-around-the-world
tags: []
title: '# 世界各地的人格特征'
translation_model: gpt-4o
---

*来自 [Vectors of Mind](https://www.vectorsofmind.com/p/personality-around-the-world) - 原始文章中的图片。*

---

好吧，让我们从智慧的讨论中稍作休息。实际上，在被意识的号召吸引之前，我已经准备了一些心理测量学的内容。实在是很难移开目光。

[*[图片：原始文章中的视觉内容]*](https://substackcdn.com/image/fetch/$s_!X2nA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F62106fb3-6e73-444d-96f1-07b95ec828f9_1024x506.jpeg)[尤利西斯与塞壬](https://en.wikipedia.org/wiki/Ulysses_and_the_Sirens_\(Waterhouse\))，由[约翰·威廉·沃特豪斯](https://en.wikipedia.org/wiki/John_William_Waterhouse)绘制

我开始这个博客是为了从机器学习的角度探索词汇假设。人格模型定义了语言中最被谈论的特质，而在GPT时代，我们可以更好地测量这些特质。无论是从词向量还是传统调查中得出的人格模型，最终都回到了几个相同的特质，尤其是大二：社会自我调节和活力。想要回顾一下，请查看[大五人格是词向量](https://vectors.substack.com/p/the-big-five-are-word-vectors)和[人格的主要因素](https://vectors.substack.com/p/primary-factor-of-personality-part)。

大五人格在许多语言中被独立发现，但语言之间的比较总是定性的。研究人员在土耳其语或德语中进行人格形容词的调查，进行因子分析，并大致观察这些因子是否相同。这些数据不能用于说明“外向性在德语中相对于英语的责任心偏移了15度”。要达到如此精确的程度，两种语言必须共享某种基础。

如果你在多种语言中进行问卷调查，可以通过1）找到能够用两种语言回答的双语群体，或2）假设单词的翻译是1:1的（例如，_fun_在西班牙语中完美等同于_divertido_）来关联它们。在前一种情况下，存在强烈的选择效应。如果双语者往往受教育程度更高呢？后一种情况显然不成立。事实上，将语言结合起来进行因子分析的原因是为了理解人格结构在不同语言之间可能的差异。假设单词相同则违背了这一目的。

**[我的研究](https://arxiv.org/abs/2203.02092)表明，你可以从英语的语言模型中提取人格结构。一个自然的问题是，当你加入其他语言时，这种结构会如何变化。** 使用在几十种语言上训练的模型，这变得相对容易探索。你可以将任意数量的语言映射到相同的基础上。

## 再次探讨大二

我使用[XLM-RoBERTa](https://huggingface.co/xlm-roberta-base)来分配人格形容词之间的相似性。奇怪的是，这个模型是缅甸种族灭绝的结果。Meta处于一个不受欢迎的位置，他们需要在对某些地方几乎没有了解的情况下移除内容。从技术上讲，这被称为迁移学习问题。他们希望在英语（或其他资源丰富的语言）中训练一个仇恨言论分类器，然后将其应用于其他语言。在语言建模的黑暗时代（2018年），这效果很差。缅甸语中“让我们围捕同性恋并杀掉他们”的口语在他们的分类器看来就像是“应该少一些彩虹”。这当然滑过了他们的内容审核。《纽约时报》解释了后果：_**[缅甸军方在Facebook上煽动的种族灭绝](https://www.nytimes.com/2018/10/15/technology/myanmar-facebook-genocide.html)**_

Meta的回应是构建一个语言模型，可以更好地将任何语言（实际上是100种语言）映射到相同的词向量空间。这样，训练在英语中的仇恨言论分类器可以更好地扩展到其他语言。（需要更少的缅甸语来微调它。）使用这个模型，我在四种语言中嵌入了人格词汇：英语、西班牙语、法语和土耳其语。以下是前两个因素：

[*[图片：原始文章中的视觉内容]*](https://substackcdn.com/image/fetch/$s_!eLVQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd3ff00d-d96d-4e3b-ada4-640e3cd66089_1245x954.png)

这些用于区分不同的语言。第一个因素将土耳其语与印欧语言区分开来。在第二个因素上，罗曼语族语言相邻（尽管也接近土耳其语）。

这很合理。模型被训练来预测句子的下一个词，因此自然会包含语言特定的信息。如果有人在讲西班牙语，他们不会经常切换到土耳其语。希望在向量空间中也有对应于人格信息的方向。

如果语言相对独立，你至少需要3个维度来将4种语言分成各自不重叠的组。让我们看看下一个主成分。

[*[图片：原始文章中的视觉内容]*](https://substackcdn.com/image/fetch/$s_!PRKA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5eb70bd2-8684-4844-94bd-aa12adc030bf_1256x954.png)

因素4是第一个不是为了区分语言而学习的因素，它是人格的一般因素！在英语中：_专横、无情、强迫_和_自私_ **对比** _慷慨、温柔_和_体贴_。[我曾经论证](https://vectors.substack.com/p/primary-factor-of-personality-part)这个因素最好理解为遵循黄金法则的倾向。意识的夏娃理论实际上是[思考这在我们的进化历史中会选择什么](https://vectors.substack.com/p/consequences-of-conscience)的结果。因素5也是关于人格的，将它们一起绘制：

[*[图片：原始文章中的视觉内容]*](https://substackcdn.com/image/fetch/$s_!pD64!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F192dc8f4-db5e-4d96-b8a5-ce16c1cbf1f6_1264x954.png)

我们得到了大二！因素五（或人格因素中的二）是活力：_冒险、富有想象力_和_热情_**对比** _谨慎、保守_和_胆小_。这如此规律地出现，令人惊讶。**关于大二的论文有[2,500篇引用](https://scholar.google.com/scholar?cites=11052969740325606797&as_sdt=2005&sciodt=0,5&hl=en)，但研究人员仍未意识到它们只是一般人格的前两个未旋转因素。** 认为它们以某种方式与大五存在层级关系的普遍信念来自于研究人员在制作大五清单后不久就放弃了直接处理语言。自那时起，任何试图理解基本或一般人格的尝试都必须参考大五。但词语是先来的，而语言模型现在使得在这一基本层面上分析语言变得容易。

[分享](https://www.vectorsofmind.com/p/personality-around-the-world?utm_source=substack&utm_medium=email&utm_content=share&action=share)

## 我们必须更深入

加入俄语和波斯语后，得到了相同的因素：

[*[图片：原始文章中的视觉内容]*](https://substackcdn.com/image/fetch/$s_!IIKx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F976f1c11-fd97-4184-a74a-a384a09b0579_2078x1715.png)要更好地查看单词，请下载图片并放大。

按照我懒惰的工程师标准，这相当费力，因为这需要为每种语言找到一个好的提示。我与谷歌翻译和母语者合作以确保准确，你可以看到波斯语在因素4上的分布仍然偏离。我猜测我忽略任何不共享因素的方法对于这么多语言来说太粗糙。因素4可能被用作GFP，也用于稍微区分波斯语。这些因素没有保持纯净的保障，我们真的很幸运分布如此良好。进行一些预处理（如对每个语言簇进行零均值化）可能会解决这个问题。

据我所知，这是第一次将多种语言一起进行因子分析。仅凭英语和西班牙语的结果就可以发表，而我达到了六种语言，包括两种非印欧语言。这也揭示了大二的本质，这是心理测量学中最受欢迎且被误解的构造之一。

## 缺点

我以几乎最愚蠢的方式进行了这项研究。我在ESL指南中找到了100个性格词，然后用谷歌翻译将它们翻译成其他语言。如果有重复，我就删除它们。这并不像看起来那么糟糕。无论你使用100个还是500个词，英语中的前两个因素几乎没有变化。但是，如果这是篇正式的论文，你显然会希望在每种词汇中独立开发一组词汇。还有其他几个缺点：

**语言不够多！** 如果我发表这篇文章，我希望增加十几种在人格科学中不常研究的语言。这实际上是我一直没有发表的原因。这需要大量工作，并需要几种亚洲语言的母语者。

**多语言模型受训练数据的影响。** 语言模型被训练来预测句子的下一个词。如果你用多种语言进行训练，模型会尝试转移一些知识。然而，对于较小的语言，这可能看起来更像是它们的意义被强行比喻为资源更丰富的语言（英语、中文、俄语等）中的类比。

**查询是研究者的自由度。** 我用来嵌入词汇的方法是“我的性格可以描述为<mask>和[word]”，其中[word]是其中一个性格词。由于句子的写法，模型在mask标记上加载纯粹的人格信息，然后嵌入它。在我的论文中，我发现这效果最好。当然，这有无数种变体，你必须选择一种。理论上，研究者可能会有特定的结果预期，然后找到支持该结果的查询。IMO这不是太大的风险，考虑到这个结果与调查方法产生的结果非常相似。我们对因子分析中发现的人格结构有相当强的先验知识。这种方法重现它是方法有效的证据。

**过时的语言模型。** 我在两年多前做了这项工作，远在GPT-4问世之前。那是简单的时代。

## 结论

如果我仍在学术界，这将是我的研究议程。尽可能多地添加语言，并尝试理解所有可能导致方法偏差的方式。最终，它可能会产生一个优于大五的人格通用模型。它将帮助我们更好地理解我们是谁，甚至可能了解我们来自哪里。因为现在是语言定义了我们的物种，而语言在过去深刻地塑造了我们的心灵。我们习惯性地社交，因为几千年前，未能管理好你的声誉就意味着死亡。人格模型是语言的地图；它们是我们心灵进化的向量。

[立即订阅](https://www.vectorsofmind.com/subscribe?)

[*[图片：原始文章中的视觉内容]*](https://substackcdn.com/image/fetch/$s_!MDwl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F935dcb92-8e91-41c3-9630-2a80f2bc9a06_1024x1024.png)