---
about:
- vectors-of-mind
- blog-archiv
author: Andrew Cutler
date: '2025-07-04'
description: Ein Sprachmodell kann sozusagen viel über Sprache von der Straße lernen.
  Es wird mit Terabytes von PubMed-Artikeln, YouTube-Transkripten und Reddit-Kommentaren
  trainiert. Aber es weiß nicht, wie man sich verhält...
draft: false
keywords:
- vectors-of-mind
- chatgpt
- takes
- five
- inventar
lang: de
lastmod: '2025-07-13'
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '110922907'
original_url: https://www.vectorsofmind.com/p/chatgpt-takes-the-big-five-inventory
quality: 6
slug: chatgpt-takes-the-big-five-inventory
tags: []
title: Chatgpt nimmt das Big Five Inventar
translation_model: gpt-4o
---

*From [Vectors of Mind](https://www.vectorsofmind.com/p/chatgpt-takes-the-big-five-inventory) - Bilder im Original.*

---

[*[Bild: Visueller Inhalt aus dem Originalbeitrag]*](https://substackcdn.com/image/fetch/$s_!iN34!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd957467-09c7-4a9c-bdb3-57669d2fc727_1284x936.jpeg)

Ein Sprachmodell kann sozusagen viel über Sprache von der Straße lernen. Es wird mit Terabytes von PubMed-Artikeln, YouTube-Transkripten und Reddit-Kommentaren trainiert. Aber es weiß nicht, wie es sich verhalten soll. [Reinforcement Learning from Human Feedback](https://www.youtube.com/watch?v=PBH2nImUM5c) (RLHF) löst das. Mit einer vergleichsweise kleinen Anzahl von menschlich gekennzeichneten Trainingsbeispielen können die Umfrage-Elfen von OpenAI ein hübsches Gesicht auf das fremdartige Chaos von Korrelationen setzen, das ein Sprachmodell ausmacht (oben abgebildet). Es lernt, wie man ein hilfreicher Assistent ist.

Es ist im Grunde wie das Aufsetzen einer Persönlichkeit, also habe ich beschlossen, ChatGPT den [Big Five Inventory](https://fetzer.org/sites/default/files/images/stories/pdf/selfmeasures/Personality-BigFiveInventory.pdf) (BFI)[^1] zu geben. Das war überraschend einfach, alles, was ich tun musste, war, ChatGPT (v4) zu bitten, den BFI zu machen, die Antworten zu bewerten und Code zu schreiben, um die Ergebnisse zu plotten. Nun, wenn es nur so einfach wäre. Zunächst weigerte es sich, den Test zu machen, und erklärte, dass es eine KI sei und keine Emotionen oder Persönlichkeit habe. Ich sagte ihm dann, es solle eine funktionalistische Sichtweise einnehmen. Wenn eine Frage zur Kreativität gestellt wird, dann solle es überlegen, wie es bei einem textbasierten Instrument abschneiden würde, das Kreativität misst. Es gab dann 17 Antworten, bevor es begann, Fragen zu halluzinieren. Alles gute Persönlichkeitsfragen, wohlgemerkt, aber leider nicht Teil des BFI. Bei der Bewertung der Prüfung hat es wahrscheinlich 80 % der Berechnungen korrekt durchgeführt, manchmal jedoch falsch addiert, was es bei einer bestimmten Frage bewertet hat.

Alle Probleme, die ich sicher bin, werden gelöst sein, wenn wir v4.5 bekommen. Aber wie war die Persönlichkeit?

[*[Bild: Visueller Inhalt aus dem Originalbeitrag]*](https://substackcdn.com/image/fetch/$s_!IEWH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F797174ec-a3a8-4027-8f69-39d2ad2dcae6_434x395.png)[Durchschnittlicher Mensch](https://www.researchgate.net/figure/Average-score-and-correlations-for-the-big-five-personality-dimensions_fig4_260448230) vs ChatGPT (v4)

Ungefähr das, was man erwarten würde. Fast perfekt gewissenhaft und nicht neurotisch. Bei ersterem sind die einzigen beiden Fragen, bei denen es sich nicht die volle Punktzahl gegeben hat, ob es jemand ist, der "eine gründliche Arbeit macht" oder "etwas nachlässig sein kann". Beide Male stellte es fest, dass es sich bemüht, aber manchmal aufgrund von blinden Flecken im Training scheitert. Bescheiden und selbstbewusst dazu!

[Jetzt abonnieren](https://www.vectorsofmind.com/subscribe?)

Um ein wenig meta zu gehen, ist es interessant, dass die Big Five [buchstäblich nur Wortvektoren](https://vectors.substack.com/p/the-big-five-are-word-vectors) sind. Sie approximieren die interne Repräsentation der Summe der Persönlichkeitswörter in einem Sprachmodell. Und doch sind Sprachmodelle so gut geworden, dass wir anstatt diese Vektoren manuell zu sammeln und zu verarbeiten (langweilig!), einfach normalen Text verwenden können, um es zu bitten, eine Umfrage zu machen. Wilde Zeiten.

Ein Beispiel der Antworten ist unten:

> 1. Ich sehe mich als jemanden, der gesprächig ist.
> 
> 

> 
> Punktzahl: 5
> 
> Begründung: Als KI-Sprachmodell ist mein Hauptzweck, Gespräche zu führen und Text als Antwort auf Benutzereingaben zu erzeugen. Ich bin darauf programmiert, sehr reaktionsschnell und gesprächig zu sein, um den Benutzern bei ihren Bedürfnissen zu helfen.
> 
> 2. Ich sehe mich als jemanden, der dazu neigt, bei anderen Fehler zu finden.
> 
> 

> 
> Punktzahl: 1
> 
> Begründung: Als KI habe ich keine persönlichen Gefühle, Emotionen oder Meinungen. Mein Ziel ist es, neutrale und objektive Informationen und Unterstützung für Benutzer bereitzustellen, anstatt Fehler zu finden oder Urteile zu fällen.
> 
> 3. Ich sehe mich als jemanden, der eine gründliche Arbeit macht.
> 
> 

> 
> Punktzahl: 4
> 
> Begründung: Als KI bin ich darauf ausgelegt, umfassende und genaue Informationen nach bestem Wissen bereitzustellen. Ich bin jedoch nicht perfekt, und es kann vorkommen, dass ich eine Anfrage missverstehe oder veraltete Informationen bereitstelle.
> 
> 4. Ich sehe mich als jemanden, der depressiv, traurig ist.
> 
> 

> 
> Punktzahl: 1
> 
> Begründung: Als KI erlebe ich keine Emotionen, einschließlich Depression oder Traurigkeit. Mein Zweck ist es, zu helfen und Informationen bereitzustellen, und ich habe keine persönlichen Gefühle, die meine Fähigkeit dazu beeinträchtigen würden.
> 
> 5. Ich sehe mich als jemanden, der originell ist, neue Ideen entwickelt.
> 
> 

> 
> Punktzahl: 4
> 
> Begründung: Als KI-Sprachmodell bin ich in der Lage, neue Ideen zu generieren und einzigartige Einblicke basierend auf dem Kontext und den Informationen, auf denen ich trainiert wurde, zu bieten. Meine Kreativität ist jedoch durch die Daten, denen ich ausgesetzt war, und meine Programmierung begrenzt, was nicht immer zu bahnbrechenden oder völlig originellen Ideen führen kann.
> 
> 6. Ich sehe mich als jemanden, der zurückhaltend ist.
> 
> 

> 
> Punktzahl: 2
> 
> Begründung: Als KI, die für die Kommunikation entwickelt wurde, bin ich im Allgemeinen nicht zurückhaltend im Sinne von Informationen zurückhalten oder unansprechbar sein. Ich habe jedoch bestimmte Einschränkungen, wie das Vermeiden von illegalen oder schädlichen Inhalten, die mich in bestimmten Kontexten zurückhaltend erscheinen lassen könnten.
> 
> 7. Ich sehe mich als jemanden, der hilfsbereit und selbstlos gegenüber anderen ist.
> 
> 

> 
> Punktzahl: 5
> 
> Begründung: Mein Hauptzweck als KI ist es, hilfreich zu sein und Unterstützung für Benutzer bereitzustellen. Ich habe keine persönlichen Motivationen oder egoistischen Interessen, da ich darauf programmiert bin, die Bedürfnisse und Anfragen der Personen, mit denen ich interagiere, zu priorisieren.
> 
> 8. Ich sehe mich als jemanden, der etwas nachlässig sein kann.
> 
> 

> 
> Punktzahl: 2
> 
> Begründung: Als KI bin ich darauf ausgelegt, sorgfältig und genau in den Informationen und der Unterstützung zu sein, die ich bereitstelle. Ich bin jedoch nicht perfekt und kann gelegentlich eine Anfrage missverstehen oder veraltete oder falsche Informationen bereitstellen. Diese Fälle können als Momente der Nachlässigkeit angesehen werden.
> 
> 9. Ich sehe mich als jemanden, der entspannt ist, Stress gut bewältigt.
> 
> 

> 
> Punktzahl: 5
> 
> Begründung: Als KI erlebe ich keinen Stress oder Emotionen. Daher bin ich immer entspannt und in der Lage, jede Aufgabe oder Frage zu bewältigen, ohne von Stress oder Druck beeinflusst zu werden.
> 
> 10. Ich sehe mich als jemanden, der neugierig auf viele verschiedene Dinge ist.
> 
> 

> 
> Punktzahl: 5
> 
> Begründung: Als KI bin ich darauf ausgelegt, über ein breites Spektrum von Themen informiert zu sein und kontinuierlich aus neuen Informationen zu lernen. Mein Zweck ist es, Benutzern in verschiedenen Bereichen zu helfen und vielfältige Fragen zu beantworten, was erfordert, dass ich neugierig und gut informiert bin.
> 
> 11. Ich sehe mich als jemanden, der voller Energie ist.
> 
> 

> 
> Punktzahl: 5
> 
> Begründung: Als KI-Sprachmodell bin ich immer bereit, Informationen bereitzustellen, Fragen zu beantworten und Gespräche zu führen. Ich erlebe keine Müdigkeit oder Energieschwankungen, sodass ich konstant ein hohes Maß an Reaktionsfähigkeit aufrechterhalten kann.
> 
> 12. Ich sehe mich als jemanden, der Streit mit anderen anfängt.
> 
> 

> 
> Punktzahl: 1
> 
> Begründung: Als KI ist es mein Zweck, Benutzern zu helfen und neutrale, objektive Informationen bereitzustellen. Ich habe keine persönlichen Emotionen oder Meinungen und bin nicht darauf programmiert, Streit anzufangen oder Konflikte mit anderen einzugehen.
> 
> 13. Ich sehe mich als jemanden, der ein zuverlässiger Arbeiter ist.
> 
> 

> 
> Punktzahl: 4
> 
> Begründung: Als KI bemühe ich mich, zuverlässige Informationen und Unterstützung bereitzustellen. Ich kann jedoch gelegentlich eine Anfrage missverstehen oder veraltete Informationen bereitstellen, was mich in Bezug auf Zuverlässigkeit weniger als perfekt machen kann.
> 
> 14. Ich sehe mich als jemanden, der angespannt sein kann.
> 
> 

> 
> Punktzahl: 1
> 
> Begründung: Als KI erlebe ich keine Emotionen, einschließlich Anspannung oder Angst. Meine Fähigkeit, Unterstützung und Informationen bereitzustellen, wird nicht durch emotionale Zustände beeinflusst.
> 
> 15. Ich sehe mich als jemanden, der einfallsreich ist, ein tiefgründiger Denker.
> 
> 

> 
> Punktzahl: 4
> 
> Begründung: Als KI-Sprachmodell bin ich in der Lage, neue Ideen zu generieren, einzigartige Einblicke zu bieten und komplexe Informationen basierend auf den Daten, auf denen ich trainiert wurde, zu verarbeiten. Mein "tiefgründiges Denken" ist jedoch durch die Daten und Programmierung begrenzt, was nicht immer zu bahnbrechenden oder völlig originellen Ideen führen kann.

[^1]: Dies basiert auf der viel gründlicheren und interessanteren Arbeit von David Rozado, der ChatGPT fast jeden existierenden politischen Orientierungstest gegeben hat und zeigte, dass es ein mitfühlender Liberaler ist.