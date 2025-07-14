---
about:
- vectors-of-mind
- blog-archive
author: Andrew Cutler
date: '2025-07-04'
description: Los estudios léxicos en psicología y el Análisis Semántico Latente en
  informática se introdujeron con medio siglo de diferencia para resolver diferentes
  problemas y, sin embargo, son matemáticamente equivalentes. Esto no es un meta...
draft: false
keywords:
- vectors-of-mind
- cinco
- palabra
- vectores
lang: es
lastmod: '2025-07-13'
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '50351822'
original_url: https://www.vectorsofmind.com/p/the-big-five-are-word-vectors
quality: 6
slug: the-big-five-are-word-vectors
tags: []
title: Los Cinco Grandes Son Vectores de Palabras
translation_model: gpt-4o
---

*From [Vectors of Mind](https://www.vectorsofmind.com/p/the-big-five-are-word-vectors) - Bilder im Original.*

---

Lexikalische Studien in der Psychologie und die Latent-Semantic-Analyse in der Informatik wurden mit einem halben Jahrhundert Abstand eingeführt, um unterschiedliche Probleme zu lösen, und sind dennoch mathematisch äquivalent. Dies ist kein metaphorischer Vergleich auf einer bestimmten Abstraktionsebene _;_ die Big Five sind Dimensionen von [Wortvektoren](https://dzone.com/articles/introduction-to-word-vectors).

Zunächst jedoch etwas Hintergrundwissen. Die Lexikalische Hypothese besagt, dass die Persönlichkeitsstruktur in die Sprache eingeschrieben wird, da die Sprecher die auffälligsten Merkmale ihrer Mitmenschen beschreiben müssen. Die Schönheit dieser Idee liegt darin, dass nicht eine einzelne Person ein Modell der Persönlichkeit vorschlägt, sondern die Sprache aufzeichnet, was Millionen von Menschen implizit als nützlich erachten. Die Aufgabe des Psychometrikers besteht lediglich darin, diese Struktur zu identifizieren. Dies wurde typischerweise dadurch erreicht, dass Psychologiestudenten eingeladen wurden, sich selbst anhand von Listen von Adjektiven zu bewerten und eine Faktorenanalyse der Korrelationsmatrix durchzuführen. Bereits 1933 führte LL Thurstone eine Umfrage mit 60 Adjektiven bei 1300 Personen durch. In seinem wegweisenden Werk [The Vectors of Mind](http://psych.colorado.edu/~carey/Courses/PSYC5112/Readings/VectorsOfMind_Thurstone.pdf) berichtet er, dass "fünf Faktoren ausreichen", um die Daten zu erklären. In den folgenden Jahrzehnten führten solche Studien mehr oder weniger zu fünf Hauptkomponenten: Verträglichkeit, Extraversion, Gewissenhaftigkeit, Neurotizismus und Offenheit/Intellekt. (Für eine ausgezeichnete Behandlung des Themas siehe [Lexical Foundations of the Big Five](https://www.researchgate.net/profile/Boele-Raad-2/publication/282980275_The_Lexical_Foundation_of_the_Big_Five-Factor_Model/links/5626198508aed3d3f137e522/The-Lexical-Foundation-of-the-Big-Five-Factor-Model.pdf).)

Die Latent-Semantic-Analyse wurde [eingeführt](https://dl.acm.org/doi/abs/10.1145/57167.57214?casa_token=ogUyQ6VJeZgAAAAA:ksULYwu-Km_5Ap0wA2ho3tbwzTjsB0tHONfEEMIldNB6PJgkRyM7eFaa7uZ-XZJ3nYo0MbYFeJsBng) als Information Retrieval Technik im Jahr 1988. Wörter können als Vektoren dargestellt werden und Dokumente oder Sätze können als Mittelwert ihrer Wortvektoren dargestellt werden. Wenn Sie eine große Datenbank durchsuchen möchten (z.B. Wikipedia), reichen Schlüsselwörter für jede Seite nur bedingt aus. Eine Möglichkeit, dies zu umgehen, besteht darin, sowohl Dokumente (Wiki-Artikel) als auch Anfragen (Suchbegriffe) als Mittelwert ihrer Wortvektoren darzustellen. Relevante Dokumente können nun mit einem einfachen Skalarprodukt gefunden werden. (In diesem Beitrag behandle ich LSA und Wortvektoren als synonym. Es gibt andere Möglichkeiten, Sprache zu vektorisieren und speziell Wortvektoren zu erstellen, aber diese sind vorerst außerhalb des Rahmens.)

Trotz ihrer unterschiedlichen Anwendungen und Geschichte sind die Schritte die gleichen:

 1. Sammeln einer Wort x Dokument Häufigkeitsmatrix

 2. Nichtlineare Transformation

 3. Matrixzerlegung

 4. Rotation (Optional)

Das Ergebnis ist eine Reihe von Wortvektoren, die jedes Wort prägnant beschreiben. Diese können für eine Vielzahl von nachgelagerten Aufgaben verwendet werden, von der Sentiment-Analyse bis zur Vorhersage von Narzissmus aus Studentenaufsätzen. Im Fall von Persönlichkeitsadjektiven wurden die Dimensionen der Wortvektoren analysiert, benannt und über Jahrzehnte hinweg diskutiert. Im Folgenden wird auf die Unterschiede in jedem Schritt eingegangen.

**Häufigkeitsmatrix.** LSA umfasst in der Regel eine große Anzahl unterschiedlicher Dokumente (z.B. Millionen von Amazon-Produktbewertungen). Diese werden in eine Wort x Dokument Matrix umgewandelt, indem gezählt wird, wie oft jedes Wort in jedem Dokument vorkommt. In der Psychologie ist ein Dokument die Wörter, denen ein Proband zustimmt, dass sie ihn beschreiben. Dies erstreckt sich auch auf Likert-Skalen. Wenn jemand sagt, ein Wort beschreibe ihn 5/7, dann wird das Wort einfach fünfmal im Dokument wiederholt.

**Nichtlineare Transformation.** Lexikalische Studien ipsatisieren oft die Daten (z-Wert entlang der Subjektachse) und führen dann eine Pearson-Korrelation durch. Thurstone verwendete in seiner Studie eine archaische Tetrarchkorrelation. In der LSA ist die häufigste Transformation TF-IDF, gefolgt von einem Logarithmus. Dies stellt sicher, dass die Matrix nicht von allgemeinen Begriffen dominiert wird. Oft führt die Transformation zu einer Wort x Wort Affinitätsmatrix (z.B. Korrelationsmatrix). Dieser Schritt ist praktisch sehr wichtig, aber nicht allzu theoretisch. Die zu wählende Transformation ist diejenige, die am Ende ein vernünftiges Ergebnis liefert.

**Matrixzerlegung.** Es gibt viele Methoden der Matrixzerlegung. Einige, wie PCA, erfordern eine quadratische Matrix. Andere sind robust gegenüber fehlenden Daten. Bei Persönlichkeitsdaten spielt die Wahl keine große Rolle; die Ergebnisse sind sehr ähnlich. Allgemeine Wortvektoren erfordern ~300 Dimensionen, um die Bedeutung eines Wortes, Wortart, Slang und vieles mehr, was der Sprache Textur verleiht, darzustellen. Da Umfragen so gestaltet sind, dass vieles davon konstant gehalten wird, werden nur ~5 Dimensionen benötigt. Thurstone rechtfertigte seine Wahl von fünf, indem er den Rekonstruktionsfehler betrachtete, den er als Histogramm berichtet. Spätere Psychologen rechtfertigten 5 durch den Rekonstruktionsfehler (gemessen mit Eigenwerten) sowie durch die Berücksichtigung von Interpretierbarkeit und Reproduzierbarkeit.

[*[Bild: Visueller Inhalt aus dem Originalbeitrag]*](https://substackcdn.com/image/fetch/$s_!Zw-J!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd562c1c2-1576-4fad-896c-52e799d4598b_1600x1066.png)Rekonstruktionsfehler der Wortkorrelationsmatrix. Trotz der rechnerischen Einschränkungen ist seine Stichprobe um eine Größenordnung größer als viele moderne Studien.

**Rotation.** Haben Sie schon einmal von der Überextraktion von Komponenten gehört? Das ist keine Geschichte, die Ihnen die Psychologen erzählen würden. Es ist, wenn ein Forscher zu viele Hauptkomponenten extrahiert und dann die Varianz von den früheren, gültigen PCs auf die späteren marginalen PCs rotiert. Genau das ist mit den Big Five passiert, glauben Sie es oder nicht! Was heute Verträglichkeit ist, war einst ein viel robusterer und theoretisch befriedigender 'Sozialisations'-Faktor, der über die PCs 3-5 verteilt wurde, um Gewissenhaftigkeit, Neurotizismus und Offenheit zu schaffen. Rotation _kann_ gerechtfertigt sein, um interpretierbare Faktoren zu erzeugen. Aber wenn Sie sich jemals dabei ertappen, zu rotieren und dann über die richtige Anzahl von Faktoren zu streiten, überprüfen Sie sich selbst!

**Die Big Three aus Wortvektoren**

Ich begann meine Promotion mit der Vorhersage von Big Five Merkmalen aus Facebook-Statusmeldungen. Nachdem ich gelesen hatte, wie die Persönlichkeit "Wurst" gemacht wurde, erkannte ich, dass das Projekt Wortvektoren (von Facebook-Statusmeldungen) verwendete, um ungenaue Annäherungen daran vorherzusagen, wo Individuen im Big Five Raum lebten, der ursprünglich durch Wortvektoren definiert wurde. Es schien interessanter, direkt zur Sache zu kommen und etwas Grundlegendes über Persönlichkeit aus Wortvektoren zu lernen. (Außerdem wurde der Datensatz, den ich verwendete, nach Cambridge Analytica toxisch.) Der Rest meiner Promotion bestand darin, Wortvektoren einzuschränken, um die Big Five zu reproduzieren. Dies beinhaltete die Verwendung von Transformatoren anstelle von LSA (mehr dazu in zukünftigen Beiträgen). Die resultierende Korrelation zwischen Faktoren aus Wortvektoren (DeBERTa) vs. Umfragen ist unten dargestellt. Wie Sie sehen können, gibt es eine sehr enge Übereinstimmung für die ersten drei Faktoren. Wo die Ergebnisse abweichen, ist nicht klar, welche Methode im Fehler ist. Vielleicht haben Umfragen recht, und alle Korrelationen werden auf 1 gehen, wenn wir GPT-5 bekommen. Vielleicht sind Umfragen einfach voreingenommen und ungenau, und es wurden zu viele PCs extrahiert. Vielleicht messen sie unterschiedliche Dinge, und wir müssen unsere Interpretation beider verfeinern. Jedenfalls ist es für mich nicht offensichtlich, dass Umfragen zwischen den beiden als Goldstandard betrachtet werden sollten. Die Lexikalische Hypothese handelt schließlich von der Sprachstruktur, und die Psychologie ist das einzige Feld, das Umfragen verwendet, um natürliche Sprache zu analysieren.

[*[Bild: Visueller Inhalt aus dem Originalbeitrag]*](https://substackcdn.com/image/fetch/$s_!lY1-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6bf087b4-76cc-4272-a2f7-037d606ed2ba_726x682.png)Die unrotierten Umfrage-PCs stammen aus einer der [Studien](https://onlinelibrary.wiley.com/doi/10.1002/\(SICI\)1099-0984\(199603\)10:1%3C61::AID-PER246%3E3.0.CO;2-D), die die Big Five definierten. DeBERTa PCs werden aus Wortvektoren extrahiert. Lesen Sie über diesen Prozess [hier](https://psyarxiv.com/gdm5v/).

**Fazit**

Thurstone entwickelte in den 30er Jahren Methoden in Statistik und Linearer Algebra, um die Lexikalische Hypothese zu erforschen. Es ist bemerkenswert, dass er eine Methode entwickelte, um Wörter darzustellen, die später für das Information Retrieval wiederentdeckt wurde und nun das Informationszeitalter antreibt. Die Berechnung zwang Thurstone, die reiche Landschaft der Sprache auf Umfrageantworten zu reduzieren. In den letzten 30 Jahren hat die NLP mehrere Revolutionen erlebt. Wenn Thurstone ein Teleskop erfand, um die Sprachstruktur zu betrachten, haben wir jetzt Hubble. Viele Erkenntnisse warten!