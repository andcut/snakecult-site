---
about:
- vectors-of-mind
- blog-archiv
author: Andrew Cutler
date: '2025-07-04'
description: '"Wer nach außen schaut, träumt; wer nach innen schaut, erwacht." -Carl
  Jung'
draft: false
keywords:
- vectors-of-mind
- deja
- rekursiv
- konstruktion
lang: de
lastmod: '2025-07-13'
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '114599293'
original_url: https://www.vectorsofmind.com/p/deja-you-the-recursive-construction
quality: 6
slug: deja-you-the-recursive-construction
tags: []
title: Deja Du Die Rekursive Konstruktion
translation_model: gpt-4o
---

*From [Vectors of Mind](https://www.vectorsofmind.com/p/deja-you-the-recursive-construction) - Bilder im Original.*

---

"Wer nach außen schaut, träumt; wer nach innen schaut, erwacht." -Carl Jung

[*[Bild: Visueller Inhalt aus dem Originalbeitrag]*](https://substackcdn.com/image/fetch/$s_!yd8k!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Facfafcba-f620-4405-85ac-cd814afd48c1_1000x582.png)_Echo und Narziss_ , John William Waterhouse

Das ungeprüfte Leben ist nicht lebenswert, und doch gibt es Drachen. Der Seher Tiresias warnte, dass Narziss ein langes Leben führen würde, wenn "er sich selbst nie erkennt". Tatsächlich starb er, während er das tat, was er liebte: sein schönes Spiegelbild betrachtete und von einem Liebhaber umschwärmt wurde. Mäßigung in allen Dingen, nehme ich an.

Was uns menschlich macht, wird seit Jahrtausenden von Philosophen debattiert, wobei die Introspektion ein starker Kandidat bleibt. Der Blick nach innen erfordert das mathematische Prinzip der Rekursion; das Selbst nimmt sich selbst wahr. In jüngerer Zeit haben sich Linguisten dem Thema angeschlossen und Erkenntnisse aus der Informatik mitgebracht. Überraschenderweise führte ihr sehr unterschiedlicher Ansatz zur Frage der Menschlichkeit zur gleichen Antwort. Rekursion ermöglicht es uns, uns eine Zukunft vorzustellen und dann darauf hinzuarbeiten. Damit können wir Luftschlösser bauen, sowohl im Himmel als auch auf der Erde. Indem wir die memetische Nische betreten haben, dominieren wir alle Arten, die ausschließlich in der materiellen Welt leben.

Es ist selten, dass so unterschiedliche Ansätze konvergieren oder dass eine Eigenschaft so viel erklären kann. Daher wird diese Serie eine maximalistische Position zur Rolle der Rekursion in der menschlichen Evolution einnehmen. Es ist ein gut begangenes Terrain, und die ersten beiden Beiträge werden die Arbeiten anderer Menschen überprüfen: Was ist Rekursion und wann hat sie sich entwickelt? Ich habe die Theorie aufgestellt, dass Rekursion bis zu einem gewissen Grad gelehrt werden kann. Die nachfolgenden Beiträge werden diskutieren, wie diese Idee eine Zeitleiste vorschlägt, die die evolutionären und archäologischen Beweise besser synchronisiert. Schließlich untersuche ich die Möglichkeit, dass Selbstbewusstsein ursprünglich geschlechtsspezifisch war. Frauen entdeckten das innere Leben, und Männer folgten.

### Informatik

_"Geld für nichts, Mädels umsonst"_ ~die Dire Straits

Mit dem Alter erkennt man, dass es kein kostenloses Mittagessen gibt. Alles kostet; es gibt immer einen Haken. In diesem Zusammenhang können Informatiker manchmal naiv erscheinen. Der Grund ist ihr Versäumnis, das Prinzip des kostenlosen Mittagessens zu verinnerlichen, nachdem sie von Rekursion gelernt haben. Sie wissen, dass man Berechnungen kostenlos erhalten kann; sie haben es gesehen!

Eine rekursive Funktion wendet sich auf ihre eigene Ausgabe an. Oft wird jede nachfolgende Anwendung eine Unterroutine sein, bei der der Input immer einfacher wird, bis eine Stoppbedingung erreicht ist. Algorithmisch ist es eine Superkraft. Betrachten Sie das untenstehende Fraktal. Der offensichtliche Weg, das Bild zu speichern, besteht darin, die Farbe jedes Pixels zu enumerieren. Alternativ könnte man es als JPEG komprimieren. [Unter der Haube verwendet JPEG Rekursion](https://qr.ae/prJyDe), um die schnelle Fourier-Transformation zu berechnen. Ohne Rekursion wäre es [Größenordnungen langsamer](https://arxiv.org/html/math/0302212#:~:text=Graphical%20explanation%20for%20the%20speed%20of%20the%20Fast%20Fourier%20Transform&text=For%20a%20sample%20set%20of,of%20the%20Cooley%2DTukey%20algorithm.).

[*[Bild: Visueller Inhalt aus dem Originalbeitrag]*](https://substackcdn.com/image/fetch/$s_!dOxu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2ff23125-7299-4679-b999-af6e51c20a23_1140x890.png)_"Fraktale sind die Architektur der Natur und enthüllen die zugrunde liegenden rekursiven Muster, die unsere Welt formen."_ \- Benoît Mandelbrot

Man kann für dieses Bild einen Schritt weiter gehen, da es mit einem rekursiven Prozess erzeugt wird. Daher kann das Bild verlustfrei mit den wenigen Bytes kodiert werden, die erforderlich sind, um den rekursiven Algorithmus zu schreiben—[ein paar Zeilen Code](https://en.scratch-wiki.info/wiki/Recursion_and_Fractals). Nicht nur das, sondern die Darstellung würde sich ins Unendliche erstrecken, denn man kann in jeden Rand hineinzoomen und das Fraktal sich selbst auf immer feineren Skalen wiederholen sehen. Rekursion ist fast alchemistisch, da sie so viel aus so wenig produziert. In den Worten des legendären Programmierers Niklaus Wirth:

> _Die Macht der Rekursion liegt offensichtlich in der Möglichkeit, eine unendliche Menge von Objekten durch eine endliche Aussage zu definieren. In gleicher Weise kann eine unendliche Anzahl von Berechnungen durch ein endliches rekursives Programm beschrieben werden, selbst wenn dieses Programm keine expliziten Wiederholungen enthält._

Mein Bereich der Verarbeitung natürlicher Sprache verwendet ebenfalls Rekursion. Bis vor kurzem waren rekurrente neuronale Netze das Modell der Wahl für Sprache. Wie ihr Name schon sagt, verarbeiten RNNs Sätze rekursiv, ein Wort nach dem anderen[^1]. Diese sequentielle Verarbeitung stellt zeitliche Informationen kostenlos dar, die Position eines Wortes in einem Satz ist durch die Reihenfolge bekannt, in der es empfangen wird. Seit 2018 sind fast alle Sprachmodelle eine Art Feedforward-Netzwerk, das als Transformer bezeichnet wird. Allerdings muss man bei der Verwendung eines Feedforward-Netzwerks jedem Wort zeitliche Informationen hinzufügen. Am Ende sind Computer leistungsfähig genug, um sich keine Sorgen über die Ineffizienz zu machen, aber wir werden auf die Idee zurückkommen, dass Rekursion automatisch die Zeit darstellt. Wenn sie im Gehirn implementiert wird, wäre es ein phänomenologischer Sprung gewesen.

### **Philosophie**

Um sich selbst bewusst zu sein, muss das Selbst sich seiner selbst bewusst sein. Seine eigenen internen Prozesse nehmen sich selbst als Input. Das ist Rekursion.

Ich stelle es mir so vor. Stellen Sie sich ein ursprüngliches Selbst vor, das sich selbst nicht wahrnehmen kann. Geschrieben als Funktion: _self(perceptions)_. Dies wäre Ihr eigenes Modell Ihres eigenen Geistes oder Ihrer Interessen. Als Input würde es alles empfangen, was Sie wahrnehmen. Introspektion würde notwendigerweise Rekursion erzeugen; das Selbst würde sich selbst als Input empfangen: self(self, perceptions). Zwei Zeitschritte der Introspektion könnten geschrieben werden[^2]:

[*[Bild: Visueller Inhalt aus dem Originalbeitrag]*](https://substackcdn.com/image/fetch/$s_!31ID!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F243087e5-033e-4e36-9c6e-ba24939efa4c_1215x73.png)

Aus dem Beispiel der RNNs, stellen Sie sich vor, wie diese Rekursion unsere Wahrnehmung und Erfahrung von Zeit verändern könnte. Es wäre eine neue Art, diese Dimension kostenlos darzustellen, eine radikale Transformation des Lebens in einem bestimmten Moment.

Es ist auch fruchtbar, sich den steinigen Anfang dieser Funktion vorzustellen. Rekursive Programme neigen dazu, zu explodieren, und dieses läuft in Ihrem Kopf. Nehmen Sie zum Beispiel die einfachste Funktion f(x) = x+1. Wenn Sie den Output bei jedem Zeitschritt rekursiv als Input verwenden, wird diese Funktion ins Unendliche wachsen. Es ist zweifelhaft, dass die Kette des Bewusstseins anfangs ungebrochen oder angenehm war. Sie hätte in Schüben und Ausbrüchen begonnen, das Selbst tauchte für einen Moment auf, nur um von seinem eigenen exponentiellen Wachstum erstickt zu werden. Neuronen können nur so viel Aufregung ertragen. Die Funktion würde ein Kontrollsystem benötigen, um die Rekursion zu stabilisieren und biologische Grenzen nicht zu überschreiten. Es muss mehr gespaltene Persönlichkeiten und innere Stimmen gegeben haben, mit denen wir uns nicht identifizierten. Abgesehen von Halluzinationen scheint es auch wahrscheinlich, dass explodierende Rekursion andere Nebenwirkungen wie unerträgliche Kopfschmerzen hervorrufen könnte. Die Entwicklung der Rekursion hätte ein paar Eier zerbrochen.

Es gibt Gründe zu glauben, dass das Selbst rekursiv ist, selbst wenn wir nicht nach innen blicken. Das ist die Position des Papiers [Consciousness as recursive, spatiotemporal self-location](https://pubmed.ncbi.nlm.nih.gov/19763611/) und Douglas Hofstadters _[I Am a Strange Loop](https://en.wikipedia.org/wiki/I_Am_a_Strange_Loop)_[^3]. Es gibt jedoch viel Debatte zu diesem Punkt.

[Jetzt abonnieren](https://www.vectorsofmind.com/subscribe?)

### **Linguistik**

Descartes setzte Subjektivität mit Selbstbewusstsein gleich[^4]. Tiere, denen die erforderliche Sprache und allgemeine Intelligenz fehlten, um _"Ich denke, also bin ich"_ zu produzieren, waren Automaten–Fleischmaschinen. Linguisten machen keine Aussagen über die subjektive Erfahrung von Tieren[^5], aber sie haben sich auf Rekursion als Trennlinie zwischen Mensch und Tier geeinigt. Dies war Chomskys bedeutender Beitrag: dass alle Sprachen von Natur aus rekursiv sind, was den Menschen einzigartige Fähigkeiten verleiht.

Um mehr über Rekursion in der Linguistik zu erfahren, empfehle ich Corballis' [Artikel](https://www.americanscientist.org/article/the-uniqueness-of-human-recursive-thinking) oder die Fußnote[^6]. Aber für diesen Beitrag reicht es zu wissen, dass Linguisten Rekursion weithin als wesentlich für eine Sprache mit Grammatik akzeptieren.

### **Psychologie**

Aufmerksame Leser könnten von dem potenziellen Köder und Wechselspiel erschüttert sein. Nur weil wir _Rekursion_ verwenden, um all diese Dinge zu beschreiben, bedeutet das nicht, dass sie gleich sind! Und das ist fair. Es gibt wahrscheinlich einige Unterschiede. Aber es ist völlig im Mainstream, viele Arten von Rekursion zusammenzufassen. Der Psychologe und Linguist Michael Corballis fügt in seinem Buch [The Recursive Mind](https://www.amazon.com/Recursive-Mind-Origins-Language-Civilization/dp/0691160945) mehrere andere psychologische Superkräfte hinzu, einschließlich mentaler Zeitreisen und der Fähigkeit zu zählen. Mentale Zeitreisen beziehen sich darauf, sich in die Vergangenheit oder Zukunft zu projizieren. Da dies eine imaginierte Zukunft ist, impliziert es auch die Fähigkeit, Fiktion zu schaffen, Welten, die nicht existieren. Diese Trennung erzeugt das Leib-Seele-Problem, bei dem "Ich" erstmals von der materiellen Welt getrennt wird. Sobald wir Rekursion hatten, nutzten viele Systeme sie.

### Wie hat sie sich entwickelt?

Pinker und Jackendoff schreiben in [The Faculty of Language](https://www.sciencedirect.com/science/article/abs/pii/S0010027704001763):

> _"Der einzige Grund, warum Sprache rekursiv sein muss, ist, dass ihre Funktion darin besteht, rekursive Gedanken auszudrücken. Wenn es keine rekursiven Gedanken gäbe, bräuchte das Ausdrucksmittel auch keine Rekursion."_

Das heißt, Rekursion könnte sich unabhängig von der Sprache entwickelt haben und dann in unser Kommunikationssystem transplantiert worden sein, nachdem sie entstanden war. Kommunikation selbst erfordert keine Rekursion. Da so viele Fähigkeiten Rekursion erfordern, warum hat sie sich zuerst entwickelt? Das ist die Millionen-Dollar-Frage! Niemand weiß es.

> _"Hier ist das Problem nicht ein Mangel an Kandidaten für evolutionäre Vorläufer, sondern ein Überfluss. Wie Herbert Simon darauf hingewiesen hat, sind wahrscheinlich alle komplexen Systeme durch hierarchische Organisation gekennzeichnet. Wenn "Rekursion" mit hierarchischer Zerlegung identifiziert und als Kriterium verwendet wird, um eine vorbestehende kognitive Funktion als Quelle für die Exaptation zur Sprache zu identifizieren, können Spekulationen unkontrolliert proliferieren." ~_ Pinker und Jackendoff

Sie bieten auch einige Möglichkeiten an: Musik, soziale Kognition, die Zerlegung von Objekten in Teile und die Formulierung komplexer Handlungssequenzen.

#### Der Fall für die Theorie des Geistes

[*[Bild: Visueller Inhalt aus dem Originalbeitrag]*](https://substackcdn.com/image/fetch/$s_!NjWR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4eff3129-d607-485c-bac7-9370716b2018_1024x1024.png)Bevor er einen unreinen Geist austrieb, fragte Jesus nach seinem Namen. "Legion, denn wir sind viele", sagten sie. Ebenso enthalten Sie eine Vielzahl.

Unter diesen Vorläufern sticht die soziale Kognition hervor. Rekursion ist offensichtlich nützlich, wenn man andere Geister modelliert. Betrachten Sie die grundlegende moralische Regel: _Behandle andere so, wie du von ihnen behandelt werden möchtest_. Dies ist ein rekursives Modell richtigen Verhaltens. Um auch nur grobe Versionen davon zu verwenden, würde man sich der Rekursion annähern. Darwin schrieb, dass das Management des Rufs der Hauptselektionsfaktor für Menschen wäre:

> _Nachdem die Sprachfähigkeit erworben worden war und die Wünsche der Gemeinschaft ausgedrückt werden konnten, würde die allgemeine Meinung darüber, wie jedes Mitglied zum Wohle der Allgemeinheit handeln sollte, auf natürliche Weise in höchstem Maße der Leitfaden für das Handeln werden. ~Die Abstammung des Menschen_

Dies ist tatsächlich die [Erkenntnis, die mich ursprünglich in dieses Kaninchenloch gelockt hat](https://vectors.substack.com/p/consequences-of-conscience). Ich bemerkte, dass in Persönlichkeitsmodellen der [dominante Faktor im Wesentlichen die Goldene Regel ist](https://vectors.substack.com/p/primary-factor-of-personality-part). So unterstützt die moderne Sprachmodellierung Darwin in dieser Hinsicht.

Ähnlich stellte Dunbar die [Hypothese des sozialen Gehirns](https://onlinelibrary.wiley.com/doi/abs/10.1002/\(SICI\)1520-6505\(1998\)6:5%3C178::AID-EVAN5%3E3.0.CO;2-8) auf, die besagt, dass die Selektion für Intelligenz hauptsächlich darin bestand, soziale Probleme zu lösen. Direkter nimmt das Papier [Recursion: what is it, who has it, and how did it evolve?](https://www.academia.edu/6885660/Recursion_what_is_it_who_has_it_and_how_did_it_evolve_INTRODUCTION) die ToM ernst als einen Weg zur Rekursion. Bei einem bestimmten Schwellenwert der Raffinesse könnte eine Phasenänderung in der ToM Rekursion erzeugen. Ich bot oben einen Weg an, bei dem das Modell des Selbst so umgebaut wurde, dass es sich selbst als Input nimmt.

Es ist also unklar, woher die Rekursion kam, aber die soziale Kognition ist ein guter Ansatzpunkt. Wenn zufällig die linguistische Rekursion dieselbe ist wie die für das Selbstbewusstsein erforderliche Rekursion, erklärt dies prägnant, was Sprache mit Bewusstsein zu tun hat. Selbstbewusstsein erfordert Rekursion. Im Gegenzug ermöglicht Rekursion vollständige syntaktische Sprache.

### Fazit

[*[Bild: Visueller Inhalt aus dem Originalbeitrag]*](https://substackcdn.com/image/fetch/$s_!BPnn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6e29fae1-f7b3-46a4-86b9-0c0c9dbfe873_1024x1024.png)Die Geburt der ~~Venus~~ Rekursion

Wenn die Evolution des Auges es uns ermöglichte, das elektromagnetische Spektrum zu sehen, wäre die Evolution der Rekursion ein "drittes Auge"[^7] gewesen, das es uns ermöglicht, nach innen auf uns selbst und die symbolische Welt zu blicken. Damit sahen wir imaginierte Zukünfte und betraten die memetische Nische. Man konnte einem prä-rekursiven Menschen nicht den Satz des Pythagoras oder möglicherweise sogar das Zählen beibringen[^8]. Darüber hinaus bot die Rekursion eine natürliche Möglichkeit, Zeit darzustellen, und enthüllte eine völlig neue phänomenologische Dimension[^9]. Wir blickten nach innen und leben seitdem dort.

Rekursion ist per Definition erforderlich für Selbstbewusstsein. Sie ermöglicht Erkenntnisse wie _"Ich denke, also bin ich"_ und wahrscheinlich vieles mehr. Viele Experten argumentieren, dass Subjektivität, Sprache, Zählen und mentale Zeitreisen ebenfalls Rekursion erfordern. Mehrere Beweislinien deuten darauf hin, dass nur Menschen diese Fähigkeit besitzen, die der Schlüssel zu unserem Erfolg ist.

In diesem Beitrag haben wir die Komponenten des rekursiven Werkzeugsatzes untersucht. Die [nächste Folge](https://vectors.substack.com/p/when-did-recursion-evolve) wird verschiedene Versuche untersuchen, zu datieren, wann sie sich entwickelt hat. Als Teaser, stellen Sie sich das erste selbstbewusste Individuum vor. Wie wäre das gewesen? Waren sie ein Kind oder ein Erwachsener? Männlich oder weiblich? Ein Krustentier? Schimpanse? Mensch? Es gibt eine große Bandbreite an Antworten in der Literatur.

[Teilen](https://www.vectorsofmind.com/p/deja-you-the-recursive-construction?action=share)

[^1]: Zum Beispiel wird bei dem Satz "die Katze jagte die Ratte" das RNN zuerst "die" als Input empfangen und einen Kontextvektor erzeugen, eine Art Gedächtnis von allem, was das Netzwerk bisher gesehen hat. Dieser Kontextvektor wird im nächsten Schritt zusammen mit dem nächsten Wort als Input empfangen. Wenn also "Katze" verarbeitet wird, geschieht dies mit Bezug auf den Kontextvektor. Der Kontextvektor wird dann aktualisiert, und "jagte" wird damit verarbeitet. Dieser Prozess wiederholt sich bis zum letzten Wort. Bei jedem Schritt wird der Kontextvektor aktualisiert und dann an die nächste Stufe übergeben.

[^2]: Es hätte Zwischenstufen gegeben. Stellen Sie sich diese fast rekursiven Aufrufe vor: self(rival(self)) oder mother(self(mother)). Tatsächlich kann man argumentieren, dass diese rekursiv sind, aber es ist einfach nicht standardisiert, wie viele Zeitschritte dazwischen liegen oder welche Informationen durch jede Funktion gelangen. Es muss viele Module gegeben haben, und Informationen, die zwischen ihnen hin- und hergesprungen sind. Wenn self() oft aufgerufen wurde, könnte es Vorteile gegeben haben, zu standardisieren, wie oft und auf welche Weise die Informationen über das Selbst zum Selbst zurückkehren würden. Eine Lösung ist konstante Rekursion.

[^3]: Siehe auch die Arbeiten von Nick Humphrey: "Ein evolutionärer Ansatz zum Bewusstsein kann das 'harte Problem' lösen – mit radikalen Auswirkungen auf die Empfindungsfähigkeit von Tieren"

[^4]: Nun, es gab mehrere Schritte. Er war ein Substanzdualismus und glaubte an unterschiedliche spirituelle und materielle Arten von Materie. Allgemeine Intelligenz und Introspektion waren Beweise für die erstere Art.

[^5]: Warum sollten sie? Für Linguisten ist diese Verbindung eine unnötige Büchse der Pandora. Sie haben genügend Beweise dafür, dass Rekursion für Menschen wichtig ist, warum auch argumentieren, dass ohne sie Tiere Automaten sind?

[^6]: Linguistische Rekursion bedeutet, wie in anderen Bereichen, dass Sätze über selbstreferenzielle Unterroutinen analysiert werden können. Zum Beispiel kann der Satz Watson schrieb, dass Holmes deduzierte, dass die Leiche im Schuppen war in drei Teile geteilt werden:X1 = Watson schriebX2 = Holmes deduzierteX3 = die Leiche war im SchuppenUm X2 zu analysieren, muss man zuerst X3 analysieren. Zusammen wäre dies P(P(X3), X2). Das Ergebnis kann wiederum mit X1 kombiniert werden: P(P(P(X3), X2) X1). Die Bedeutung des Satzes ändert sich vollständig mit jedem zusätzlichen Satzteil, und dies kann unendlich fortgesetzt werden. Wir können Jane sagte, dass John sagte, dass Harold sagte, dass… zu X1 + X2 + X3 für immer hinzufügen. Auch wenn es eine endliche Anzahl von Wörtern gibt, gibt es keinen längsten grammatikalischen Satz. Durch den alchemistischen Prozess der Rekursion entlocken wir endliche Bausteine der Unendlichkeit.

[^7]: In der Wissenschaft werden Konnotationen als Ballast betrachtet, und es gibt ein Rennen, um Wörter zu finden, die von jeglicher emotionaler Valenz unberührt sind. Daher wird der erste Persönlichkeitsfaktor als "soziale Selbstregulation" bezeichnet. Ich ziehe es vor, ihn mit der Goldenen Regel und den tausenden Jahren religiöser und philosophischer Debatten, die sie hervorgebracht haben, zu verbinden. Ebenso finde ich "drittes Auge" eine gute Möglichkeit, unsere Fähigkeit zur Introspektion zu beschreiben, auch wenn es von Religionen, einschließlich zuletzt der New-Age-Bewegung, verwendet wurde.

[^8]: Interessant für mich, wie viel Mystik in der Entdeckung des Satzes des Pythagoras involviert war.

[^9]: Offensichtlich existieren Tiere auch in der Zeit. Das Argument ist, dass Rekursion phänomenologisch wichtig gewesen sein könnte.