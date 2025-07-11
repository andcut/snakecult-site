---
about:
- vectors-of-mind
- blog-archive
author: Andrew Cutler
date: 2025-07-04
description: The Eve Theory of Consciousness proposes that self-awareness was discovered
  by women and spread memetically. To make this case I draw on linguistics, archeology,
  pharmacology, genetics, anthropology, ...
draft: false
keywords:
- vectors-of-mind
- basis

lastmod: 2025-07-07
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '121454386'
original_url: https://www.vectorsofmind.com/p/the-ai-basis-of-the-eve-theory-of
quality: 6
slug: the-ai-basis-of-the-eve-theory-of
tags: []
title: 'The AI Basis Of The Eve Theory Of'
translation_model: gpt-4o
---

*来自 [心灵的向量](https://www.vectorsofmind.com/p/the-ai-basis-of-the-eve-theory-of) - 原文中的图像。*

---

[*[图像：原始文章中的视觉内容]*](https://substackcdn.com/image/fetch/$s_!0pra!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff5166314-7a08-4939-9b16-2311d6214e87_1456x816.png)

[意识的夏娃理论](https://vectors.substack.com/p/eve-theory-of-consciousness-v2)提出，自我意识是由女性发现并通过模因传播的。为了证明这一点，我借用了[语言学](https://vectors.substack.com/p/the-unreasonable-effectiveness-of)、[考古学](https://vectors.substack.com/i/95941288/the-genesis-of-religion)、[药理学](https://vectors.substack.com/p/comments-on-snake-venom)、[遗传学](https://vectors.substack.com/p/y-chromosome-bottleneck)、[人类学](https://vectors.substack.com/p/the-snake-cult-of-consciousness)和[神经科学](https://vectors.substack.com/i/114650037/women-lead-the-way)。然而，我是一名电气工程师。在一个许多人有实际训练的领域，我如何能有价值的见解呢？实际上，EToC的想法源于机器学习。长期读者已经[见证了博客的进展](https://substack.com/profile/31996842-andrew/note/c-16789002?utm_source=notes-share-action)，从ML心理测量学到递归和比较神话学。让我解释我是如何走到这一步的。

## 从词汇中构建人格结构

心理学存在一个基本事实问题。一位研究人员可能会理论化认为人类只有几个基本的变异轴，最主要的是内化与外化。另一位可能会说必须有[30个基本因素](https://www.scholars.northwestern.edu/en/publications/exploring-the-persome-the-power-of-the-item-in-understanding-pers)，因为人类就是如此复杂。谁是对的？早在1890年，[高尔顿](https://astralcodexten.substack.com/p/galton-ehrlich-buck)建议，与其让心理学家基于他们的个人理论来构建人格模型，最好的模型已经嵌入在语言中。每一个人格形容词的存在都是因为数百万人在判断他人时发现它有用。这些词汇必定揭示了人格的所有重要方面。正式提出为词汇假设：

1. 对一群人重要的人格特征最终会成为该群体语言的一部分。

2. 更重要的人格特征更有可能被编码为单个词汇。

这个想法可以用来构建人格模型。只需创建一个人格形容词列表，查看它们之间的关系，并将其压缩为几个潜在因素[^1]。（LL Thurstone发明了因子分析来实现这一点，[论文](https://psycnet.apa.org/record/1934-02322-001)是这个博客的名字来源。）传统上，形容词之间的关系是通过询问心理学本科生哪些词最能描述他们来估计的。那些说自己是_聪明的_的人也倾向于说自己是_思想开放的_。这表明它们都与某个潜在因素有关。在我的论文中，[我使用语言模型来估计词汇相似性](https://vectors.substack.com/p/the-big-five-are-word-vectors)，并产生了与传统调查相似的结果（两种方法的第一个因素相关性为r=0.93）。

通过一个例子最容易理解这个过程。这里有100个随机人格形容词，绘制在捕捉最多人格信息的两个维度上。将这些视为[大五人格](https://en.wikipedia.org/wiki/Big_Five_personality_traits)中的两个（尽管它们的[旋转方式有所不同](https://vectors.substack.com/i/61936908/relation-to-the-big-five)）。人格心理学家的任务之一是查看这样的图表并对其进行定性描述。你可以在[猜测因素](https://vectors.substack.com/p/guess-the-factor)中练习这个练习，或者在下面进行。你会如何总结因素1？

[*[图像：原始文章中的视觉内容]*](https://substackcdn.com/image/fetch/$s_!N5Ou!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3c50c0d0-6e09-4758-bfad-6c9135f154af_1423x891.png)因素1和2是使用[PCA](https://builtin.com/data-science/step-step-explanation-principal-component-analysis)生成的，这是一种将人格信息提炼到最少轴的方法。有关如何从词向量中获取这些信息的更多信息，请参阅我的论文[深层词汇假设](https://arxiv.org/abs/2203.02092)。你也可以使用我的[代码](https://colab.research.google.com/drive/1SXZNVqH0m_Bnd2hvIJFYiKQvHWpGu8ZM?usp=sharing)重现这一结果（以及更多），该代码在Google Colab上免费运行。

从统计学的角度来看，因素1已经裸露并挥舞着一面大旗“我是迄今为止最重要的”，正如我在[人格的主要因素](https://vectors.substack.com/p/primary-factor-of-personality-part)（PFP）中解释的那样。定性地说，它本质上是“社会对你的期望”。要体贴和尊重，不要傲慢或不合作。

要以另一种方式抽象PFP（因素1），回溯2000年是有用的。以色列人有专门用于社会规则及其正确应用的图书馆。经过几个世纪的辩论和解释，法律的字面意义倍增。但也有一种运动试图提炼法律的精神。

根据传统叙述，一位潜在的皈依者接近拉比沙迈，要求他在单脚站立时解释整个《托拉》。以严格遵守犹太法律而闻名的拉比沙迈认为这个问题不敬，拒绝了皈依者。

不屈不挠的皈依者随后以同样的请求接近拉比希勒尔。希勒尔以其同情心和智慧而闻名，以不同的方式回应。希勒尔没有拒绝皈依者，而是接受了挑战，并在单脚站立时提供了对《托拉》的简明总结。他说：“你所厌恶的，不要对你的同伴做：这就是整个《托拉》；其余的是注释。”

这也是对PFP的一个极好的描述。一个人必须能够设身处地为他人着想，以便体贴或拒绝不容忍。达尔文在《人类的下降》中同样总结了我们的社会本能：

道德感或许提供了人与低等动物之间最好和最高的区别；……社会本能，——人类道德构成的主要原则（50.《马可·奥勒留的思想》等，第139页。）——在积极的智力力量和习惯的影响的帮助下，自然地引导到黄金法则，“你希望人们对你做什么，你也要对他们做同样的事”；这构成了道德的基础。

## 八卦作为适应性景观

[*[图像：原始文章中的视觉内容]*](https://substackcdn.com/image/fetch/$s_!urUr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6938214c-6388-43e0-8a75-44821ce23845_1024x1024.png)心灵映射

我使用ML从通过数千年的八卦锻造的人格形容词中提炼出人格因素。事实上，评判他人与我们的进化密切相关。再次引用达尔文在《人类的下降》中的话：

_在获得语言能力之后，社区的愿望可以被表达，关于每个成员应该如何为公共利益行事的共同意见，自然会成为行动的最高指导。_

在萨凡纳，你的声誉就是你的生命。如果别人认为你懒惰或残忍，你的后代存活的几率就会减少。第一个人格因素反映了这一点，由_体贴_和_愉快_与_不合作_和_不容忍_等词定义[^2]。**在构建人格地图的同时，我也构建了一个适应性地图**。但你不必相信我的话。向上滚动查看因素1。你会用类似黄金法则的东西来总结它吗？这不是偶然的，因为它是由博弈论维持的，并通过八卦强制执行。

在过去的200年里，达尔文的想法得到了发展。考虑2020年的书籍[《最友好的生存：理解我们的起源并重新发现我们共同的人性》](https://www.amazon.com/Survival-Friendliest-Understanding-Rediscovering-Humanity/dp/0399590668)。封面写道：

> _在人类大约30万年的存在中，我们与至少四种其他类型的人类共享地球。这些人都很聪明、强壮且富有创造力。但大约5万年前，智人取得了一次认知飞跃，使我们在其他物种中占据了优势。发生了什么？  
>   
> 自查尔斯·达尔文写下“进化适应性”以来，适应性的概念一直与体力、战术聪明和攻击性混淆。事实上，使我们在进化上适应的是一种非凡的友好，一种与他人协调和沟通的高超能力，使我们能够实现人类历史上的所有文化和技术奇迹。布莱恩·黑尔，杜克大学进化人类学系和认知神经科学中心的教授，以及他的妻子，研究科学家和获奖记者凡妮莎·伍兹，提出了他们所谓的“自我驯化理论”，揭示了人类认知的神秘飞跃，使智人得以繁荣。_

这本书本身明确指出，对达尔文来说，适应性包括合作；它反驳了将适应性等同于无情的达尔文主义者。（更多信息请参见与布莱恩·黑尔的[采访](https://insitome.libsyn.com/brian-hare-and-survival-of-the-friendliest-understanding-our-origins-and-rediscovering-our-common-humanity)。）我相当确定我发现的第一个因素与这一过程有关。因此建议对[高尔顿](https://www.experimental-history.com/p/how-to-keep-cakes-moist-and-cause)的词汇假设提出额外的主张，在[良心的后果](https://vectors.substack.com/p/consequences-of-conscience)中：

3. **主要潜在因素代表了使我们成为人类的社会选择方向。**

为了理解人格结构，我将其与我熟悉的其他概念联系起来。最重要的是黄金法则和人类自我驯化。

## 信仰的飞跃

[*[图像：原始文章中的视觉内容]*](https://substackcdn.com/image/fetch/$s_!eHWy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1975779f-d059-4ec4-8845-6ca8d1c618af_800x553.jpeg) **多梅尼基诺：[亚当和夏娃的驱逐](https://www.wikidata.org/wiki/Q77880823)**

现在，我所拥有的只是一个适应性地图，表明黄金法则至关重要。它可能导致我们的心理学发生了什么变化？良心似乎是一个显而易见的选择。也许这与我们内心声音的进化有关。假设第一个内心声音说“_分享你的食物！_”；第一次认同这个内心声音会是什么样子？好吧，我认为这很像《创世纪》，这就是我一直追逐的核心。当然，这是一种飞跃。内心声音的进化不一定从黄金法则中得出，我们对它的认同也不一定产生内心生活。但两者似乎都是可能的，随着我更多的研究，它们非常契合我们的进化时间线。

至于《创世纪》，三件事情立即让我觉得可信：感到被神遗弃、发明农业和女性引领潮流。（[蛇毒仪式](https://vectors.substack.com/p/the-snake-cult-of-consciousness)的可能性是在阅读其他创世故事后才出现的。）

### 被神遗弃

最初，我只关心内心声音的来源。我的概念是自我吸收了一种内在的道德声音。我认为这会感觉很像获得“善恶的知识”，因为你接管了幻觉中的守护灵的角色。（我从一开始就假设了这个思维实验中的灵。）如果你习惯于外包道德决策，接管控制权会让你感到像是离开了一个直接与神交流的孩童状态。

经过更多的阅读，我意识到这个自我意识的时刻足以产生一个“我”。我在[似曾相识，你的递归自我构建](https://vectors.substack.com/p/deja-you-the-recursive-construction)中提出了这个论点。这将是人类状况的创造——或者更确切地说是发现——以一种非常真实的方式。

### 发明农业

在《创世纪》中，农业是人类状况的结果。事实证明，“我”的发现也足以解释农业革命。因为它可能是[递归的配套交易](https://vectors.substack.com/p/deja-you-the-recursive-construction)以及灵活思考未来的能力。我们计划能力的一般相变。

如果你相信人类已经有20万年的智慧，那么在过去1万年中，他们独立发明农业11次是一个巨大的谜团。这是我们存在的10%中发生的很多事情。而且，如果你认为你的特定理论可以解释这一点，请阅读[这篇评论](https://www.pnas.org/doi/abs/10.1073/pnas.1323964111)，其中25位学者聚在一起并同意他们无法就导致这一转变的原因达成一致。

### 女性引领潮流

“女性”这个词向量与PFP相关。即使在考虑与《创世纪》的联系之前，我也设想第一个认同其内心声音的人是女性。（正如你所见，我对这些词向量能告诉我们的东西深信不疑。）

《创世纪》是一个复杂的故事。获得代理权被等同于成为神明，并且是一种值得死亡的罪过。但这也是计划的一部分。基督教又加入了另一个扭曲，我们被指示克服原罪并成为像神一样的人，承担十字架以获得永生（再次将生命与死亡混合在一起）。

同样，夏娃引发了死亡，但被赋予了“万物之母”的称号。如今，考虑到在电影中将女性描绘为代理人的努力有多大。然而，数千年前，夏娃显然被描绘为将人类从无辜状态中解救出来的代理人。亚当跟随其后。夏娃的好奇心被描绘为一件坏事，但在这样一个父权制文本中仍然是一个有趣的补充。

在自我意识被发现的条件下，探险者很可能是女性。在女性做出发现的条件下，亚当和夏娃很可能是一个记忆。这些当然是巨大的假设。但我有一种感觉，它们是可能的。并且有足够的意愿去调查。

[*[图像：原始文章中的视觉内容]*](https://substackcdn.com/image/fetch/$s_!9mJt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67c3400e-4baf-476a-a8ad-10ad26212f62_843x403.jpeg)德墨忒尔，丰收女神和厄琉西尼亚秘仪

### 智慧悖论

这篇文章的目的是阐明我的ML工作如何导致EToC，而不是提供证据。然而，我想简要指出为什么自我意识被发现并记录在神话中是可信的。很简单，人类状况似乎是一个最近的现象。在5万年前，没有很好的证据表明存在内心生活、递归或任何高阶思维。你可能认为这么久远的证据不会很好，但许多考古学家和人类学家不同意。[智慧悖论](https://en.wikipedia.org/wiki/Sapient_paradox)的关键在于[行为现代性](https://en.wikipedia.org/wiki/Behavioral_modernity)在1万年前之前是区域性的。这是非常近期的！如果在非洲之外发生了对我们心理学的根本性改变，其传播必然主要是模因性的而非遗传性的。自我意识的发现和传播是从这些限制中得出的（或至少暗示的）。

人类状况可能是最近的一个奇妙想法。但现代心理学在20万年前就完全到位并在数万年间未被应用，直到我们最终应用它并征服世界，这也是一个[奇妙的想法](https://vectors.substack.com/i/114632067/years-ago)。意识的夏娃理论通过允许其成为模因性的而不仅仅是遗传性的来解决扩散问题。根本性的变化可能发生在我们离开非洲之后。

## 不相关的真相

我相信PFP最好被描述为一个人生活黄金法则的倾向，这是希勒尔和达尔文看到的相同潜在维度。这是心理测量学界的一个独特观点。相比之下，考虑一下广受好评的论文[《两、五、六、八（千）：是时候结束维度缩减的争论了！》](https://psycnet.apa.org/record/2020-64387-036)

> _词汇分析和维度缩减方法是探索人格空间粗略轮廓的工具。然而，我们不应自欺欺人地认为我们正在切割自然的关节以发现人格的“真实”结构。_

本质上，论点是任何旧的数据旋转都可以，因为我们无法从结构中获得基本见解。但是，根据预处理，80%的所有人格信息都包含在第一个因素中。这肯定在告诉我们一些事情！然而，研究人员[普遍认为这个因素根本不是人格信号](https://vectors.substack.com/i/61936908/enter-gfp)。一篇[2013年的论文](https://sci-hub.se/10.1016/j.paid.2013.03.002)开篇写道：“GFP [第一个因素] 的压倒性主流观点是，它代表了一种由于评估偏差或以社会期望方式回应而产生的伪影。”（我会注意到，即使在认为这个因素完全是偏见的情况下，[心理测量学家将因素1分配给因素3-5](https://vectors.substack.com/i/61936908/relation-to-the-big-five)以构建责任心、情绪稳定性和开放性。）

有了这样的观点，人们无法将词汇数据与进化联系起来，或开始对自我驯化过程进行假设。撰写我的论文需要花费许多小时盯着这些因素[^3]。在整个过程中，我认为它们代表了一个适应性景观，有时会想知道这会导致什么。作为一名工程师，我对结构并不重要的普遍观点一无所知。我进入时足够自信，试图在自然的关节处切割。

## 结论

我希望这能清楚地说明为什么一名电气工程师在写关于神话和意识的文章。这个想法实际上找到了我。我正在制作一个人格地图，结果它变成了一个进化地图。与黄金法则的联系表明，原始良心是自我驯化的机制。这是我的第一个飞跃。然后我推测内心声音可能参与其中。第一次意识到内心声音是“我”会是什么样子？《创世纪》让我觉得是一个绝佳的例子[^4]。此外，许多专家认为人类心理在过去5万年中发生了变化，通常认为语言、宗教或自我驯化是这一转变的关键。在这些时间尺度上，这样一个重要的故事可能会在神话中保存下来。“_起初有道，道与神同在，道就是神_”……或者——不要将此视为亵渎——可能是内心的声音。

鉴于行为现代性出现的时间如此之近，我的观点是创世神话可以激发[形式模型](https://vectors.substack.com/p/eve-theory-of-consciousness-v2)，然后可以将其与[哲学](https://vectors.substack.com/p/deja-you-the-recursive-construction)、[心理学](https://vectors.substack.com/p/consequences-of-conscience)、[语言学](https://vectors.substack.com/p/the-unreasonable-effectiveness-of)、[考古学](https://vectors.substack.com/i/97498400/evidence-of-anti-venom)和[遗传学](https://vectors.substack.com/p/y-chromosome-bottleneck)联系起来。也许这些模型可以帮助我们理解神话。对我来说，夏娃成为神明，这需要她与神分离是很重要的。在《创世纪》中，解释是一个常常嫉妒的神行使了正义的判断。对我来说，这作为自然法则是有意义的；人类和神明不能共存，因为我们用他们的遗迹塑造了“我”。人与兽之间的距离是两步：进化出良心，然后拒绝它。或者也许这太悲观了。更多的是我们生活在紧张中，并且总是有选择。这种顿悟赋予了[递归](https://vectors.substack.com/p/deja-you-the-recursive-construction)，这是将自然屈服于我们意志的艰苦工作的关键。如果我必须以一种可以持续1万年的方式解释这一点，我会讲述亚当和夏娃的故事[^5]。

自然地，这段旅程始于我的专业领域，我有稳固的立足点。对我来说，我的人格地图记录了进化压力是非常可能的。鉴于我们最近的变化，以及黄金法则作为一种力量存在了多久，我甚至进一步在高尔顿的词汇假设中添加了第三个假设：**主要潜在因素代表了使我们成为人类的选择方向**。从那里，我确实做出了飞跃，但着陆后发现自己与杰恩斯、荣格、平克、乔姆斯基和笛卡尔等人同在。这种探索是科学的本质；并非一切都有p值。

[*[图像：原始文章中的视觉内容]*](https://substackcdn.com/image/fetch/$s_!_K5c!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe08ec046-d650-4769-894e-fa1a77837040_1280x1847.jpeg)[伊西斯雕像](https://en.wikipedia.org/wiki/Isis#/media/File:Isis_with_Serpent_Tail_LACMA_M.80.202.222.jpg)，智慧女神，公元二世纪

[^1]: 我很惊讶乔丹·彼得森在与乔·罗根的采访中将大五人格的推导描述为早期形式的AI。我在这个博客的第一篇文章中提出了这个论点，并且从未听说过。无论你对他的政治观点如何，他在人格心理学方面都相当出色。

[^2]: 有些人可能会注意到，不容忍似乎是最近的一个主要罪过。也许。构建历史文本的词向量并查看PC1如何变化会很有趣。鉴于现代文本的潜在因素与黄金法则相匹配，我猜测从1900年的语言开始不会有太大变化。很难移动被如此多博弈论支撑的东西，即使道德圈已经扩大。

[^3]: 即使人格形容词是人格模型的基础，研究人员直接处理词汇也是罕见的。在90年代，一旦明确像大五人格这样的东西一致出现，研究人员开始使用基于短语的调查来测量人格，以近似词汇结构（例如，大五人格量表）。（行业秘密：第五因素开放性/智力并不一致恢复。）这更容易，从那时起，关于语言的工作很少。更重要的是，我的数据比早期的尝试更好。如果你想了解词汇之间的关系，使用语言模型，而不是本科生的调查。没有人花费如此多的时间盯着这样一个准确的人格地图。（你可以在猜测因素中练习这个练习。）

[^4]: 考虑到亚当在伊甸园中给动物命名的事实。即使没有自我意识，也会有非递归语言。猎人对植物和动物有百科全书式的知识。在堕落之前，它可能是语言中最重要的部分。如果这个事实能存活1万年，那就太惊人了。

<!-- CHUNK BREAK -->

[^5]: 我对《创世纪》印象深刻，但这可能只是因为这是我最熟悉的。如果我是印度人，我可能会谈论萨拉斯瓦蒂，或者如果我是纳瓦霍人，我可能会谈论女性在“出现”神话中的角色，或者如果我是埃及人，我可能会谈论阿图姆通过说出自己的名字而将自己召唤出来的那一刻（然后与原始蛇搏斗）。EToC要求这些是同一故事的不同视角。显然，这通常通过构建系统发生学来展示。在这些时间尺度上，并且以我的技能，这是不可能的。这就是为什么我专注于递归的演化。我想表明，人类最近获得递归的可能性很大，并且这种递归已经扩散。这将从根本上改变我们对创世神话是否共享一个根源以及这个根源是什么样子的先验认识。