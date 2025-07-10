---
about:
- vecteurs-de-l'esprit
- archive-du-blog
author: Andrew Cutler
date: '2025-07-04'
description: Les études lexicales en psychologie et l'Analyse Sémantique Latente en
  informatique ont été introduites à un demi-siècle d'intervalle pour résoudre des
  problèmes différents et pourtant sont mathématiquement équivalentes. Ce n'est pas
  un méta...
draft: false
keywords:
- vecteurs-de-l'esprit
- cinq
- mot
- vecteurs
lang: fr
lastmod: '2025-07-09'
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '50351822'
original_url: https://www.vectorsofmind.com/p/the-big-five-are-word-vectors
quality: 6
slug: the-big-five-are-word-vectors
tags: []
title: Les Big Five sont des vecteurs de mots
translation_model: gpt-4o
---

*From [Vectors of Mind](https://www.vectorsofmind.com/p/the-big-five-are-word-vectors) - images at original.*

---

Les études lexicales en psychologie et l'analyse sémantique latente en informatique ont été introduites à un demi-siècle d'intervalle pour résoudre des problèmes différents et pourtant elles sont mathématiquement équivalentes. Ce n'est pas une métaphore qui fonctionne à un certain niveau d'abstraction _;_ les Big Five sont des dimensions de [vecteurs de mots](https://dzone.com/articles/introduction-to-word-vectors).

Mais d'abord, un peu de contexte. L'hypothèse lexicale affirme que la structure de la personnalité sera inscrite dans la langue car les locuteurs doivent décrire les attributs les plus saillants de ceux qui les entourent. La beauté de cette idée est que, au lieu qu'une seule personne propose un modèle de personnalité, la langue enregistre ce que des millions de personnes considèrent implicitement comme utile. Le travail du psychométricien est simplement d'identifier cette structure. Cela a généralement été accompli en invitant des étudiants en psychologie à s'auto-évaluer sur des listes d'adjectifs et en effectuant une analyse factorielle sur la matrice de corrélation. En 1933, LL Thurstone a administré une enquête de 60 adjectifs à 1300 personnes. Dans son ouvrage seminal [The Vectors of Mind](http://psych.colorado.edu/~carey/Courses/PSYC5112/Readings/VectorsOfMind_Thurstone.pdf), il rapporte que "cinq facteurs suffisent" pour expliquer les données. Dans les décennies suivantes, de telles études ont, plus ou moins, abouti à cinq composantes principales : Agréabilité, Extraversion, Conscienciosité, Névrosisme et Ouverture/Intellect. (Pour un excellent traitement du sujet, voir [Lexical Foundations of the Big Five](https://www.researchgate.net/profile/Boele-Raad-2/publication/282980275_The_Lexical_Foundation_of_the_Big_Five-Factor_Model/links/5626198508aed3d3f137e522/The-Lexical-Foundation-of-the-Big-Five-Factor-Model.pdf).)

L'analyse sémantique latente a été [introduite](https://dl.acm.org/doi/abs/10.1145/57167.57214?casa_token=ogUyQ6VJeZgAAAAA:ksULYwu-Km_5Ap0wA2ho3tbwzTjsB0tHONfEEMIldNB6PJgkRyM7eFaa7uZ-XZJ3nYo0MbYFeJsBng) comme une technique de recherche d'information en 1988. Les mots peuvent être représentés comme des vecteurs et les documents ou phrases peuvent être représentés comme la moyenne de leurs vecteurs de mots. Si vous voulez rechercher dans une grande base de données (par exemple, Wikipédia), les mots-clés pour chaque page ne vous mèneront que jusqu'à un certain point. Une façon de contourner cela est de représenter à la fois les documents (articles wiki) et les requêtes (termes de recherche) comme la moyenne de leurs vecteurs de mots. Trouver des documents pertinents peut désormais être accompli avec un simple produit scalaire. (Dans cet article, je traite l'ASL et les vecteurs de mots comme synonymes. Il existe d'autres façons de vectoriser le langage et, plus spécifiquement, de créer des vecteurs de mots, mais celles-ci dépassent le cadre de cet article.)

Malgré leurs utilisations et histoires différentes, les étapes sont les mêmes :

 1. Collecter une matrice de comptage mot x document

 2. Transformation non linéaire

 3. Décomposition matricielle

 4. Rotation (Optionnelle)




Le résultat est un ensemble de vecteurs de mots qui décrivent succinctement chaque mot. Ceux-ci peuvent être utilisés pour une multitude de tâches en aval, de l'analyse des sentiments à la prédiction du narcissisme à partir de dissertations d'étudiants. Dans le cas des adjectifs de personnalité, les dimensions des vecteurs de mots ont été analysées, nommées et débattues pendant des décennies. Ce qui suit est une discussion des différences à chaque étape.

**Matrice de comptage.** L'ASL implique généralement un grand nombre de documents variés (par exemple, des millions de critiques de produits Amazon). Ceux-ci sont transformés en matrice mot x doc en comptant combien de fois chaque mot apparaît dans chaque doc. En psychologie, un document est constitué des mots qu'un sujet accepte pour se décrire. Cela s'étend également aux échelles de Likert. Si quelqu'un dit qu'un mot le décrit à 5/7, alors il suffit de répéter le mot cinq fois dans le document. 

**Transformation non linéaire.** Les études lexicales ipsatisent souvent les données (score z le long de l'axe du sujet) puis effectuent une corrélation de Pearson. Thurstone a utilisé une corrélation tétrarchique archaïque dans son étude. Dans l'ASL, la transformation la plus courante est TF-IDF, suivie d'un logarithme. Cela garantit que la matrice n'est pas dominée par des termes courants. Souvent, la transformation aboutit à une matrice d'affinité mot x mot (par exemple, matrice de corrélation). Cette étape est pratiquement très importante mais pas si théorique. La transformation à choisir est celle qui vous donne un résultat raisonnable à la fin.

**Décomposition matricielle.** Il existe de nombreuses méthodes de décomposition matricielle. Certaines, comme l'ACP, nécessitent une matrice carrée. D'autres sont robustes aux données manquantes. Avec les données de personnalité, le choix importe peu ; les résultats sont très similaires. Les vecteurs de mots généraux nécessitent environ 300 dimensions pour représenter le sens d'un mot, sa catégorie grammaticale, son argot et bien d'autres éléments qui donnent de la texture au langage. Comme les enquêtes sont conçues pour maintenir une grande partie de cela constant, seules environ 5 dimensions sont nécessaires. Thurstone a justifié son choix de cinq en examinant l'erreur de reconstruction qu'il rapporte sous forme d'histogramme. Plus tard, les psychologues ont justifié 5 par l'erreur de reconstruction (mesurée avec des valeurs propres), ainsi qu'en considérant l'interprétabilité et la reproductibilité.

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!Zw-J!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd562c1c2-1576-4fad-896c-52e799d4598b_1600x1066.png)Erreur de reconstruction de la matrice de corrélation des mots. Malgré les contraintes computationnelles, son échantillon est d'un ordre de grandeur plus grand que de nombreuses études modernes.

**Rotation.** Avez-vous déjà entendu parler de la surextraction de composantes ? Ce n'est pas une histoire que les psychologues vous raconteraient. C'est quand un chercheur extrait trop de composantes principales et transfère ensuite la variance des premières CP valides sur les CP marginales ultérieures. C'est ce qui est arrivé avec les Big Five, croyez-le ou non ! Ce qui est maintenant l'Agréabilité était autrefois un facteur de 'Socialisation' beaucoup plus robuste et théoriquement satisfaisant, qui a été réparti sur les CP 3-5 pour créer la Conscienciosité, le Névrosisme et l'Ouverture. La rotation _peut_ être justifiée pour produire des facteurs interprétables. Mais si vous vous retrouvez à faire des rotations puis à débattre du nombre correct de facteurs, vérifiez-vous !

**Les Big Three à partir des vecteurs de mots**

J'ai commencé mon doctorat en prédisant les traits des Big Five à partir des statuts Facebook. Après avoir lu comment la "saucisse de personnalité" était fabriquée, j'ai réalisé que le projet utilisait des vecteurs de mots (des statuts Facebook) pour prédire des approximations bruyantes de l'endroit où les individus se situaient dans l'espace des Big Five, qui était à l'origine défini par des vecteurs de mots. Il semblait plus intéressant d'aller droit au but et d'apprendre quelque chose de fondamental sur la personnalité à partir des vecteurs de mots. (De plus, le jeu de données que j'utilisais est devenu toxique après Cambridge Analytica.) Le reste de mon doctorat a consisté à contraindre les vecteurs de mots afin de reproduire les Big Five. Cela impliquait d'utiliser des transformateurs plutôt que l'ASL (plus à ce sujet dans de futurs articles). La corrélation résultante entre les facteurs des vecteurs de mots (DeBERTa) et les enquêtes est ci-dessous. Comme vous pouvez le voir, il y a un accord très étroit pour les trois premiers facteurs. Là où les résultats divergent, il n'est pas clair quelle méthode est en erreur. Peut-être que les enquêtes ont raison, et que toutes les corrélations iront à 1 lorsque nous aurons GPT-5. Peut-être que les enquêtes sont simplement biaisées et bruyantes, et que trop de CP ont été extraites. Peut-être qu'elles mesurent des choses différentes, et nous devons affiner notre interprétation des deux. En tout cas, il ne m'est pas évident que les enquêtes devraient être considérées comme la norme d'or entre les deux. L'hypothèse lexicale concerne la structure du langage, après tout, et la psychologie est le seul domaine qui utilise des enquêtes pour analyser le langage naturel.

[*[Image: Visual content from original post]*](https://substackcdn.com/image/fetch/$s_!lY1-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6bf087b4-76cc-4272-a2f7-037d606ed2ba_726x682.png)Les CP non rotées de l'enquête proviennent de l'une des [études](https://onlinelibrary.wiley.com/doi/10.1002/\(SICI\)1099-0984\(199603\)10:1%3C61::AID-PER246%3E3.0.CO;2-D) qui ont défini les Big Five. Les CP DeBERTa sont extraites des vecteurs de mots. Lisez à propos de ce processus [ici](https://psyarxiv.com/gdm5v/).

**Conclusion**

Thurstone a été un pionnier des méthodes statistiques et de l'algèbre linéaire pour explorer l'hypothèse lexicale dans les années 30. Il est remarquable qu'il ait développé une manière de représenter les mots qui a été redécouverte plus tard pour la recherche d'information, qui alimente maintenant l'ère de l'information. Le calcul a forcé Thurstone à aplatir le riche paysage du langage en réponses d'enquête. Au cours des 30 dernières années, le traitement du langage naturel a connu de multiples révolutions. Si Thurstone a inventé un télescope pour observer la structure du langage, nous avons maintenant Hubble. De nombreuses découvertes nous attendent !