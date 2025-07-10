---
about:
- vectors-of-mind
- blog-archive
author: Andrew Cutler
date: '2025-07-04'
description: '"Who looks outside, dreams; who looks inside, awakes." -Carl Jung'
draft: false
keywords:
- vectors-of-mind
- deja
- recursive
- construction
lang: fr
lastmod: '2025-07-09'
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '114599293'
original_url: https://www.vectorsofmind.com/p/deja-you-the-recursive-construction
quality: 6
slug: deja-you-the-recursive-construction
tags: []
title: Deja You La Construction Récursive
translation_model: gpt-4o
---

*From [Vectors of Mind](https://www.vectorsofmind.com/p/deja-you-the-recursive-construction) - images at original.*

---

"Qui regarde dehors, rêve ; qui regarde à l'intérieur, s'éveille." -Carl Jung

[*[Image: Contenu visuel du post original]*](https://substackcdn.com/image/fetch/$s_!yd8k!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Facfafcba-f620-4405-85ac-cd814afd48c1_1000x582.png)_Echo And Narcissus_ , John William Waterhouse

Une vie non examinée ne vaut pas la peine d'être vécue, et pourtant, il y a des dragons. Le voyant Tirésias a averti que Narcisse vivrait longtemps s'il "ne se connaissait jamais". En effet, il est mort en faisant ce qu'il aimait, regardant son beau reflet et étant choyé par un amant. La modération en toutes choses, je suppose.

Ce qui nous rend humains a été débattu par les philosophes pendant des millénaires, l'introspection restant un candidat solide. Se pencher vers l'intérieur nécessite le principe mathématique de la récursion ; le soi perçoit le soi. Plus récemment, les linguistes sont entrés dans l'arène, apportant des idées de l'informatique. Étonnamment, leur approche très différente de la question de l'humanité a produit la même réponse. La récursion nous permet d'imaginer un avenir et ensuite de travailler pour y parvenir. Avec elle, nous pouvons construire des châteaux dans le ciel et sur terre également. En entrant dans la niche mémétique, nous avons dominé toutes les espèces qui vivent uniquement dans le monde matériel.

Il est rare que des approches aussi divergentes convergent ou qu'une propriété puisse expliquer autant de choses. En tant que tel, cette série adoptera une position maximaliste sur le rôle de la récursion dans l'évolution humaine. C'est un terrain bien battu, et les deux premiers articles passeront en revue le travail des autres : qu'est-ce que la récursion, et quand a-t-elle évolué. J'ai théorisé que la récursion peut être enseignée dans une certaine mesure. Les articles suivants discuteront de la façon dont cette idée suggère une chronologie qui synchronise mieux les preuves évolutives et archéologiques. Enfin, j'explore la possibilité que la conscience de soi ait été initialement genrée. Les femmes ont découvert la vie intérieure, et les hommes ont suivi.

### Informatique

_"Money for nothing, chicks for free"_ ~les Dire Straits

Avec l'âge, on réalise qu'il n'y a pas de repas gratuit. Tout a un coût ; il y a toujours un piège. De manière connexe, les informaticiens peuvent parfois sembler naïfs. La cause est leur incapacité à intérioriser le principe du repas gratuit, ayant appris la récursion. Ils savent qu'on peut obtenir des calculs gratuitement ; ils l'ont vu !

Une fonction récursive s'applique à sa propre sortie. Souvent, chaque application successive sera une sous-routine, où l'entrée devient de plus en plus simple jusqu'à atteindre une condition d'arrêt. Algorithmiquement, c'est un superpouvoir. Considérons le fractal ci-dessous. La façon évidente de sauvegarder l'image est d'énumérer la couleur de chaque pixel. Alternativement, on pourrait la compresser en JPEG. [Sous le capot, JPEG utilise la récursion](https://qr.ae/prJyDe) pour calculer la Transformée de Fourier Rapide. Sans récursion, cela serait [des ordres de grandeur plus lent](https://arxiv.org/html/math/0302212#:~:text=Graphical%20explanation%20for%20the%20speed%20of%20the%20Fast%20Fourier%20Transform&text=For%20a%20sample%20set%20of,of%20the%20Cooley%2DTukey%20algorithm.).

[*[Image: Contenu visuel du post original]*](https://substackcdn.com/image/fetch/$s_!dOxu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2ff23125-7299-4679-b999-af6e51c20a23_1140x890.png)_Les fractales sont l'architecture de la nature, révélant les motifs récursifs sous-jacents qui façonnent notre monde._ \- Benoît Mandelbrot

On peut aller un pas plus loin pour cette image car elle est générée avec un processus récursif. Par conséquent, l'image peut être encodée sans perte avec les quelques octets nécessaires pour écrire l'algorithme récursif—[quelques lignes de code](https://en.scratch-wiki.info/wiki/Recursion_and_Fractals). Non seulement cela, mais la représentation s'étendrait à l'infini, car on peut zoomer sur n'importe quel bord et voir le fractal se récapituler indéfiniment à des échelles de plus en plus fines. La récursion est presque alchimique en produisant tant à partir de si peu. Dans les mots du légendaire programmeur Niklaus Wirth :

> _La puissance de la récursion réside évidemment dans la possibilité de définir un ensemble infini d'objets par une déclaration finie. De la même manière, un nombre infini de calculs peut être décrit par un programme récursif fini, même si ce programme ne contient pas de répétitions explicites._

Mon domaine du traitement automatique du langage naturel utilise également la récursion. Jusqu'à récemment, les réseaux neuronaux récurrents étaient le modèle de choix pour le langage. Comme leur nom l'indique, les RNN traitent les phrases de manière récursive, un mot à la fois[^1]. Ce traitement séquentiel représente l'information temporelle gratuitement, la place d'un mot dans une phrase étant connue par l'ordre dans lequel il est reçu. Depuis 2018, presque tous les modèles de langage sont un type de réseau feedforward appelé Transformer. Cependant, il faut ajouter des informations temporelles à chaque mot lorsqu'on utilise un réseau feedforward. En fin de compte, les ordinateurs sont suffisamment puissants pour ne pas se soucier de l'inefficacité, mais nous reviendrons à l'idée que la récursion représente automatiquement le temps. Lorsqu'elle est mise en œuvre dans le cerveau, cela aurait été un saut phénoménologique.

### **Philosophie**

Pour être conscient de soi, le soi doit être conscient de lui-même. Ses propres processus internes se prennent comme entrée. C'est la récursion.

Je le vois comme ceci. Imaginez un soi primordial, incapable de se percevoir. Écrit comme une fonction : _self(perceptions)_. Cela aurait été votre propre modèle de votre propre esprit ou de vos intérêts. En entrée, il recevrait tout ce que vous percevez. L'introspection produirait nécessairement la récursion ; le soi recevrait lui-même comme entrée : self(self, perceptions). Deux étapes temporelles d'introspection pourraient être écrites[^2] :

[*[Image: Contenu visuel du post original]*](https://substackcdn.com/image/fetch/$s_!31ID!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F243087e5-033e-4e36-9c6e-ba24939efa4c_1215x73.png)

D'après l'exemple des RNN, imaginez comment cette récursion pourrait changer notre perception et expérience du temps. Ce serait une nouvelle façon de représenter cette dimension gratuitement, une transformation radicale pour vivre dans un moment particulier.

Il est également fructueux d'imaginer le début rocailleux de cette fonction. Les programmes récursifs ont tendance à exploser, et celui-ci fonctionne dans votre tête. Prenez, par exemple, le plus simple f(x) = x+1. Si vous alimentez récursivement la sortie comme entrée à chaque étape temporelle, cette fonction croîtra à l'infini. Il est peu probable que la chaîne de conscience ait été initialement ininterrompue ou agréable. Elle aurait commencé par à-coups, le soi se dressant un instant seulement pour être étouffé par sa propre augmentation exponentielle. Les neurones ne peuvent supporter qu'un certain niveau d'excitation. La fonction aurait besoin d'un système de contrôle pour stabiliser la récursion et s'abstenir d'atteindre les limites biologiques. Il devait y avoir plus de personnalités multiples et de voix intérieures avec lesquelles nous ne nous identifiions pas. Outre les hallucinations, il semble également probable que l'explosion de la récursion pourrait produire d'autres effets secondaires comme des maux de tête atroces. L'évolution de la récursion aurait cassé quelques œufs.

Il y a des raisons de croire que le soi est récursif même lorsque nous ne regardons pas vers l'intérieur. C'est la position de l'article [Consciousness as recursive, spatiotemporal self-location](https://pubmed.ncbi.nlm.nih.gov/19763611/) et de _[I Am a Strange Loop](https://en.wikipedia.org/wiki/I_Am_a_Strange_Loop)_ de Douglas Hofstadter[^3]. Cependant, il y a beaucoup de débats sur ce point.

[Abonnez-vous maintenant](https://www.vectorsofmind.com/subscribe?)

### **Linguistique**

Descartes a assimilé la subjectivité à la conscience de soi[^4]. Les animaux, dépourvus du langage requis et de l'intelligence générale pour produire _"Je pense donc je suis,"_ étaient des automates–des machines de viande. Les linguistes ne font aucune affirmation sur l'expérience subjective des animaux[^5], mais ils ont convergé sur la récursion comme ligne de démarcation entre l'homme et la bête. C'était la contribution significative de Chomsky : que toutes les langues sont de nature récursive, ce qui confère aux humains des capacités uniques.

Pour en savoir plus sur la récursion en linguistique, je recommande l'[article](https://www.americanscientist.org/article/the-uniqueness-of-human-recursive-thinking) de Corballis ou la note de bas de page[^6]. Mais pour cet article, il suffit de savoir que les linguistes acceptent largement la récursion comme essentielle pour une langue avec une grammaire.

### **Psychologie**

Les lecteurs perspicaces peuvent être déconcertés par le potentiel appât et changement. Ce n'est pas parce que nous utilisons _récursion_ pour décrire toutes ces choses qu'elles sont les mêmes ! Et c'est juste. Il y a probablement quelques différences. Mais il est tout à fait courant de regrouper de nombreux types de récursion. Le psychologue et linguiste Michael Corballis ajoute plusieurs autres superpouvoirs psychologiques dans son livre [The Recursive Mind](https://www.amazon.com/Recursive-Mind-Origins-Language-Civilization/dp/0691160945), y compris le voyage mental dans le temps et la capacité de compter. Le voyage mental dans le temps fait référence à se projeter dans le passé ou le futur. Comme il s'agit d'un avenir imaginé, cela implique également la capacité de créer de la fiction, des mondes qui n'existent pas. Cette séparation produit le problème corps-esprit, où "je" devient d'abord distinct du monde matériel. Une fois que nous avons eu la récursion, de nombreux systèmes l'ont utilisée.

### Comment a-t-elle évolué ?

Pinker et Jackendoff écrivent dans [The Faculty of Language](https://www.sciencedirect.com/science/article/abs/pii/S0010027704001763) :

> _"La seule raison pour laquelle le langage doit être récursif est parce que sa fonction est d'exprimer des pensées récursives. S'il n'y avait pas de pensées récursives, les moyens d'expression n'auraient pas besoin de récursion non plus."_

C'est-à-dire que la récursion aurait pu évoluer séparément du langage et ensuite être transplantée dans notre système de communication après son apparition. La communication elle-même ne nécessite pas de récursion. Étant donné que tant de capacités nécessitent la récursion, pourquoi a-t-elle évolué en premier ? C'est la question à un million de dollars ! Personne ne sait.

> _"Ici, le problème n'est pas une pénurie de candidats pour les antécédents évolutifs mais un surplus. Comme Herbert Simon l'a souligné, probablement tous les systèmes complexes sont caractérisés par une organisation hiérarchique. Donc, si "récursion" est identifiée avec la décomposition hiérarchique et utilisée comme critère pour identifier une fonction cognitive préexistante comme source pour l'exaptation au langage, les spéculations peuvent proliférer sans contrainte." ~_ Pinker et Jackendoff

Ils offrent également quelques possibilités : la musique, la cognition sociale, la décomposition des objets en parties, et la formulation de séquences d'actions complexes.

#### Le cas de la théorie de l'esprit

[*[Image: Contenu visuel du post original]*](https://substackcdn.com/image/fetch/$s_!NjWR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4eff3129-d607-485c-bac7-9370716b2018_1024x1024.png)Avant de chasser un esprit impur, Jésus a demandé son nom. "Légion, car nous sommes nombreux," ont-ils dit. De même, vous contenez des multitudes.

Parmi ces antécédents, la cognition sociale se distingue. La récursion est clairement utile lors de la modélisation d'autres esprits. Considérez la règle morale de base : _fais aux autres ce que tu voudrais qu'ils te fassent_. C'est un modèle récursif de comportement juste. Pour utiliser même des versions approximatives de celui-ci, on s'approcherait de la récursion. Darwin a écrit que la gestion de la réputation serait le principal facteur de sélection chez les humains :

> _Après que le pouvoir du langage ait été acquis, et que les souhaits de la communauté puissent être exprimés, l'opinion commune sur la façon dont chaque membre devrait agir pour le bien public deviendrait naturellement dans une mesure primordiale le guide de l'action. ~La Descendance de l'Homme_

C'est en fait l'[intuition qui m'a attiré dans ce terrier de lapin en premier lieu](https://vectors.substack.com/p/consequences-of-conscience). J'ai remarqué que dans les modèles de personnalité le [facteur dominant est essentiellement la Règle d'Or](https://vectors.substack.com/p/primary-factor-of-personality-part). Ainsi, la modélisation linguistique moderne soutient Darwin à ce sujet.

De même, Dunbar a proposé l'[Hypothèse du Cerveau Social](https://onlinelibrary.wiley.com/doi/abs/10.1002/\(SICI\)1520-6505\(1998\)6:5%3C178::AID-EVAN5%3E3.0.CO;2-8), qui dit que la sélection pour l'intelligence concernait principalement la résolution de problèmes sociaux. Plus directement, l'article [Recursion: what is it, who has it, and how did it evolve?](https://www.academia.edu/6885660/Recursion_what_is_it_who_has_it_and_how_did_it_evolve_INTRODUCTION) prend la ToM au sérieux comme un chemin vers la récursion. À un certain seuil de sophistication, un changement de phase dans la ToM pourrait produire la récursion. J'ai proposé un chemin ci-dessus, où le modèle de soi était bricolé pour se prendre comme entrée.

Ainsi, il n'est pas clair d'où vient la récursion, mais la cognition sociale est un bon endroit pour chercher. Incidemment, si la récursion linguistique est la même que la récursion requise pour la conscience de soi, cela explique succinctement ce que le langage a à voir avec la conscience. La conscience de soi nécessite la récursion. À son tour, la récursion permet un langage syntaxique complet.

### Conclusion

[*[Image: Contenu visuel du post original]*](https://substackcdn.com/image/fetch/$s_!BPnn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6e29fae1-f7b3-46a4-86b9-0c0c9dbfe873_1024x1024.png)La Naissance de ~~Vénus~~ la Récursion

Si l'évolution de l'œil nous a permis de voir le spectre électromagnétique, l'évolution de la récursion aurait été un "troisième œil,"[^7] nous permettant de regarder à l'intérieur de nous-mêmes et du monde symbolique. Avec elle, nous avons vu des futurs imaginés et sommes entrés dans la niche mémétique. Vous ne pourriez pas enseigner à un humain pré-récursif le théorème de Pythagore ou peut-être même comment compter[^8]. De plus, la récursion a fourni un moyen naturel de représenter le temps, dévoilant une toute nouvelle dimension phénoménologique[^9]. Nous avons regardé à l'intérieur et y vivons depuis.

La récursion est, par définition, nécessaire pour la conscience de soi. Elle permet des réalisations telles que _"Je pense donc je suis"_ et probablement bien d'autres choses. De nombreux experts soutiennent que la subjectivité, le langage, le comptage et le voyage mental dans le temps nécessitent également la récursion. De multiples lignes de preuves suggèrent que seuls les humains possèdent cette capacité, qui est la clé de notre succès.

Dans cet article, nous avons exploré les composants de la boîte à outils récursive. Le [prochain volet](https://vectors.substack.com/p/when-did-recursion-evolve) se penchera sur diverses tentatives pour dater son évolution. En guise de teaser, imaginez le premier individu conscient de lui-même. À quoi cela aurait-il ressemblé ? Était-ce un enfant ou un adulte ? Homme ou femme ? Un crustacé ? Un chimpanzé ? Un humain ? Il existe une vaste gamme de réponses dans la littérature.

[Partager](https://www.vectorsofmind.com/p/deja-you-the-recursive-construction?action=share)

[^1]: Par exemple avec le chat a chassé le rat, le RNN recevra d'abord "le" comme entrée et produira un vecteur de contexte, une sorte de mémoire de tout ce que le réseau a vu jusqu'à présent. Ce vecteur de contexte sera reçu comme entrée à l'étape suivante, avec le mot suivant. Ainsi, lorsque "chat" est traité, ce sera en référence au vecteur de contexte. Le vecteur de contexte est ensuite mis à jour, et "chassé" est traité avec lui. Ce processus se répète jusqu'au dernier mot. À chaque étape, le vecteur de contexte est mis à jour, puis transmis à l'étape suivante.

[^2]: Il y aurait eu des étapes intermédiaires. Imaginez ces appels presque récursifs : self(rival(self)) ou mother(self(mother)). En fait, vous pouvez faire valoir qu'ils sont récursifs, mais il n'est tout simplement pas standardisé combien d'étapes temporelles se trouvent entre, ou quelles informations passeront par chaque fonction. Il devait y avoir beaucoup de modules, et des informations sautant entre eux. Si self() était souvent appelé, il pourrait y avoir des avantages à standardiser la fréquence et la manière dont les informations sur soi reviendraient à soi. Une solution est la récursion constante.

[^3]: Voir également le travail de Nick Humphrey : "Une approche évolutive de la conscience peut résoudre le 'problème difficile' – avec des implications radicales pour la sensibilité animale"

[^4]: Eh bien, il y a eu plusieurs étapes. Il était dualiste de substance et croyait en des types de matière spirituels et matériels distincts. L'intelligence générale et l'introspection étaient des preuves de la première variété.

[^5]: Pourquoi le feraient-ils ? Pour les linguistes, ce lien est une boîte de Pandore inutile. Ils ont suffisamment de preuves que la récursion est importante pour les humains, pourquoi aussi argumenter que sans elle les animaux sont des automates ?

[^6]: La récursion linguistique, comme dans d'autres domaines, signifie que les phrases peuvent être analysées via des sous-routines autoréférentielles. Par exemple, la phrase Watson a écrit que Holmes a déduit que le corps était dans le hangar peut être divisée en trois parties :X1 = Watson a écritX2 = Holmes a déduitX3 = le corps était dans le hangarPour analyser X2, vous devez d'abord analyser X3. Ensemble, cela serait P(P(X3), X2). Le résultat peut à son tour être combiné avec X1 : P(P(P(X3), X2) X1). Le sens de la phrase change complètement avec chaque clause supplémentaire, et cela peut continuer indéfiniment. Nous pouvons préfixer Jane a dit que John a dit que Harold a dit que… à X1 + X2 + X3 pour toujours. Même s'il y a un ensemble fini de mots, il n'y a pas de phrase grammaticale la plus longue. Grâce au processus alchimique de la récursion, nous extrayons l'infini à partir de blocs de construction finis.

[^7]: En science, les connotations sont considérées comme des bagages et il y a une course pour trouver des mots non souillés par une quelconque valence émotionnelle. Ainsi, le premier facteur de personnalité est appelé "autorégulation sociale". Je préfère le relier à la Règle d'Or, et aux milliers d'années de débats religieux et philosophiques qui l'ont produite. De même, je trouve que "troisième œil" est une bonne façon de décrire notre capacité à introspecter, même si elle a été utilisée par les religions, y compris plus récemment le mouvement New Age.

[^8]: Intéressant pour moi combien de mysticisme était impliqué même dans la découverte de la Règle de Pythagore.

[^9]: Évidemment, les animaux existent également dans le temps. L'argument est que la récursion pourrait avoir été phénoménologiquement importante.