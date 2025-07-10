---
about:
- vectors-of-mind
- blog-archive
author: Andrew Cutler
date: '2025-07-04'
description: 'My work has become dangerously close to a Prompt Engineer1. This is
  fine by me, as it combines my love of writing, psychometrics, and NLP. Here are
  some of the most overpowered prompting techniques:'
draft: false
keywords:
- vectors-of-mind
- prompt
- chatgpt
lang: fr
lastmod: '2025-07-09'
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '145544092'
original_url: https://www.vectorsofmind.com/p/how-to-prompt-chatgpt
quality: 6
slug: how-to-prompt-chatgpt
tags: []
title: "# Comment inciter ChatGPT\n\n## Introduction\n\nChatGPT est un modèle de langage
  développé par OpenAI, conçu pour comprendre et générer du texte de manière conversationnelle.
  Pour tirer le meilleur parti de ChatGPT, il est essentiel de savoir comment formuler
  des invites efficaces. Ce guide vous fournira des conseils et des stratégies pour
  interagir avec ChatGPT de manière optimale.\n\n## Comprendre les bases\n\nAvant
  de commencer à inciter ChatGPT, il est important de comprendre quelques concepts
  de base :\n\n- **Modèle de langage** : ChatGPT est un modèle de langage qui prédit
  le texte suivant basé sur le texte d'entrée.\n- **Contexte** : Le modèle utilise
  le contexte fourni pour générer des réponses pertinentes.\n- **Prompt** : L'invite
  est le texte que vous fournissez à ChatGPT pour générer une réponse.\n\n## Conseils
  pour formuler des invites efficaces\n\n1. **Soyez clair et précis** : Formulez votre
  question ou demande de manière claire et précise pour obtenir des réponses pertinentes.\n
  \  \n   Exemple : Au lieu de dire \"Parle-moi de la science\", dites \"Quels sont
  les principes fondamentaux de la physique quantique ?\"\n\n2. **Fournissez un contexte
  suffisant** : Plus vous fournissez de contexte, plus ChatGPT peut générer des réponses
  précises.\n\n   Exemple : \"Je travaille sur un projet de biologie moléculaire.
  Peux-tu expliquer le rôle de l'ARN messager ?\"\n\n3. **Utilisez des questions ouvertes**
  : Les questions ouvertes encouragent des réponses plus détaillées.\n\n   Exemple
  : \"Quels sont les impacts du changement climatique sur la biodiversité marine ?\"\n\n4.
  **Spécifiez le format de la réponse** : Si vous avez besoin d'une réponse dans un
  format particulier, indiquez-le clairement.\n\n   Exemple : \"Peux-tu fournir une
  liste des étapes pour résoudre une équation quadratique ?\"\n\n5. **Expérimentez
  avec des variations** : Si vous n'obtenez pas la réponse souhaitée, essayez de reformuler
  votre invite.\n\n   Exemple : \"Explique la théorie de la relativité\" peut être
  reformulé en \"Quels sont les concepts clés de la théorie de la relativité d'Einstein
  ?\"\n\n## Exemples d'invites\n\n- \"Décris les causes et les effets de la révolution
  industrielle.\"\n- \"Quels sont les avantages et les inconvénients de l'énergie
  solaire ?\"\n- \"Peux-tu expliquer la théorie de l'évolution de Darwin ?\"\n\n##
  Conclusion\n\nSavoir comment inciter ChatGPT efficacement peut améliorer considérablement
  la qualité des réponses que vous recevez. En suivant ces conseils et en expérimentant
  avec différentes approches, vous pouvez optimiser vos interactions avec le modèle
  pour obtenir des informations précises et utiles."
translation_model: gpt-4o
---

*De [Vectors of Mind](https://www.vectorsofmind.com/p/how-to-prompt-chatgpt) - images à l'original.*

---

[*[Image: Contenu visuel du post original]*](https://substackcdn.com/image/fetch/$s_!EpIx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F719d87af-7c69-45fd-8c84-595b16af3dae_1024x1024.webp)Vous après avoir lu cet article

Mon travail est devenu dangereusement proche de celui d'un Ingénieur de Prompt[^1]. Cela me convient, car cela combine mon amour pour l'écriture, la psychométrie et le NLP. Voici quelques-unes des techniques de prompt les plus puissantes :

 1. Utiliser des instructions claires et spécifiques

 2. Raisonnement en chaîne

 3. Rassembler les informations requises avant d'effectuer une tâche

 4. Diviser les tâches en étapes

 5. Les termes techniques sont vos amis

 6. Collection de phrases utiles




#### **1\. Instructions claires et spécifiques**


Les avocats et les informaticiens sont naturellement doués pour cela. En fait, l'un des plaisirs du prompt est que l'on peut être beaucoup moins précis par rapport au code régulier, et les LLM comprennent souvent l'essentiel. Cependant, de nombreuses demandes peuvent être améliorées en étant simplement explicite sur la tâche et le format que la réponse doit prendre. Par exemple, j'ai récemment improvisé ce repas :

[*[Image: Contenu visuel du post original]*](https://substackcdn.com/image/fetch/$s_!dVwU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F216d83a0-b1be-4f15-877a-bfbb9842c0ed_1284x1253.jpeg)

C'était délicieux, merci de demander. Autres exemples :

 * "Résumez l'histoire de l'IA en un paragraphe."

 * "Créez un tableau des plus anciennes familles de langues classées par âge. Soyez exhaustif."[^2]

 * "Réécrivez le texte cité à la manière de White et Strunk. Donnez-moi trois options."

 * "Calculez une matrice de corrélation de Pearson pour les colonnes 2-7 du fichier attached.csv."

 * suivi : "Écrivez un code pour afficher les résultats sous forme de carte thermique avec une résolution suffisamment élevée pour être utilisée dans une affiche. Utilisez les meilleures pratiques en matière de choix esthétiques"




Les instructions spécifiques incluent souvent des exemples spécifiques. White et Strunk ont écrit _Elements of Style_. Citer leur livre est mieux que d'utiliser des adjectifs tels que "concise", "professionnelle" ou "excellente" écriture. En partie parce que les LLM ont tendance à sur-livrer, surtout sur des adjectifs spécifiques. Ainsi, si vous voulez que le robot adopte une personnalité impertinente, essayez de lui dire d'agir comme Veronica Mars ou Regina George de Mean Girls.

#### **2\. Raisonnement en chaîne**


Les LLM sont entraînés sur un corpus de texte énorme pour prédire le mot suivant. Étonnamment, cela les rend bons pour approximer le raisonnement, mais cela se dégrade rapidement pour les tâches complexes. Ici, "complexe" peut signifier quelque chose comme "additionner les nombres dans la colonne 1". C'est très difficile à faire en un coup, et il crachera un nombre qui semble raisonnable et sera probablement dans la bonne fourchette mais pas la bonne réponse. Ajouter "réfléchissez-y par étapes" fait des merveilles. Souvent, vous n'avez même pas besoin de spécifier quelles sont les étapes ; les LLM peuvent en déduire que pour additionner une colonne, les étapes intermédiaires sont d'écrire "n1 + n2 + n3 + … + n100 =" C'est essentiellement se donner un prompt pour obtenir une meilleure réponse du bon côté de ce signe égal. Ou, par analogie, se donner le temps d'y réfléchir. Pour tout problème, la phrase "réfléchissez-y par étapes" est votre première ligne de défense contre les hallucinations des LLM. Si cela ne fonctionne pas, énumérez les étapes vous-même (une technique à laquelle nous reviendrons).

#### **3\. Rassembler les informations requises avant d'effectuer une tâche**


Si vous demandez à chatGPT d'écrire un article de blog (je ne le ferais jamais) ou une fonction Python (je le ferais absolument), il le fera sans demander les détails de ce que vous voulez réellement. Beaucoup de cela peut être évité en disant quelque chose comme, "Je veux écrire une fonction qui fait X ; quelles informations dois-je rassembler avant de coder ?" ou "Écrivez une fonction qui fait X, mais demandez d'abord toutes les informations requises avant d'écrire le code." où "X" est une description partielle.

#### 4\. Diviser les tâches en étapes


Chaque fois que chatGPT échoue à une tâche et que le raisonnement en chaîne ne fonctionne pas, divisez la tâche en sous-tâches. C'est souvent la moitié du travail d'une tâche pour commencer et, par coïncidence, ce qui est (actuellement) difficile pour les LLM à faire par eux-mêmes. Cependant, notez que vous pouvez souvent externaliser cela au LLM également[^3]. Par exemple, j'ai demandé à chatGPT de proposer des éléments pour un test de créativité (que vous pouvez parcourir) :

> J'essaie de trouver plus de questions similaires au Test d'Associations Distantes (RAT). Le RAT exige que les individus trouvent un mot commun qui relie trois mots apparemment sans rapport. Voici quelques ensembles de mots exemples :
> 
> 1\. Cottage, Suisse, Gâteau (Réponse : Fromage)
> 
> 2\. Haut, Livre, Chaise (Réponse : École)
> 
> 3\. Fruit, Regard, Trafic (Réponse : Confiture)
> 
> 4\. Crème, Patin, Eau (Réponse : Glace)
> 
> 5\. Douleur, Chasseur, Chou (Réponse : Tête)
> 
> 6\. Manières, Rond, Tennis (Réponse : Table)
> 
> 7\. Chute, Acteur, Poussière (Réponse : Étoile)
> 
> 8\. Lumière, Anniversaire, Bâton (Réponse : Bougie)
> 
> 9\. Salade, Tête, Oie (Réponse : Œuf)
> 
> 10\. Musique, Douleur, Vert (Réponse : Pomme) 
> 
> Quelles sont les meilleures pratiques ? Comment devrais-je y réfléchir par étapes ?

Comme comprendre comment additionner des nombres, chatGPT est excellent pour produire des "recettes" pour accomplir des tâches. Après qu'il ait livré, tout ce que j'avais à dire était :

> "Super ! Maintenant, suivez ce processus pour produire 5 nouvelles questions"

Et puis cinq de plus, et cinq de plus. J'avais précédemment essayé de demander directement de nouveaux éléments, et les suggestions étaient atroces. Pour un [exemple beaucoup plus compliqué](https://redwoodresearch.substack.com/p/getting-50-sota-on-arc-agi-with-gpt), voyez comment un institut de sécurité de l'IA a utilisé cette technique (parmi d'autres astuces) pour résoudre un problème conçu pour être impossible pour les LLM.

#### 5\. Les termes techniques sont vos amis


Les termes techniques sont des bassins d'attraction pour un comportement compétent des LLM. Par exemple, décrire une maladie et demander ce qui est "indiqué" vous mènera plus loin que de demander, "Que devrais-je faire ?" Utiliser "indiqué" indique au LLM de mapper vos symptômes à chaque manuel médical jamais écrit. Le second revient à demander des conseils médicaux/de vie, ce qu'il a été formé à ne pas donner. Utiliser des termes techniques ou non colloquiaux vous sort de l'espace assistant normatif, qui a le plus de garde-fous et de conseils de niveau Reddit.

#### 6\. Collection de phrases utiles


Voici quelques phrases que je me retrouve à utiliser

 * "Est-ce correct ?"

 * Chaque fois que j'écris un résumé du travail de quelqu'un d'autre ou que je décris une idée que je ne connais pas totalement, je copie-colle mon écriture et demande si c'est correct. Il est généralement assez bon pour repousser lorsque certaines parties sont discutables

 * "Êtes-vous sûr ?"

 * De même, chaque fois que je soupçonne qu'un LLM débite des absurdités, je demande s'il est sûr. S'il change d'avis, alors prenez l'affirmation avec une grande pincée de sel.

 * "Aidez-moi à réfléchir." "Soyez créatif"

 * L'un des meilleurs usages d'un LLM est de vous aider à explorer l'espace des idées. Parfois, il a besoin d'encouragement pour s'éloigner des réponses modales.




Si vous avez des phrases favorites, ajoutez-les dans les commentaires !

[Partager](https://www.vectorsofmind.com/p/how-to-prompt-chatgpt?action=share)

[^1]: C'est aussi devenu plus irrégulier que je ne le souhaiterais, donc si vous avez un travail de contrat en science des données, IA ou psychométrie, contactez-moi !

[^2]: Il est vrai qu'il n'y a aucun moyen qu'un LLM liste toutes les 142-420 familles de langues dans le monde. Comme cela est "impossible" (c'est-à-dire trop éloigné de son comportement par défaut, au-delà d'une certaine limite de tokens), "exhaustif" sert à lutter contre la gravité d'une réponse courte, rendant le LLM plus minutieux. C'est l'inconvénient du prompt, qui se dégrade parfois en mendicité, supplication, corruption et menace.

[^3]: Le fait que vous puissiez obtenir de l'aide d'un LLM pour diviser la sous-tâche indique que cela sera également de plus en plus automatisé. Qui sait ce dont les générations futures seront capables.