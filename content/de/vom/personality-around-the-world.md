---
about:
- vectors-of-mind
- blog-archive
author: Andrew Cutler
date: '2025-07-04'
description: Bien, tomemos un pequeño respiro de las cosas de la sapiencia. En realidad
  tenía un montón de psicometría preparada antes de ser atraído por el llamado claro
  de la conciencia. Es tan difícil mirar hacia otro lado...
draft: false
keywords:
- vectors-of-mind
- personalidad
- alrededor
- mundo
lang: es
lastmod: '2025-07-13'
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '108601152'
original_url: https://www.vectorsofmind.com/p/personality-around-the-world
quality: 6
slug: personality-around-the-world
tags: []
title: Personalidad Alrededor Del Mundo
translation_model: gpt-4o
---

*Von [Vectors of Mind](https://www.vectorsofmind.com/p/personality-around-the-world) - Bilder im Original.*

---

Okay, lassen Sie uns eine kleine Pause von der Sapienz-Sache machen. Ich hatte tatsächlich eine Menge Psychometrie vorbereitet, bevor ich vom klaren Ruf des Bewusstseins angezogen wurde. Es ist einfach so schwer, wegzuschauen.

[*[Bild: Visueller Inhalt aus dem Originalbeitrag]*](https://substackcdn.com/image/fetch/$s_!X2nA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F62106fb3-6e73-444d-96f1-07b95ec828f9_1024x506.jpeg)[Ulysses und die Sirenen](https://en.wikipedia.org/wiki/Ulysses_and_the_Sirens_\(Waterhouse\)), Gemälde von [John William Waterhouse](https://en.wikipedia.org/wiki/John_William_Waterhouse)

Ich habe diesen Blog gestartet, um die Lexikalische Hypothese aus einer maschinellen Lernperspektive zu erkunden. Persönlichkeitsmodelle definieren die am meisten diskutierten Eigenschaften in einer Sprache, und wir können das im Zeitalter von GPT viel besser messen. Persönlichkeitsmodelle, die entweder aus Wortvektoren oder traditionellen Umfragen abgeleitet werden, kommen immer wieder auf dieselben wenigen Eigenschaften zurück, insbesondere die Großen Zwei: soziale Selbstregulation und Dynamik. Für eine Auffrischung dazu schauen Sie sich [Die Big Five sind Wortvektoren](https://vectors.substack.com/p/the-big-five-are-word-vectors) und [Der Primärfaktor der Persönlichkeit](https://vectors.substack.com/p/primary-factor-of-personality-part) an.

Die Big Five wurden in vielen Sprachen unabhängig voneinander gefunden, aber der Vergleich zwischen den Sprachen ist immer qualitativ. Forscher führen eine Umfrage zu Persönlichkeitsadjektiven in Türkisch oder Deutsch durch, faktorisieren sie und betrachten die Faktoren, um zu sehen, ob sie gleich sind. Diese Daten können nicht verwendet werden, um zu sagen: "Extraversion ist um 15 Grad von Gewissenhaftigkeit in Deutsch im Vergleich zu Englisch verschoben." Um so präzise zu sein, müssten beide Sprachen eine gemeinsame Basis teilen.

Wenn Sie Fragen in mehreren Sprachen stellen, können Sie sie durch 1) Finden einer zweisprachigen Kohorte, die in beiden Sprachen antworten kann, oder 2) Annahme, dass die Übersetzungen der Wörter 1:1 sind (z.B. _fun_ ist perfekt äquivalent zu _divertido_ in Spanisch), in Beziehung setzen. Im ersten Fall gibt es einen starken Selektionseffekt. Was, wenn zweisprachige Menschen tendenziell besser gebildet sind? Letzteres ist einfach nicht wahr. Tatsächlich besteht der Grund, Sprachen zusammen zu faktorisieren, darin, zu verstehen, wie sich die Persönlichkeitsstruktur zwischen ihnen unterscheiden kann. Die Annahme, dass die Wörter gleich sind, widerspricht dem Zweck.

**[Meine Forschung](https://arxiv.org/abs/2203.02092) zeigte, dass man Persönlichkeitsstrukturen aus Sprachmodellen im Englischen extrahieren kann. Eine natürliche Frage ist, wie sich das ändert, wenn man andere Sprachen hinzufügt.** Mit Modellen, die auf Dutzenden von Sprachen trainiert sind, wird dies ziemlich schmerzlos zu erkunden. Sie können eine beliebige Anzahl von Sprachen auf dieselbe Basis abbilden.

## Die Großen Zwei, noch einmal

Ich habe [XLM-RoBERTa](https://huggingface.co/xlm-roberta-base) verwendet, um die Ähnlichkeit zwischen Persönlichkeitsadjektiven zuzuweisen. Seltsamerweise ist dieses Modell ein Ergebnis des Völkermords in Myanmar. Meta befindet sich in der unenviablen Position, Inhalte in Regionen entfernen zu müssen, von denen sie sehr wenig verstehen. Technisch gesehen ist dies ein sogenanntes Transfer-Learning-Problem. Sie möchten einen Hassrede-Klassifikator in Englisch (oder einer anderen gut dokumentierten Sprache) trainieren und diesen dann auf andere Sprachen anwenden. In den dunklen Zeiten der Sprachmodellierung (2018) funktionierte dies sehr schlecht. Umgangssprachliche Rede auf Burmesisch für "lasst uns die Schwulen zusammentreiben und töten" sah für ihre Klassifikatoren aus wie "es sollte weniger Regenbögen geben". Dies rutschte natürlich an ihrer Inhaltsmoderation vorbei. Die NYT erklärte die Konsequenz: _**[Ein Völkermord, angestiftet auf Facebook, mit Beiträgen des myanmarischen Militärs](https://www.nytimes.com/2018/10/15/technology/myanmar-facebook-genocide.html)**_

Metas Antwort war, ein Sprachmodell zu bauen, das jede Sprache (nun, 100 Sprachen) besser auf Wortvektoren im selben gemeinsamen Raum abbilden kann. Auf diese Weise kann ein in Englisch trainierter Hassrede-Klassifikator besser auf andere Sprachen ausgeweitet werden. (Weniger Burmesisch ist nötig, um es fein abzustimmen.) Mit diesem Modell habe ich Persönlichkeitswörter in vier Sprachen eingebettet: Englisch, Spanisch, Französisch und Türkisch. Unten sind die ersten beiden Faktoren:

[*[Bild: Visueller Inhalt aus dem Originalbeitrag]*](https://substackcdn.com/image/fetch/$s_!eLVQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd3ff00d-d96d-4e3b-ada4-640e3cd66089_1245x954.png)

Diese dienen dazu, die verschiedenen Sprachen zu trennen. Der erste Faktor unterscheidet Türkisch von den indoeuropäischen Sprachen. Beim zweiten Faktor sind die romanischen Sprachen benachbart (obwohl auch nahe an Türkisch).

Das macht Sinn. Das Modell ist darauf trainiert, das nächste Wort eines Satzes vorherzusagen, und wird daher natürlich sprachspezifische Informationen enthalten. Wenn jemand auf Spanisch spricht, wechselt er nicht oft zu Türkisch. Die Hoffnung ist, dass es auch Richtungen im Vektorraum gibt, die Persönlichkeitsinformationen entsprechen.

Wenn Sprachen ziemlich unabhängig sind, benötigen Sie mindestens 3 Dimensionen, um 4 Sprachen in ihren eigenen, nicht überlappenden Gruppen zu trennen. Schauen wir uns die nächsten Hauptkomponenten an.

[*[Bild: Visueller Inhalt aus dem Originalbeitrag]*](https://substackcdn.com/image/fetch/$s_!PRKA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5eb70bd2-8684-4844-94bd-aa12adc030bf_1256x954.png)

Faktor 4 ist der erste Faktor, der nicht gelernt wurde, um die Sprachen zu trennen, und es ist der Allgemeine Persönlichkeitsfaktor! Auf Englisch: _dominant, rücksichtslos, zwanghaft_ und _egoistisch_ **vs** _großzügig, sanft_ und _nachdenklich_. [Ich habe argumentiert](https://vectors.substack.com/p/primary-factor-of-personality-part), dass dieser Faktor am besten als die Tendenz verstanden wird, die Goldene Regel zu leben. Die Eva-Theorie des Bewusstseins war tatsächlich ein Ergebnis des [Nachdenkens darüber, was dies in unserer evolutionären Geschichte selektieren würde](https://vectors.substack.com/p/consequences-of-conscience). Faktor 5 handelt ebenfalls von Persönlichkeit, und wenn man sie zusammen darstellt:

[*[Bild: Visueller Inhalt aus dem Originalbeitrag]*](https://substackcdn.com/image/fetch/$s_!pD64!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F192dc8f4-db5e-4d96-b8a5-ce16c1cbf1f6_1264x954.png)

Wir erhalten die Großen Zwei! Faktor Fünf (oder zwei der Persönlichkeitsfaktoren) ist Dynamik: _abenteuerlustig, fantasievoll_ und _begeistert_ **vs** _vorsichtig, reserviert_ und _feige._ Es ist erstaunlich, dass dies so regelmäßig auftaucht. **Es gibt [2.500 Zitationen zum Big Two-Paper](https://scholar.google.com/scholar?cites=11052969740325606797&as_sdt=2005&sciodt=0,5&hl=en), und dennoch erkennen Forscher nicht, dass sie einfach die ersten beiden unrotierten Faktoren der allgemeinen Persönlichkeit sind.** Der allgemeine Glaube, dass sie irgendwie in einer hierarchischen Beziehung zu den Big Five existieren, stammt von Forschern, die kurz nach der Erstellung der Big Five-Inventare den direkten Umgang mit Sprache aufgegeben haben. Seitdem muss jeder Versuch, grundlegende oder allgemeine Persönlichkeit zu verstehen, in Bezug auf die Big Five erfolgen. Aber Wörter kamen zuerst, und Sprachmodelle machen es jetzt einfach, Sprache auf dieser grundlegenden Ebene zu analysieren.

[Teilen](https://www.vectorsofmind.com/p/personality-around-the-world?action=share)

## Wir müssen tiefer gehen

Das Hinzufügen von Russisch und Farsi ergibt dieselben Faktoren:

[*[Bild: Visueller Inhalt aus dem Originalbeitrag]*](https://substackcdn.com/image/fetch/$s_!IIKx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F976f1c11-fd97-4184-a74a-a384a09b0579_2078x1715.png)Um die Wörter besser zu sehen, laden Sie das Bild herunter und zoomen Sie hinein.

Nach meinen faulen Ingenieurstandards ist dies ziemlich arbeitsintensiv, da es erfordert, einen guten Prompt für jede Sprache zu finden. Ich habe mit Google Translate und Muttersprachlern zusammengearbeitet, um dies richtig hinzubekommen, und Sie können sehen, dass die Farsi-Verteilung bei Faktor 4 immer noch abweicht. Meine Vermutung ist, dass meine Methode, jeden nicht geteilten Faktor zu ignorieren, für so viele Sprachen zu ungenau ist. Faktor 4 wird wahrscheinlich als GFP verwendet und auch, um Farsi (ein wenig) zu trennen. Es gibt nichts, was diese Faktoren rein hält, wir haben wirklich Glück, dass die Verteilung so gutmütig ist, wie sie ist. Einige Vorverarbeitungen (wie das Nullsetzen jedes Sprachclusters) könnten dies lösen.

Meines Wissens ist dies das erste Mal, dass mehrere Sprachen zusammen faktorisert wurden. Dies wäre mit Ergebnissen nur auf Englisch und Spanisch veröffentlichbar, und hier habe ich es auf sechs gebracht, einschließlich zweier nicht-indoeuropäischer Sprachen. Es wirft auch Licht auf die Natur der Großen Zwei, einer der beliebtesten und missverstandenen Konstrukte in der Psychometrie.

## Schwächen

Ich habe diese Forschung auf die dümmste Art und Weise durchgeführt. Ich fand 100 Persönlichkeitswörter in einem ESL-Leitfaden und übersetzte diese dann mit Google Translate in andere Sprachen. Wenn es Duplikate gab, habe ich sie entfernt. Das ist nicht so schlimm, wie es scheint. Die ersten beiden Faktoren sind im Englischen praktisch unverändert, egal ob man 100 oder 500 Wörter verwendet. Aber wenn dies ein echtes Papier wäre, würde man natürlich ein Set von Wörtern in jedem Vokabular unabhängig entwickeln wollen. Es gibt mehrere andere Schwächen:

**Nicht genug Sprachen!** Wenn ich dies veröffentlichen würde, würde ich gerne ein Dutzend weiterer Sprachen hinzufügen, die in der Persönlichkeitsforschung normalerweise nicht untersucht werden. Das ist tatsächlich der Grund, warum ich nie dazu gekommen bin, es zu veröffentlichen. Das ist viel Arbeit und würde Muttersprachler mehrerer asiatischer Sprachen erfordern.

**Mehrsprachige Modelle, die durch Trainingsdaten verzerrt sind.** Sprachmodelle sind darauf trainiert, das nächste Wort eines Satzes vorherzusagen. Wenn Sie mit mehreren Sprachen trainieren, wird das Modell versuchen, einen Teil des Wissens zu übertragen. Für die kleineren Sprachen könnte dies jedoch eher so aussehen, als würden ihre Bedeutungen zu Analogien innerhalb der besser dokumentierten Sprachen (Englisch, Chinesisch, Russisch usw.) gezwungen.

**Die Anfragen sind ein Forscher-Freiheitsgrad.** Die Methode, die ich verwende, um Wörter einzubetten, ist "Meine Persönlichkeit kann beschrieben werden als <mask> und [Wort]", wobei [Wort] eines der Persönlichkeitswörter ist. Aufgrund der Art und Weise, wie der Satz geschrieben ist, lädt das Modell reine Persönlichkeitsinformationen auf das Masken-Token und bettet es dann ein. In meiner Dissertation fand ich, dass dies am besten funktionierte. Natürlich gibt es unendlich viele Variationen davon, und man muss eine auswählen. Theoretisch könnte ein Forscher ein bestimmtes Ergebnis im Kopf haben und dann eine Anfrage finden, die dieses unterstützt. Meiner Meinung nach ist das nicht allzu riskant, angesichts der Ähnlichkeit dieses Ergebnisses mit dem, was Umfragemethoden produzieren. Wir haben eine ziemlich starke Vorannahme darüber, welche Persönlichkeitsstruktur wir mit der Faktorenanalyse finden. Dass diese Methode es wiederholt, ist ein Beweis dafür, dass die Methode funktioniert.

**Veraltetes Sprachmodell.** Ich habe diese Arbeit vor über 2 Jahren gemacht, lange bevor GPT-4 herauskam. Einfachere Zeiten.

## Fazit

Wenn ich noch in der Wissenschaft wäre, wäre dies meine Forschungsagenda. So viele Sprachen wie möglich hinzufügen und versuchen, alle Möglichkeiten zu verstehen, wie die Methode voreingenommen sein kann. Am Ende könnte es ein universelles Persönlichkeitsmodell hervorbringen, das den Big Five überlegen ist. Es würde uns helfen, besser zu verstehen, wer wir sind, und vielleicht sogar, woher wir kommen. Denn es ist die Sprache, die unsere Spezies jetzt definiert, und es war die Sprache, die unsere Psyche tief in der Vergangenheit geformt hat. Wir sind gewohnheitsmäßig sozial, weil es vor Tausenden von Jahren bedeutete, zu sterben, wenn man seinen Ruf nicht managen konnte. Persönlichkeitsmodelle sind Karten der Sprache; sie sind Vektoren in der Evolution unseres Geistes.

[Jetzt abonnieren](https://www.vectorsofmind.com/subscribe?)

[*[Bild: Visueller Inhalt aus dem Originalbeitrag]*](https://substackcdn.com/image/fetch/$s_!MDwl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F935dcb92-8e91-41c3-9630-2a80f2bc9a06_1024x1024.png)