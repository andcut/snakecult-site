---
about:
- vectors-of-mind
- blog-archive
author: Andrew Cutler
date: '2025-07-04'
description: “In the beginning was the Word, and the Word was with Psychology, and
  the Word was Psychology” ~New Vector Translation
draft: false
keywords:
- vectors-of-mind
- beginning
- word

lastmod: '2025-07-05'
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '51210419'
original_url: https://www.vectorsofmind.com/p/in-the-beginning-was-the-word
quality: 6
slug: in-the-beginning-was-the-word
tags: []
title: En el principio era el Verbo
translation_model: gpt-4o
---

*From [Vectors of Mind](https://www.vectorsofmind.com/p/in-the-beginning-was-the-word) - imágenes en el original.*

---

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!5qwE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9f7c2505-9587-4daa-aac2-648b8bf16efb_1200x544.png)

_“En el principio era la Palabra, y la Palabra estaba con la Psicología, y la Palabra era Psicología” ~Nueva Traducción Vectorial_

Todos los constructos de personalidad se describen primero con palabras. Desde los modelos impulsados por cocaína de Freud hasta los sobrios Cinco Grandes, todos son en algún momento palabras. Gran parte de la psicología académica se ocupa de comparar constructos. Para hacer esto, deben compartir una base, típicamente un conjunto de sujetos. A los sujetos se les da un instrumento (generalmente una encuesta) que aproxima dónde se encuentran en el espacio de constructos. Basado en cómo covarían las respuestas de los sujetos, se hacen afirmaciones generales sobre los constructos. En este post exploramos otra manera. Los avances en PNL permiten la comparación cuantitativa de constructos en su hábitat natural: el lenguaje.

### Hoja de ruta

En el [último post](https://vectors.substack.com/p/the-big-five-are-word-vectors?s=w) argumenté que los Cinco Grandes son vectores de palabras. Este post hace la misma afirmación sobre escalas independientes, lo que permite comparar constructos sin involucrar a sujetos. Para demostrar esto, se introduce un modelo amplio de personalidad, así como un método para representar constructos en el espacio de palabras. El esquema sigue:

  1. Comparar constructos en el espacio de sujetos vs espacio de palabras

  2. Problemas con el espacio de sujetos

  3. Relacionar el altruismo de parentesco y el altruismo recíproco con los Cinco Grandes usando sujetos

  4. La misma comparación en el espacio de palabras

    1. Introducir un modelo de cinco factores (temporal) identificado usando PNL

    2. Proyectar palabras de altruismo en ese espacio

    3. Código disponible [aquí](https://colab.research.google.com/drive/13DA2IKQ9zRimGedww_09iGT6ehuYriVz?usp=sharing).

  5. Discusión, limitaciones, trabajo futuro

### **Un camino tortuoso**

Para comparar el altruismo con los Cinco Grandes, la señal debe pasar por muchas transformaciones: Altruismo (ideal) → descrito por palabras → encuesta desarrollada (y con suerte validada) para aproximar este constructo → administrada al sujeto que interpreta estas palabras y busca en su alma → puntuación de altruismo del sujeto → **correlación en el espacio de sujetos** ← puntuación del Inventario de los Cinco Grandes (BFI) del sujeto ← el sujeto interpreta los ítems del BFI y busca en su alma ← desarrollar el BFI para medir aproximadamente esto ← constructo definido/comunicado por descripción cualitativa ← Cinco Grandes (definidos por cargas de palabras). Luego se hacen afirmaciones sobre los dos ideales, Altruismo y los Cinco Grandes. 

### **El camino recto y estrecho**

¿Por qué no usar vectores de palabras como la base compartida en lugar de sujetos? El camino es mucho más directo: Altruismo (ideal) → descrito por palabras → vectorizado al espacio de palabras → **comparación en el espacio de palabras** ← Cinco Grandes, que ya existen en el espacio de palabras, como se discutió en el [post anterior](https://vectors.substack.com/p/the-big-five-are-word-vectors?s=w). Para aquellos que llevan la cuenta, son 4 vs 10 transformaciones. (Se puntúa como en el golf.)

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!tbb9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb8b6c50-e94e-4462-8772-78359189f70e_1600x1305.png)Realidades estadísticas visitando el campo de la psicología. Han sido unos años difíciles.

### **Tal el Revelador**

La dificultad de usar sujetos para hacer afirmaciones sobre constructos verbales no es un secreto.

> _“La mayoría de las teorías e hipótesis en psicología son de naturaleza verbal, sin embargo, su evaluación depende abrumadoramente de procedimientos estadísticos inferenciales. La validez del paso de un análisis cualitativo a uno cuantitativo depende de que las expresiones verbales y estadísticas de una hipótesis estén estrechamente alineadas, es decir, que ambas deben referirse aproximadamente al mismo conjunto de observaciones hipotéticas. Aquí, argumento que muchas aplicaciones de la inferencia estadística en psicología no cumplen con esta condición básica.” ~Tal Yarkoni,_ La [crisis de generalización](https://psyarxiv.com/jqw35/)

La validez aquí se refiere a una puntuación que captura el constructo que se pretende medir. Vale la pena leer los argumentos y ejemplos en su totalidad. Pero para nosotros, la conclusión es qué se puede hacer, dadas estas realidades. Él sugiere:

  1. Hacer algo diferente (entrar en otros campos). 

  2. Abrazar la investigación cualitativa

  3. Adoptar mejores estándares (incluyendo 7 sugerencias). 

>  _“Uno siempre es libre de pretender que valores p pequeños obtenidos de operacionalizaciones estadísticas extremadamente estrechas pueden proporcionar una base adecuada para inferencias verbales amplias sobre constructos psicológicos complejos. Pero nadie más—ni los colegas, ni los financiadores, ni el público, y ciertamente no el registro científico a largo plazo—está obligado a honrar la farsa.”_

Incluso si tu visión de la investigación en psicología no es tan sombría, seguramente los lectores han sido quemados por artículos que hacen afirmaciones pero emplean experimentos que solo están tenuemente relacionados. Todas las soluciones disponibles son dolorosas. El campo puede tener que adoptar una visión más estrecha y dejar las grandes preguntas a aquellos que estudian historia, literatura y álgebra lineal. Propongo otra forma de avanzar.

### **Convertirse al espacio de palabras**

. 4. Usar vectores de palabras como una base compartida

Los constructos viven juntos en el espacio de palabras, y sin embargo, cuando se hacen comparaciones, los arrastramos al espacio de sujetos. Esto es un enorme, costoso, problema. ¿Qué pasaría si pudieran permanecer seguros en el espacio de palabras? La pretensión del procesamiento del lenguaje natural es que las palabras son vectores en un espacio continuo. Analizar estos vectores funciona lo suficientemente bien como para ser un [proceso](https://blog.google/products/search/search-language-understanding-bert/) [de carga](https://www.amazon.jobs/en/search?base_query=natural+language+processing&loc_query=&latitude=&longitude=&loc_group_id=&invalid_location=false&country=&city=&region=&county=) [de trabajo](https://youtu.be/SGzMElJ11Cc?t=6667) en industrias de billones de dólares, y actualmente se está ([re](https://vectors.substack.com/p/the-big-five-are-word-vectors?s=w))introduciendo a la psicología.

### **Practica lo que predicas**

Aquí veremos un estudio tradicional realizado en el espacio de sujetos y luego intentaremos mejorarlo moviéndolo al espacio de palabras. Para evitar un hombre de paja, el objeto es [Altruismo de Parentesco, Altruismo Recíproco y los Cinco Factores de Personalidad](https://www.sciencedirect.com/science/article/abs/pii/S1090513898000099?casa_token=05bTreOjGKUAAAAA:nLHTWhK3z45xUbN5nTVd7a3-Qaz9No22rQtVY6vpUjYpeZ1bkPy-cBig9UgRbn-GnqJScTCPpSY) que ha sido citado cientos de veces y cuyo primer autor tiene un índice h de 70.

Los sujetos son medidos usando tres instrumentos: Cinco Grandes (a través de una encuesta de adjetivos), Empatía/Apego y Perdón/No Retaliación (encuesta de frases), y altruismo en un juego de reparto de dinero. Debido a que los autores hipotetizan que el espacio intersticial entre Amabilidad y Estabilidad Emocional (también conocido como Neuroticismo) diferencia los dos altruismos, se agregan algunas palabras para medir mejor esa área. De manera similar, se diseña un nuevo cuestionario para medir Empatía/Apego y Perdón/No Retaliación, que se teoriza están relacionados con el altruismo de parentesco vs recíproco. Más allá de este tipo de estudio, se utiliza un juego para medir el altruismo.

> _“En la versión de la tarea de asignación de dinero utilizada para medir el altruismo de parentesco, la otra persona fue descrita como un amigo cercano—alguien con quien el participante tenía una larga historia de amistad y con quien el participante tenía mucho en común. Esperábamos que al describir la amistad como una antigua y al amigo como alguien muy similar al participante, la amistad se asemejara mucho a la relación que uno tiene con un pariente. La razón por la que no usamos un pariente como el objeto potencial de altruismo fue para evitar introducir varianza en las respuestas debido al pariente particular involucrado; por ejemplo, muchas personas podrían estar más dispuestas a comportarse altruistamente hacia un hermano que hacia otro.”_

En otras palabras, para no ensuciar los datos con sentimientos del mundo real hacia los parientes, se mide el altruismo recíproco.

> _“En la versión de la tarea de asignación de dinero utilizada para medir el altruismo recíproco, la otra persona fue descrita como un no cooperador—alguien que había sido grosero, desagradable e inconsiderado hacia el participante.”_

Y para medir el altruismo recíproco miden … ¿altruismo no recíproco? Naturalmente hay correlaciones y los autores concluyen:

> _“Los resultados de este estudio apoyan la sugerencia de que los rasgos de personalidad que involucran empatía y apego facilitan el altruismo que se dirige principalmente hacia los parientes (es decir, altruismo de parentesco), y que los rasgos de personalidad que involucran perdón y no retaliación facilitan el altruismo que se dirige principalmente hacia los no parientes (es decir, altruismo recíproco).”_

Pero si el altruismo recíproco nunca fue medido, ¿cómo pueden los resultados apoyar esa afirmación? Las estadísticas en los artículos de psicología son, como señala Tal, a menudo un adorno retórico. ¡Pero no tenemos que seguir el juego! Veamos qué tiene que decir el espacio de palabras.

### **Una tierra de leche y miel (bienvenidos al espacio de palabras)**

En los estudios tradicionales, debido a los costos de mapear sujetos en el espacio de personalidad, la resolución solo puede ser alta en unas pocas áreas de personalidad a la vez. Es por eso que los autores exploraron la Empatía y la No Retaliación y el espacio entre Amabilidad y Estabilidad Emocional. Todos esos ejes [existen en el espacio regular de los Cinco Grandes](https://psyarxiv.com/vebtm/), pero se miden de manera bastante granular. En el espacio de palabras podemos comparar el altruismo con los Cinco Grandes completos en todo su esplendor de alta resolución. En mi github hay 2819 vectores de palabras factorizados en cinco PCs. Podemos usar esos para conveniencia. El primer paso es seleccionar conjuntos de palabras que describan cada altruismo. Para las palabras de parentesco elegí aquellas que encarnan roles familiares:_fraternal, sororal, maternal, maternal, paternal, abuelita, abuelito, conyugal, maternal, paternal._ Para el altruismo recíproco, sigo la definición de Trivers. 

>  _“En cuanto al altruismo recíproco humano, se muestra que los detalles del sistema psicológico que regula este altruismo pueden explicarse por el modelo. Específicamente, **amistad, aversión, agresión moralista, gratitud, simpatía, confianza, sospecha, confiabilidad, aspectos de culpa y algunas formas de deshonestidad e hipocresía** pueden explicarse como adaptaciones importantes para regular el sistema altruista. Se considera que cada humano individual posee **tendencias altruistas y de engaño**, cuya expresión es sensible a variables de desarrollo que fueron seleccionadas para establecer las tendencias en un equilibrio apropiado para el entorno social y ecológico local.” _[La Evolución del Altruismo Recíproco](https://www.journals.uchicago.edu/doi/abs/10.1086/406755), Robert Trivers (negritas añadidas)

Considerando esto, elegí:_discriminador, implacable, vengativo, leal, vecinal, cooperativo, confiable,_ y _justo._ Esto es más o menos igual en errar hacia la cooperación pero siguiendo con agresión moralista cuando las cosas salen mal. Además, intenta capturar este altruismo como la antítesis del engaño (por ejemplo, _justo_, _confiable_).

(Para una excelente explicación de la evolución de la confianza, vea [esta](https://ncase.me/trust/) demostración interactiva.)

#### ¿Puedo presentarte el desconocido Modelo de Cinco Factores?

Teóricamente, podríamos usar las cargas de palabras de los Cinco Grandes producidas a través de encuestas, pero la mayoría de estas palabras son lo suficientemente raras como para no ser incluidas. Esto es lo mejor ya que no se obtendría una buena estimación de _abuelita_ por autoinforme entre estudiantes de psicología. Como tal, vectores de palabras calculados usando el modelo de lenguaje RoBERTa. Derivado de una lista grande y [bien caracterizada](https://openpsychologydata.metajnl.com/articles/10.5334/jopd.57/) de palabras de personalidad, los cinco factores resultantes son, en resumen:

  1. Afiliación (o Socialización). ¿Cuánto quieres a esta persona en tu equipo? Similar a Amabilidad pero excluye ser un felpudo. _Crédulo_, por ejemplo, carga neutralmente en Afiliación pero positivamente en Amabilidad.

  2. Dinamismo. Bastante cercano a la Extroversión, pero más sobre un sentido de aventura, y menos sobre confianza.

  3. Orden. Conciencia con un filo. Capacidad para lograr tus propios objetivos. _Exigente_ vs _blando_.

  4. Apego Emocional. Mientras que el Neuroticismo se preocupa por la inestabilidad, esto trata sobre el apego; tanto _cariñoso_ como _rencoroso_ están altamente cargados.

  5. Trascendencia. Este factor se caracteriza por _único, complicado, destinado, discapacitado, místico, con el corazón roto, de otro mundo_ vs. _no filosófico, despreocupado, testarudo, grosero, materialista, egocéntrico, superficial_. Involucra mirar más allá de uno mismo y lo mundano. Ese proceso está, aparentemente, ligado al dolor. De hecho, "perturbado" carga más en Trascendencia que en Apego Emocional (el factor relacionado con el Neuroticismo).

Los nombres para los primeros tres factores se toman del trabajo [pan cultural](https://journals.sagepub.com/doi/10.1002/per.1953) de De Raad porque, cualitativamente, la coincidencia es más cercana que con los Cinco Grandes. Cada factor merece su propio post. (Para aquellos en psicología industrial, sospecho que el Orden está más correlacionado con el éxito empresarial que la Conciencia ya que es más calculador que llegar a tiempo.) Pero proponer modelos no es mi fuerte, y estudios de lenguaje más finos están por venir, lo que puede producir una estructura diferente. Por ahora, estos factores son suficientes. Aquí está su correlación con los Cinco Grandes: 

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!Sxlw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F63c86f00-e0cc-4854-bd8a-e6ba3fc55449_366x374.png)

#### Resultados

Cargas de palabras de altruismo en los primeros cuatro factores (la Trascendencia no es importante en este estudio):

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!Q5sr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4efdfb85-197d-4d57-8a8b-3675eaf2b162_955x735.png)Es prosocial tener fuertes lazos familiares (alta Afiliación), aunque un poco aburrido (neutral a bajo Dinamismo). Todas las palabras se mapean a un lugar similar.

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!f7oe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb08b529e-7443-4f5b-af1e-ce080e36a4b7_961x735.png)Las palabras familiares cargan fuertemente en el apego emocional. Nótese que las relaciones de padres y abuelos están bastante marcadas por género. Los hombres están menos apegados, como predice la [teoría de la inversión parental](http://joelvelasco.net/teaching/3330/trivers72-parentalinvestment.pdf) de Trivers, y las [estadísticas](https://www.pewresearch.org/social-trends/2013/07/02/the-rise-of-single-fathers/) lo confirman. Sin embargo, los hermanos y hermanas están igualmente apegados, y en menor grado que los padres. Pensándolo bien, _conyugal_ no debería haberse incluido en el altruismo sobre parientes de sangre. En acuerdo con los [programas de entrevistas diurnas](https://www.youtube.com/watch?v=jXZB0FeTyE8), carga menos en apego que maternal o abuelita.

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!FYnd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa40e5562-577f-4b55-bd16-d34ccec1c388_955x735.png)Las palabras recíprocas intentan capturar el comportamiento ideal de ojo por ojo cuando un compañero está cooperando o engañando. Como tal, estas palabras están mucho más dispersas, aunque todavía mayormente positivas. Incluso 'discriminador' es ligeramente positivo, lo que significa que no creo que la palabra esté siendo codificada como algo así como 'discriminador racial'—a veces estos lenguajes se confunden con la similitud fonética (por ejemplo, excéntrico y etnocéntrico).

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!lGox!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6eb4b7d2-4728-4f66-83ce-cd95e2346144_961x735.png)La cooperación y la vecindad implican ligeramente que los propios objetivos están quedando en segundo plano. Implacable y discriminador son para aquellos que van en serio.

Para comparar los altruismos, nos gustaría reducir cada uno de estos conjuntos de palabras a solo un vector. (Hay espacio para debatir si eso siquiera tiene sentido dado que el recíproco—y en menor medida el de parentesco—requiere diferentes respuestas a diferentes escenarios.) La solución rápida y sucia es tratar cada constructo como una [Bolsa de Palabras](https://en.wikipedia.org/wiki/Bag-of-words_model) y tomar el promedio. Las cargas medias son:

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!TMN7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe3aaf685-9bb3-4dbf-974f-0ab994f40a88_356x238.png)Estos están estandarizados contra todas las 2819 palabras. En promedio, las palabras de parentesco están de 1 a 1.5 DE en Afiliación y Apego Emocional.

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!mDHG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fba83d4f1-2f47-42e8-a158-368c7681a2db_356x238.png)El altruismo recíproco también involucra Orden, logrando tus propios objetivos.

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!48eW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd912d107-48f4-4d5e-bb23-fe24dd932b78_356x238.png)Diferencia: Cargas de Parentesco menos Recíproco. Dominado por Orden.

### **Discusión**

No creo que el artículo en el espacio de sujetos incluya una medida válida de altruismo de parentesco o recíproco y como tal no agrega a nuestra comprensión de cómo se relaciona con la personalidad. Este es un modo de falla sorprendentemente común. El espacio de palabras proporciona cierta seguridad contra comparaciones inválidas. Tenemos mejor intuición de dónde debería estar una palabra en el espacio de palabras, que de cómo el sujeto 112 debería responder una encuesta. Es más fácil detectar errores. 

Desde un punto de vista bayesiano, algo diferente está sucediendo en el espacio de sujetos vs el espacio de palabras. Los experimentos que incluyen sujetos buscan aportar nueva información a la mesa. La esperanza es que eso actualice la visión del mundo de los lectores. Pero los investigadores (y la gente común) tienen mucha experiencia social y una percepción más aguda de los procesos psicológicos que la instantánea proporcionada por una encuesta. Es difícil mover mucho la aguja. El espacio de palabras es más parecido a visualizar nuestros priors que a producir nuevo conocimiento. Esta visión es valiosa porque el lenguaje es donde la goma se encuentra con el camino, por así decirlo. Como lo expresó JL Austin:

> _“Nuestro acervo común de palabras encarna todas las distinciones que los hombres han encontrado valiosas de trazar, y las conexiones que han encontrado valiosas de marcar, en la vida de muchas generaciones: Estas seguramente son más numerosas, más sólidas, ya que han resistido la larga prueba de la supervivencia del más apto, y más sutiles, al menos en todos los asuntos prácticos ordinarios y razonables, que cualquiera que tú o yo podamos pensar en nuestra butaca una tarde—el método alternativo más favorito.”[Una súplica por excusas](https://sites.ualberta.ca/~francisp/NewPhil448/AustinPlea56.pdf)_

El análisis en el espacio de palabras es comparativamente sencillo. En lugar de tablas de correlaciones y valores p, las palabras simplemente se trazan en los ejes de interés y se hacen juicios visuales. Las palabras de altruismo de parentesco se agrupan estrechamente tanto en Afiliación como en Apego Emocional, los únicos dos factores con cargas considerables. Los padres, pero no los hermanos, están menos apegados que sus contrapartes femeninas, en línea con la teoría de la inversión parental de Trivers. Los hermanos y hermanas tienen tanta razón para cuidar de sus hermanos. Sin embargo, los padres tienen menos razón que las madres. El esperma es barato. Los óvulos y el embarazo son costosos.

Las palabras recíprocas están más dispersas, reflejando rasgos ideales para responder a diferentes escenarios: cooperación o deserción del compañero. La diferencia más destacada es una carga promedio más alta en Orden—lograr los propios objetivos. Inicialmente llamado _altruismo de retorno diferido_, el altruismo recíproco no se trata de sacrificarse por un extraño sino de invertir en tu propio futuro a través de medios prosociales. Por otro lado, el altruismo de parentesco se refiere a ayudar a la familia incluso a expensas propias debido a los genes egoístas tirando de las cuerdas del corazón. Esto es evidente en las cargas más altas de las palabras de altruismo de parentesco en Apego Emocional, apoyando la hipótesis de Ashton. Pero la acción principal está en Orden, lejos de donde los instrumentos del espacio de sujetos fueron diseñados para detectar. Los costos de muestreo en el espacio de sujetos hacen que los resultados dependan más de los priors del investigador.

Interpretar estos gráficos puede sentirse como leer hojas de té, pero estoy aproximadamente un 70% seguro de lo que hay aquí. Una cosa que me hace dudar es que los dos altruismos están representados de diferentes maneras. Las palabras de parentesco describen todas relaciones (por ejemplo, _madre, padre, hermano_), mientras que las palabras recíprocas son una mezcla de relaciones (por ejemplo, _vecino_) y rasgos adecuados en juegos de suma positiva repetidos (por ejemplo, _vengativo, discriminador, cooperativo_). Aparte de la incertidumbre, ¿no sería genial si en una tarde realizara un experimento que combina la experiencia vivida del altruismo de millones de personas? Lo que las generaciones han acordado hace que alguien sea paternal, sororal o vecinal. Como siempre con una nueva fuente de señal, uno comienza disparando desde la cadera. Eventualmente, el Lejano Oeste se domestica; emergen métodos y heurísticas. Hay mucho espacio para mejorar. Los lectores pueden ajustar los conjuntos de palabras y obtener nuevos resultados en cuestión de minutos usando este [cuaderno de colab](https://colab.research.google.com/drive/13DA2IKQ9zRimGedww_09iGT6ehuYriVz?usp=sharing). ¡Por favor, háganlo!

#### Ventajas del espacio de palabras

  1. Conectado a la Hipótesis Léxica. Basado en la realidad social descentralizada.

  2. Menos transformaciones. Cada paso es costoso y introduce sesgo.

  3. Menos intensivo estadísticamente después de la conversión al espacio de palabras. (Menor barrera de entrada.)

  4. El tamaño efectivo de la muestra (aquellos que contribuyeron al modelo de lenguaje a través de comentarios en reddit, escribiendo libros o artículos en pubMed) es mucho más grande y diverso que la mayoría de los estudios.

  5. Mejores perspectivas laborales para doctores en psicología que conocen PNL. 

  6. Más fácil de hacer trabajo multilingüe/multicultural. Algunos modelos están entrenados en 100 idiomas simultáneamente (que es como Meta entrena [filtros de discurso de odio](https://ai.facebook.com/blog/how-ai-is-getting-better-at-detecting-hate-speech/) en idiomas con pocos ejemplos).

  7. Los modelos de lenguaje [siguen](https://openai.com/blog/introducing-text-and-code-embeddings/) [mejorando](https://say-can.github.io).

  8. Ciencia abierta.

  9. [Evitar el IRB](https://slatestarcodex.com/2017/08/29/my-irb-nightmare/).

#### Desventajas

  1. Más partes móviles. ¡Hay miles de millones de parámetros en un modelo de lenguaje! Sin embargo, incluso miles de millones de neuronas y docenas de decisiones de entrenamiento pueden resultar en una representación estable. Cualquier modelo de lenguaje que valga la pena puede completar la analogía “marido es a esposa como rey es a ____”.

  2. No se pueden desglosar los resultados por demografía. A veces es interesante conocer la personalidad de los maestros de escuela primaria entre 25-30. O saber cómo algún constructo se correlaciona con el historial de arrestos. Imposible en el espacio de palabras.

  3. ¿No están los modelos de lenguaje sesgados? Bueno, no más que el autoinforme.

  4. Definir el altruismo como la suma de un montón de vectores de palabras (es decir, una bolsa de palabras) es un poco rudimentario. Hay un margen sustancial para mejorar aquí.

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!ctzj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F455fdb70-3c84-4dfe-81bf-6bf6e676fd44_1600x1128.jpeg)Psicólogos felices con otros 40 años vagando por el espacio de sujetos.

### **Dioses extranjeros**

 _“Creo que Kafka tenía razón cuando dijo que, para un hombre moderno, la burocracia estatal es el único contacto restante con la dimensión de lo divino.”_ ~Zizek, Una Guía del Pervertido para la Ideología

<!-- CHUNK BREAK -->

Él está describiendo aquí, por supuesto, la sensación trascendental de presentar una apelación ante el IRB. Tengo una predicción. El espacio de palabras es lo correcto y adecuado desde una perspectiva de procesamiento de señales, pero su adopción será impulsada tanto por la conveniencia de no estar regulado. El corolario es que el IRB será el primer organismo gubernamental en declarar a los modelos de lenguaje como sintientes.

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!6nGN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fedfc8bac-cf78-40f9-88d3-9a30066ff108_817x1600.jpeg)John difundiendo la buena palabra espacio

### **Preparando el camino**

Nos gustaría extraer relaciones entre constructos de los modelos de lenguaje. Hacerlo de una manera que agregue señal en lugar de más ruido requiere mucho trabajo de validación. Inicialmente, esto significa comparar con resultados de encuestas bien establecidas. ¿Pueden ser recuperados usando vectores de palabras? ¿Dónde fallan? Una vez que eso se ha establecido, cada artículo que termina con "se necesita más investigación" debería encontrar una manera de plantear la pregunta en el espacio de palabras.

Pasé más de un año afinando un [método](https://psyarxiv.com/gdm5v/) para extraer relaciones de personalidad de [RoBERTa](https://arxiv.org/abs/1907.11692), el modelo de última generación en ese momento. Poco después se lanzó GPT-3 y tuvo un mejor desempeño directamente. Que el cómputo supere el conocimiento del dominio es una [lección amarga](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) recurrente dentro de la IA. El cómputo aumenta exponencialmente. Si puedes obtener un 30% de ganancias sobre una solución general de ML usando conocimiento del dominio, también puedes simplemente esperar a que el [cómputo se ponga al día](https://twitter.com/russelljkaplan/status/1513128016452337667) y obtener los mismos resultados usando métodos generales. Encontrar formas de relacionar preguntas de psicología con modelos de PLN disponibles es, por lo tanto, un buen camino a seguir. Un nuevo modelo con un rendimiento notablemente mejor se hace público cada seis meses aproximadamente. Aquellos que validan el espacio de palabras están preparando el camino para inteligencias mayores—[PaLM](https://ai.googleblog.com/2022/04/pathways-language-model-palm-scaling-to.html), GPT-7, OSCar (**O** ptimal **S** entience **Car** tography)—para que lluevan verdades psicológicas.

El lenguaje natural está lleno de teorías compartidas sobre el mundo. Ahora que podemos cuantificarlas, ¿no pueden usarse como evidencia?

Si encuentras esto interesante, ¡por favor comparte!

[Compartir](https://www.vectorsofmind.com/p/in-the-beginning-was-the-word?utm_source=substack&utm_medium=email&utm_content=share&action=share)