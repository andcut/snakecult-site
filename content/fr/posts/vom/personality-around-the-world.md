---
about:
- vecteurs-de-l'esprit
- archive-du-blog
author: Andrew Cutler
date: '2025-07-04'
description: D'accord, prenons un petit répit des affaires de sapience. J'avais en
  fait une série de psychométriques en attente avant d'être attiré par l'appel claironnant
  de la conscience. C'est juste si difficile de détourner le regard...
draft: false
keywords:
- vecteurs-de-l'esprit
- personnalité
- autour
- monde
lang: fr
lastmod: '2025-07-09'
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '108601152'
original_url: https://www.vectorsofmind.com/p/personality-around-the-world
quality: 6
slug: personality-around-the-world
tags: []
title: La personnalité à travers le monde
translation_model: gpt-4o
---

*From [Vectors of Mind](https://www.vectorsofmind.com/p/personality-around-the-world) - images at original.*

---

D'accord, prenons une petite pause des sujets de sapience. J'avais en fait une série de psychométrie prête avant d'être attiré par l'appel claironnant de la conscience. C'est juste si difficile de détourner le regard.

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!X2nA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F62106fb3-6e73-444d-96f1-07b95ec828f9_1024x506.jpeg)[Ulysse et les Sirènes](https://en.wikipedia.org/wiki/Ulysses_and_the_Sirens_\(Waterhouse\)), peinture de [John William Waterhouse](https://en.wikipedia.org/wiki/John_William_Waterhouse)

J'ai commencé ce blog pour explorer l'Hypothèse Lexicale d'un point de vue d'apprentissage automatique. Les modèles de personnalité définissent les traits les plus discutés dans une langue, et nous pouvons mesurer cela beaucoup mieux à l'ère de GPT. Les modèles de personnalité dérivés soit de vecteurs de mots soit d'enquêtes traditionnelles reviennent aux mêmes quelques traits, en particulier les Deux Grands : l'autorégulation sociale et le dynamisme. Pour un rappel à ce sujet, consultez [Les Cinq Grands sont des Vecteurs de Mots](https://vectors.substack.com/p/the-big-five-are-word-vectors) et [Le Facteur Principal de la Personnalité](https://vectors.substack.com/p/primary-factor-of-personality-part).

Les Cinq Grands ont été trouvés dans de nombreuses langues indépendamment, mais la comparaison entre les langues est toujours qualitative. Les chercheurs administrent une enquête d'adjectifs de personnalité en turc ou en allemand, la factorisent, et examinent les facteurs pour voir s'ils sont les mêmes. Ces données ne peuvent pas être utilisées pour dire "L'Extraversion est décalée de 15 degrés par rapport à la Conscience en allemand par rapport à l'anglais." Pour être si précis, les deux langues devraient partager une certaine base.

Si vous administrez des questions dans plusieurs langues, vous pouvez les relier en 1) trouvant un groupe bilingue qui peut répondre dans les deux langues ou 2) en supposant que les traductions des mots sont 1:1 (par exemple, _fun_ est parfaitement équivalent à _divertido_ en espagnol). Dans le premier cas, il y a un fort effet de sélection. Et si les personnes bilingues avaient tendance à être mieux éduquées ? Le second n'est tout simplement pas vrai. En fait, la raison de factoriser les langues ensemble est de comprendre comment la structure de la personnalité peut diverger entre elles. Supposer que les mots sont les mêmes va à l'encontre du but.

**[Ma recherche](https://arxiv.org/abs/2203.02092) a montré que vous pouvez extraire la structure de la personnalité à partir de modèles de langage en anglais. Une question naturelle est de savoir comment cela change lorsque vous ajoutez d'autres langues.** Avec des modèles entraînés sur des dizaines de langues, cela devient plutôt facile à explorer. Vous pouvez mapper n'importe quel nombre de langues sur la même base.

## Les Deux Grands, encore une fois

J'ai utilisé [XLM-RoBERTa](https://huggingface.co/xlm-roberta-base) pour attribuer une similarité entre les adjectifs de personnalité. Étrangement, ce modèle est le résultat du génocide au Myanmar. Meta se trouve dans la position peu enviable où ils doivent supprimer du contenu dans des endroits qu'ils comprennent très peu. Techniquement, c'est ce qu'on appelle un problème d'apprentissage par transfert. Ils aimeraient entraîner un classificateur de discours haineux en anglais (ou dans une autre langue bien documentée), puis l'appliquer à d'autres langues. Dans les âges sombres de la modélisation du langage (2018), cela fonctionnait très mal. Le discours familier en birman pour "rassemblons les gays et tuons-les" ressemblait à leurs classificateurs à "il devrait y avoir moins d'arcs-en-ciel". Cela, bien sûr, échappait à leur modération de contenu. Le NYT a expliqué la conséquence : _**[Un Génocide Incité sur Facebook, Avec des Publications de l'Armée du Myanmar](https://www.nytimes.com/2018/10/15/technology/myanmar-facebook-genocide.html)**_

La réponse de Meta a été de construire un modèle de langage qui pourrait mieux mapper n'importe quelle langue (enfin, 100 langues) sur des vecteurs de mots dans le même espace partagé. De cette façon, un classificateur de discours haineux entraîné en anglais peut mieux s'étendre à d'autres langues. (Moins de birman est nécessaire pour l'affiner.) En utilisant ce modèle, j'ai intégré des mots de personnalité dans quatre langues : anglais, espagnol, français et turc. Voici les deux premiers facteurs :

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!eLVQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd3ff00d-d96d-4e3b-ada4-640e3cd66089_1245x954.png)

Ceux-ci servent à séparer les différentes langues. Le premier facteur distingue le turc des langues indo-européennes. Sur le deuxième facteur, les langues romanes sont adjacentes (bien que proches aussi du turc).

Cela a du sens. Le modèle est entraîné à prédire le mot suivant d'une phrase, il inclura donc naturellement des informations spécifiques à la langue. Si quelqu'un parle en espagnol, il ne passe pas souvent au turc. L'espoir est qu'il y ait aussi des directions dans l'espace vectoriel qui correspondent à des informations de personnalité.

Si les langues sont assez indépendantes, vous avez besoin d'au moins 3 dimensions pour séparer 4 langues dans leurs propres groupes non chevauchants. Vérifions les composants principaux suivants.

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!PRKA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5eb70bd2-8684-4844-94bd-aa12adc030bf_1256x954.png)

Le Facteur 4 est le premier facteur qui n'a pas été appris pour séparer les langues, et c'est le Facteur Général de la Personnalité ! En anglais : _dominateur, impitoyable, compulsif_ et _égoïste_ **vs** _généreux, doux,_ et _réfléchi_. [J'ai soutenu](https://vectors.substack.com/p/primary-factor-of-personality-part) que ce facteur est mieux compris comme la tendance à vivre la Règle d'Or. La Théorie d'Ève de la Conscience était en fait le résultat de [se demander ce que cela sélectionnerait](https://vectors.substack.com/p/consequences-of-conscience) dans notre histoire évolutive. Le Facteur 5 concerne également la personnalité, les traçant ensemble :

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!pD64!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F192dc8f4-db5e-4d96-b8a5-ce16c1cbf1f6_1264x954.png)

Nous obtenons les Deux Grands ! Le Facteur Cinq (ou deux, des facteurs de personnalité) est le Dynamisme : _aventureux, imaginatif,_ et _enthousiaste_ **vs** _prudent, réservé,_ et _lâche._ C'est incroyable que cela ressorte si régulièrement. **Il y a [2 500 citations sur l'article des Deux Grands](https://scholar.google.com/scholar?cites=11052969740325606797&as_sdt=2005&sciodt=0,5&hl=en), et pourtant les chercheurs ne réalisent pas qu'ils sont simplement les deux premiers facteurs non tournés de la personnalité générale.** La croyance commune qu'ils existent d'une manière ou d'une autre dans une relation hiérarchique avec les Cinq Grands vient des chercheurs abandonnant de traiter directement avec le langage peu après avoir créé les inventaires des Cinq Grands. Depuis lors, toute tentative de comprendre la personnalité de base ou générale doit être faite en référence aux Cinq Grands. Mais les mots sont venus en premier, et les modèles de langage rendent facile l'analyse du langage à ce niveau fondamental maintenant.

[Partager](https://www.vectorsofmind.com/p/personality-around-the-world?action=share)

## Nous devons aller plus loin

Ajouter le russe et le farsi donne les mêmes facteurs :

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!IIKx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F976f1c11-fd97-4184-a74a-a384a09b0579_2078x1715.png)Pour mieux voir les mots, téléchargez l'image et zoomez.

Selon mes standards d'ingénieur paresseux, c'est assez laborieux car cela nécessite de trouver une bonne invite pour chaque langue. J'ai travaillé avec Google Translate et des locuteurs natifs pour bien faire cela, et vous pouvez voir que la distribution du farsi est encore décalée sur le Facteur 4. Mon hypothèse est que ma méthode d'ignorer tout facteur qui n'est pas partagé est trop bancale pour autant de langues. Le Facteur 4 est probablement utilisé comme le GFP, et aussi pour séparer le farsi (juste un peu). Il n'y a rien qui garde ces facteurs purs, nous avons vraiment de la chance que la distribution soit aussi bien comportée qu'elle l'est. Faire un peu de prétraitement (comme donner une signification nulle à chaque groupe linguistique) pourrait résoudre cela.

À ma connaissance, c'est la première fois que plusieurs langues sont factorisées ensemble. Cela serait publiable avec des résultats sur seulement l'anglais et l'espagnol et ici j'ai atteint jusqu'à six, y compris deux langues non indo-européennes. Cela éclaire également la nature des Deux Grands, l'un des concepts les plus populaires - et mal compris - en psychométrie.

## Lacunes

J'ai fait cette recherche de la manière la plus stupide possible. J'ai trouvé 100 mots de personnalité dans un guide ESL, puis je les ai traduits dans d'autres langues en utilisant Google Translate. S'il y avait des doublons, je les ai supprimés. Ce n'est pas aussi mauvais que cela en a l'air. Les deux premiers facteurs sont pratiquement inchangés en anglais que vous utilisiez 100 ou 500 mots. Mais, si c'était un vrai article, vous voudriez évidemment développer un ensemble de mots dans chaque vocabulaire indépendamment. Il y a plusieurs autres lacunes :

**Pas assez de langues !** Si je publiais cela, j'aimerais ajouter une douzaine de langues supplémentaires qui ne sont pas typiquement étudiées en science de la personnalité. C'est, en fait, pourquoi je n'ai jamais publié cela. C'est beaucoup de travail et nécessiterait des locuteurs natifs de plusieurs langues asiatiques.

**Modèles multilingues déformés par les données d'entraînement.** Les modèles de langage sont entraînés à prédire le mot suivant d'une phrase. Si vous vous entraînez avec plusieurs langues, le modèle essaiera de transférer une partie des connaissances. Cependant, pour les langues plus petites, cela pourrait ressembler davantage à leurs significations étant forcées à des analogies au sein des langues mieux documentées (anglais, chinois, russe, etc.).

**Les requêtes sont un degré de liberté du chercheur.** La méthode que j'utilise pour intégrer des mots est "Ma personnalité peut être décrite comme <mask> et [mot]" où [mot] est l'un des mots de personnalité. En raison de la façon dont la phrase est écrite, le modèle charge des informations de personnalité pures sur le jeton de masque, puis l'intègre. Dans ma thèse, j'ai trouvé que cela fonctionnait le mieux. Bien sûr, il y a des variations infinies à cela, et vous devez en choisir une. Théoriquement, un chercheur pourrait avoir un résultat particulier en tête, puis trouver une requête qui le soutient. À mon avis, ce n'est pas trop risqué, étant donné à quel point ce résultat est similaire à ce que les méthodes d'enquête produisent. Nous avons un a priori assez fort sur la structure de personnalité que nous trouvons avec l'analyse factorielle. Cette méthode la récapitulant est une preuve que la méthode fonctionne.

**Modèle de langage obsolète.** J'ai fait ce travail il y a plus de 2 ans, bien avant la sortie de GPT-4. Des temps plus simples.

## Conclusion

Si j'étais encore dans le milieu universitaire, ce serait mon programme de recherche. Ajouter autant de langues que possible, et essayer de comprendre toutes les façons dont la méthode peut être biaisée. En fin de compte, cela pourrait produire un modèle universel de personnalité supérieur aux Cinq Grands. Cela nous aiderait à mieux comprendre qui nous sommes, et peut-être même d'où nous venons. Car c'est le langage qui définit notre espèce maintenant, et c'est le langage qui a forgé notre psyché dans le passé. Nous sommes habituellement sociaux parce qu'il y a des milliers d'années, échouer à gérer sa réputation signifiait mourir. Les modèles de personnalité sont des cartes du langage ; ce sont des vecteurs dans l'évolution de notre esprit.

[Abonnez-vous maintenant](https://www.vectorsofmind.com/subscribe?)

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!MDwl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F935dcb92-8e91-41c3-9630-2a80f2bc9a06_1024x1024.png)