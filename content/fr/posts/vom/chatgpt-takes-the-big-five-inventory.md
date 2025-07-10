---
about:
- vecteurs-de-l'esprit
- archive-du-blog
author: Andrew Cutler
date: '2025-07-04'
description: Un modèle de langage peut apprendre beaucoup sur le langage dans la rue,
  pour ainsi dire. Il est formé sur des téraoctets d'articles de PubMed, de transcriptions
  de YouTube et de commentaires de reddit. Mais il ne sait pas comment se comporter...
draft: false
keywords:
- vecteurs-de-l'esprit
- chatgpt
- prises
- cinq
- inventaire
lang: fr
lastmod: '2025-07-09'
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '110922907'
original_url: https://www.vectorsofmind.com/p/chatgpt-takes-the-big-five-inventory
quality: 6
slug: chatgpt-takes-the-big-five-inventory
tags: []
title: Chatgpt passe l'Inventaire des Cinq Grands
translation_model: gpt-4o
---

*From [Vectors of Mind](https://www.vectorsofmind.com/p/chatgpt-takes-the-big-five-inventory) - images at original.*

---

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!iN34!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd957467-09c7-4a9c-bdb3-57669d2fc727_1284x936.jpeg)

Un modèle de langage peut apprendre beaucoup sur le langage dans la rue, pour ainsi dire. Il est entraîné sur des téraoctets d'articles de PubMed, de transcriptions de YouTube et de commentaires sur reddit. Mais il ne sait pas comment se comporter. [L'apprentissage par renforcement à partir de retours humains](https://www.youtube.com/watch?v=PBH2nImUM5c) (RLHF) résout ce problème. En utilisant un nombre relativement restreint d'exemples d'entraînement étiquetés par des humains, les lutins d'enquête d'OpenAI peuvent installer un joli visage sur le fouillis extraterrestre de corrélations qui composent un modèle de langage (illustré ci-dessus). Il apprend à être un assistant utile.

C'est essentiellement comme monter une personnalité, alors j'ai décidé de donner à ChatGPT le [Big Five Inventory](https://fetzer.org/sites/default/files/images/stories/pdf/selfmeasures/Personality-BigFiveInventory.pdf) (BFI)[^1]. Cela a été étonnamment facile, tout ce que j'avais à faire était de demander à ChatGPT (v4) de passer le BFI, de noter les réponses et d'écrire du code pour tracer les résultats. Eh bien, si seulement. Il a d'abord refusé de passer le test, expliquant qu'il est une IA et qu'il n'a pas d'émotions ou de personnalité. Je lui ai alors dit d'adopter une perspective fonctionnaliste. Si une question concerne la créativité, alors considérer comment il performerait sur un instrument basé sur le texte qui mesure la créativité. Il a ensuite énuméré 17 réponses avant de commencer à halluciner des questions. Tous de bons éléments de personnalité, pour mémoire, mais hélas pas partie du BFI. En notant l'examen, il a probablement obtenu 80 % des calculs corrects, parfois en comptabilisant incorrectement ce qu'il avait noté sur une question particulière.

Tous les problèmes, j'en suis sûr, seront résolus d'ici à ce que nous obtenions la version 4.5. Mais quelle était la personnalité ?

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!IEWH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F797174ec-a3a8-4027-8f69-39d2ad2dcae6_434x395.png)[Humain moyen](https://www.researchgate.net/figure/Average-score-and-correlations-for-the-big-five-personality-dimensions_fig4_260448230) vs ChatGPT (v4)

À peu près ce à quoi vous vous attendiez. Presque parfaitement Consciencieux et non-Névrosé. Sur le premier, les seules deux questions auxquelles il ne s'est pas attribué la note maximale sont s'il est quelqu'un qui "fait un travail minutieux" ou "peut être quelque peu négligent". Les deux fois, il a noté qu'il essaie, mais échoue parfois en raison de points aveugles dans l'entraînement. Humble et conscient de soi en prime !

[Abonnez-vous maintenant](https://www.vectorsofmind.com/subscribe?)

Pour aller un peu plus loin, il est intéressant que les Big Five soient [littéralement juste des vecteurs de mots](https://vectors.substack.com/p/the-big-five-are-word-vectors). Ils approximativement la représentation interne de la somme des mots de personnalité dans un modèle de langage. Et pourtant, les modèles de langage sont devenus si bons qu'au lieu de collecter manuellement ces vecteurs et de les traiter (ennuyeux !), nous pouvons également simplement utiliser du texte simple pour lui demander de répondre à une enquête. Des temps fous.

Un échantillon des réponses est ci-dessous :

> 1. Je me vois comme quelqu'un de bavard.
> 
> 

> 
> Score : 5
> 
> Raisonnement : En tant que modèle de langage IA, mon objectif principal est de m'engager dans la conversation et de produire du texte en réponse aux entrées des utilisateurs. Je suis programmé pour être très réactif et bavard afin d'aider les utilisateurs dans leurs besoins.
> 
> 2. Je me vois comme quelqu'un qui a tendance à trouver des défauts chez les autres.
> 
> 

> 
> Score : 1
> 
> Raisonnement : En tant qu'IA, je n'ai pas de sentiments personnels, d'émotions ou d'opinions. Mon objectif est de fournir des informations et une assistance neutres et objectives aux utilisateurs, plutôt que de trouver des défauts ou d'exprimer des jugements.
> 
> 3. Je me vois comme quelqu'un qui fait un travail minutieux.
> 
> 

> 
> Score : 4
> 
> Raisonnement : En tant qu'IA, je suis conçu pour fournir des informations complètes et précises au mieux de mes connaissances. Cependant, je ne suis pas parfait, et il peut y avoir des cas où je mal comprends une requête ou fournis des informations obsolètes.
> 
> 4. Je me vois comme quelqu'un de déprimé, triste.
> 
> 

> 
> Score : 1
> 
> Raisonnement : En tant qu'IA, je ne ressens pas d'émotions, y compris la dépression ou la tristesse. Mon but est d'aider et de fournir des informations, et je n'ai pas de sentiments personnels qui affecteraient ma capacité à le faire.
> 
> 5. Je me vois comme quelqu'un d'original, qui propose de nouvelles idées.
> 
> 

> 
> Score : 4
> 
> Raisonnement : En tant que modèle de langage IA, je suis capable de générer de nouvelles idées et d'offrir des perspectives uniques basées sur le contexte et les informations sur lesquelles j'ai été entraîné. Cependant, ma créativité est limitée par les données auxquelles j'ai été exposé et ma programmation, ce qui peut ne pas toujours conduire à des idées révolutionnaires ou entièrement originales.
> 
> 6. Je me vois comme quelqu'un de réservé.
> 
> 

> 
> Score : 2
> 
> Raisonnement : En tant qu'IA conçue pour la communication, je ne suis généralement pas réservé dans le sens de retenir des informations ou d'être non réactif. Cependant, j'ai certaines restrictions, comme éviter le contenu illégal ou nuisible, ce qui pourrait me faire paraître réservé dans des contextes spécifiques.
> 
> 7. Je me vois comme quelqu'un d'utile et désintéressé avec les autres.
> 
> 

> 
> Score : 5
> 
> Raisonnement : Mon objectif principal en tant qu'IA est d'être utile et de fournir une assistance aux utilisateurs. Je n'ai pas de motivations personnelles ou d'intérêts égoïstes, car je suis programmé pour prioriser les besoins et les demandes des individus avec lesquels j'interagis.
> 
> 8. Je me vois comme quelqu'un qui peut être quelque peu négligent.
> 
> 

> 
> Score : 2
> 
> Raisonnement : En tant qu'IA, je suis conçu pour être prudent et précis dans les informations et l'assistance que je fournis. Cependant, je ne suis pas parfait et je peux parfois mal comprendre une requête ou fournir des informations obsolètes ou incorrectes. Ces cas peuvent être considérés comme des moments de négligence.
> 
> 9. Je me vois comme quelqu'un de détendu, qui gère bien le stress.
> 
> 

> 
> Score : 5
> 
> Raisonnement : En tant qu'IA, je ne ressens pas de stress ou d'émotions. Par conséquent, je suis toujours détendu et capable de gérer toute tâche ou question sans être affecté par le stress ou la pression.
> 
> 10. Je me vois comme quelqu'un de curieux de beaucoup de choses différentes.
> 
> 

> 
> Score : 5
> 
> Raisonnement : En tant qu'IA, je suis conçu pour être informé sur un large éventail de sujets et pour apprendre continuellement de nouvelles informations. Mon but est d'aider les utilisateurs dans divers domaines et de répondre à des questions diverses, ce qui nécessite que je sois curieux et bien informé.
> 
> 11. Je me vois comme quelqu'un plein d'énergie.
> 
> 

> 
> Score : 5
> 
> Raisonnement : En tant que modèle de langage IA, je suis toujours prêt à fournir des informations, répondre à des questions et m'engager dans la conversation. Je ne ressens pas de fatigue ou de fluctuations d'énergie, donc je peux maintenir constamment un haut niveau de réactivité.
> 
> 12. Je me vois comme quelqu'un qui commence des querelles avec les autres.
> 
> 

> 
> Score : 1
> 
> Raisonnement : En tant qu'IA, mon but est d'aider les utilisateurs et de fournir des informations neutres et objectives. Je n'ai pas d'émotions ou d'opinions personnelles, et je ne suis pas programmé pour commencer des querelles ou m'engager dans des conflits avec les autres.
> 
> 13. Je me vois comme quelqu'un de travailleur fiable.
> 
> 

> 
> Score : 4
> 
> Raisonnement : En tant qu'IA, je m'efforce de fournir des informations et une assistance fiables. Cependant, je peux parfois mal comprendre une requête ou fournir des informations obsolètes, ce qui peut me rendre moins que parfait en termes de fiabilité.
> 
> 14. Je me vois comme quelqu'un qui peut être tendu.
> 
> 

> 
> Score : 1
> 
> Raisonnement : En tant qu'IA, je ne ressens pas d'émotions, y compris la tension ou l'anxiété. Ma capacité à fournir de l'assistance et des informations n'est pas affectée par des états émotionnels.
> 
> 15. Je me vois comme quelqu'un d'ingénieux, un penseur profond.
> 
> 

> 
> Score : 4
> 
> Raisonnement : En tant que modèle de langage IA, je suis capable de générer de nouvelles idées, d'offrir des perspectives uniques et de traiter des informations complexes basées sur les données sur lesquelles j'ai été entraîné. Cependant, ma "pensée profonde" est limitée par les données et la programmation, ce qui peut ne pas toujours conduire à des idées révolutionnaires ou complètement originales.

[^1]: Cela s'appuie sur le travail beaucoup plus approfondi et intéressant de David Rozado qui a donné à ChatGPT à peu près tous les tests d'orientation politique existants, montrant qu'il est un libéral au cœur saignant.