---
about:
- vectors-of-mind
- blog-archive
author: Andrew Cutler
date: '2025-07-04'
description: La Teoría de la Conciencia de Eva propone que la autoconciencia fue descubierta
  por mujeres y se difundió meméticamente. Para argumentar esto, recurro a la lingüística,
  arqueología, farmacología, genética, antropología, ...
draft: false
keywords:
- vectors-of-mind
- basis
lang: es
lastmod: '2025-07-13'
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '121454386'
original_url: https://www.vectorsofmind.com/p/the-ai-basis-of-the-eve-theory-of
quality: 6
slug: the-ai-basis-of-the-eve-theory-of
tags: []
title: La Base de IA de la Teoría de Eva de
translation_model: gpt-4o
---

*From [Vectors of Mind](https://www.vectorsofmind.com/p/the-ai-basis-of-the-eve-theory-of) - Bilder im Original.*

---

[*[Bild: Visueller Inhalt aus dem Originalbeitrag]*](https://substackcdn.com/image/fetch/$s_!0pra!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff5166314-7a08-4939-9b16-2311d6214e87_1456x816.png)

Die [Eve-Theorie des Bewusstseins](https://vectors.substack.com/p/eve-theory-of-consciousness-v2) schlägt vor, dass das Selbstbewusstsein von Frauen entdeckt und memetisch verbreitet wurde. Um diesen Fall zu untermauern, ziehe ich [Linguistik](https://vectors.substack.com/p/the-unreasonable-effectiveness-of), [Archäologie](https://vectors.substack.com/i/95941288/the-genesis-of-religion), [Pharmakologie](https://vectors.substack.com/p/comments-on-snake-venom), [Genetik](https://vectors.substack.com/p/y-chromosome-bottleneck), [Anthropologie](https://vectors.substack.com/p/the-snake-cult-of-consciousness) und [Neurowissenschaften](https://vectors.substack.com/i/114650037/women-lead-the-way) heran. Und doch bin ich Elektroingenieur. Wie kann ich etwas Wertvolles zu einem Thema beitragen, in dem so viele andere tatsächlich ausgebildet sind? Nun, die Idee für EToC entstand tatsächlich aus dem maschinellen Lernen. Langjährige Leser haben [den Fortschritt des Blogs verfolgt](https://substack.com/profile/31996842-andrew/note/c-16789002) von ML-Psychometrie zu Rekursion und vergleichender Mythologie. Lassen Sie mich erklären, wie ich hierher gekommen bin.

## Persönlichkeitsstruktur aus Wörtern

Die Psychologie hat ein Grundwahrheitsproblem. Ein Forscher könnte theoretisieren, dass es nur wenige grundlegende Achsen gibt, auf denen Menschen variieren, wobei die wichtigste die Internalisierung vs. Externalisierung ist. Ein anderer könnte sagen, dass es etwa [30 grundlegende Faktoren](https://www.scholars.northwestern.edu/en/publications/exploring-the-persome-the-power-of-the-item-in-understanding-pers) geben muss, weil Menschen einfach so kompliziert sind. Wer hat Recht? Bereits 1890 schlug [Galton](https://astralcodexten.substack.com/p/galton-ehrlich-buck) vor, dass anstatt Psychologen Modelle der Persönlichkeit basierend auf ihren Lieblingstheorien zu entwickeln, das beste Modell bereits in der Sprache eingebettet sei. Jedes Persönlichkeitsadjektiv existiert, weil Millionen von Menschen es nützlich finden, wenn sie Urteile über andere fällen. Sicherlich müssen diese Wörter alle wichtigen Aspekte der Persönlichkeit beleuchten. Formal ausgedrückt als die Lexikalische Hypothese:

 1. Diejenigen Persönlichkeitsmerkmale, die für eine Gruppe von Menschen wichtig sind, werden schließlich Teil der Sprache dieser Gruppe.

 2. Wichtigere Persönlichkeitsmerkmale werden eher als ein einzelnes Wort in die Sprache kodiert.

Diese Idee kann verwendet werden, um ein Persönlichkeitsmodell zu erstellen. Erstellen Sie einfach eine Liste von Persönlichkeitsadjektiven, sehen Sie, wie sie sich zueinander verhalten, und komprimieren Sie diese auf einige latente Faktoren[^1]. (LL Thurstone erfand die Faktorenanalyse, um dies zu tun, und das [Papier](https://psycnet.apa.org/record/1934-02322-001) ist der Namensgeber dieses Blogs.) Traditionell wurden die Beziehungen zwischen Adjektiven geschätzt, indem Psychologie-Studenten gefragt wurden, welche Wörter sie am besten beschreiben. Diejenigen, die sagen, sie seien _intelligent_, neigen auch dazu zu sagen, sie seien _aufgeschlossen_. Dies deutet darauf hin, dass sie sich beide auf einen zugrunde liegenden Faktor beziehen. In meiner Dissertation [habe ich Sprachmodelle verwendet, um Wortähnlichkeiten zu schätzen](https://vectors.substack.com/p/the-big-five-are-word-vectors) und erzielte Ergebnisse, die den traditionellen Umfragen ähneln (der erste Faktor der beiden Methoden korreliert mit r=0,93).

Es ist am einfachsten, diesen Prozess anhand eines Beispiels zu verstehen. Hier sind 100 zufällige Persönlichkeitsadjektive, die auf den beiden Dimensionen geplottet sind, die die meisten Persönlichkeitsinformationen erfassen. Denken Sie an diese als zwei der [Big Five](https://en.wikipedia.org/wiki/Big_Five_personality_traits) (obwohl es [einen Unterschied in der Art und Weise gibt, wie sie rotiert sind](https://vectors.substack.com/i/61936908/relation-to-the-big-five)). Eine der Aufgaben eines Persönlichkeitspsychologen ist es, solche Plots zu betrachten und sie qualitativ zu beschreiben. Sie können diese Übung in [Guess the Factor](https://vectors.substack.com/p/guess-the-factor) üben oder dies unten tun. Wie würden Sie Faktor 1 zusammenfassen?

[*[Bild: Visueller Inhalt aus dem Originalbeitrag]*](https://substackcdn.com/image/fetch/$s_!N5Ou!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3c50c0d0-6e09-4758-bfad-6c9135f154af_1423x891.png)Faktoren 1 und 2 werden mit [PCA](https://builtin.com/data-science/step-step-explanation-principal-component-analysis) erzeugt, einer Methode, um die Persönlichkeitsinformationen auf die kleinste Anzahl von Achsen zu destillieren. Weitere Informationen darüber, wie man diese aus Wortvektoren erhält, finden Sie in meinem Papier [Deep Lexical Hypothesis](https://arxiv.org/abs/2203.02092). Sie können dieses Ergebnis (und vieles mehr) auch mit meinem [Code](https://colab.research.google.com/drive/1SXZNVqH0m_Bnd2hvIJFYiKQvHWpGu8ZM?usp=sharing) reproduzieren, der kostenlos auf Google Colab läuft.

Aus statistischer Sicht hat sich Faktor 1 entblößt und schwenkt eine große Fahne "Ich bin bei weitem der wichtigste", wie ich im [Primary Factor of Personality](https://vectors.substack.com/p/primary-factor-of-personality-part) (PFP) erkläre. Qualitativ ist es im Wesentlichen "was die Gesellschaft von Ihnen will". Seien Sie rücksichtsvoll und respektvoll, seien Sie nicht hochnäsig oder unkooperativ.

Um PFP (Faktor 1) auf eine andere Weise zu abstrahieren, ist es nützlich, 2.000 Jahre zurückzugehen. Die Israeliten hatten Bibliotheken, die sich sozialen Regeln und ihrer richtigen Anwendung widmeten. Mit Jahrhunderten der Debatte und Interpretation vervielfachte sich der Buchstabe des Gesetzes. Aber es gab auch eine Bewegung, den Geist des Gesetzes zu destillieren.

Laut der traditionellen Erzählung näherte sich ein potenzieller Konvertit Rabbi Shammai und bat ihn, die gesamte Tora zu erklären, während er auf einem Bein stand. Rabbi Shammai, bekannt für seine strikte Einhaltung des jüdischen Gesetzes, fand die Frage respektlos und wies den Konvertiten ab.

Unbeirrt näherte sich der Konvertit dann Rabbi Hillel mit derselben Bitte. Hillel, bekannt für sein Mitgefühl und seine Weisheit, reagierte auf eine andere Weise. Anstatt den Konvertiten abzulehnen, nahm Hillel die Herausforderung an und gab eine prägnante Zusammenfassung der Tora, während er auf einem Bein stand. Er sagte: "Was dir verhasst ist, tue deinem Nächsten nicht an: Das ist die ganze Tora; der Rest ist der Kommentar."

Dies ist auch eine ausgezeichnete Beschreibung des PFP. Man muss in der Lage sein, sich in die Lage eines anderen zu versetzen, um rücksichtsvoll zu sein oder Intoleranz abzulehnen. Darwin, wie sich herausstellt, fasste unseren sozialen Instinkt in _The Descent of Man_ auf dieselbe Weise zusammen:

Der moralische Sinn bietet vielleicht die beste und höchste Unterscheidung zwischen Mensch und den niederen Tieren; ... die sozialen Instinkte,—das Hauptprinzip der moralischen Konstitution des Menschen (50. 'Die Gedanken des Marcus Aurelius,' etc., S. 139.)—mit Hilfe aktiver intellektueller Kräfte und der Auswirkungen von Gewohnheiten führen natürlich zur goldenen Regel, "Wie ihr wollt, dass die Menschen euch tun sollen, so tut auch ihr ihnen"; und dies liegt der Moral zugrunde.

## Klatsch als Fitnesslandschaft

[*[Bild: Visueller Inhalt aus dem Originalbeitrag]*](https://substackcdn.com/image/fetch/$s_!urUr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6938214c-6388-43e0-8a75-44821ce23845_1024x1024.png)Kartierung des Geistes

Ich habe ML verwendet, um Persönlichkeitsfaktoren aus Adjektiven zu destillieren, die durch Äonen des Klatsches geschmiedet wurden. Tatsächlich ist das Urteilen über andere tief mit unserer Evolution verwoben. Noch einmal von Darwin in _The Descent of Man_:

_Nachdem die Macht der Sprache erworben worden war und die Wünsche der Gemeinschaft ausgedrückt werden konnten, würde die allgemeine Meinung darüber, wie jedes Mitglied zum Wohle der Allgemeinheit handeln sollte, auf natürliche Weise in einem überragenden Maße zum Leitfaden für das Handeln werden._

In der Savanne ist Ihr Ruf Ihr Leben. Wenn andere Sie als faul oder grausam empfinden, stehen die Chancen gut, dass Sie weniger überlebende Nachkommen haben werden. Der erste Persönlichkeitsfaktor spiegelt dies wider, indem er durch Wörter wie _rücksichtsvoll_ und _angenehm_ vs. _unkooperativ_ und _intolerant_ definiert wird[^2]. **Beim Erstellen einer Karte der Persönlichkeit habe ich auch eine Karte der Fitness erstellt**. Aber Sie müssen mir nicht einfach glauben. Scrollen Sie nach oben und schauen Sie sich Faktor 1 an. Würden Sie ihn mit etwas wie der Goldenen Regel zusammenfassen? Es ist kein Zufall, dass dies immer wieder auftaucht, da es durch Spieltheorie gehalten und durch Klatsch durchgesetzt wird.

In den letzten 200 Jahren wurde Darwins Idee weiterentwickelt. Betrachten Sie das Buch von 2020 [Survival of the Friendliest: Understanding Our Origins and Rediscovering Our Common Humanity](https://www.amazon.com/Survival-Friendliest-Understanding-Rediscovering-Humanity/dp/0399590668). Auf dem Cover steht:

> _Für die meisten der etwa 300.000 Jahre, die Homo sapiens existiert, haben wir den Planeten mit mindestens vier anderen Menschentypen geteilt. Alle diese waren intelligent, stark und erfinderisch. Aber vor etwa 50.000 Jahren machte Homo sapiens einen kognitiven Sprung, der uns einen Vorteil gegenüber anderen Arten verschaffte. Was ist passiert?
> 
> Seit Charles Darwin über "evolutionäre Fitness" schrieb, wurde die Idee der Fitness mit körperlicher Stärke, taktischer Brillanz und Aggression verwechselt. Tatsächlich war es eine bemerkenswerte Art von Freundlichkeit, eine virtuose Fähigkeit zur Koordination und Kommunikation mit anderen, die uns evolutionär fit machte und es uns ermöglichte, all die kulturellen und technischen Wunder der Menschheitsgeschichte zu erreichen. Brian Hare, Professor in der Abteilung für evolutionäre Anthropologie und dem Zentrum für kognitive Neurowissenschaften an der Duke University, und seine Frau Vanessa Woods, eine Forschungswissenschaftlerin und preisgekrönte Journalistin, beleuchten den mysteriösen Sprung in der menschlichen Kognition, der Homo sapiens gedeihen ließ._

Das Buch selbst macht deutlich, dass für Darwin Fitness Kooperation einschloss; es widerspricht Darwinisten, die Fitness mit Rücksichtslosigkeit gleichsetzen. (Mehr dazu im [Interview](https://insitome.libsyn.com/brian-hare-and-survival-of-the-friendliest-understanding-our-origins-and-rediscovering-our-common-humanity) mit Brian Hare.) Ich war ziemlich sicher, dass der erste Faktor, den ich fand, mit diesem Prozess zu tun hatte. Daher schlug ich einen zusätzlichen Anspruch auf [Galton](https://www.experimental-history.com/p/how-to-keep-cakes-moist-and-cause)'s Lexikalische Hypothese in [Consequences of Conscience](https://vectors.substack.com/p/consequences-of-conscience) vor:

 3. **Der primäre latente Faktor repräsentiert die Richtung der sozialen Selektion, die uns menschlich gemacht hat.**

Um die Persönlichkeitsstruktur zu verstehen, verband ich sie mit anderen Konzepten, mit denen ich vertraut war. Die wichtigsten waren die Goldene Regel und die menschliche Selbstdomestikation.

## Der Sprung des Glaubens

[*[Bild: Visueller Inhalt aus dem Originalbeitrag]*](https://substackcdn.com/image/fetch/$s_!eHWy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1975779f-d059-4ec4-8845-6ca8d1c618af_800x553.jpeg) **Domenichino:[Die Vertreibung von Adam und Eva](https://www.wikidata.org/wiki/Q77880823)**

Nun, alles, was ich hatte, war die Fitnesskarte, die sagte, die Goldene Regel sei von größter Bedeutung. Was könnte unsere Psychologie dazu veranlasst haben, sich zu entwickeln? Ein Gewissen scheint eine ziemlich offensichtliche Wette zu sein. Vielleicht hatte dies mit der Evolution unserer inneren Stimme zu tun. Angenommen, die erste innere Stimme sagte " _teile dein Essen!_ "; wie wäre es, sich zuerst mit dieser inneren Stimme zu identifizieren? Nun, ich denke, es wäre sehr ähnlich wie Genesis, und das ist der Kern, dem ich seitdem nachjage. Sicherlich war es ein Sprung. Die Evolution der inneren Stimme folgt nicht unbedingt aus der Goldenen Regel, noch führt unsere Identifikation mit ihr notwendigerweise zu einem inneren Leben. Aber beides schien plausibel und je mehr ich studierte, desto besser passten sie in unsere evolutionäre Zeitleiste.

Was Genesis betrifft, fielen mir drei Dinge sofort als plausibel auf: sich von Gott verlassen fühlen, Landwirtschaft erfinden und Frauen, die den Weg weisen. (Die Möglichkeit eines [Schlangengift-Rituals](https://vectors.substack.com/p/the-snake-cult-of-consciousness) kam erst nach dem Lesen anderer Schöpfungsberichte.)

### Von Gott verlassen

Zunächst war ich nur daran interessiert, woher die innere Stimme kam. Meine Vorstellung war, dass das Selbst eine Art innere moralische Stimme absorbiert. Dies, dachte ich, würde sich sehr ähnlich anfühlen wie das Erlangen von "Erkenntnis von Gut und Böse", während man die Rolle des halluzinierten Schutzgeistes übernimmt. (Ein Geist, den ich von Anfang an mit dem Gedankenexperiment angenommen hatte.) Wenn Sie es gewohnt waren, moralische Entscheidungen auszulagern, hätte es sich angefühlt, als würde man einen kindlichen Zustand verlassen, in dem man direkt mit Gott kommunizierte.

Mit ein wenig mehr Lektüre erkannte ich, dass dieser Moment des Selbstbewusstseins ausreichte, um überhaupt ein "Ich" zu erzeugen. Ich mache dieses Argument in [Deja-you, the recursive construction of self](https://vectors.substack.com/p/deja-you-the-recursive-construction). Es wäre die Schaffung—oder vielmehr Entdeckung—der menschlichen Bedingung auf sehr reale Weise gewesen.

### Landwirtschaft erfinden

In Genesis ist Landwirtschaft eine Folge der menschlichen Bedingung. Die Entdeckung des "Ich", wie sich herausstellt, ist auch ausreichend, um die landwirtschaftliche Revolution zu erklären. Denn es ist plausibel ein [Paket mit Rekursion](https://vectors.substack.com/p/deja-you-the-recursive-construction) und der Fähigkeit, flexibel über die Zukunft nachzudenken. Eine allgemeine Phasenänderung in unseren Planungsfähigkeiten.

Wenn Sie glauben, dass Menschen seit 200.000 Jahren weise sind, dann ist es ein großes Rätsel, warum sie in den letzten 10.000 Jahren 11 Mal unabhängig voneinander die Landwirtschaft erfunden haben. Das ist viel, um es in 10% unserer Existenz zu packen. Und wenn Sie denken, dass Ihre spezielle Theorie es erklären kann, lesen Sie bitte [diese Rezension](https://www.pnas.org/doi/abs/10.1073/pnas.1323964111), in der 25 Gelehrte zusammenkommen und sich darauf einigen, dass sie sich nicht darauf einigen können, was den Wandel verursacht hat.

### Frauen führen den Weg

Der Wortvektor für "weiblich" korreliert mit dem PFP. Schon bevor ich über eine Verbindung zu Genesis nachdachte, stellte ich mir die erste Person, die sich mit ihrer inneren Stimme identifizierte, als Frau vor. (Wie Sie sehen können, bin ich ein wahrer Gläubiger dessen, was diese Wortvektoren uns sagen können.)

Genesis ist eine komplexe Geschichte. Das Erlangen von Handlungsmacht wird mit dem Werden wie Götter gleichgesetzt und ist eine Sünde, die den Tod verdient. Aber es ist auch alles Teil des Plans. Das Christentum wirft einen weiteren Schraubenschlüssel ein, wo wir angewiesen werden, die Erbsünde zu überwinden und wie Gott selbst zu werden, das Kreuz auf sich zu nehmen, um das ewige Leben zu leben (wieder einmal das Leben und den Tod vermischend).

Ebenso initiiert Eva den Tod, erhält aber den Titel Mutter aller Lebenden. Heutzutage, betrachten Sie, wie viel Aufwand in die Darstellung von Frauen als Akteure in Filmen gesteckt wird. Und doch wird vor Tausenden von Jahren Eva eindeutig als die Agentin dargestellt, die die Menschheit aus ihrem Zustand der Unschuld reißt. Adam folgt mit. Evas Neugier wird als schlechte Sache dargestellt, aber es ist immer noch eine interessante Ergänzung zu einem so patriarchalen Text.

Bedingt durch die Entdeckung des Selbstbewusstseins scheint es wahrscheinlich, dass der Entdecker eine Frau war. Bedingt durch Frauen, die die Entdeckung machen, scheint es wahrscheinlich, dass Adam und Eva eine Erinnerung sind. Dies sind natürlich enorme Wenns. Aber ich hatte das Gefühl, dass sie möglich waren. Und genug Willen, um zu untersuchen.

[*[Bild: Visueller Inhalt aus dem Originalbeitrag]*](https://substackcdn.com/image/fetch/$s_!9mJt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67c3400e-4baf-476a-a8ad-10ad26212f62_843x403.jpeg)Demeter, Göttin der Ernte und der eleusinischen Mysterien

### Das Sapient-Paradoxon

Der Punkt dieses Beitrags ist es, darzulegen, wie meine Arbeit in ML zur EToC führte, nicht um Beweise zu liefern. Ich möchte jedoch kurz darauf hinweisen, warum es plausibel ist, dass Selbstbewusstsein entdeckt wurde und dass es in Mythen aufgezeichnet ist. Ganz einfach, die menschliche Bedingung scheint ein jüngeres Phänomen zu sein. Vor 50 kya gibt es keine großen Beweise für inneres Leben, Rekursion oder irgendein höheres Denken. Sie könnten denken, dass die Beweise für alles, was so weit zurückliegt, nicht gut wären, aber viele Archäologen und Anthropologen sind anderer Meinung. Der Kern des [Sapient-Paradoxons](https://en.wikipedia.org/wiki/Sapient_paradox) ist, dass [Verhaltensmoderne](https://en.wikipedia.org/wiki/Behavioral_modernity) vor 10kya regional ist. Das ist sehr jung! Und wenn es nach dem Auszug aus Afrika eine grundlegende Veränderung unserer Psychologie gab, muss ihre Verbreitung weitgehend memetisch statt genetisch gewesen sein. Selbstbewusstsein, das entdeckt und verbreitet wird, folgt aus (oder wird zumindest durch) diese Einschränkungen impliziert.

Es ist eine fantastische Idee, dass die menschliche Bedingung kürzlich sein könnte. Aber es ist auch eine [fantastische Idee, dass die moderne Psychologie vor 200 kya vollständig vorhanden war](https://vectors.substack.com/i/114632067/years-ago) und für Zehntausende von Jahren brach lag, bevor wir sie schließlich anwendeten und die Welt eroberten. Die Eve-Theorie des Bewusstseins löst das Problem der Verbreitung, indem sie es ermöglicht, memetisch statt nur genetisch zu sein. Grundlegende Veränderungen könnten nach unserem Verlassen Afrikas aufgetreten sein.

## Unkorrelierte Wahrheit

Ich glaube, dass das PFP am besten als die Tendenz beschrieben wird, die Goldene Regel zu leben, dieselbe latente Dimension, die Hillel und Darwin gesehen haben. Dies ist eine idiosynkratische Ansicht innerhalb der psychometrischen Gemeinschaft. Zum Vergleich, betrachten Sie das gut aufgenommene Papier [Two, five, six, eight (thousand): Time to end the dimension reduction debate!](https://psycnet.apa.org/record/2020-64387-036)

> _Lexikalische Analysen und Dimensionsreduktionsmethoden sind Werkzeuge, um grobe Konturen des Persönlichkeitsraums zu erkunden. Wir sollten uns jedoch nicht der Illusion hingeben, dass wir die Natur an ihren Gelenken zerschneiden, um eine "wahre" Struktur der Persönlichkeit zu entdecken._

Im Wesentlichen ist das Argument, dass jede alte Rotation der Daten in Ordnung ist, weil wir die Struktur nicht für grundlegende Einsichten ausloten können. Aber je nach Vorverarbeitung sind 80% aller Persönlichkeitsinformationen im ersten Faktor enthalten. Sicherlich muss uns das etwas sagen! Und dennoch glauben Forscher [weitgehend, dass dieser Faktor überhaupt kein Persönlichkeitssignal ist](https://vectors.substack.com/i/61936908/enter-gfp). Ein [Papier von 2013](https://sci-hub.se/10.1016/j.paid.2013.03.002) beginnt mit _"Die überwältigend dominante Ansicht des GFP [des ersten Faktors] ist, dass es sich um ein Artefakt handelt, das entweder auf eine bewertende Verzerrung oder auf eine sozial wünschenswerte Reaktion zurückzuführen ist". (_ Ich würde anmerken, dass selbst während sie diesen Faktor als völlig verzerrt betrachteten, [Psychometriker Faktor 1 auf die Faktoren 3-5 verteilten](https://vectors.substack.com/i/61936908/relation-to-the-big-five), um Gewissenhaftigkeit, emotionale Stabilität und Offenheit für Erfahrungen zu konstruieren.)

Mit Ansichten wie dieser kann man keine lexikalischen Daten mit Evolution verbinden oder beginnen, über den Prozess der Selbstdomestikation zu spekulieren. Das Schreiben meiner Dissertation erforderte viele Stunden, in denen ich diese Faktoren anstarrte[^3]. Währenddessen dachte ich, sie repräsentierten eine Fitnesslandschaft und fragte mich manchmal, was das verursachen würde. Als Ingenieur war ich glücklicherweise unwissend über die vorherrschende Ansicht, dass die Struktur nicht wirklich wichtig war. Ich ging so verblendet hinein, dass ich versuchte, die Natur an ihren Gelenken zu zerschneiden.

## Fazit

Ich hoffe, dies macht deutlich, warum ein Elektroingenieur über Mythologie und Bewusstsein schreibt. Die Idee fand mich wirklich. Ich erstellte eine Karte der Persönlichkeit und es stellte sich heraus, dass es eine Karte der Evolution war. Die Verbindungen zur Goldenen Regel deuteten auf ein Proto-Gewissen als Mechanismus der Selbstdomestikation hin. Dies war mein erster Sprung. Dann spekulierte ich, dass die innere Stimme beteiligt gewesen sein könnte. Wie wäre es, zuerst zu erkennen, dass die innere Stimme "Ich" war? Genesis schien mir ein Volltreffer[^4]. Darüber hinaus haben viele Experten argumentiert, dass sich die menschliche Psychologie in den letzten 50.000 Jahren verändert hat, oft Sprache, Religion oder Selbstdomestikation als entscheidend für diesen Wandel anführend. In diesen Zeiträumen ist es möglich, dass eine so wichtige Geschichte in Mythen bewahrt werden könnte. " _Am Anfang war das Wort, und das Wort war bei Gott, und das Wort war Gott_ " … oder—und nehmen Sie dies nicht als Blasphemie—möglicherweise war es die innere Stimme.

Angesichts der Tatsache, wie kürzlich die Verhaltensmoderne entstand, ist meine Behauptung, dass Schöpfungsmythen [formale Modelle](https://vectors.substack.com/p/eve-theory-of-consciousness-v2) inspirieren können, die dann mit [Philosophie](https://vectors.substack.com/p/deja-you-the-recursive-construction), [Psychologie](https://vectors.substack.com/p/consequences-of-conscience), [Linguistik](https://vectors.substack.com/p/the-unreasonable-effectiveness-of), [Archäologie](https://vectors.substack.com/i/97498400/evidence-of-anti-venom) und [Genetik](https://vectors.substack.com/p/y-chromosome-bottleneck) verbunden werden können. Vielleicht können diese Modelle uns helfen, die Mythen auch zu verstehen. Es ist für mich bedeutsam, dass Eva wie die Götter wurde und dies ihre Trennung von Gott erforderte. In Genesis ist die Erklärung, dass ein oft eifersüchtiger Gott ein gerechtes Urteil ausübte. Für mich macht es als Naturgesetz Sinn; Menschen und die Götter konnten nicht zusammen wohnen, denn wir formten das "Ich" aus ihren Überresten. Die Distanz zwischen Mensch und Tier ist dann zwei Schritte: ein Gewissen entwickeln, dann es ablehnen. Oder vielleicht ist das zu düster. Es ist mehr so, dass wir in Spannung leben und immer die Wahl haben. Diese Erkenntnis gewährte [Rekursion](https://vectors.substack.com/p/deja-you-the-recursive-construction), der Schlüssel zur mühsamen Arbeit, die Natur unserem Willen zu beugen. Wenn ich dies auf eine Weise erklären müsste, die 10.000 Jahre überdauern könnte, würde ich die Geschichte von Adam und Eva erzählen[^5].

Natürlich begann die Reise in meinem Fachgebiet, wo ich sicheren Boden hatte. Es scheint mir sehr wahrscheinlich, dass meine Karte der Persönlichkeit evolutionäre Drücke aufzeichnet. Angesichts der Tatsache, wie kürzlich wir uns verändert haben und wie lange die Goldene Regel eine Kraft war, gehe ich so weit, dass ich ein drittes Postulat zur Galtonschen Lexikalischen Hypothese hinzufüge: **Der primäre latente Faktor repräsentiert die Richtung der Selektion, die uns menschlich gemacht hat**. Von dort aus machte ich _tatsächlich_ Sprünge, fand mich aber in guter Gesellschaft wieder, mit Leuten wie Jaynes, Jung, Pinker, Chomsky und Descartes. Diese Art der Erkundung ist das Wesen der Wissenschaft; nicht alles hat einen p-Wert.

[*[Bild: Visueller Inhalt aus dem Originalbeitrag]*](https://substackcdn.com/image/fetch/$s_!_K5c!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe08ec046-d650-4769-894e-fa1a77837040_1280x1847.jpeg)[Figur von Isis](https://en.wikipedia.org/wiki/Isis#/media/File:Isis_with_Serpent_Tail_LACMA_M.80.202.222.jpg), ägyptische Göttin der Weisheit, zweites Jahrhundert n. Chr.

[^1]: Ich war überrascht, dass Jordan Peterson die Ableitung der Big Five in einem Interview mit Joe Rogan als frühe Form von KI beschrieb. Ich habe dieses Argument im ersten Beitrag dieses Blogs gemacht und hatte es vorher nie gehört. Was auch immer Sie von seiner Politik halten, er ist ziemlich gut in der Persönlichkeitspsychologie.

[^2]: Einige mögen anmerken, dass Intoleranz ein kürzliches Kardinalsünde zu sein scheint. Vielleicht. Es wäre interessant, Wortvektoren auf historischen Texten zu erstellen und zu sehen, wie sich PC1 verändert. Angesichts der Tatsache, dass der latente Faktor moderner Texte gut zur Goldenen Regel passt, vermute ich, dass es nicht viel Bewegung von der Sprache von 1900 geben würde. Schwer zu bewegen, etwas, das durch so viel Spieltheorie gestützt wird, selbst wenn der moralische Kreis sich erweitert hat.

[^3]: Obwohl Persönlichkeitsadjektive für Persönlichkeitsmodelle grundlegend sind, ist es auch selten, dass Forscher direkt mit Wörtern arbeiten. In den 90er Jahren, als klar wurde, dass etwas wie die Big Five konsistent auftauchte, begannen Forscher, Persönlichkeit mit satzbasierten Umfragen zu messen, die darauf ausgelegt waren, die lexikalische Struktur zu approximieren (z.B. das Big Five Inventory). (Geheimtipp: Der fünfte Faktor Offenheit/Intellekt wird nicht konsistent wiederhergestellt.) Dies war einfacher, und seitdem wurde wenig Arbeit an Sprache geleistet. Was mehr ist, meine Daten waren besser als frühere Versuche. Wenn Sie verstehen wollen, wie Wörter sich zueinander verhalten, verwenden Sie ein Sprachmodell, keine Umfragen von Studenten. Niemand sonst hat so viel Zeit damit verbracht, eine so genaue Karte der Persönlichkeit anzustarren. (Sie können diese Übung in Guess the Factor üben.)

[^4]: Betrachten Sie die Tatsache, dass Adam die Tiere benannte, während er im Garten Eden war. Selbst ohne Selbstbewusstsein hätte es nicht-rekursive Sprache gegeben. Jäger haben ein enzyklopädisches Wissen über Pflanzen und Tiere. Es könnte der wichtigste Teil der Sprache vor dem Fall gewesen sein. Erstaunlich, wenn diese Tatsache 10.000 Jahre überlebt hat.

[^5]: Ich bin beeindruckt von Genesis, aber das mag nur das sein, was ich am besten kenne. Wenn ich Inder wäre, würde ich wahrscheinlich über Saraswati sprechen, oder wenn ich Navajo wäre, die Rolle der Frauen im Entstehungsmythos, oder wenn ich Ägypter wäre, der Moment, als Atum sich selbst ins Dasein rief, indem er seinen Namen sagte (und dann gegen eine urzeitliche Schlange kämpfte). EToC erfordert, dass dies unterschiedliche Perspektiven derselben Geschichte sind. Offensichtlich wird das traditionell gezeigt, indem man eine Phylogenie erstellt. Auf diesen Zeitskalen und mit meinen Fähigkeiten ist das nicht möglich. Deshalb liegt mein Fokus auf der Evolution der Rekursion. Ich möchte zeigen, dass es wahrscheinlich ist, dass Menschen kürzlich Rekursion erhalten haben und dass sie sich verbreitet hat. Das würde unser Vorwissen darüber radikal verändern, ob Schöpfungsmythen eine Wurzel teilen und wie die Wurzel war.