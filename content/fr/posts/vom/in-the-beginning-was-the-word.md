---
about:
- vectors-of-mind
- blog-archive
author: Andrew Cutler
date: '2025-07-04'
description: “In the beginning was the Word, and the Word was with Psychology, and
  the Word was Psychology” ~New Vector Translation
draft: false
keywords:
- vectors-of-mind
- beginning
- word
lang: fr
lastmod: '2025-07-09'
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '51210419'
original_url: https://www.vectorsofmind.com/p/in-the-beginning-was-the-word
quality: 6
slug: in-the-beginning-was-the-word
tags: []
title: Au Commencement Était Le Verbe
translation_model: gpt-4o
---

*From [Vectors of Mind](https://www.vectorsofmind.com/p/in-the-beginning-was-the-word) - images at original.*

---

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!5qwE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9f7c2505-9587-4daa-aac2-648b8bf16efb_1200x544.png)

_"Au commencement était le Verbe, et le Verbe était avec la Psychologie, et le Verbe était la Psychologie" ~Nouvelle Traduction Vectorielle_

Tous les concepts de personnalité sont d'abord décrits par des mots. Des modèles alimentés par la cocaïne de Freud aux Big Five austères, ils sont tous à un moment donné des mots. Une grande partie de la psychologie académique s'intéresse à la comparaison des concepts. Pour ce faire, ils doivent partager une base, généralement un ensemble de sujets. Les sujets reçoivent un instrument (généralement un sondage) qui approximativement situe leur position dans l'espace des concepts. En se basant sur la covariation des réponses des sujets, des affirmations générales sont ensuite faites sur les concepts. Dans cet article, nous explorons une autre voie. Les avancées en PNL permettent une comparaison quantitative des concepts dans leur habitat naturel : le langage.

### Feuille de route

Dans le [dernier article](https://vectors.substack.com/p/the-big-five-are-word-vectors?s=w), j'ai soutenu que les Big Five sont des vecteurs de mots. Cet article fait la même affirmation concernant les échelles autonomes, ce qui permet ensuite de comparer les concepts sans impliquer de sujets. Pour démontrer cela, un modèle de personnalité large est introduit, ainsi qu'une méthode pour représenter les concepts dans l'espace des mots. Le plan suit :

 1. Comparer les concepts dans l'espace des sujets vs l'espace des mots

 2. Problèmes avec l'espace des sujets

 3. Relier l'altruisme de parenté et l'altruisme réciproque aux Big Five en utilisant des sujets

 4. La même comparaison dans l'espace des mots

 1. Introduire un modèle à cinq facteurs (temporaire) identifié en utilisant la PNL

 2. Projeter les mots d'altruisme dans cet espace

 3. Code disponible [ici](https://colab.research.google.com/drive/13DA2IKQ9zRimGedww_09iGT6ehuYriVz?usp=sharing).

 5. Discussion, limitations, travaux futurs

### **Un chemin tortueux**

Pour comparer l'altruisme avec les Big Five, le signal doit passer par de nombreuses transformations : Altruisme (idéal) → décrit par des mots → enquête développée (et espérons-le validée) pour approximer ce concept → administrée au sujet qui interprète ces mots et cherche dans son âme → score d'altruisme du sujet → **corrélation dans l'espace des sujets** ← score de l'Inventaire des Big Five (BFI) du sujet ← le sujet interprète les éléments du BFI et cherche dans son âme ← développer le BFI pour mesurer approximativement cela ← concept défini/communiqué par description qualitative ← Big Five (défini par des charges de mots). Des affirmations sont ensuite faites sur les deux idéaux, l'Altruisme et les Big Five.

### **Le droit chemin**

Pourquoi ne pas utiliser les vecteurs de mots comme base commune au lieu des sujets ? Le chemin est beaucoup plus direct : Altruisme (idéal) → décrit par des mots → vectorisé dans l'espace des mots → **comparaison dans l'espace des mots** ← Big Five, qui existent déjà dans l'espace des mots, comme discuté dans le [précédent article](https://vectors.substack.com/p/the-big-five-are-word-vectors?s=w). Pour ceux qui tiennent le score, cela fait 4 contre 10 transformations. (C'est compté comme au golf.)

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!tbb9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb8b6c50-e94e-4462-8772-78359189f70e_1600x1305.png)Les réalités statistiques visitant le domaine de la psychologie. Cela a été quelques années difficiles.

### **Tal le Révélateur**

La difficulté d'utiliser des sujets pour faire des affirmations sur des concepts verbaux n'est pas un secret.

> _"La plupart des théories et hypothèses en psychologie sont de nature verbale, mais leur évaluation repose de manière écrasante sur des procédures statistiques inférentielles. La validité du passage de l'analyse qualitative à l'analyse quantitative dépend de l'alignement étroit des expressions verbales et statistiques d'une hypothèse – c'est-à-dire que les deux doivent se référer à peu près au même ensemble d'observations hypothétiques. Ici, je soutiens que de nombreuses applications de l'inférence statistique en psychologie ne répondent pas à cette condition de base." ~Tal Yarkoni,_ La [crise de la généralisabilité](https://psyarxiv.com/jqw35/)

La validité ici se réfère à un score capturant le concept qu'il est censé mesurer. Cela vaut la peine de lire les arguments et les exemples dans leur intégralité. Mais pour nous, la leçon à retenir est ce qui peut être fait, compte tenu de ces réalités. Il suggère :

 1. Faire autre chose (entrer dans d'autres domaines).

 2. Adopter la recherche qualitative

 3. Adopter de meilleures normes (y compris 7 suggestions).

> _"On est toujours libre de prétendre que de petites valeurs p obtenues à partir d'opérationnalisations statistiques extrêmement étroites peuvent fournir une base adéquate pour des inférences verbales générales sur des concepts psychologiques complexes. Mais personne d'autre – ni ses pairs, ni ses bailleurs de fonds, ni le public, et certainement pas le dossier scientifique à long terme – n'est obligé d'honorer la mascarade."_

Même si votre vision de la recherche en psychologie n'est pas si sombre, les lecteurs ont sûrement été brûlés par des articles qui font des affirmations mais emploient des expériences qui ne sont que faiblement liées. Toutes les solutions disponibles sont douloureuses. Le domaine peut devoir adopter une vision plus étroite et laisser les grandes questions à ceux qui étudient l'histoire, la littérature et l'algèbre linéaire. Je propose une autre voie à suivre.

### **Convertir à l'espace des mots**. 4. Utiliser les vecteurs de mots comme base commune

Les concepts vivent ensemble dans l'espace des mots, et pourtant, lorsque des comparaisons sont faites, nous les traînons dans l'espace des sujets. C'est un énorme tracas, avec perte. Et s'ils pouvaient rester en sécurité dans l'espace des mots ? La prétention du traitement du langage naturel est que les mots sont des vecteurs dans un espace continu. L'analyse de ces vecteurs fonctionne suffisamment bien pour être un [processus](https://blog.google/products/search/search-language-understanding-bert/) [porteur](https://www.amazon.jobs/en/search?base_query=natural+language+processing&loc_query=&latitude=&longitude=&loc_group_id=&invalid_location=false&country=&city=&region=&county=) [de charge](https://youtu.be/SGzMElJ11Cc?t=6667) dans des industries valant des billions de dollars, et est actuellement [réintroduite](https://vectors.substack.com/p/the-big-five-are-word-vectors?s=w) en psychologie.

### **Pratiquer ce que vous prêchez**

Ici, nous examinerons une étude traditionnelle réalisée dans l'espace des sujets, puis essaierons de l'améliorer en passant à l'espace des mots. Pour éviter un homme de paille, l'objet est [Kin Altruism, Reciprocal Altruism, and the Big Five Personality Factors](https://www.sciencedirect.com/science/article/abs/pii/S1090513898000099?casa_token=05bTreOjGKUAAAAA:nLHTWhK3z45xUbN5nTVd7a3-Qaz9No22rQtVY6vpUjYpeZ1bkPy-cBig9UgRbn-GnqJScTCPpSY) qui a été cité des centaines de fois et dont le premier auteur a un indice h de 70.

Les sujets sont mesurés à l'aide de trois instruments : Big Five (via une enquête d'adjectifs), Empathie/Attachement et Pardon/Non-Rétorsion (enquête de phrases), et altruisme dans un jeu de partage d'argent. Parce que les auteurs émettent l'hypothèse que l'espace interstitiel entre l'Agréabilité et la Stabilité Émotionnelle (alias Névrosisme) différencie les deux altruisms, certains mots sont ajoutés pour mieux mesurer cette zone. De même, un nouveau questionnaire est conçu pour mesurer l'Empathie/Attachement et le Pardon/Non-Rétorsion, qui sont théorisés comme liés à l'altruisme de parenté vs réciproque. Au-delà de ce type d'étude, un jeu est utilisé pour mesurer l'altruisme.

> _"Dans la version de la tâche d'allocation d'argent utilisée pour mesurer l'altruisme de parenté, l'autre personne était décrite comme un ami proche – quelqu'un avec qui le participant avait une longue histoire d'amitié et avec qui le participant avait beaucoup en commun. Nous espérions qu'en décrivant l'amitié comme ancienne et l'ami comme quelqu'un de très similaire au participant, l'amitié ressemblerait étroitement à la relation que l'on a avec un parent. La raison pour laquelle nous n'avons pas utilisé un parent comme objet potentiel de l'altruisme était d'éviter d'introduire une variance dans les réponses en raison du parent particulier impliqué ; par exemple, de nombreuses personnes pourraient être plus disposées à se comporter de manière altruiste envers un frère ou une sœur qu'un autre."_

En d'autres termes, pour ne pas souiller les données avec des sentiments réels envers la parenté, l'altruisme réciproque est mesuré.

> _"Dans la version de la tâche d'allocation d'argent utilisée pour mesurer l'altruisme réciproque, l'autre personne était décrite comme un non-coopérateur – quelqu'un qui avait été impoli, méchant et inconsidéré envers le participant."_

Et pour mesurer l'altruisme réciproque, ils mesurent … l'altruisme non réciproqué ? Naturellement, il y a des corrélations et les auteurs concluent :

> _"Les résultats de cette étude soutiennent la suggestion que les traits de personnalité impliquant l'empathie et l'attachement facilitent l'altruisme principalement dirigé vers la parenté (c'est-à-dire l'altruisme de parenté), et que les traits de personnalité impliquant le pardon et la non-rétorsion facilitent l'altruisme principalement dirigé vers les non-parents (c'est-à-dire l'altruisme réciproque)."_

Mais si l'altruisme réciproque n'a jamais été mesuré, comment les résultats peuvent-ils soutenir cette affirmation ? Les statistiques dans les articles de psychologie sont, comme le souligne Tal, souvent une figure de style rhétorique. Mais nous n'avons pas à jouer le jeu ! Voyons ce que l'espace des mots a à dire.

### **Une terre de lait et de miel (bienvenue dans l'espace des mots)**

Dans les études traditionnelles, en raison des coûts de cartographie des sujets dans l'espace de la personnalité, la résolution ne peut être élevée que dans quelques domaines de la personnalité à la fois. C'est pourquoi les auteurs ont sondé l'Empathie et la Non-Rétorsion et l'espace entre l'Agréabilité et la Stabilité Émotionnelle. Tous ces axes [existent dans l'espace régulier des Big Five](https://psyarxiv.com/vebtm/), mais sont mesurés de manière assez granulaire. Dans l'espace des mots, nous pouvons comparer l'altruisme aux Big Five complets dans toute leur gloire haute résolution. Sur mon github, il y a 2819 vecteurs de mots factorisés en cinq CP. Nous pouvons les utiliser par commodité. La première tâche est de sélectionner des ensembles de mots qui décrivent chaque altruisme. Pour les mots de parenté, j'ai choisi ceux qui incarnent les rôles familiaux : _fraternel, sororal, maternel, maternel, paternel, grand-maternel, grand-paternel, conjugal, maternel, paternel._ Pour l'altruisme réciproque, je suis la définition de Trivers.

> _"En ce qui concerne l'altruisme réciproque humain, il est montré que les détails du système psychologique qui régule cet altruisme peuvent être expliqués par le modèle. Plus précisément, **l'amitié, l'antipathie, l'agression moralisatrice, la gratitude, la sympathie, la confiance, la suspicion, la fiabilité, certains aspects de la culpabilité, et certaines formes de malhonnêteté et d'hypocrisie** peuvent être expliqués comme des adaptations importantes pour réguler le système altruiste. Chaque humain individuel est vu comme possédant des tendances altruistes et trompeuses, dont l'expression est sensible aux variables de développement qui ont été sélectionnées pour équilibrer les tendances de manière appropriée à l'environnement social et écologique local." _[L'Évolution de l'Altruisme Réciproque](https://www.journals.uchicago.edu/doi/abs/10.1086/406755), Robert Trivers (mise en gras ajoutée)

En considérant cela, j'ai choisi : _discriminant, impitoyable, vengeur, loyal, voisin, coopératif, digne de confiance,_ et _équitable._ Cela est à peu près égal en penchant vers la coopération mais en suivant avec une agression moralisatrice lorsque les choses tournent mal. De plus, il essaie de capturer cet altruisme comme l'antithèse de la tricherie (par exemple, _équitable, digne de confiance_).

(Pour une excellente explication de l'évolution de la confiance, voir [cette](https://ncase.me/trust/) démo interactive.)

#### Puis-je vous présenter le modèle des cinq facteurs inconnus ?

Théoriquement, nous pourrions utiliser les charges de mots des Big Five produites via des enquêtes, mais la plupart de ces mots sont suffisamment rares pour ne pas être inclus. C'est pour le mieux car on n'obtiendrait pas une bonne estimation de _grand-maternel_ par auto-évaluation parmi les étudiants en psychologie. En tant que tel, les vecteurs de mots sont calculés en utilisant le modèle de langage RoBERTa. Dérivés d'une liste de mots de personnalité large et [bien caractérisée](https://openpsychologydata.metajnl.com/articles/10.5334/jopd.57/), les cinq facteurs résultants sont, en bref :

 1. Affiliation (ou Socialisation). À quel point voulez-vous cette personne dans votre équipe ? Semblable à l'Agréabilité mais exclut d'être une carpette. _Crédule_, par exemple, charge de manière neutre sur l'Affiliation mais positivement sur l'Agréabilité.

 2. Dynamisme. Assez proche de l'Extraversion, mais plus sur un sens de l'aventure, et moins sur la confiance.

 3. Ordre. Conscienciosité avec un tranchant. Capacité à atteindre ses propres objectifs. _Exigeant_ vs _mou_.

 4. Attachement Émotionnel. Alors que le Névrosisme concerne l'instabilité, il s'agit d'attachement ; à la fois _attentionné_ et _rancunier_ sont fortement chargés.

 5. Transcendance. Ce facteur est caractérisé par _unique, compliqué, maudit, handicapé, mystique, au cœur brisé, d'un autre monde_ vs. _non philosophique, insouciant, entêté, grossier, matérialiste, égocentrique, désinvolte_. Il implique de regarder au-delà de soi-même et du banal. Ce processus est, apparemment, lié à la douleur. En fait, "troublé" charge plus sur Transcendant que sur Attachement Émotionnel (le facteur lié au Névrosisme).

Les noms des trois premiers facteurs sont empruntés au travail [pan culturel](https://journals.sagepub.com/doi/10.1002/per.1953) de De Raad car, qualitativement, la correspondance est plus proche qu'avec les Big Five. Chaque facteur mérite son propre article. (Pour ceux en psychologie industrielle, je soupçonne que l'Ordre est plus corrélé avec le succès en affaires que la Conscienciosité car il est plus calculateur que d'arriver à l'heure.) Mais proposer des modèles n'est pas mon fort, et des études linguistiques plus fines sont à venir qui pourraient donner une structure différente. Pour l'instant, ces facteurs suffisent. Voici leur corrélation avec les Big Five :

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!Sxlw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F63c86f00-e0cc-4854-bd8a-e6ba3fc55449_366x374.png)

#### Résultats

Charges des mots d'altruisme sur les quatre premiers facteurs (la Transcendance n'est pas importante dans cette étude) :

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!Q5sr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4efdfb85-197d-4d57-8a8b-3675eaf2b162_955x735.png)C'est prosocial d'avoir des liens familiaux forts (haute Affiliation), si un peu ennuyeux (Dynamisme neutre à bas). Tous les mots se mappent à un endroit similaire.

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!f7oe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb08b529e-7443-4f5b-af1e-ce080e36a4b7_961x735.png)Les mots familiaux chargent fortement sur l'attachement émotionnel. Remarquez que les relations parentales et grand-parentales sont assez genrées. Les hommes sont moins attachés, comme le prédit la [théorie de l'investissement parental](http://joelvelasco.net/teaching/3330/trivers72-parentalinvestment.pdf) de Trivers, et les [statistiques](https://www.pewresearch.org/social-trends/2013/07/02/the-rise-of-single-fathers/) le confirment. Les frères et sœurs, cependant, sont également attachés, et à un degré moindre que les parents. En y réfléchissant, _conjugal_ n'aurait pas dû être inclus dans l'altruisme concernant les parents de sang. En accord avec les [émissions de talk-show de jour](https://www.youtube.com/watch?v=jXZB0FeTyE8), il charge moins sur l'attachement que maternel ou grand-maternel.

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!FYnd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa40e5562-577f-4b55-bd16-d34ccec1c388_955x735.png)Les mots réciproques essaient de capturer le comportement idéal du donnant-donnant lorsqu'un partenaire coopère ou triche. En tant que tels, ces mots sont beaucoup plus dispersés, bien que toujours principalement positifs. Même 'discriminant' est légèrement positif, ce qui signifie que je ne pense pas que le mot soit codé comme quelque chose comme 'discriminatoire racialement' – parfois ces modèles de langage se confondent avec une similarité phonétique (par exemple, excentrique et ethnocentrique).

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!lGox!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6eb4b7d2-4728-4f66-83ce-cd95e2346144_961x735.png)La coopération et la convivialité impliquent légèrement que ses propres objectifs passent au second plan. Impitoyable et discriminant sont pour ceux qui veulent dire affaires.

Pour comparer les altruisms, nous aimerions réduire chacun de ces ensembles de mots à un seul vecteur. (Il y a place à débat si cela a même du sens étant donné que le réciproque – et dans une moindre mesure le parent – nécessite des réponses différentes à différents scénarios.) La solution bon marché et sale est de traiter chaque concept comme un [Sac de Mots](https://en.wikipedia.org/wiki/Bag-of-words_model) et de prendre la moyenne. Les charges moyennes sont :

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!TMN7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe3aaf685-9bb3-4dbf-974f-0ab994f40a88_356x238.png)Ceux-ci sont normalisés par rapport à tous les 2819 mots. En moyenne, les mots de parenté sont de 1 à 1,5 écart-type sur à la fois l'Affiliation et l'Attachement Émotionnel.

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!mDHG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fba83d4f1-2f47-42e8-a158-368c7681a2db_356x238.png)L'altruisme réciproque implique également l'Ordre, accomplir ses propres objectifs.

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!48eW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd912d107-48f4-4d5e-bb23-fe24dd932b78_356x238.png)Différence : Charges de parenté moins réciproques. Dominé par l'Ordre.

### **Discussion**

Je ne pense pas que l'article dans l'espace des sujets inclut une mesure valide de l'altruisme de parenté ou réciproque et, en tant que tel, n'ajoute pas à notre compréhension de la façon dont il se rapporte à la personnalité. C'est un mode d'échec étonnamment courant. L'espace des mots offre une certaine assurance contre les comparaisons invalides. Nous avons une meilleure intuition de l'endroit où un mot devrait être dans l'espace des mots, que de la façon dont le sujet 112 devrait répondre à une enquête. Il est plus facile de repérer les erreurs.

D'un point de vue bayésien, quelque chose de différent se passe dans l'espace des sujets par rapport à l'espace des mots. Les expériences incluant des sujets cherchent à apporter de nouvelles informations à la table. L'espoir est que cela mettra à jour la vision du monde des lecteurs. Mais les chercheurs (et les profanes) ont beaucoup d'expérience sociale et une perception plus aiguë des processus psychologiques que l'instantané fourni par une enquête. Il est difficile de déplacer beaucoup l'aiguille. L'espace des mots est plus proche de la visualisation de nos a priori que de la production de nouvelles connaissances. Cette vue est précieuse car le langage est là où le caoutchouc rencontre la route, pour ainsi dire. Comme JL Austin l'a dit :

> _"Notre stock commun de mots incarne toutes les distinctions que les hommes ont jugé bon de faire, et les connexions qu'ils ont jugé bon de marquer, au cours de la vie de nombreuses générations : celles-ci sont sûrement plus nombreuses, plus solides, car elles ont résisté à l'épreuve du temps de la survie du plus apte, et plus subtiles, du moins dans toutes les affaires pratiques ordinaires et raisonnables, que celles que vous ou moi sommes susceptibles de concevoir dans notre fauteuil un après-midi – la méthode alternative la plus favorite." [A plea for excuses](https://sites.ualberta.ca/~francisp/NewPhil448/AustinPlea56.pdf)_

L'analyse dans l'espace des mots est relativement simple. Plutôt que des tableaux de corrélations et de valeurs p, les mots sont simplement tracés sur les axes d'intérêt et des jugements visuels sont faits. Les mots d'altruisme de parenté se regroupent étroitement sur à la fois l'Affiliation et l'Attachement Émotionnel, les deux seuls facteurs avec des charges considérables. Les pères, mais pas les frères, sont moins attachés que leurs homologues féminins, en ligne avec la théorie de l'investissement parental de Trivers. Les frères et sœurs ont autant de raisons de s'occuper de leurs frères et sœurs. Les pères, cependant, ont moins de raisons que les mères. Le sperme est bon marché. Les œufs et la grossesse sont coûteux.

Les mots réciproques sont plus dispersés, reflétant des traits idéaux pour répondre à différents scénarios : coopération ou défection du partenaire. La différence la plus saillante est une charge moyenne plus élevée sur l'Ordre – accomplir ses propres objectifs. Initialement appelé _altruisme à retour différé_, l'altruisme réciproque ne consiste pas à se sacrifier pour un étranger mais plutôt à investir dans son propre avenir par des moyens prosociaux. D'autre part, l'altruisme de parenté se réfère à aider la famille même à ses propres frais en raison des gènes égoïstes qui tirent sur vos cordes sensibles. Cela est apparent dans les charges plus élevées des mots d'altruisme de parenté sur l'Attachement Émotionnel, soutenant l'hypothèse d'Ashton. Mais l'action principale est sur l'Ordre, loin de l'endroit où les instruments de l'espace des sujets ont été conçus pour détecter. Les coûts de l'échantillonnage dans l'espace des sujets rendent les résultats plus dépendants des a priori des chercheurs.

Interpréter ces graphiques peut donner l'impression de lire dans les feuilles de thé, mais je suis environ 70% sûr de ce qui est ici. Une chose qui me fait hésiter est que les deux altruisms sont représentés de différentes manières. Les mots de parenté décrivent tous des relations (par exemple, _mère, père, frère_), tandis que les mots réciproques sont un mélange de relations (par exemple, _voisin_) et de traits adaptés aux jeux à somme positive répétés (par exemple, _vengeur, discriminant, coopératif_). Incertitude mise à part, ne serait-il pas cool que dans un après-midi, je mène une expérience qui combine l'expérience vécue de l'altruisme de millions de personnes ? Ce que les générations ont convenu fait de quelqu'un de paternel, sororal ou voisin. Comme toujours avec une nouvelle source de signal, on commence à tirer à l'aveuglette. Finalement, le Far West est apprivoisé ; des méthodes et des heuristiques émergent. Il y a beaucoup de place pour l'amélioration. Les lecteurs peuvent ajuster les ensembles de mots et obtenir de nouveaux résultats en quelques minutes en utilisant ce [carnet colab](https://colab.research.google.com/drive/13DA2IKQ9zRimGedww_09iGT6ehuYriVz?usp=sharing). Veuillez le faire !

#### Avantages de l'espace des mots

 1. Connecté à l'Hypothèse Lexicale. Ancré dans la réalité sociale décentralisée.

 2. Moins de transformations. Chaque étape est avec perte et introduit un biais.

 3. Moins intensif en statistiques après la conversion à l'espace des mots. (Barrière à l'entrée plus basse.)

 4. La taille effective de l'échantillon (ceux qui ont contribué au modèle de langage via des commentaires sur reddit, l'écriture de livres ou des articles pubMed) est beaucoup plus grande et diversifiée que la plupart des études.

 5. Meilleures perspectives d'emploi pour les doctorants en psychologie qui connaissent la PNL.

 6. Plus facile de faire du travail multilingue/multiculturel. Certains modèles sont entraînés sur 100 langues simultanément (c'est ainsi que Meta entraîne les [filtres de discours de haine](https://ai.facebook.com/blog/how-ai-is-getting-better-at-detecting-hate-speech/) dans des langues avec peu d'exemples).

 7. Les modèles de langage [continuent](https://openai.com/blog/introducing-text-and-code-embeddings/) [de s'améliorer](https://say-can.github.io).

 8. Science ouverte.

 9. [Éviter le CER](https://slatestarcodex.com/2017/08/29/my-irb-nightmare/).

#### Inconvénients

 1. Plus de pièces mobiles. Il y a des milliards de paramètres dans un modèle de langage ! Cependant, même des milliards de neurones et des dizaines de décisions d'entraînement peuvent aboutir à une représentation stable. Tout modèle de langage digne de ce nom peut compléter l'analogie "mari est à femme ce que roi est à ____".

 2. Impossible de décomposer les résultats par démographie. Parfois, il est intéressant de connaître la personnalité des enseignants du primaire entre 25 et 30 ans. Ou de savoir comment un certain concept corrèle avec le casier judiciaire. Impossible dans l'espace des mots.

 3. Les modèles de langage ne sont-ils pas biaisés ? Eh bien, pas plus que l'auto-évaluation.

 4. Définir l'altruisme comme la somme d'un tas de vecteurs de mots (c'est-à-dire, un sac de mots) est un peu bricolé. Il y a une marge substantielle d'amélioration ici.

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!ctzj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F455fdb70-3c84-4dfe-81bf-6bf6e676fd44_1600x1128.jpeg)Les psychologues heureux avec encore 40 ans à errer dans l'espace des sujets.

### **Dieux étrangers**

_"Je pense que Kafka avait raison quand il a dit que, pour un homme moderne, la bureaucratie d'État est le seul contact restant avec la dimension du divin."_ ~Zizek, A Pervert's Guide to Ideology

Il décrit ici, bien sûr, le sentiment transcendant de déposer un appel auprès du CER. J'ai une prédiction. L'espace des mots est la bonne chose à faire d'un point de vue du traitement du signal, mais son adoption sera autant motivée par la commodité de ne pas être réglementé. Le corollaire est que le CER sera le premier organisme gouvernemental à déclarer les modèles de langage sentients.

<!-- CHUNK BREAK -->

[*[Image : Contenu visuel du post original]*](https://substackcdn.com/image/fetch/$s_!6nGN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fedfc8bac-cf78-40f9-88d3-9a30066ff108_817x1600.jpeg)John répandant la bonne parole spatiale

### **Préparer le chemin**

Nous souhaitons extraire des relations entre des constructions à partir de modèles de langage. Pour le faire de manière à ajouter du signal plutôt que du bruit, un travail de validation considérable est nécessaire. Initialement, cela signifie comparer avec des résultats d'enquêtes bien établis. Peuvent-ils être récupérés en utilisant des vecteurs de mots ? Où échouent-ils ? Une fois cela établi, chaque article qui se termine par "plus de recherches nécessaires" devrait trouver un moyen de poser la question dans l'espace des mots.

J'ai passé plus d'un an à peaufiner une [méthode](https://psyarxiv.com/gdm5v/) pour extraire des relations de personnalité à partir de [RoBERTa](https://arxiv.org/abs/1907.11692), le modèle à la pointe de la technologie à l'époque. Peu de temps après, GPT-3 a été publié et il a mieux performé dès le départ. Que le calcul surpasse la connaissance du domaine est une [leçon amère](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) récurrente dans l'IA. Le calcul augmente de manière exponentielle. Si vous pouvez obtenir des gains de 30 % par rapport à une solution ML générale en utilisant la connaissance du domaine, vous pouvez également simplement attendre que [le calcul rattrape](https://twitter.com/russelljkaplan/status/1513128016452337667) et obtenir les mêmes résultats en utilisant des méthodes générales. Trouver des moyens de relier les questions de psychologie aux modèles NLP prêts à l'emploi est donc une bonne voie à suivre. Un nouveau modèle avec des performances nettement meilleures est rendu public tous les six mois environ. Ceux qui valident l'espace des mots préparent le chemin pour des intelligences supérieures—[PaLM](https://ai.googleblog.com/2022/04/pathways-language-model-palm-scaling-to.html), GPT-7, OSCar (**O**ptimal **S**entience **Car**tography)—pour faire pleuvoir des vérités psychologiques.

Le langage naturel regorge de théories partagées sur le monde. Maintenant que nous pouvons les quantifier, ne peuvent-elles pas être utilisées comme preuves ?

Si vous trouvez cela intéressant, veuillez partager !

[Partager](https://www.vectorsofmind.com/p/in-the-beginning-was-the-word?action=share)