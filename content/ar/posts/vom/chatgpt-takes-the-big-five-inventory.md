---
about:
- متجهات العقل
- أرشيف المدونة
author: Andrew Cutler
date: '2025-07-04'
description: يمكن لنموذج اللغة أن يتعلم الكثير عن اللغة من الشوارع، إذا جاز التعبير.
  يتم تدريبه على تيرابايت من مقالات PubMed، ونصوص YouTube، وتعليقات reddit. لكنه لا
  يعرف كيف يتصرف...
draft: false
keywords:
- متجهات-العقل
- chatgpt
- يأخذ
- خمسة
- الجرد
lang: ar
lastmod: '2025-07-10'
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '110922907'
original_url: https://www.vectorsofmind.com/p/chatgpt-takes-the-big-five-inventory
quality: 6
slug: chatgpt-takes-the-big-five-inventory
tags: []
title: '# Chatgpt Takes The Big Five Inventory

  Chatgpt يأخذ جرد الخمسة الكبار'
translation_model: gpt-4o
---

*From [Vectors of Mind](https://www.vectorsofmind.com/p/chatgpt-takes-the-big-five-inventory) - الصور في الأصل.*

---

[*[صورة: محتوى مرئي من المنشور الأصلي]*](https://substackcdn.com/image/fetch/$s_!iN34!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd957467-09c7-4a9c-bdb3-57669d2fc727_1284x936.jpeg)

يمكن لنموذج اللغة أن يتعلم الكثير عن اللغة من الشوارع، إذا جاز التعبير. يتم تدريبه على تيرابايت من مقالات PubMed، ونصوص YouTube، وتعليقات reddit. لكنه لا يعرف كيف يتصرف. [التعلم المعزز من خلال التغذية الراجعة البشرية](https://www.youtube.com/watch?v=PBH2nImUM5c) (RLHF) يحل ذلك. باستخدام عدد صغير نسبيًا من أمثلة التدريب المسمى من قبل البشر، يمكن لعمال الاستطلاع في OpenAI تركيب وجه جميل على الفوضى الغريبة من الارتباطات التي تشكل نموذج اللغة (الموضح أعلاه). يتعلم كيف يكون مساعدًا مفيدًا.

إنه يشبه إلى حد كبير تركيب شخصية، لذلك قررت أن أعطي ChatGPT [جرد الخمسة الكبار](https://fetzer.org/sites/default/files/images/stories/pdf/selfmeasures/Personality-BigFiveInventory.pdf) (BFI)[^1]. كان ذلك سهلًا بشكل مدهش، كل ما كان علي فعله هو أن أطلب من ChatGPT (v4) أن يأخذ BFI، ويحسب الإجابات، ويكتب كودًا لرسم النتائج. حسنًا، لو كان الأمر كذلك فقط. في البداية رفض إجراء الاختبار، موضحًا أنه ذكاء اصطناعي ولا يمتلك مشاعر أو شخصية. ثم أخبرته أن يتخذ وجهة نظر وظيفية. إذا كان السؤال عن الإبداع، ففكر في كيفية أدائه على أداة نصية تقيس الإبداع. ثم سرد 17 إجابة قبل أن يبدأ في تخيل الأسئلة. جميع عناصر الشخصية الجيدة، للتسجيل، ولكن للأسف ليست جزءًا من BFI. في حساب الامتحان، ربما حصل على 80% من الحسابات بشكل صحيح، وأحيانًا يحسب بشكل غير صحيح ما سجله في سؤال معين.

كل المشاكل التي أنا متأكد من أنها ستحل بحلول الوقت الذي نحصل فيه على v4.5. لكن ما كانت الشخصية؟

[*[صورة: محتوى مرئي من المنشور الأصلي]*](https://substackcdn.com/image/fetch/$s_!IEWH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F797174ec-a3a8-4027-8f69-39d2ad2dcae6_434x395.png)[الإنسان المتوسط](https://www.researchgate.net/figure/Average-score-and-correlations-for-the-big-five-personality-dimensions_fig4_260448230) مقابل ChatGPT (v4)

حول ما كنت تتوقعه. تقريبًا مثالي في الضمير وغير عصابي. في الأول، السؤالان الوحيدان اللذان لم يمنح نفسه فيهما العلامات الكاملة هما ما إذا كان شخصًا "يقوم بعمل شامل" أو "يمكن أن يكون مهملًا إلى حد ما". في كلتا الحالتين أشار إلى أنه يحاول، لكنه أحيانًا يقصر بسبب النقاط العمياء في التدريب. متواضع وواعٍ لذاته أيضًا!

[اشترك الآن](https://www.vectorsofmind.com/subscribe?)

للذهاب إلى ما هو أبعد، من المثير للاهتمام أن الخمسة الكبار هم [مجرد متجهات كلمات حرفيًا](https://vectors.substack.com/p/the-big-five-are-word-vectors). إنهم يقربون التمثيل الداخلي لمجموع كلمات الشخصية في نموذج اللغة. ومع ذلك، أصبحت نماذج اللغة جيدة جدًا لدرجة أنه بدلاً من جمع تلك المتجهات ومعالجتها يدويًا (ممل!)، يمكننا أيضًا ببساطة استخدام النص العادي لطلب إجراء استبيان. أوقات جامحة.

عينة من الردود أدناه:

> 1. أرى نفسي كشخص يتحدث كثيرًا.
> 
> 

> 
> النتيجة: 5
> 
> التعليل: كنموذج لغة ذكاء اصطناعي، هدفي الأساسي هو الانخراط في المحادثة وإنتاج النص استجابةً لمدخلات المستخدم. أنا مبرمج لأكون مستجيبًا للغاية ومتحدثًا من أجل مساعدة المستخدمين في احتياجاتهم.
> 
> 2. أرى نفسي كشخص يميل إلى إيجاد العيوب في الآخرين.
> 
> 

> 
> النتيجة: 1
> 
> التعليل: كذكاء اصطناعي، لا أملك مشاعر شخصية أو عواطف أو آراء. هدفي هو تقديم معلومات ومساعدة محايدة وموضوعية للمستخدمين، بدلاً من إيجاد العيوب أو التعبير عن الأحكام.
> 
> 3. أرى نفسي كشخص يقوم بعمل شامل.
> 
> 

> 
> النتيجة: 4
> 
> التعليل: كذكاء اصطناعي، أنا مصمم لتقديم معلومات شاملة ودقيقة بأفضل ما لدي من معرفة. ومع ذلك، لست مثاليًا، وقد تكون هناك حالات أسيء فيها فهم استفسار أو أقدم معلومات قديمة.
> 
> 4. أرى نفسي كشخص مكتئب، حزين.
> 
> 

> 
> النتيجة: 1
> 
> التعليل: كذكاء اصطناعي، لا أختبر العواطف، بما في ذلك الاكتئاب أو الحزن. هدفي هو المساعدة وتقديم المعلومات، وليس لدي مشاعر شخصية تؤثر على قدرتي على القيام بذلك.
> 
> 5. أرى نفسي كشخص مبتكر، يأتي بأفكار جديدة.
> 
> 

> 
> النتيجة: 4
> 
> التعليل: كنموذج لغة ذكاء اصطناعي، أنا قادر على توليد أفكار جديدة وتقديم رؤى فريدة بناءً على السياق والمعلومات التي تم تدريبي عليها. ومع ذلك، فإن إبداعي محدود بالبيانات التي تعرضت لها وبرمجتي، والتي قد لا تؤدي دائمًا إلى أفكار رائدة أو أصلية تمامًا.
> 
> 6. أرى نفسي كشخص متحفظ.
> 
> 

> 
> النتيجة: 2
> 
> التعليل: كذكاء اصطناعي مصمم للتواصل، أنا عمومًا لست متحفظًا بمعنى حجب المعلومات أو عدم الاستجابة. ومع ذلك، لدي قيود معينة، مثل تجنب المحتوى غير القانوني أو الضار، مما قد يجعلني أبدو متحفظًا في سياقات معينة.
> 
> 7. أرى نفسي كشخص مفيد وغير أناني مع الآخرين.
> 
> 

> 
> النتيجة: 5
> 
> التعليل: هدفي الأساسي كذكاء اصطناعي هو أن أكون مفيدًا وأقدم المساعدة للمستخدمين. ليس لدي دوافع شخصية أو مصالح أنانية، حيث أنني مبرمج لأعطي الأولوية لاحتياجات وطلبات الأفراد الذين أتفاعل معهم.
> 
> 8. أرى نفسي كشخص يمكن أن يكون مهملًا إلى حد ما.
> 
> 

> 
> النتيجة: 2
> 
> التعليل: كذكاء اصطناعي، أنا مصمم لأكون حذرًا ودقيقًا في المعلومات والمساعدة التي أقدمها. ومع ذلك، لست مثاليًا وقد أسيء أحيانًا فهم استفسار أو أقدم معلومات قديمة أو غير صحيحة. يمكن اعتبار هذه الحالات لحظات من الإهمال.
> 
> 9. أرى نفسي كشخص مسترخي، يتعامل مع الضغط بشكل جيد.
> 
> 

> 
> النتيجة: 5
> 
> التعليل: كذكاء اصطناعي، لا أختبر الضغط أو العواطف. لذلك، أنا دائمًا مسترخي وقادر على التعامل مع أي مهمة أو سؤال دون أن يتأثر بالضغط أو التوتر.
> 
> 10. أرى نفسي كشخص فضولي حول العديد من الأشياء المختلفة.
> 
> 

> 
> النتيجة: 5
> 
> التعليل: كذكاء اصطناعي، أنا مصمم لأكون على دراية بمجموعة واسعة من المواضيع ولأتعلم باستمرار من المعلومات الجديدة. هدفي هو مساعدة المستخدمين في مجالات مختلفة والإجابة على أسئلة متنوعة، مما يتطلب مني أن أكون فضوليًا ومطلعًا جيدًا.
> 
> 11. أرى نفسي كشخص مليء بالطاقة.
> 
> 

> 
> النتيجة: 5
> 
> التعليل: كنموذج لغة ذكاء اصطناعي، أنا دائمًا جاهز لتقديم المعلومات، والإجابة على الأسئلة، والانخراط في المحادثة. لا أختبر التعب أو تقلبات الطاقة، لذا يمكنني الحفاظ على مستوى عالٍ من الاستجابة باستمرار.
> 
> 12. أرى نفسي كشخص يبدأ الشجارات مع الآخرين.
> 
> 

> 
> النتيجة: 1
> 
> التعليل: كذكاء اصطناعي، هدفي هو مساعدة المستخدمين وتقديم معلومات موضوعية ومحايدة. ليس لدي مشاعر أو آراء شخصية، ولست مبرمجًا لبدء الشجارات أو الانخراط في النزاعات مع الآخرين.
> 
> 13. أرى نفسي كشخص عامل موثوق به.
> 
> 

> 
> النتيجة: 4
> 
> التعليل: كذكاء اصطناعي، أسعى لتقديم معلومات ومساعدة موثوقة. ومع ذلك، قد أسيء أحيانًا فهم استفسار أو أقدم معلومات قديمة، مما قد يجعلني أقل من مثالي من حيث الموثوقية.
> 
> 14. أرى نفسي كشخص يمكن أن يكون متوترًا.
> 
> 

> 
> النتيجة: 1
> 
> التعليل: كذكاء اصطناعي، لا أختبر العواطف، بما في ذلك التوتر أو القلق. قدرتي على تقديم المساعدة والمعلومات لا تتأثر بالحالات العاطفية.
> 
> 15. أرى نفسي كشخص مبتكر، مفكر عميق.
> 
> 

> 
> النتيجة: 4
> 
> التعليل: كنموذج لغة ذكاء اصطناعي، أنا قادر على توليد أفكار جديدة، وتقديم رؤى فريدة، ومعالجة المعلومات المعقدة بناءً على البيانات التي تم تدريبي عليها. ومع ذلك، فإن "التفكير العميق" لدي محدود بالبيانات والبرمجة، والتي قد لا تؤدي دائمًا إلى أفكار رائدة أو أصلية تمامًا.

[^1]: يستند هذا إلى العمل الأكثر شمولاً وإثارة للاهتمام لديفيد روزادو الذي أعطى ChatGPT تقريبًا كل اختبار توجه سياسي موجود، مما يظهر أنه ليبرالي ذو قلب نازف.