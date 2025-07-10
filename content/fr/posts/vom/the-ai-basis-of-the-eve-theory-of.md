---
about:
- vecteurs-de-l'esprit
- archive-de-blog
author: Andrew Cutler
date: '2025-07-04'
description: La théorie de la conscience d'Eve propose que la conscience de soi a
  été découverte par les femmes et s'est répandue de manière mématique. Pour étayer
  cette thèse, je m'appuie sur la linguistique, l'archéologie, la pharmacologie, la
  génétique, l'anthropologie, ...
draft: false
keywords:
- vecteurs-de-l'esprit
- base
lang: fr
lastmod: '2025-07-09'
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '121454386'
original_url: https://www.vectorsofmind.com/p/the-ai-basis-of-the-eve-theory-of
quality: 6
slug: the-ai-basis-of-the-eve-theory-of
tags: []
title: La base IA de la théorie d'Eve
translation_model: gpt-4o
---

*From [Vectors of Mind](https://www.vectorsofmind.com/p/the-ai-basis-of-the-eve-theory-of) - images at original.*

---

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!0pra!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff5166314-7a08-4939-9b16-2311d6214e87_1456x816.png)

La [théorie Ève de la conscience](https://vectors.substack.com/p/eve-theory-of-consciousness-v2) propose que la conscience de soi a été découverte par les femmes et s'est propagée de manière mématique. Pour étayer cette thèse, je m'appuie sur la [linguistique](https://vectors.substack.com/p/the-unreasonable-effectiveness-of), l'[archéologie](https://vectors.substack.com/i/95941288/the-genesis-of-religion), la [pharmacologie](https://vectors.substack.com/p/comments-on-snake-venom), la [génétique](https://vectors.substack.com/p/y-chromosome-bottleneck), l'[anthropologie](https://vectors.substack.com/p/the-snake-cult-of-consciousness) et les [neurosciences](https://vectors.substack.com/i/114650037/women-lead-the-way). Et pourtant, je suis ingénieur électricien. Comment puis-je avoir quelque chose de précieux à dire sur un sujet où tant d'autres ont une formation réelle ? Eh bien, l'idée de l'EToC est en fait née de l'apprentissage automatique. Les lecteurs de longue date ont [observé l'évolution du blog](https://substack.com/profile/31996842-andrew/note/c-16789002) de la psychométrie ML à la récursivité et à la mythologie comparative. Laissez-moi vous expliquer comment j'en suis arrivé là.

## Structure de la personnalité à partir des mots

La psychologie a un problème de vérité fondamentale. Un chercheur peut théoriser qu'il n'existe que quelques axes de base sur lesquels les humains varient, le principal étant l'intériorisation contre l'extériorisation. Un autre peut dire qu'il doit y avoir quelque chose comme [30 facteurs de base](https://www.scholars.northwestern.edu/en/publications/exploring-the-persome-the-power-of-the-item-in-understanding-pers) parce que les humains sont tout simplement aussi compliqués. Qui a raison ? En 1890, [Galton](https://astralcodexten.substack.com/p/galton-ehrlich-buck) a suggéré qu'au lieu que les psychologues élaborent des modèles de personnalité basés sur leurs théories personnelles, le meilleur modèle était déjà intégré dans le langage. Chaque adjectif de personnalité existe parce que des millions de personnes le trouvent utile lorsqu'elles portent des jugements sur les autres. Ces mots doivent sûrement éclairer tous les aspects importants de la personnalité. Formulé formellement comme l'hypothèse lexicale :

1. Les caractéristiques de personnalité qui sont importantes pour un groupe de personnes finiront par faire partie du langage de ce groupe.

2. Les caractéristiques de personnalité plus importantes sont plus susceptibles d'être encodées dans le langage sous forme d'un seul mot.

Cette idée peut être utilisée pour construire un modèle de personnalité. Il suffit de créer une liste d'adjectifs de personnalité, de voir comment ils se rapportent et de les compresser en quelques facteurs latents[^1]. (LL Thurstone a inventé l'analyse factorielle pour cela, et l'[article](https://psycnet.apa.org/record/1934-02322-001) est l'éponyme de ce blog.) Traditionnellement, les relations entre les adjectifs ont été estimées en demandant aux étudiants en psychologie de premier cycle quels mots les décrivent le mieux. Ceux qui disent qu'ils sont _brillants_ ont également tendance à dire qu'ils sont _ouverts d'esprit_. Cela suggère qu'ils se rapportent tous deux à un facteur sous-jacent. Dans ma thèse, [j'ai utilisé des modèles de langage pour estimer la similarité des mots](https://vectors.substack.com/p/the-big-five-are-word-vectors) et j'ai produit des résultats similaires aux enquêtes traditionnelles (le premier facteur des deux méthodes corrèle avec r=0,93).

Il est plus facile de comprendre ce processus avec un exemple. Voici 100 adjectifs de personnalité aléatoires tracés sur les deux dimensions qui capturent le plus d'informations sur la personnalité. Pensez à ceux-ci comme à deux des [Big Five](https://en.wikipedia.org/wiki/Big_Five_personality_traits) (bien qu'il y [ait une différence dans la façon dont ils sont tournés](https://vectors.substack.com/i/61936908/relation-to-the-big-five)). L'un des travaux d'un psychologue de la personnalité est de regarder de tels graphiques et de les décrire qualitativement. Vous pouvez pratiquer cet exercice dans [Guess the Factor](https://vectors.substack.com/p/guess-the-factor), ou le faire ci-dessous. Comment résumeriez-vous le Facteur 1 ?

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!N5Ou!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3c50c0d0-6e09-4758-bfad-6c9135f154af_1423x891.png)Les facteurs 1 et 2 sont produits à l'aide de [PCA](https://builtin.com/data-science/step-step-explanation-principal-component-analysis), une méthode pour distiller l'information de la personnalité sur le plus petit nombre d'axes. Pour plus d'informations sur la façon d'obtenir cela à partir de vecteurs de mots, voir mon article [Deep Lexical Hypothesis](https://arxiv.org/abs/2203.02092). Vous pouvez également reproduire ce résultat (et bien plus encore) en utilisant mon [code](https://colab.research.google.com/drive/1SXZNVqH0m_Bnd2hvIJFYiKQvHWpGu8ZM?usp=sharing), qui s'exécute gratuitement sur Google Colab.

D'un point de vue statistique, le Facteur 1 s'est déshabillé et agite un grand drapeau "Je suis de loin le plus important", comme je l'explique dans le [Facteur Principal de la Personnalité](https://vectors.substack.com/p/primary-factor-of-personality-part) (PFP). Qualitativement, il est essentiellement "ce que la société attend de vous". Soyez prévenant et respectueux, ne soyez pas snob ou non coopératif.

Pour abstraire le PFP (Facteur 1) d'une autre manière, il est utile de remonter 2 000 ans en arrière. Les Israélites avaient des bibliothèques consacrées aux règles sociales et à leur application correcte. Avec des siècles de débat et d'interprétation, la lettre de la loi s'est multipliée. Mais il y avait aussi un mouvement pour distiller l'esprit de la loi.

Selon le récit traditionnel, un potentiel converti a approché le rabbin Shammaï et lui a demandé d'expliquer toute la Torah en se tenant sur un pied. Le rabbin Shammaï, connu pour son strict respect de la loi juive, a trouvé la question irrespectueuse et a repoussé le converti, le rejetant.

Indemne, le converti a ensuite approché le rabbin Hillel avec la même demande. Hillel, renommé pour sa compassion et sa sagesse, a répondu d'une manière différente. Au lieu de rejeter le converti, Hillel a accepté le défi et a fourni un résumé concis de la Torah en se tenant sur un pied. Il a dit : "Ce qui est odieux pour toi, ne le fais pas à ton prochain : c'est toute la Torah ; le reste est le commentaire."

C'est aussi une excellente description du PFP. Il faut être capable de se mettre à la place de l'autre pour être prévenant ou rejeter l'intolérance. Darwin, il s'avère, a résumé notre instinct social de la même manière dans _La descendance de l'homme_ :

Le sens moral offre peut-être la meilleure et la plus haute distinction entre l'homme et les animaux inférieurs ;... les instincts sociaux,—le principe premier de la constitution morale de l'homme (50. 'Les pensées de Marc Aurèle,' etc., p. 139.)—avec l'aide de puissances intellectuelles actives et des effets de l'habitude, conduisent naturellement à la règle d'or, "Comme vous voudriez que les hommes vous fassent, faites-leur de même"; et cela est à la base de la moralité.

## Le commérage comme paysage de fitness

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!urUr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6938214c-6388-43e0-8a75-44821ce23845_1024x1024.png)Cartographier l'esprit

J'ai utilisé le ML pour distiller les facteurs de personnalité à partir d'adjectifs forgés à travers des éons de commérages. En fait, juger les autres est profondément lié à notre évolution. Encore une fois de Darwin dans _La descendance de l'homme_ :

_Après que le pouvoir du langage ait été acquis, et que les souhaits de la communauté puissent être exprimés, l'opinion commune sur la façon dont chaque membre devrait agir pour le bien public deviendrait naturellement dans une mesure primordiale le guide de l'action._

Sur la savane, votre réputation est votre vie. Si les autres vous trouvent paresseux ou cruel, il y a de fortes chances que vous ayez moins de descendants survivants. Le premier facteur de personnalité reflète cela, étant défini par des mots tels que _prévenant_ et _agréable_ contre _non coopératif_ et _intolérant_[^2]. **En construisant une carte de la personnalité, j'ai également construit une carte de la fitness**. Mais vous n'avez pas à me croire sur parole. Faites défiler vers le haut et regardez le Facteur 1. Le résumeriez-vous avec quelque chose comme la Règle d'Or ? Ce n'est pas un accident si cela revient sans cesse, car il est maintenu en place par la théorie des jeux et appliqué via le commérage.

Au cours des 200 dernières années, l'idée de Darwin a été développée. Considérez le livre de 2020 [Survival of the Friendliest: Understanding Our Origins and Rediscovering Our Common Humanity](https://www.amazon.com/Survival-Friendliest-Understanding-Rediscovering-Humanity/dp/0399590668). La couverture lit :

> _Pendant la majeure partie des quelque 300 000 ans que Homo sapiens a existé, nous avons partagé la planète avec au moins quatre autres types d'humains. Tous étaient intelligents, forts et inventifs. Mais il y a environ 50 000 ans, Homo sapiens a fait un saut cognitif qui nous a donné un avantage sur les autres espèces. Que s'est-il passé ?
>
> Depuis que Charles Darwin a écrit sur la "fitness évolutive", l'idée de fitness a été confondue avec la force physique, la brillance tactique et l'agression. En fait, ce qui nous a rendus évolutivement aptes était une sorte remarquable d'amitié, une capacité virtuose à coordonner et à communiquer avec les autres qui nous a permis de réaliser toutes les merveilles culturelles et techniques de l'histoire humaine. Avançant ce qu'ils appellent la "théorie de l'auto-domestication", Brian Hare, professeur au département d'anthropologie évolutive et au Centre de neurosciences cognitives de l'Université Duke et sa femme, Vanessa Woods, scientifique de recherche et journaliste primée, éclairent le saut mystérieux dans la cognition humaine qui a permis à Homo sapiens de prospérer._

Le livre lui-même clarifie que, pour Darwin, la fitness incluait la coopération ; il repousse les darwinistes, qui assimilent la fitness à la cruauté. (Pour plus d'informations, voir [l'interview](https://insitome.libsyn.com/brian-hare-and-survival-of-the-friendliest-understanding-our-origins-and-rediscovering-our-common-humanity) avec Brian Hare.) J'étais assez sûr que le premier facteur que j'ai trouvé avait à voir avec ce processus. D'où la suggestion d'une revendication supplémentaire à l'[hypothèse lexicale de Galton](https://www.experimental-history.com/p/how-to-keep-cakes-moist-and-cause) dans [Conséquences de la conscience](https://vectors.substack.com/p/consequences-of-conscience) :

3. **Le facteur latent principal représente la direction de la sélection sociale qui nous a rendus humains.**

Pour comprendre la structure de la personnalité, je l'ai reliée à d'autres concepts avec lesquels j'étais familier. Les plus importants étaient la Règle d'Or et l'auto-domestication humaine.

## Le saut de foi

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!eHWy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1975779f-d059-4ec4-8845-6ca8d1c618af_800x553.jpeg) **Domenichino:[L'Expulsion d'Adam et Ève](https://www.wikidata.org/wiki/Q77880823)**

Maintenant, tout ce que j'avais était la carte de fitness qui disait que la Règle d'Or était primordiale. Qu'est-ce que notre psychologie pourrait-elle avoir causé à évoluer ? Une conscience semble être un pari assez évident. Peut-être que cela avait à voir avec l'évolution de notre voix intérieure. Disons que la première voix intérieure disait " _partage ta nourriture !_ "; à quoi ressemblerait-il de s'identifier pour la première fois à cette voix intérieure ? Eh bien, je pense que ce serait beaucoup comme la Genèse, et c'est le noyau que je poursuis depuis. Certainement, c'était un saut. L'évolution de la voix intérieure ne suit pas nécessairement de la Règle d'Or, ni notre identification avec elle ne produit nécessairement une vie intérieure. Mais les deux semblaient plausibles et, à mesure que j'étudiais davantage, ils s'intégraient très bien dans notre chronologie évolutive.

Quant à la Genèse, trois choses m'ont immédiatement frappé comme plausibles : se sentir abandonné par Dieu, inventer l'agriculture et les femmes menant la voie. (La possibilité d'un [rituel de venin de serpent](https://vectors.substack.com/p/the-snake-cult-of-consciousness) n'est venue qu'après avoir lu d'autres récits de création.)

### Abandonné par Dieu

Au départ, je ne me préoccupais que de l'origine de la voix intérieure. Ma conception était que le soi absorbait en quelque sorte une voix morale interne. Cela, je pensais, ressemblerait beaucoup à l'obtention de la "connaissance du bien et du mal" alors que vous preniez le rôle de l'esprit tutélaire halluciné. (Un esprit que j'avais supposé dès le départ avec l'expérience de pensée.) Si vous étiez habitué à externaliser les décisions morales, prendre les rênes aurait ressemblé à quitter un état enfantin où vous communiquiez directement avec Dieu.

Avec un peu plus de lecture, j'ai réalisé que ce moment de conscience de soi était suffisant pour produire un "je" en premier lieu. Je fais cet argument dans [Déjà-vous, la construction récursive du soi](https://vectors.substack.com/p/deja-you-the-recursive-construction). Cela aurait été la création—ou plutôt la découverte—de la condition humaine d'une manière très réelle.

### Inventer l'agriculture

Dans la Genèse, l'agriculture est une conséquence de la condition humaine. La découverte du "je", il s'avère, est également suffisante pour expliquer la Révolution agricole. Car c'est probablement un [package deal avec la récursivité](https://vectors.substack.com/p/deja-you-the-recursive-construction) et la capacité de penser de manière flexible à l'avenir. Un changement de phase général dans nos capacités de planification.

Si vous croyez que les humains sont sapients depuis 200 000 ans, alors il est un grand mystère pourquoi ils auraient inventé l'agriculture 11 fois indépendamment au cours des 10 000 dernières années. C'est beaucoup à entasser dans 10% de notre existence. Et, si vous pensez que votre théorie particulière peut l'expliquer, veuillez lire [cette revue](https://www.pnas.org/doi/abs/10.1073/pnas.1323964111) où 25 chercheurs se réunissent et conviennent qu'ils ne peuvent pas s'accorder sur ce qui a causé le changement.

### Les femmes mènent la voie

Le vecteur de mot pour "féminin" corrèle avec le PFP. Même avant de contempler une connexion à la Genèse, j'ai conçu la première personne à s'identifier à sa voix intérieure comme une femme. (Comme vous pouvez le constater, je suis un vrai croyant en ce que ces vecteurs de mots peuvent nous dire.)

La Genèse est une histoire complexe. Obtenir l'agence est assimilé à devenir comme des dieux et est un péché digne de mort. Mais cela fait aussi partie du plan. Le christianisme ajoute une autre clé, où nous sommes instruits de surmonter le péché originel et de devenir comme Dieu lui-même, prenant la croix pour vivre la vie éternelle (encore une fois mélangeant vie et mort).

De même, Ève initie la mort mais reçoit le titre de Mère de tous les vivants. De nos jours, considérez combien d'efforts sont déployés pour représenter les femmes comme des agents dans les films. Et pourtant, il y a des milliers d'années, Ève est clairement peinte comme l'agent qui arrache l'humanité à son état d'innocence. Adam suit. La curiosité d'Ève est dépeinte comme une mauvaise chose, mais c'est toujours un ajout intéressant à un texte aussi patriarcal.

Conditionné à la découverte de la conscience de soi, il semble probable que l'explorateur était une femme. Conditionné à la découverte faite par les femmes, il semble probable qu'Adam et Ève soient un souvenir. Ce sont, bien sûr, d'énormes si. Mais j'avais le sentiment qu'ils étaient possibles. Et assez de volonté pour enquêter.

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!9mJt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67c3400e-4baf-476a-a8ad-10ad26212f62_843x403.jpeg)Déméter, Déesse de la Récolte et des Mystères d'Éleusis

### Le Paradoxe Sapient

Le but de cet article est de montrer comment mon travail en ML a conduit à l'EToC, pas de fournir des preuves. Cependant, je veux brièvement souligner pourquoi il est plausible que la conscience de soi ait été découverte et que cela soit enregistré dans les mythes. Tout simplement, la condition humaine semble être un phénomène récent. Avant 50 kya, il n'y a pas de grandes preuves de vie intérieure, de récursivité ou de toute pensée de haut niveau. Vous pourriez penser que les preuves de quelque chose d'aussi lointain ne seraient pas bonnes, mais de nombreux archéologues et anthropologues ne sont pas d'accord. Le nœud du [Paradoxe Sapient](https://en.wikipedia.org/wiki/Sapient_paradox) est que la [Modernité Comportementale](https://en.wikipedia.org/wiki/Behavioral_modernity) est régionale avant 10 kya. C'est très récent ! Et s'il y a eu un changement fondamental dans notre psychologie après la sortie d'Afrique, sa diffusion doit avoir été largement mématique plutôt que génétique. La découverte et la propagation de la conscience de soi suivent (ou sont au moins impliquées par) ces contraintes.

C'est une idée fantastique que la condition humaine puisse être récente. Mais c'est aussi une [idée fantastique que la psychologie moderne était pleinement en place il y a 200 kya](https://vectors.substack.com/i/114632067/years-ago) et est restée en jachère pendant des dizaines de milliers d'années avant que nous ne l'appliquions enfin et conquérions le monde. La théorie Ève de la conscience résout le problème de la diffusion en permettant qu'elle soit mématique plutôt que simplement génétique. Des changements fondamentaux auraient pu se produire après notre sortie d'Afrique.

## Vérité non corrélée

Je crois que le PFP est mieux décrit comme la tendance de chacun à vivre la Règle d'Or, la même dimension latente vue par Hillel et Darwin. C'est une vue idiosyncratique au sein de la communauté psychométrique. Pour contraste, considérez l'article bien accueilli [Two, five, six, eight (thousand): Time to end the dimension reduction debate!](https://psycnet.apa.org/record/2020-64387-036)

> _Les analyses lexicales et les méthodes de réduction de dimension sont des outils pour explorer les contours approximatifs de l'espace de personnalité. Nous ne devrions pas, cependant, nous illusionner en pensant que nous découpons la nature à ses articulations pour découvrir une "véritable" structure de la personnalité._

Essentiellement, l'argument est que toute rotation des données est acceptable parce que nous ne pouvons pas sonder la structure pour des aperçus fondamentaux. Mais, selon le prétraitement, 80% de toutes les informations de personnalité sont contenues dans le premier facteur. Cela doit sûrement nous dire quelque chose ! Et pourtant, encore, les chercheurs [croient largement que ce facteur n'est pas du tout un signal de personnalité](https://vectors.substack.com/i/61936908/enter-gfp). Un [article de 2013](https://sci-hub.se/10.1016/j.paid.2013.03.002) ouvre _"Le point de vue dominant écrasant du GFP [le premier facteur] est qu'il représente un artefact dû soit à un biais évaluatif soit à une réponse de manière socialement désirable". (_ Je noterais que même en croyant que ce facteur est entièrement biaisé [les psychométriciens ont distribué le facteur 1 aux facteurs 3-5](https://vectors.substack.com/i/61936908/relation-to-the-big-five) pour construire la Conscienciosité, la Stabilité Émotionnelle et l'Ouverture à l'Expérience.)

Avec des vues comme celle-ci, on ne peut pas connecter les données lexicales à l'évolution ou commencer à émettre des hypothèses sur le processus d'auto-domestication. Écrire ma thèse a nécessité de passer de nombreuses heures à regarder ces facteurs[^3]. Tout au long, je pensais qu'ils représentaient un paysage de fitness, et je me demandais parfois ce que cela causerait. En tant qu'ingénieur, j'étais délicieusement ignorant du point de vue dominant selon lequel la structure n'avait pas vraiment d'importance. Je suis entré assez délirant pour essayer de découper la nature à ses articulations.

## Conclusion

J'espère que cela clarifie pourquoi un ingénieur électricien écrit sur la mythologie et la conscience. L'idée m'a trouvé, vraiment. Je faisais une carte de la personnalité et elle s'est avérée être une carte de l'évolution. Les connexions à la Règle d'Or ont suggéré une proto-conscience comme mécanisme d'auto-domestication. C'était mon premier saut. J'ai ensuite spéculé que la voix intérieure pourrait être impliquée. À quoi ressemblerait-il de réaliser pour la première fois que la voix intérieure était "je" ? La Genèse m'a frappé comme un coup de maître[^4]. De plus, de nombreux experts ont soutenu que la psychologie humaine a changé au cours des 50 000 dernières années, invoquant souvent le langage, la religion ou l'auto-domestication comme cruciaux pour ce changement. À ces échelles de temps, il est possible qu'une histoire aussi importante puisse être préservée dans le mythe. " _Au commencement était le Verbe, et le Verbe était avec Dieu, et le Verbe était Dieu_ " … ou—et ne prenez pas cela comme un blasphème—peut-être que c'était la voix intérieure.

Étant donné la récente apparition de la Modernité Comportementale, ma contention est que les mythes de création peuvent inspirer des [modèles formels](https://vectors.substack.com/p/eve-theory-of-consciousness-v2) qui peuvent ensuite être connectés à la [philosophie](https://vectors.substack.com/p/deja-you-the-recursive-construction), à la [psychologie](https://vectors.substack.com/p/consequences-of-conscience), à la [linguistique](https://vectors.substack.com/p/the-unreasonable-effectiveness-of), à l'[archéologie](https://vectors.substack.com/i/97498400/evidence-of-anti-venom), et à la [génétique](https://vectors.substack.com/p/y-chromosome-bottleneck). Peut-être que ces modèles peuvent nous aider à comprendre les mythes également. Il est significatif pour moi qu'Ève soit devenue comme les dieux et que cela ait nécessité sa séparation de Dieu. Dans la Genèse, l'explication est qu'un Dieu souvent jaloux a exercé un jugement juste. Pour moi, cela a du sens comme une loi naturelle ; les humains et les dieux ne pouvaient pas habiter ensemble car nous avons façonné "je" à partir de leurs restes. La distance entre l'homme et la bête est alors de deux étapes : évoluer une conscience, puis la rejeter. Ou peut-être que c'est trop sombre. C'est plus que nous vivons en tension, et avons toujours le choix. Cette épiphanie a accordé [la récursivité](https://vectors.substack.com/p/deja-you-the-recursive-construction), la clé du travail éreintant de plier la nature à notre volonté. Si je devais expliquer cela d'une manière qui pourrait durer 10 000 ans, je raconterais l'histoire d'Adam et Ève[^5].

Naturellement, le voyage a commencé dans mon domaine d'expertise où j'avais une base solide. Il me semble très probable que ma carte de la personnalité enregistre les pressions évolutives. Étant donné à quel point nous avons récemment changé, et combien de temps la Règle d'Or a été une force, je vais jusqu'à ajouter un troisième postulat à l'hypothèse lexicale de Galton : **Le facteur latent principal représente la direction de la sélection qui nous a rendus humains**. De là, j'ai _fait_ des sauts mais en atterrissant je me suis retrouvé en bonne compagnie, avec des gens comme Jaynes, Jung, Pinker, Chomsky et Descartes. Ce type d'exploration est l'essence même de la science ; tout n'a pas une valeur p.

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!_K5c!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe08ec046-d650-4769-894e-fa1a77837040_1280x1847.jpeg)[Figurine d'Isis](https://en.wikipedia.org/wiki/Isis#/media/File:Isis_with_Serpent_Tail_LACMA_M.80.202.222.jpg), Déesse égyptienne de la Sagesse, deuxième siècle CE

[^1]: J'ai été surpris que Jordan Peterson décrive la dérivation des Big Five comme une forme précoce d'IA dans une interview avec Joe Rogan. J'ai fait cet argument dans le premier post de ce blog et je ne l'avais jamais entendu auparavant. Quoi que vous pensiez de sa politique, il est assez bon en psychologie de la personnalité.

[^2]: Certains peuvent noter que l'intolérance semble être un péché cardinal récent. Peut-être. Il serait intéressant de construire des vecteurs de mots sur des textes historiques et de voir comment le PC1 change. Étant donné que le facteur latent du texte moderne est un bon match pour la Règle d'Or, je suppose qu'il n'y aurait pas beaucoup de mouvement à partir, disons, du langage de 1900. Difficile de déplacer quelque chose soutenu par tant de théorie des jeux, même si le cercle moral s'est élargi.

[^3]: Même si les adjectifs de personnalité sont fondamentaux pour les modèles de personnalité, il est également rare que les chercheurs traitent directement avec les mots. Dans les années 90, une fois qu'il était clair que quelque chose comme les Big Five émergeait de manière cohérente, les chercheurs ont commencé à mesurer la personnalité avec des enquêtes basées sur des phrases conçues pour approximer la structure lexicale (par exemple, l'Inventaire des Big Five). (Secret commercial : le cinquième facteur Ouverture/Intellect n'est pas récupéré de manière cohérente.) C'était plus facile, et depuis lors peu de travail a été fait sur le langage. De plus, mes données étaient meilleures que les tentatives antérieures. Si vous voulez comprendre comment les mots se rapportent, utilisez un modèle de langage, pas des enquêtes auprès d'étudiants de premier cycle. Personne d'autre n'a passé autant de temps à regarder une carte de la personnalité aussi précise. (Vous pouvez pratiquer cet exercice dans Guess the Factor.)

[^4]: Considérez le fait qu'Adam a nommé les animaux alors qu'il était dans le Jardin d'Éden. Même sans conscience de soi, il y aurait eu un langage non récursif. Les chasseurs ont une connaissance encyclopédique des plantes et des animaux. Cela aurait pu être la partie la plus importante du langage avant la Chute. Étonnant si ce fait a survécu 10 000 ans.

<!-- CHUNK BREAK -->

[^5]: Je suis impressionné par la Genèse, mais c'est peut-être simplement ce que je connais le mieux. Si j'étais Indien, je parlerais probablement de Saraswati, ou si j'étais Navajo, du rôle des femmes dans le mythe de l'Émergence, ou si j'étais Égyptien, du moment où Atum s'est appelé à l'existence en prononçant son nom (et a ensuite combattu un serpent primordial). EToC exige que ce soient des perspectives différentes de la même histoire. Évidemment, cela est traditionnellement montré en construisant une phylogénie. À ces échelles de temps et avec mes compétences, ce n'est pas possible. C'est pourquoi je me concentre sur l'évolution de la récursivité. Je veux montrer qu'il est probable que les humains ont récemment acquis la récursivité et qu'elle s'est diffusée. Cela changerait radicalement notre a priori sur la question de savoir si les mythes de création partagent une racine et à quoi ressemblait cette racine.