---
about:
- vectors-of-mind
- blog-archive
author: Andrew Cutler
date: 2025-07-04
description: “In the beginning was the Word, and the Word was with Psychology, and
  the Word was Psychology” ~New Vector Translation
draft: false
keywords:
- vectors-of-mind
- beginning
- word

lastmod: 2025-07-07
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '51210419'
original_url: https://www.vectorsofmind.com/p/in-the-beginning-was-the-word
quality: 6
slug: in-the-beginning-was-the-word
tags: []
title: 起初有道
translation_model: gpt-4o
---

*From [Vectors of Mind](https://www.vectorsofmind.com/p/in-the-beginning-was-the-word) - 原文中的图像。*

---

[*[图像：原文中的视觉内容]*](https://substackcdn.com/image/fetch/$s_!5qwE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9f7c2505-9587-4daa-aac2-648b8bf16efb_1200x544.png)

_“起初有言，言与心理学同在，言就是心理学” ~新向量翻译_

所有的人格构建首先都是通过词语描述的。从弗洛伊德的可卡因驱动模型到稳重的五大人格特质，它们在某一时刻都是词语。大量的学术心理学关注于比较构建。为此，它们必须共享一个基础，通常是一组受试者。受试者会被给予一个工具（通常是调查问卷），以近似他们在构建空间中的位置。基于受试者反应的协变性，随后对构建做出一般性声明。在这篇文章中，我们探索另一种方法。自然语言处理的进步允许在其自然栖息地中对构建进行定量比较：语言。

### 路线图

在[上一篇文章](https://vectors.substack.com/p/the-big-five-are-word-vectors?s=w)中，我论证了五大人格特质是词向量。这篇文章对独立量表提出了相同的主张，这使得构建可以在不涉及受试者的情况下进行比较。为了证明这一点，引入了一个广泛的人格模型，以及一种在词空间中表示构建的方法。大纲如下：

1. 比较受试者空间与词空间中的构建

2. 受试者空间的问题

3. 使用受试者将亲属和互惠利他主义与五大人格特质联系起来

4. 在词空间中进行相同的比较

   1. 介绍一个（临时的）使用NLP识别的五因素模型

   2. 将利他主义词汇投射到该空间中

   3. 代码可在[此处](https://colab.research.google.com/drive/13DA2IKQ9zRimGedww_09iGT6ehuYriVz?usp=sharing)获取。

5. 讨论、局限性、未来工作

### **曲折的道路**

要将利他主义与五大人格特质进行比较，信号必须经过许多转换：利他主义（理想）→用词语描述→开发（并希望验证）调查问卷以近似该构建→施用于解释这些词语并探寻内心的受试者→受试者利他主义得分→**受试者空间中的相关性**←受试者五大人格量表（BFI）得分←受试者解释BFI项目并探寻内心←开发BFI以近似测量这点←通过定性描述定义/传达的构建←由词负荷定义的五大人格特质。然后对两个理想，利他主义和五大人格特质，做出声明。

### **直截了当**

为什么不使用词向量作为共享基础而不是受试者呢？路径要直接得多：利他主义（理想）→用词语描述→向量化到词空间→**在词空间中比较**←五大人格特质，正如在[上一篇文章](https://vectors.substack.com/p/the-big-five-are-word-vectors?s=w)中讨论的那样，已经存在于词空间中。对于那些记分的人来说，这是4比10次转换。（记分方式类似于高尔夫。）

[*[图像：原文中的视觉内容]*](https://substackcdn.com/image/fetch/$s_!tbb9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb8b6c50-e94e-4462-8772-78359189f70e_1600x1305.png)统计现实造访心理学领域。这几年过得很艰难。

### **启示者Tal**

使用受试者对语言构建进行声明的困难并不是秘密。

> _“心理学中的大多数理论和假设本质上是语言的，但它们的评估却主要依赖于推论统计程序。从定性到定量分析的有效性取决于假设的语言和统计表达是否紧密一致——即，两者必须大致指向同一组假设观察。在这里，我认为心理学中许多统计推断的应用未能满足这一基本条件。” ~Tal Yarkoni,_ [可推广性危机](https://psyarxiv.com/jqw35/)

这里的有效性指的是一个分数捕捉到其意图测量的构建。值得完整阅读这些论点和例子。但对我们来说，关键是面对这些现实可以做些什么。他建议：

1. 做其他事情（进入其他领域）。

2. 拥抱定性研究

3. 采用更好的标准（包括7个建议）。

> _“人们总是可以假装从极其狭窄的统计操作中获得的小p值可以为关于复杂心理构建的广泛语言推论提供充分的基础。但没有人——不是同行，不是资助者，不是公众，当然也不是长期的科学记录——有义务尊重这种伪装。”_

即使你对心理学研究的看法没有那么悲观，读者肯定也曾被那些做出声明但实验与之关系微弱的论文所伤害。所有可用的解决方案都很痛苦。该领域可能不得不采取更狭隘的观点，将大问题留给研究历史、文学和线性代数的人。我提出另一种前进的方式。

### **转换到词空间**

4. 使用词向量作为共享基础

构建在词空间中共同存在，而当进行比较时，我们将它们拖入受试者空间。这是一个巨大的、有损的麻烦。如果它们可以安全地留在词空间中呢？自然语言处理的假设是，词语是连续空间中的向量。分析这些向量在万亿美元的行业中足够好用，并且目前正在被（[重新](https://vectors.substack.com/p/the-big-five-are-word-vectors?s=w)）引入心理学。

### **实践所宣扬的**

在这里，我们将查看一个在受试者空间中完成的传统研究，然后尝试通过转移到词空间来改进它。为了避免稻草人，研究对象是[亲属利他主义、互惠利他主义和五大人格因素](https://www.sciencedirect.com/science/article/abs/pii/S1090513898000099?casa_token=05bTreOjGKUAAAAA:nLHTWhK3z45xUbN5nTVd7a3-Qaz9No22rQtVY6vpUjYpeZ1bkPy-cBig9UgRbn-GnqJScTCPpSY)，该研究已被引用数百次，其第一作者的h指数为70。

受试者使用三种工具进行测量：五大人格（通过形容词调查）、同情/依恋和宽恕/不报复（短语调查），以及在金钱分配游戏中的利他主义。由于作者假设宜人性和情绪稳定性（即神经质）之间的间隙区分了两种利他主义，因此添加了一些词语以更好地测量该区域。同样，设计了一份新的问卷来测量同情/依恋和宽恕/不报复，这些被理论化为分别与亲属和互惠利他主义相关。对于这种类型的研究，使用游戏来测量利他主义是超出常规的。

> _“在用于测量亲属利他主义的金钱分配任务版本中，另一个人被描述为一个亲密的朋友——一个与参与者有长期友谊历史并有很多共同点的人。我们希望通过将友谊描述为一个旧的，并将朋友描述为与参与者非常相似的人，友谊将非常接近一个人与亲属的关系。我们没有使用亲属作为潜在的利他主义对象的原因是为了避免由于涉及特定亲属而导致的反应差异；例如，许多人可能更愿意对一个兄弟姐妹表现出利他主义而不是另一个。”_

换句话说，为了不因对亲属的真实世界感情而玷污数据，测量了互惠利他主义。

> _“在用于测量互惠利他主义的金钱分配任务版本中，另一个人被描述为一个不合作的人——一个对参与者粗鲁、讨厌和不体贴的人。”_

而为了测量互惠利他主义，他们测量了……未被回报的利他主义？自然地，存在相关性，作者得出结论：

> _“这项研究的结果支持这样一种观点，即涉及同情和依恋的人格特质促进了主要针对亲属的利他主义（即亲属利他主义），而涉及宽恕和不报复的人格特质促进了主要针对非亲属的利他主义（即互惠利他主义）。”_

但如果从未测量过互惠利他主义，结果如何支持这一主张？正如Tal指出的，心理学论文中的统计数据往往是一种修辞上的点缀。但我们不必参与其中！让我们看看词空间有什么要说的。

### **奶与蜜之地（欢迎来到词空间）**

在传统研究中，由于将受试者映射到人格空间的成本，分辨率只能在少数人格区域中很高。这就是为什么作者探测同情和不报复以及宜人性和情绪稳定性之间的空间。所有这些轴线[存在于常规的五大人格空间中](https://psyarxiv.com/vebtm/)，但测量得非常细致。在词空间中，我们可以将利他主义与完整的五大人格进行比较，展现其高分辨率的辉煌。在我的github上，有2819个词向量被分解为五个主成分。我们可以方便地使用这些。首要任务是选择描述每种利他主义的词集。对于亲属词，我选择那些体现家庭角色的词：_兄弟般的、姐妹般的、母亲般的、母性的、父亲般的、祖母般的、祖父般的、妻子的、母性的、父性的。_对于互惠利他主义，我遵循Trivers的定义。

> _“关于人类互惠利他主义，表明调节这种利他主义的心理系统的细节可以通过模型解释。具体来说，**友谊、厌恶、道德攻击、感激、同情、信任、怀疑、可信赖性、某些形式的内疚以及某些形式的不诚实和虚伪**可以被解释为调节利他系统的重要适应。每个人类个体被视为拥有**利他和欺骗倾向**，其表达对被选择的变量敏感，这些变量被选择用于在当地社会和生态环境中适当地平衡这些倾向。” _[互惠利他主义的进化](https://www.journals.uchicago.edu/doi/abs/10.1086/406755)，Robert Trivers（加粗部分为重点）

考虑到这一点，我选择了：_挑剔的、不宽容的、复仇的、忠诚的、邻里的、合作的、可信赖的_和_公平的。_这大致等于倾向于合作但在事情出错时进行道德攻击。此外，它试图将这种利他主义捕捉为欺骗的对立面（例如，_公平的_，_可信赖的_）。

（有关信任进化的精彩解释，请参见[此](https://ncase.me/trust/)互动演示。）

#### 让我向您介绍未知的五因素模型？

理论上，我们可以使用通过调查产生的五大人格词负荷，但大多数这些词语都很少见，以至于未被包括。这是最好的，因为在心理学学生中通过自我报告无法获得_祖母般的_的良好估计。因此，使用语言模型RoBERTa计算的词向量。源自一个大型且[特征明确的](https://openpsychologydata.metajnl.com/articles/10.5334/jopd.57/)人格词列表，所得的五个因素简而言之：

1. 亲和力（或社会化）。你有多想让这个人成为你的团队成员？类似于宜人性，但不包括成为一个软弱的人。_轻信_，例如，在亲和力上负荷中性，但在宜人性上负荷积极。

2. 活力。与外向性非常接近，但更多关于冒险感，而不是自信。

3. 秩序。具有锋芒的尽责性。实现自己目标的能力。_严格_对比_含糊_。

4. 情感依附。虽然神经质关注不稳定性，但这是关于依附；_关心_和_恶意_都高度负荷。

5. 超越。这个因素的特征是_独特、复杂、命运多舛、残疾、神秘、心碎、超凡脱俗_对比_不哲学、无忧无虑、顽固、粗鲁、物质主义、自我中心、油腔滑调_。它涉及超越自我和世俗。这个过程显然与痛苦紧密相连。事实上，“困扰”在超越性上的负荷比情感依附（与神经质相关的因素）更高。

前三个因素的名称取自De Raad的跨文化[工作](https://journals.sagepub.com/doi/10.1002/per.1953)，因为定性上，它们与五大人格的匹配更为接近。每个因素都值得单独讨论。（对于工业心理学领域的人来说，我怀疑秩序与商业成功的相关性比尽责性更高，因为它更具计算性而不是准时到达。）但提出模型不是我的强项，更精细的语言研究即将到来，可能会产生不同的结构。目前这些因素足够了。以下是它们与五大人格的相关性：

[*[图像：原文中的视觉内容]*](https://substackcdn.com/image/fetch/$s_!Sxlw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F63c86f00-e0cc-4854-bd8a-e6ba3fc55449_366x374.png)

#### 结果

利他主义词在前四个因素上的负荷（超越性在本研究中不重要）：

[*[图像：原文中的视觉内容]*](https://substackcdn.com/image/fetch/$s_!Q5sr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4efdfb85-197d-4d57-8a8b-3675eaf2b162_955x735.png)拥有强烈的家庭纽带是亲社会的（高亲和力），如果有点无聊（活力中性到低）。所有词都映射到相似的位置。

[*[图像：原文中的视觉内容]*](https://substackcdn.com/image/fetch/$s_!f7oe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb08b529e-7443-4f5b-af1e-ce080e36a4b7_961x735.png)家庭词在情感依附上负荷强烈。注意父母和祖父母的关系是相当性别化的。男性的依附性较低，正如Trivers的[父母投资理论](http://joelvelasco.net/teaching/3330/trivers72-parentalinvestment.pdf)所预测的那样，[统计数据](https://www.pewresearch.org/social-trends/2013/07/02/the-rise-of-single-fathers/)也证实了这一点。然而，兄弟姐妹的依附性是相等的，并且低于父母。想想看，_妻子般的_不应该被包括在关于血亲的利他主义中。与母亲或祖母相比，它在依附性上的负荷较低。

[*[图像：原文中的视觉内容]*](https://substackcdn.com/image/fetch/$s_!FYnd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa40e5562-577f-4b55-bd16-d34ccec1c388_955x735.png)互惠词试图捕捉理想的以牙还牙行为，当合作伙伴合作或作弊时。因此，这些词分布得更广，尽管大多数仍然是积极的。即使是“挑剔”也是略微积极的，这意味着我不认为这个词被编码为类似“种族歧视”的东西——有时这些语言会因语音相似而混淆（例如，古怪和种族中心主义）。

[*[图像：原文中的视觉内容]*](https://substackcdn.com/image/fetch/$s_!lGox!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6eb4b7d2-4728-4f66-83ce-cd95e2346144_961x735.png)合作和邻里关系略微暗示自己的目标处于次要地位。不宽容和挑剔是那些认真对待的人。

为了比较利他主义，我们希望将这些词集中的每一个都简化为一个向量。（是否有意义甚至可以辩论，因为互惠——在某种程度上亲属——需要对不同场景做出不同反应。）廉价而简单的解决方案是将每个构建视为一个[词袋](https://en.wikipedia.org/wiki/Bag-of-words_model)并取平均值。平均负荷是：

[*[图像：原文中的视觉内容]*](https://substackcdn.com/image/fetch/$s_!TMN7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe3aaf685-9bb3-4dbf-974f-0ab994f40a88_356x238.png)这些是针对所有2819个词的z分数。平均而言，亲属词在亲和力和情感依附上偏离1-1.5个标准差。

[*[图像：原文中的视觉内容]*](https://substackcdn.com/image/fetch/$s_!mDHG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fba83d4f1-2f47-42e8-a158-368c7681a2db_356x238.png)互惠利他主义也涉及秩序，实现自己的目标。

[*[图像：原文中的视觉内容]*](https://substackcdn.com/image/fetch/$s_!48eW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd912d107-48f4-4d5e-bb23-fe24dd932b78_356x238.png)差异：亲属减去互惠负荷。由秩序主导。

### **讨论**

我不认为受试者空间中的论文包含有效的亲属或互惠利他主义测量，因此没有增加我们对其与人格关系的理解。这是一种令人惊讶的常见失败模式。词空间提供了一些针对无效比较的保险。我们对一个词在词空间中应该在哪里有更好的直觉，而不是受试者112应该如何回答调查问卷。更容易发现错误。

从贝叶斯的角度来看，受试者空间与词空间中发生的事情有所不同。包括受试者的实验旨在为桌面带来新信息。希望这将更新读者对世界的看法。但研究人员（和普通人）拥有大量的社会经验和对心理过程的更敏锐感知，而不是调查问卷提供的快照。很难大幅度改变观点。词空间更类似于可视化我们的先验知识，而不是产生新知识。这种观点很有价值，因为语言是实践的关键所在。正如JL Austin所说：

> _“我们的常用词汇体现了人们在许多代人的一生中发现值得划分的所有区别，以及他们发现值得标记的联系：这些区别和联系肯定比你我在一个下午的安乐椅上想出的任何区别和联系要多、要合理，因为它们经受住了适者生存的长期考验，并且在所有普通和合理的实际事务中更为微妙。”[为借口辩护](https://sites.ualberta.ca/~francisp/NewPhil448/AustinPlea56.pdf)_

在词空间中的分析相对简单。与其说是相关性和p值的表格，不如说是将词语简单地绘制在感兴趣的轴线上并进行视觉判断。亲属利他主义词在亲和力和情感依附上紧密聚集，这是唯一两个具有显著负荷的因素。父亲，但不是兄弟，比女性同行的依附性更低，这与Trivers的父母投资理论一致。兄弟姐妹有理由照顾他们的兄弟姐妹。然而，父亲比母亲的理由更少。精子便宜。卵子和怀孕昂贵。

互惠词分布更广，反映了理想的特质以应对不同的场景：合作伙伴合作或背叛。最显著的区别是秩序上的平均负荷更高——实现自己的目标。最初称为_延迟回报利他主义_，互惠利他主义不是为了牺牲自己去帮助陌生人，而是通过亲社会手段投资于自己的未来。另一方面，亲属利他主义指的是即使在自己损失的情况下也帮助家人，因为自私的基因在牵动你的心弦。这在亲属利他主义词在情感依附上的更高负荷中显而易见，支持Ashton的假设。但主要的行动在秩序上，远离受试者空间工具设计用于检测的地方。在受试者空间中采样的成本使得结果更依赖于研究者的先验知识。

解释这些图可以感觉像是在读茶叶，但我大约70%确定这里的内容。让我犹豫的一件事是两种利他主义以不同的方式表示。亲属词都描述关系（例如，_母亲、父亲、兄弟_），而互惠词是关系（例如，_邻居_）和适合重复正和游戏的特质（例如，_复仇、挑剔、合作_）的混合。尽管存在不确定性，如果我在一个下午进行了一项结合了数百万人生活利他主义经验的实验，那不是很酷吗？几代人已经同意什么使一个人具有父亲般、姐妹般或邻里般的特质。正如新信号源总是那样，人们开始随意射击。最终，西部荒野被驯服；方法和启发式出现。还有很大的改进空间。读者可以调整词集，并在几分钟内使用这个[colab笔记本](https://colab.research.google.com/drive/13DA2IKQ9zRimGedww_09iGT6ehuYriVz?usp=sharing)获得新的结果。请这样做！

#### 词空间的优势

1. 与词汇假设相关。基于去中心化的社会现实。

2. 转换更少。每一步都是有损的并引入偏差。

3. 转换到词空间后统计强度较低。（进入门槛较低。）

4. 有效样本量（通过在reddit上发表评论、写书或pubMed文章为语言模型做出贡献的人）比大多数研究要大得多且多样化。

5. 了解NLP的心理学博士有更好的工作前景。

6. 更容易进行多语言/多文化工作。一些模型同时在100种语言上进行训练（这就是Meta如何在样本较少的语言中训练[仇恨言论过滤器](https://ai.facebook.com/blog/how-ai-is-getting-better-at-detecting-hate-speech/)）。

7. 语言模型[不断](https://openai.com/blog/introducing-text-and-code-embeddings/) [变得](https://say-can.github.io) [更好](https://ai.googleblog.com/2022/04/pathways-language-model-palm-scaling-to.html)。

8. 开放科学。

9. [避免IRB](https://slatestarcodex.com/2017/08/29/my-irb-nightmare/)。

#### 缺点

1. 移动部件更多。语言模型中有数十亿个参数！然而，即使是数十亿个神经元和数十个训练决策也可以产生稳定的表示。任何值得其盐的语言模型都可以完成类比“丈夫之于妻子如国王之于____”。

2. 无法按人口统计细分结果。有时了解25-30岁之间的小学教师的人格很有趣。或者知道某个构建与逮捕记录的相关性。在词空间中是不可能的。

3. 语言模型不是有偏见的吗？嗯，不比自我报告更有偏见。

4. 将利他主义定义为一堆词向量的总和（即词袋）有点草率。在这里有很大的改进空间。

[*[图像：原文中的视觉内容]*](https://substackcdn.com/image/fetch/$s_!ctzj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F455fdb70-3c84-4dfe-81bf-6bf6e676fd44_1600x1128.jpeg)心理学家对在受试者空间中再徘徊40年感到满意。

### **外来神祇**

_“我认为卡夫卡是对的，他说，对于现代人来说，国家官僚机构是与神圣维度唯一剩下的联系。”_ ~Zizek，《一个变态者的意识形态指南》

<!-- CHUNK BREAK -->

他在这里描述的，当然是向IRB提交上诉时那种超然的感觉。我有一个预测。从信号处理的角度来看，词空间是正确且合理的做法，但其采用将更多地受到不受监管的便利性驱动。相应地，IRB将是第一个宣布语言模型具有感知能力的政府机构。

[*[图片：原始帖子的视觉内容]*](https://substackcdn.com/image/fetch/$s_!6nGN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fedfc8bac-cf78-40f9-88d3-9a30066ff108_817x1600.jpeg)John传播良好的词空间

### **准备工作**

我们希望从语言模型中提取构念之间的关系。为了以增加信号而非噪声的方式进行，这需要大量的验证工作。最初，这意味着与已建立的调查结果进行比较。它们能否通过词向量恢复？它们在哪里失败？一旦确定，每篇以“需要更多研究”结尾的论文都应该找到一种在词空间中提出问题的方法。

我花了一年多的时间微调一种[方法](https://psyarxiv.com/gdm5v/)，以从当时最先进的模型[RoBERTa](https://arxiv.org/abs/1907.11692)中提取人格关系。不久之后，GPT-3发布了，它在初始状态下表现得更好。这种计算能力超越领域知识的现象是AI中的一个反复出现的[痛苦教训](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)。计算能力呈指数增长。如果你能通过领域知识在通用机器学习解决方案上获得30%的提升，你也可以等待[计算能力赶上](https://twitter.com/russelljkaplan/status/1513128016452337667)，并使用通用方法获得相同的结果。因此，找到将心理学问题与现成的NLP模型相关联的方法是一个很好的前进方向。每六个月左右就会有一个性能明显更好的新模型公开发布。那些验证词空间的人正在为更高智能的到来做准备——[PaLM](https://ai.googleblog.com/2022/04/pathways-language-model-palm-scaling-to.html)、GPT-7、OSCar（**O** ptimal **S** entience **Car** tography）——以揭示心理学的真相。

自然语言充满了关于世界的共享理论。既然我们可以量化它们，它们不能作为证据使用吗？

如果你觉得这很有趣，请分享！

[分享](https://www.vectorsofmind.com/p/in-the-beginning-was-the-word?utm_source=substack&utm_medium=email&utm_content=share&action=share)