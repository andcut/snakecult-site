---
about:
- vectors-of-mind
- blog-archive
author: Andrew Cutler
date: '2025-07-04'
description: The Eve Theory of Consciousness proposes that self-awareness was discovered
  by women and spread memetically. To make this case I draw on linguistics, archeology,
  pharmacology, genetics, anthropology, ...
draft: false
keywords:
- vectors-of-mind
- basis

lastmod: '2025-07-05'
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '121454386'
original_url: https://www.vectorsofmind.com/p/the-ai-basis-of-the-eve-theory-of
quality: 6
slug: the-ai-basis-of-the-eve-theory-of
tags: []
title: '# La Base de IA de la Teoría de Eva'
translation_model: gpt-4o
---

*From [Vectors of Mind](https://www.vectorsofmind.com/p/the-ai-basis-of-the-eve-theory-of) - imágenes en el original.*

---

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!0pra!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff5166314-7a08-4939-9b16-2311d6214e87_1456x816.png)

La [Teoría de Eva de la Conciencia](https://vectors.substack.com/p/eve-theory-of-consciousness-v2) propone que la autoconciencia fue descubierta por mujeres y se propagó meméticamente. Para argumentar esto, me baso en [lingüística](https://vectors.substack.com/p/the-unreasonable-effectiveness-of), [arqueología](https://vectors.substack.com/i/95941288/the-genesis-of-religion), [farmacología](https://vectors.substack.com/p/comments-on-snake-venom), [genética](https://vectors.substack.com/p/y-chromosome-bottleneck), [antropología](https://vectors.substack.com/p/the-snake-cult-of-consciousness) y [neurociencia](https://vectors.substack.com/i/114650037/women-lead-the-way). Y sin embargo, soy ingeniero eléctrico. ¿Cómo puedo tener algo valioso que decir sobre un tema en el que tantos otros tienen formación real? Bueno, la idea de EToC en realidad surgió del aprendizaje automático. Los lectores de hace tiempo han [visto el progreso del blog](https://substack.com/profile/31996842-andrew/note/c-16789002?utm_source=notes-share-action) desde psicometría de ML hasta recursión y mitología comparada. Permítanme explicar cómo llegué aquí.

## Estructura de la personalidad a partir de palabras

La psicología tiene un problema de verdad fundamental. Un investigador puede teorizar que solo hay unos pocos ejes básicos en los que los humanos varían, siendo el principal Internalización vs Externalización. Otro puede decir que deben existir algo así como [30 factores básicos](https://www.scholars.northwestern.edu/en/publications/exploring-the-persome-the-power-of-the-item-in-understanding-pers) porque los humanos son así de complicados. ¿Quién tiene razón? En 1890, [Galton](https://astralcodexten.substack.com/p/galton-ehrlich-buck) sugirió que en lugar de que los psicólogos desarrollen modelos de personalidad basados en sus teorías favoritas, el mejor modelo ya estaba incrustado en el lenguaje. Cada adjetivo de personalidad existe porque millones de personas lo encuentran útil cuando hacen juicios sobre otros. Seguramente estas palabras deben iluminar todos los aspectos importantes de la personalidad. Formalmente, como la Hipótesis Léxica:

1. Aquellas características de personalidad que son importantes para un grupo de personas eventualmente se convertirán en parte del lenguaje de ese grupo.

2. Las características de personalidad más importantes tienen más probabilidades de ser codificadas en el lenguaje como una sola palabra.

Esta idea puede usarse para construir un modelo de personalidad. Simplemente crea una lista de adjetivos de personalidad, observa cómo se relacionan y comprímelos en unos pocos factores latentes[^1]. (LL Thurstone inventó el análisis factorial para hacer esto, y el [artículo](https://psycnet.apa.org/record/1934-02322-001) da nombre a este blog). Tradicionalmente, las relaciones entre adjetivos se han estimado preguntando a estudiantes de psicología qué palabras los describen mejor. Aquellos que dicen ser _brillantes_ también tienden a decir que son _de mente abierta_. Esto sugiere que ambos se relacionan con algún factor subyacente. En mi disertación, [utilicé modelos de lenguaje para estimar la similitud de palabras](https://vectors.substack.com/p/the-big-five-are-word-vectors) y produje resultados similares a las encuestas tradicionales (el primer factor de los dos métodos se correlaciona con r=0.93).

Es más fácil entender este proceso con un ejemplo. Aquí hay 100 adjetivos de personalidad aleatorios trazados en las dos dimensiones que capturan la mayor cantidad de información de personalidad. Piensa en estos como dos de los [Cinco Grandes](https://en.wikipedia.org/wiki/Big_Five_personality_traits) (aunque hay [una diferencia en cómo están rotados](https://vectors.substack.com/i/61936908/relation-to-the-big-five)). Uno de los trabajos de un psicólogo de la personalidad es mirar tales gráficos y describirlos cualitativamente. Puedes practicar ese ejercicio en [Adivina el Factor](https://vectors.substack.com/p/guess-the-factor), o hacerlo a continuación. ¿Cómo resumirías el Factor 1?

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!N5Ou!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3c50c0d0-6e09-4758-bfad-6c9135f154af_1423x891.png)Los Factores 1 y 2 se producen utilizando [PCA](https://builtin.com/data-science/step-step-explanation-principal-component-analysis), un método para destilar la información de personalidad en el menor número de ejes. Para obtener más información sobre cómo obtener estos de los vectores de palabras, consulta mi artículo [Deep Lexical Hypothesis](https://arxiv.org/abs/2203.02092). También puedes reproducir este resultado (y mucho más) usando mi [código](https://colab.research.google.com/drive/1SXZNVqH0m_Bnd2hvIJFYiKQvHWpGu8ZM?usp=sharing), que se ejecuta gratis en Google Colab.

Desde una perspectiva estadística, el Factor 1 se ha desnudado y está ondeando una gran bandera "Soy con mucho el más importante", como explico en el [Factor Primario de Personalidad](https://vectors.substack.com/p/primary-factor-of-personality-part) (PFP). Cualitativamente, es esencialmente "lo que la sociedad quiere de ti". Sé considerado y respetuoso, no seas pretencioso o poco cooperativo.

Para abstraer el PFP (Factor 1) de otra manera, es útil retroceder 2,000 años. Los israelitas tenían bibliotecas dedicadas a las reglas sociales y su aplicación adecuada. Con siglos de debate e interpretación, la letra de la ley se multiplicó. Pero también hubo un movimiento para destilar el espíritu de la ley.

Según la narrativa tradicional, un potencial converso se acercó al Rabino Shammai y le pidió que explicara toda la Torá mientras estaba de pie sobre un pie. El Rabino Shammai, conocido por su estricta adhesión a la ley judía, encontró la pregunta irrespetuosa y rechazó al converso, despidiéndolo.

Indemne, el converso luego se acercó al Rabino Hillel con la misma solicitud. Hillel, renombrado por su compasión y sabiduría, respondió de una manera diferente. En lugar de despedir al converso, Hillel aceptó el desafío y proporcionó un resumen conciso de la Torá mientras estaba de pie sobre un pie. Dijo: "Lo que te es odioso, no lo hagas a tu prójimo: esta es toda la Torá; el resto es el comentario".

Esta es también una excelente descripción del PFP. Uno debe ser capaz de ponerse en los zapatos de otro para ser considerado o rechazar la intolerancia. Darwin, resulta, resumió nuestro instinto social de la misma manera en _El origen del hombre_:

El sentido moral quizás ofrece la mejor y más alta distinción entre el hombre y los animales inferiores;... los instintos sociales,—el principio primordial de la constitución moral del hombre (50. 'Los pensamientos de Marco Aurelio,' etc., p. 139.)—con la ayuda de poderes intelectuales activos y los efectos del hábito, naturalmente conducen a la regla de oro, "Como queréis que los hombres hagan con vosotros, haced vosotros con ellos de igual manera"; y esto yace en la base de la moralidad.

## El chisme como un paisaje de aptitud

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!urUr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6938214c-6388-43e0-8a75-44821ce23845_1024x1024.png)Mapeando la mente

Usé ML para destilar factores de personalidad a partir de adjetivos que se forjaron a través de eones de chismes. De hecho, juzgar a los demás está profundamente entrelazado con nuestra evolución. Una vez más, de Darwin en _El origen del hombre_:

_Una vez adquirida la capacidad del lenguaje, y expresados los deseos de la comunidad, la opinión común de cómo cada miembro debería actuar para el bien público, naturalmente se convertiría en la guía de acción en un grado supremo._

En la sabana, tu reputación es tu vida. Si otros te consideran perezoso o cruel, lo más probable es que tengas menos descendientes supervivientes. El primer factor de personalidad refleja esto, siendo definido por palabras como _considerado_ y _agradable_ vs _poco cooperativo_ e _intolerante_[^2]. **Al construir un mapa de la personalidad también construí un mapa de aptitud**. Pero no tienes que tomar mi palabra por ello. Desplázate hacia arriba y mira el Factor 1. ¿Lo resumirías con algo como la Regla de Oro? No es un accidente que esto siga apareciendo, ya que está sostenido por la teoría de juegos y reforzado a través del chisme.

En los últimos 200 años, la idea de Darwin ha sido desarrollada. Considera el libro de 2020 [Survival of the Friendliest: Understanding Our Origins and Rediscovering Our Common Humanity](https://www.amazon.com/Survival-Friendliest-Understanding-Rediscovering-Humanity/dp/0399590668). La portada dice:

> _Durante la mayor parte de los aproximadamente 300,000 años que Homo sapiens ha existido, hemos compartido el planeta con al menos otros cuatro tipos de humanos. Todos ellos eran inteligentes, fuertes e inventivos. Pero hace unos 50,000 años, Homo sapiens hizo un salto cognitivo que nos dio una ventaja sobre otras especies. ¿Qué sucedió?  
>   
>  Desde que Charles Darwin escribió sobre la "aptitud evolutiva", la idea de aptitud se ha confundido con fuerza física, brillantez táctica y agresión. De hecho, lo que nos hizo aptos evolutivamente fue un tipo notable de amabilidad, una habilidad virtuosa para coordinar y comunicarse con otros que nos permitió lograr todas las maravillas culturales y técnicas en la historia humana. Avanzando lo que llaman la "teoría de la autodomesticación", Brian Hare, profesor en el departamento de antropología evolutiva y el Centro de Neurociencia Cognitiva en la Universidad de Duke y su esposa, Vanessa Woods, una científica investigadora y periodista galardonada, arrojan luz sobre el misterioso salto en la cognición humana que permitió a Homo sapiens prosperar._

El libro en sí deja claro que, para Darwin, la aptitud incluía la cooperación; se opone a los darwinistas, que equiparan la aptitud con la crueldad. (Para más información, consulta la [entrevista](https://insitome.libsyn.com/brian-hare-and-survival-of-the-friendliest-understanding-our-origins-and-rediscovering-our-common-humanity) con Brian Hare.) Estaba bastante seguro de que el primer factor que encontré tenía que ver con este proceso. Por lo tanto, sugiriendo una afirmación adicional a la [Hipótesis Léxica de Galton](https://www.experimental-history.com/p/how-to-keep-cakes-moist-and-cause) en [Consequences of Conscience](https://vectors.substack.com/p/consequences-of-conscience):

3. **El factor latente primario representa la dirección de la selección social que nos hizo humanos.**

Para entender la estructura de la personalidad, la conecté con otros conceptos con los que estaba familiarizado. Los más importantes fueron la Regla de Oro y la autodomesticación humana.

## El salto de fe

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!eHWy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1975779f-d059-4ec4-8845-6ca8d1c618af_800x553.jpeg) **Domenichino:[La Expulsión de Adán y Eva](https://www.wikidata.org/wiki/Q77880823)**

Ahora, todo lo que tenía era el mapa de aptitud que decía que la Regla de Oro era primordial. ¿Qué podría haber causado que nuestra psicología evolucionara? Una conciencia parece una apuesta bastante obvia. Tal vez esto tenía que ver con la evolución de nuestra voz interior. Supongamos que la primera voz interior decía " _¡comparte tu comida!_ "; ¿cómo sería identificarse por primera vez con esta voz interior? Bueno, creo que sería muy parecido al Génesis, y ese es el núcleo que he estado persiguiendo desde entonces. Ciertamente, fue un salto. La evolución de la voz interior no necesariamente sigue de la Regla de Oro, ni nuestra identificación con ella necesariamente produce una vida interior. Pero ambos parecían plausibles y, a medida que estudiaba más, encajaban muy bien en nuestra línea de tiempo evolutiva.

En cuanto al Génesis, tres cosas me parecieron inmediatamente plausibles: sentirse abandonado por Dios, inventar la agricultura y las mujeres liderando el camino. (La posibilidad de un [ritual de veneno de serpiente](https://vectors.substack.com/p/the-snake-cult-of-consciousness) solo surgió después de leer otros relatos de creación).

### Abandonado por Dios

Inicialmente, solo me preocupaba de dónde venía la voz interior. Mi concepción era que el yo absorbía una especie de voz moral interna. Esto, pensé, se sentiría mucho como obtener "conocimiento del bien y del mal" mientras asumías el papel del espíritu tutelar alucinado. (Un espíritu que había asumido desde el principio con el experimento mental). Si estabas acostumbrado a externalizar decisiones morales, tomar las riendas habría sentido como dejar un estado infantil donde te comunicabas directamente con Dios.

Con un poco más de lectura, me di cuenta de que este momento de autoconciencia era suficiente para producir un "yo" en primer lugar. Hago ese argumento en [Deja-you, la construcción recursiva del yo](https://vectors.substack.com/p/deja-you-the-recursive-construction). Habría sido la creación—o más bien el descubrimiento—de la condición humana de una manera muy real.

### Inventar la agricultura

En el Génesis, la agricultura es una consecuencia de la condición humana. El descubrimiento del "yo", resulta, también es suficiente para explicar la Revolución Agrícola. Pues es plausiblemente un [paquete con la recursión](https://vectors.substack.com/p/deja-you-the-recursive-construction) y la capacidad de pensar de manera flexible sobre el futuro. Un cambio de fase general en nuestras habilidades de planificación.

Si crees que los humanos han sido sapientes durante 200,000 años, entonces es un gran misterio por qué inventarían la agricultura 11 veces de manera independiente en los últimos 10,000 años. Eso es mucho para meter en el 10% de nuestra existencia. Y, si crees que tu teoría particular puede explicarlo, por favor lee [esta revisión](https://www.pnas.org/doi/abs/10.1073/pnas.1323964111) donde 25 académicos se reúnen y acuerdan que no pueden ponerse de acuerdo sobre qué causó el cambio.

### Las mujeres lideran el camino

El vector de palabras para "femenino" se correlaciona con el PFP. Incluso antes de contemplar una conexión con el Génesis, concebí a la primera persona en identificarse con su voz interior como una mujer. (Como puedes ver, soy un verdadero creyente en lo que estos vectores de palabras pueden decirnos).

El Génesis es una historia compleja. Obtener agencia se equipara con convertirse en dioses y es un pecado digno de muerte. Pero también es todo parte del plan. El cristianismo introduce otra complicación, donde se nos instruye a superar el pecado original y convertirnos en Dios mismo, tomando la cruz para vivir la vida eterna (una vez más mezclando vida y muerte).

Asimismo, Eva inicia la muerte pero se le da el título de Madre de Todos los Vivientes. Hoy en día, considera cuánto esfuerzo se pone en retratar a las mujeres como agentes en el cine. Y sin embargo, hace miles de años, Eva es claramente pintada como la agente que arranca a la humanidad de su estado de inocencia. Adán la sigue. La curiosidad de Eva se retrata como algo malo, pero sigue siendo una adición interesante a un texto tan patriarcal.

Condicionado a que la autoconciencia fuera descubierta, parece probable que la exploradora fuera una mujer. Condicionado a que las mujeres hicieran el descubrimiento, parece probable que Adán y Eva sean un recuerdo. Estos, por supuesto, son enormes "si". Pero tenía la sensación de que eran posibles. Y suficiente voluntad para investigar.

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!9mJt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67c3400e-4baf-476a-a8ad-10ad26212f62_843x403.jpeg)Deméter, Diosa de la Cosecha y los Misterios Eleusinos

### La Paradoja Sapiente

El objetivo de este post es exponer cómo mi trabajo en ML llevó a la EToC, no proporcionar evidencia. Sin embargo, quiero señalar brevemente por qué es plausible que la autoconciencia fuera descubierta y que esté registrada en mitos. Muy simplemente, la condición humana parece ser un fenómeno reciente. Antes de 50 kya no hay gran evidencia de vida interior, recursión o cualquier pensamiento de orden superior. Puedes pensar que la evidencia de algo tan lejano no sería buena, pero muchos arqueólogos y antropólogos no están de acuerdo. El núcleo de la [Paradoja Sapiente](https://en.wikipedia.org/wiki/Sapient_paradox) es que la [Modernidad Conductual](https://en.wikipedia.org/wiki/Behavioral_modernity) es regional antes de 10kya. ¡Eso es muy reciente! Y si hubo un cambio fundamental en nuestra psicología después de Salir de África, su difusión debe haber sido en gran medida memética en lugar de genética. Que la autoconciencia fuera descubierta y se propagara sigue (o al menos está implícito) por estas restricciones.

Es una idea fantástica que la condición humana podría ser reciente. Pero también es una [idea fantástica que la psicología moderna estuviera completamente en su lugar hace 200 kya](https://vectors.substack.com/i/114632067/years-ago) y permaneciera inactiva durante decenas de miles de años antes de que finalmente la aplicáramos y conquistáramos el mundo. La Teoría de Eva de la Conciencia resuelve el problema de la difusión permitiendo que sea memética en lugar de solo genética. Cambios fundamentales podrían haber ocurrido después de que dejamos África.

## Verdad no correlacionada

Creo que el PFP se describe mejor como la tendencia de uno a vivir la Regla de Oro, la misma dimensión latente vista por Hillel y Darwin. Esta es una visión idiosincrática dentro de la comunidad psicométrica. Para contrastar, considera el artículo bien recibido [Two, five, six, eight (thousand): Time to end the dimension reduction debate!](https://psycnet.apa.org/record/2020-64387-036)

> _Los análisis léxicos y los métodos de reducción de dimensionalidad son herramientas para explorar los contornos aproximados del espacio de la personalidad. Sin embargo, no deberíamos engañarnos pensando que estamos cortando la naturaleza en sus articulaciones para descubrir una estructura "verdadera" de la personalidad._

Esencialmente, el argumento es que cualquier rotación de los datos está bien porque no podemos sondear la estructura para obtener ideas fundamentales. Pero, dependiendo del preprocesamiento, el 80% de toda la información de personalidad está contenida en el primer factor. ¡Seguramente eso debe estar diciéndonos algo! Y sin embargo, todavía, los investigadores [en su mayoría creen que este factor no es señal de personalidad en absoluto](https://vectors.substack.com/i/61936908/enter-gfp). Un [artículo de 2013](https://sci-hub.se/10.1016/j.paid.2013.03.002) comienza _“La visión abrumadoramente dominante del GFP [el primer factor] es que representa un artefacto debido ya sea a un sesgo evaluativo o a responder de manera socialmente deseable”. (_ Notaría que incluso mientras creen que este factor es completamente sesgo [los psicométricos distribuyeron el factor 1 a los factores 3-5](https://vectors.substack.com/i/61936908/relation-to-the-big-five) para construir Conciencia, Estabilidad Emocional y Apertura a la Experiencia.)

Con visiones como esa uno no puede conectar datos léxicos a la evolución o comenzar a hacer hipótesis sobre el proceso de autodomesticación. Escribir mi disertación requirió pasar muchas horas mirando estos factores[^3]. A lo largo, pensé que representaban un paisaje de aptitud, y a veces me preguntaba qué causaría eso. Como ingeniero, era felizmente ignorante de la visión predominante de que la estructura realmente no importaba. Entré lo suficientemente engañado como para intentar cortar la naturaleza en sus articulaciones.

## Conclusión

Espero que esto aclare por qué un ingeniero eléctrico está escribiendo sobre mitología y conciencia. La idea me encontró, realmente. Estaba haciendo un mapa de personalidad y resultó ser un mapa de evolución. Las conexiones con la Regla de Oro sugirieron una proto-conciencia como un mecanismo de autodomesticación. Este fue mi primer salto. Luego especulé que la voz interior podría haber estado involucrada. ¿Cómo sería darse cuenta por primera vez de que la voz interior era "yo"? El Génesis me pareció un ejemplo perfecto[^4]. Además, muchos expertos han argumentado que la psicología humana cambió en los últimos 50,000 años, a menudo invocando el lenguaje, la religión o la autodomesticación como cruciales para este cambio. En estas escalas de tiempo, es posible que una historia tan importante pudiera preservarse en el mito. " _En el principio era la Palabra, y la Palabra estaba con Dios, y la Palabra era Dios_ " ... o—y no tomes esto como blasfemia—posiblemente era la voz interior.

Dado lo recientemente que surgió la Modernidad Conductual, mi afirmación es que los mitos de creación pueden inspirar [modelos formales](https://vectors.substack.com/p/eve-theory-of-consciousness-v2) que luego pueden conectarse a [filosofía](https://vectors.substack.com/p/deja-you-the-recursive-construction), [psicología](https://vectors.substack.com/p/consequences-of-conscience), [lingüística](https://vectors.substack.com/p/the-unreasonable-effectiveness-of), [arqueología](https://vectors.substack.com/i/97498400/evidence-of-anti-venom) y [genética](https://vectors.substack.com/p/y-chromosome-bottleneck). Quizás estos modelos puedan ayudarnos a entender los mitos también. Es significativo para mí que Eva se convirtiera como los dioses y esto requiriera su separación de Dios. En el Génesis, la explicación es que un Dios a menudo celoso ejerció un juicio justo. Para mí tiene sentido como una ley natural; los humanos y los dioses no podían habitar juntos porque formamos el "yo" a partir de sus restos. La distancia entre el hombre y la bestia es entonces de dos pasos: evolucionar una conciencia, luego rechazarla. O quizás eso es demasiado sombrío. Es más que vivimos en tensión, y siempre tenemos la elección. Esta epifanía otorgó [recursión](https://vectors.substack.com/p/deja-you-the-recursive-construction), la clave para el arduo trabajo de doblar la naturaleza a nuestra voluntad. Si tuviera que explicar esto de una manera que pudiera durar 10,000 años, contaría la historia de Adán y Eva[^5].

Naturalmente, el viaje comenzó en mi área de especialización donde tenía un terreno seguro. Me parece muy probable que mi mapa de personalidad registre presiones evolutivas. Dado lo recientemente que hemos cambiado, y cuánto tiempo la Regla de Oro ha sido una fuerza, voy tan lejos como para añadir un tercer postulado a la Hipótesis Léxica de Galton: **El factor latente primario representa la dirección de la selección que nos hizo humanos**. Desde allí, _sí_ hice saltos pero al aterrizar me encontré en buena compañía, con personas como Jaynes, Jung, Pinker, Chomsky y Descartes. Este tipo de exploración es la esencia de la ciencia; no todo tiene un valor p.

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!_K5c!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe08ec046-d650-4769-894e-fa1a77837040_1280x1847.jpeg)[Figurilla de Isis](https://en.wikipedia.org/wiki/Isis#/media/File:Isis_with_Serpent_Tail_LACMA_M.80.202.222.jpg), Diosa Egipcia de la Sabiduría, siglo II d.C.

[^1]: Me sorprendió que Jordan Peterson describiera la derivación de los Cinco Grandes como una forma temprana de IA en una entrevista con Joe Rogan. Hice ese argumento en el primer post de este blog y nunca lo había escuchado antes. Cualquiera que sea tu opinión sobre su política, es bastante bueno en psicología de la personalidad.

[^2]: Algunos pueden notar que ser intolerante parece un pecado capital reciente. Quizás. Sería interesante construir vectores de palabras en textos históricos y ver cómo cambia el PC1. Dado que el factor latente del texto moderno es una buena coincidencia para la Regla de Oro, mi suposición es que no habría mucho movimiento desde, digamos, el lenguaje de 1900. Difícil mover algo respaldado por tanta teoría de juegos, incluso si el círculo moral se ha expandido.

[^3]: Aunque los adjetivos de personalidad son fundamentales para los modelos de personalidad, también es raro que los investigadores traten directamente con palabras. En los años 90, una vez que quedó claro que algo como los Cinco Grandes emergía consistentemente, los investigadores comenzaron a medir la personalidad con encuestas basadas en frases diseñadas para aproximar la estructura léxica (por ejemplo, el Inventario de los Cinco Grandes). (Secreto comercial: el quinto factor Apertura/Intelecto no se recupera consistentemente). Esto era más fácil, y desde entonces se ha hecho poco trabajo en el lenguaje. Además, mis datos eran mejores que los intentos anteriores. Si quieres entender cómo se relacionan las palabras, usa un modelo de lenguaje, no encuestas de estudiantes universitarios. Nadie más ha pasado tanto tiempo mirando un mapa de personalidad tan preciso. (Puedes practicar ese ejercicio en Adivina el Factor.)

[^4]: Considera el hecho de que Adán nombró a los animales mientras estaba en el Jardín del Edén. Incluso sin autoconciencia, habría habido lenguaje no recursivo. Los cazadores tienen un conocimiento enciclopédico de plantas y animales. Puede haber sido la parte más importante del lenguaje antes de La Caída. Asombroso si ese hecho sobrevivió 10,000 años.

<!-- CHUNK BREAK -->

[^5]: Estoy impresionado con el Génesis, pero eso puede ser simplemente lo que mejor conozco. Si fuera indio probablemente estaría hablando de Saraswati, o si fuera navajo del papel de las mujeres en el mito del Emergence, o si fuera egipcio del momento en que Atum se llamó a sí mismo a la existencia al decir su nombre (y luego luchó contra una serpiente primordial). EToC requiere que estas sean diferentes perspectivas de la misma historia. Obviamente, eso se muestra tradicionalmente construyendo una filogenia. En estas escalas de tiempo y con mis habilidades, eso no es posible. Por eso mi enfoque está en la evolución de la recursión. Quiero mostrar que es probable que los humanos adquirieran recientemente la recursión y que esta se difundió. Eso cambiaría radicalmente nuestra suposición sobre si los mitos de creación comparten una raíz y cómo era esa raíz.