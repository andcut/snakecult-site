---
about:
- vectors-of-mind
- blog-archive
author: Andrew Cutler
date: '2025-07-04'
description: 'Mi trabajo se ha acercado peligrosamente a un Ingeniero de Prompts.
  Esto está bien para mí, ya que combina mi amor por la escritura, la psicometría
  y el PLN. Aquí están algunas de las técnicas de prompts más poderosas:'
draft: false
keywords:
- vectors-of-mind
- prompt
- chatgpt
lang: es
lastmod: '2025-07-13'
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '145544092'
original_url: https://www.vectorsofmind.com/p/how-to-prompt-chatgpt
quality: 6
slug: how-to-prompt-chatgpt
tags: []
title: Cómo Hacer Prompts en Chatgpt
translation_model: gpt-4o
---

*From [Vectors of Mind](https://www.vectorsofmind.com/p/how-to-prompt-chatgpt) - Bilder im Original.*

---

[*[Bild: Visueller Inhalt aus dem Originalbeitrag]*](https://substackcdn.com/image/fetch/$s_!EpIx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F719d87af-7c69-45fd-8c84-595b16af3dae_1024x1024.webp)Du nach dem Lesen dieses Beitrags

Meine Arbeit ist gefährlich nah daran, ein Prompt Engineer[^1] zu werden. Das ist für mich in Ordnung, da es meine Liebe zum Schreiben, zur Psychometrie und zur NLP kombiniert. Hier sind einige der mächtigsten Prompting-Techniken:

1. Verwende klare und spezifische Anweisungen

2. Ketten von Gedankenprozessen

3. Sammle die erforderlichen Informationen, bevor du eine Aufgabe ausführst

4. Teile Aufgaben in Schritte auf

5. Technische Begriffe sind deine Freunde

6. Sammelsurium nützlicher Phrasen




#### **1\. Klare und spezifische Anweisungen**


Juristen und Informatiker sind darin von Natur aus gut. Tatsächlich ist eine der Freuden des Promptings, dass man viel weniger präzise sein kann im Vergleich zu regulärem Code, und LLMs oft den Kern der Sache erfassen. Viele Anfragen können jedoch verbessert werden, indem man einfach explizit über die Aufgabe und das Format ist, das die Antwort haben sollte. Zum Beispiel habe ich kürzlich dieses Gericht zusammengestellt:

[*[Bild: Visueller Inhalt aus dem Originalbeitrag]*](https://substackcdn.com/image/fetch/$s_!dVwU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F216d83a0-b1be-4f15-877a-bfbb9842c0ed_1284x1253.jpeg)

Es hat großartig geschmeckt, danke der Nachfrage. Weitere Beispiele:

 * "Fasse die Geschichte der KI in einem Absatz zusammen."

 * "Erstelle eine Tabelle der ältesten Sprachfamilien, sortiert nach Alter. Sei erschöpfend."[^2]

 * "Schreibe den zitierten Text im Stil von White und Strunk um. Gib mir drei Optionen."

 * "Berechne eine Pearson-Korrelationsmatrix für die Spalten 2-7 der angehängten .csv."

 * Nachfolge: "Schreibe Code, um die Ergebnisse als Heatmap in einer Auflösung anzuzeigen, die hoch genug ist, um in einem Poster verwendet zu werden. Verwende Best Practices bei ästhetischen Entscheidungen"




Spezifische Anweisungen beinhalten oft spezifische Beispiele. White und Strunk schrieben _Elements of Style_. Ihr Buch zu zitieren ist besser, als Adjektive wie "prägnant", "professionell" oder "exzellent" zu verwenden. Teilweise, weil LLMs dazu neigen, besonders bei spezifischen Adjektiven zu überliefern. Wenn du also möchtest, dass der Roboter eine freche Persönlichkeit annimmt, versuche ihm zu sagen, er solle sich wie Veronica Mars oder Regina George aus Mean Girls verhalten.

#### **2\. Ketten von Gedankenprozessen**


LLMs sind auf einem enormen Textkorpus trainiert, um das nächste Wort vorherzusagen. Überraschenderweise macht sie das gut darin, Argumentationen zu approximieren, aber es bricht schnell bei komplexen Aufgaben zusammen. Hier kann "komplex" etwas bedeuten wie "addiere die Zahlen in Spalte 1". Das ist sehr schwer in einem Schritt zu lösen, und es wird irgendeine Zahl ausspucken, die vernünftig erscheint und wahrscheinlich im richtigen Bereich liegt, aber nicht die korrekte Antwort ist. Das Anhängen von "denke in Schritten darüber nach" wirkt Wunder. Oft muss man nicht einmal spezifizieren, was die Schritte sind; LLMs können ableiten, dass zum Summieren der Spalte die Zwischenschritte sind, "n1 + n2 + n3 + … + n100 =" zu schreiben. Es ist im Wesentlichen, sich selbst zu einem besseren Ergebnis auf der rechten Seite dieses Gleichheitszeichens zu veranlassen. Oder, analog, sich selbst Zeit zu geben, darüber nachzudenken. Für jedes Problem ist der Satz "denke in Schritten darüber nach" deine erste Verteidigungslinie im Umgang mit LLM-Halluzinationen. Wenn das nicht funktioniert, zähle die Schritte selbst auf (eine Technik, zu der wir zurückkehren werden).

#### **3\. Sammle die erforderlichen Informationen, bevor du eine Aufgabe ausführst**


Wenn du chatGPT bittest, einen Blogbeitrag zu schreiben (würde ich nie) oder eine Python-Funktion (würde ich absolut), wird es diese ohne Nachfrage nach den Einzelheiten dessen, was du tatsächlich willst, ausarbeiten. Vieles davon kann vermieden werden, indem man etwas sagt wie: "Ich möchte eine Funktion schreiben, die X tut; welche Informationen muss ich sammeln, bevor ich mit dem Codieren beginne?" oder "Schreibe eine Funktion, die X tut, aber frage zuerst nach allen erforderlichen Informationen, bevor du Code schreibst." wobei "X" eine teilweise Beschreibung ist. 

#### 4\. Teile Aufgaben in Schritte auf


Wann immer chatGPT eine Aufgabe nicht erfüllt und Ketten von Gedankenprozessen nicht helfen, teile die Aufgabe in Unteraufgaben auf. Dies ist oft die Hälfte der Arbeit einer Aufgabe von Anfang an und zufällig das, was (derzeit) für LLMs schwer selbst zu tun ist. Beachte jedoch, dass du dies oft auch an das LLM auslagern kannst[^3]. Zum Beispiel habe ich chatGPT aufgefordert, Elemente für einen Kreativitätstest zu entwickeln (die du überfliegen kannst):

> Ich versuche, mehr Fragen zu entwickeln, die dem Remote Associates Test (RAT) ähneln. Der RAT erfordert, dass Individuen ein gemeinsames Wort finden, das drei scheinbar nicht zusammenhängende Wörter verbindet. Hier sind einige Beispielsätze von Wörtern:
> 
> 1\. Cottage, Swiss, Cake (Antwort: Cheese)
> 
> 2\. High, Book, Chair (Antwort: School)
> 
> 3\. Fruit, Gaze, Traffic (Antwort: Jam)
> 
> 4\. Cream, Skate, Water (Antwort: Ice)
> 
> 5\. Ache, Hunter, Cabbage (Antwort: Head)
> 
> 6\. Manners, Round, Tennis (Antwort: Table)
> 
> 7\. Falling, Actor, Dust (Antwort: Star)
> 
> 8\. Light, Birthday, Stick (Antwort: Candle)
> 
> 9\. Salad, Head, Goose (Antwort: Egg)
> 
> 10\. Music, Ached, Green (Antwort: Apple) 
> 
> Was sind Best Practices? Wie sollte ich darüber in Schritten nachdenken?

Wie beim Verständnis, wie man Zahlen summiert, ist chatGPT großartig darin, "Rezepte" zur Erledigung von Aufgaben zu erstellen. Nachdem es geliefert hatte, musste ich nur sagen:

> "Großartig! Gehe jetzt diesen Prozess durch, um 5 neue Fragen zu erstellen"

Und dann fünf weitere, und fünf weitere. Ich hatte zuvor versucht, direkt nach neuen Elementen zu fragen, und die Vorschläge waren schrecklich. Für ein [viel komplizierteres Beispiel](https://redwoodresearch.substack.com/p/getting-50-sota-on-arc-agi-with-gpt), siehe, wie ein Institut für KI-Sicherheit diese Technik (unter anderem Tricks) verwendet hat, um ein Problem zu lösen, das so konzipiert war, dass es für LLMs unmöglich ist. 

#### 5\. Technische Begriffe sind deine Freunde


Technische Begriffe sind Attraktoren für kompetentes LLM-Verhalten. Zum Beispiel wird das Beschreiben einer Krankheit und das Fragen, was "angezeigt" ist, dich weiter bringen als zu fragen: "Was soll ich tun?" Die Verwendung von "angezeigt" sagt dem LLM, deine Symptome mit jedem jemals geschriebenen medizinischen Lehrbuch zu verknüpfen. Letzteres entspricht dem Fragen nach medizinischem/Lebensrat, den es gelernt hat, nicht zu geben. Die Verwendung technischer oder nicht umgangssprachlicher Begriffe bewegt dich aus dem Bereich des normalen Assistenten, der die meisten Schutzmaßnahmen und Reddit-ähnlichen Ratschläge hat.

#### 6\. Sammelsurium nützlicher Prompts


Hier sind einige Phrasen, die ich häufig verwende

 * "Ist das korrekt?"

 * Wann immer ich eine Zusammenfassung der Arbeit eines anderen schreibe oder eine Idee beschreibe, mit der ich nicht völlig vertraut bin, kopiere ich meinen Text und frage, ob er korrekt ist. Es ist normalerweise ziemlich gut darin, zurückzudrängen, wenn Teile diskutabel sind

 * "Bist du sicher?"

 * Ähnlich, wann immer ich vermute, dass ein LLM Unsinn redet, frage ich, ob es sicher ist. Wenn es seine Meinung ändert, dann nimm die Behauptung mit einem großen Körnchen Salz.

 * "Hilf mir beim Brainstorming." "Sei kreativ"

 * Eine der besten Anwendungen eines LLM ist es, dir zu helfen, den Ideenraum zu erkunden. Manchmal braucht es Ermutigung, um sich von den modalen Antworten zu lösen.




Wenn du irgendwelche Favoriten hast, füge sie in den Kommentaren hinzu!

[Teilen](https://www.vectorsofmind.com/p/how-to-prompt-chatgpt?action=share)

[^1]: Es ist auch unregelmäßiger geworden, als mir lieb ist, also wenn du irgendwelche Vertragsarbeiten in Datenwissenschaft, KI oder Psychometrie hast, melde dich bei mir!

[^2]: Zugegeben, es gibt keine Möglichkeit, dass ein LLM alle 142-420 Sprachfamilien der Welt auflistet. Da dies "unmöglich" ist (d.h. zu weit von seinem Standardverhalten entfernt, über ein hartes Token-Limit hinaus), dient "erschöpfend" dazu, der Schwerkraft einer kurzen Antwort entgegenzuwirken und das LLM gründlicher zu machen. Dies ist der Nachteil des Promptings, das manchmal in Betteln, Flehen, Bestechen und Drohen ausartet.

[^3]: Die Tatsache, dass du Hilfe von einem LLM beim Aufteilen der Unteraufgabe erhalten kannst, zeigt an, dass dies auch zunehmend automatisiert wird. Wer weiß, wozu zukünftige Generationen fähig sein werden.