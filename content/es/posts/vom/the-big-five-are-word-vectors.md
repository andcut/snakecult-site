---
about:
- vectors-of-mind
- blog-archive
author: Andrew Cutler
date: '2025-07-04'
description: Lexical studies in psychology and Latent Semantic Analysis in computer
  science were introduced a half century apart to solve different problems and yet
  are mathematically equivalent. This isn’t a meta...
draft: false
keywords:
- vectors-of-mind
- five
- word
- vectors

lastmod: '2025-07-04'
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '50351822'
original_url: https://www.vectorsofmind.com/p/the-big-five-are-word-vectors
quality: 6
slug: the-big-five-are-word-vectors
tags: []
title: The Big Five Are Word Vectors
translation_model: gpt-4o
---

*From [Vectors of Mind](https://www.vectorsofmind.com/p/the-big-five-are-word-vectors) - imágenes en el original.*

---

Los estudios léxicos en psicología y el Análisis Semántico Latente en ciencias de la computación se introdujeron con medio siglo de diferencia para resolver problemas distintos y, sin embargo, son matemáticamente equivalentes. Esto no es una metáfora que funciona en un cierto nivel de abstracción _;_ los Cinco Grandes son dimensiones de [vectores de palabras](https://dzone.com/articles/introduction-to-word-vectors).

Pero primero, un poco de contexto. La Hipótesis Léxica sostiene que la estructura de la personalidad estará escrita en el lenguaje, ya que los hablantes deben describir los atributos más destacados de quienes los rodean. La belleza de esta idea es que, en lugar de que una sola persona sugiera un modelo de personalidad, el lenguaje registra lo que millones de personas implícitamente acuerdan que es útil. La tarea del psicometrista es simplemente identificar esta estructura. Esto se ha logrado típicamente invitando a estudiantes de psicología a calificarse a sí mismos en listas de adjetivos y realizando un análisis factorial en la matriz de correlación. En 1933, LL Thurstone administró una encuesta de 60 adjetivos a 1300 personas. En su obra seminal [The Vectors of Mind](http://psych.colorado.edu/~carey/Courses/PSYC5112/Readings/VectorsOfMind_Thurstone.pdf), informa que "cinco factores son suficientes" para explicar los datos. En las décadas siguientes, tales estudios, más o menos, resultaron en cinco componentes principales: Amabilidad, Extroversión, Responsabilidad, Neuroticismo y Apertura/Intelecto. (Para un excelente tratamiento del tema, ver [Lexical Foundations of the Big Five](https://www.researchgate.net/profile/Boele-Raad-2/publication/282980275_The_Lexical_Foundation_of_the_Big_Five-Factor_Model/links/5626198508aed3d3f137e522/The-Lexical-Foundation-of-the-Big-Five-Factor-Model.pdf).)

El Análisis Semántico Latente fue [introducido](https://dl.acm.org/doi/abs/10.1145/57167.57214?casa_token=ogUyQ6VJeZgAAAAA:ksULYwu-Km_5Ap0wA2ho3tbwzTjsB0tHONfEEMIldNB6PJgkRyM7eFaa7uZ-XZJ3nYo0MbYFeJsBng) como una técnica de recuperación de información en 1988. Las palabras pueden representarse como vectores y los documentos o frases pueden representarse como la media de sus vectores de palabras. Si deseas buscar en una gran base de datos (por ejemplo, Wikipedia), las palabras clave para cada página solo te llevarán hasta cierto punto. Una forma de solucionar esto es representar tanto los documentos (artículos de wiki) como las consultas (términos de búsqueda) como la media de sus vectores de palabras. Encontrar documentos relevantes ahora se puede lograr con un simple producto punto. (En esta publicación, trato el LSA y los vectores de palabras como sinónimos. Hay otras formas de vectorizar el lenguaje y, más específicamente, de crear vectores de palabras, pero esas están fuera del alcance por ahora.)

A pesar de sus diferentes usos e historia, los pasos son los mismos:

  1. Recopilar una matriz de conteo de palabra x documento

  2. Transformación no lineal

  3. Descomposición de la matriz

  4. Rotación (Opcional)

El resultado es un conjunto de vectores de palabras que describen sucintamente cada palabra. Estos pueden usarse para una serie de tareas posteriores, desde análisis de sentimientos hasta predicción de narcisismo a partir de ensayos de estudiantes. En el caso de los adjetivos de personalidad, las dimensiones de los vectores de palabras fueron analizadas, nombradas y debatidas durante décadas. Lo que sigue es una discusión de las diferencias en cada paso.

**Matriz de conteo.** El LSA generalmente involucra un gran número de documentos variados (por ejemplo, millones de reseñas de productos de Amazon). Estos se transforman en una matriz de palabra x documento contando cuántas veces aparece cada palabra en cada documento. En psicología, un documento son las palabras con las que un sujeto está de acuerdo que lo describen. Esto se extiende también a las escalas de Likert. Si alguien dice que una palabra lo describe 5/7, entonces simplemente repite la palabra cinco veces en el documento.

**Transformación no lineal.** Los estudios léxicos a menudo ipsatizan los datos (puntaje z a lo largo del eje del sujeto) y luego realizan una correlación de Pearson. Thurstone utilizó una antigua correlación tetrárquica en su estudio. En el LSA, la transformación más común es TF-IDF, seguida de un logaritmo. Esto asegura que la matriz no esté dominada por términos comunes. A menudo, la transformación resulta en una matriz de afinidad de palabra x palabra (por ejemplo, matriz de correlación). Este paso es prácticamente muy importante pero no tan teórico. La transformación a elegir es la que te da un resultado razonable al final.

**Descomposición de la matriz.** Hay muchos métodos de descomposición de matrices. Algunos, como el PCA, requieren una matriz cuadrada. Otros son robustos a datos faltantes. Con los datos de personalidad, la elección no importa mucho; los resultados son muy similares. Los vectores de palabras generales requieren ~300 dimensiones para representar el significado de una palabra, su parte del discurso, su jerga y mucho más que le da textura al lenguaje. Como las encuestas están diseñadas para mantener mucho de eso constante, solo se necesitan ~5 dimensiones. Thurstone justificó su elección de cinco al observar el error de reconstrucción que informa como un histograma. Psicólogos posteriores justificaron 5 por el error de reconstrucción (medido con valores propios), así como considerando la interpretabilidad y la reproducibilidad.

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!Zw-J!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd562c1c2-1576-4fad-896c-52e799d4598b_1600x1066.png)Error de reconstrucción de la matriz de correlación de palabras. A pesar de las limitaciones computacionales, su muestra es un orden de magnitud mayor que muchos estudios modernos.

**Rotación.** ¿Alguna vez has oído hablar de la sobreextracción de componentes? No es una historia que los psicólogos te contarían. Es cuando un investigador extrae demasiados Componentes Principales y luego rota la varianza de los primeros PCs válidos a los PCs marginales posteriores. ¡Esto es lo que sucedió con los Cinco Grandes, aunque no lo creas! Lo que ahora es Amabilidad fue una vez un factor de 'Socialización' mucho más robusto y teóricamente satisfactorio, que se extendió sobre los PCs 3-5 para formar Responsabilidad, Neuroticismo y Apertura. La rotación _puede_ justificarse para producir factores interpretables. Pero si alguna vez te encuentras rotando y luego discutiendo sobre el número correcto de factores, ¡revísate!

**Los Tres Grandes de los vectores de palabras**

Comencé mi doctorado prediciendo rasgos de los Cinco Grandes a partir de estados de Facebook. Después de leer cómo se hacía la salchicha de la personalidad, me di cuenta de que el proyecto usaba vectores de palabras (de estados de Facebook) para predecir aproximaciones ruidosas de dónde vivían los individuos en el espacio de los Cinco Grandes, que originalmente se definió por vectores de palabras. Parecía más interesante ir al grano y aprender algo fundamental sobre la personalidad a partir de vectores de palabras. (Además, el conjunto de datos que estaba usando se volvió tóxico después de Cambridge Analytica.) El resto de mi doctorado consistió en trabajar para restringir los vectores de palabras con el fin de reproducir los Cinco Grandes. Esto implicó usar transformadores en lugar de LSA (más sobre eso en futuras publicaciones). La correlación resultante entre factores de vectores de palabras (DeBERTa) frente a encuestas se muestra a continuación. Como puedes ver, hay una concordancia muy cercana para los primeros tres factores. Donde los resultados divergen, no está claro qué método está en error. Tal vez las encuestas sean correctas, y todas las correlaciones llegarán a 1 cuando tengamos GPT-5. Tal vez las encuestas estén sesgadas y sean ruidosas, y se extrajeron demasiados PCs. Tal vez estén midiendo cosas diferentes, y necesitamos refinar nuestra interpretación de ambos. En cualquier caso, no me parece obvio que las encuestas deban considerarse el estándar de oro entre los dos. Después de todo, la Hipótesis Léxica trata sobre la estructura del lenguaje, y la psicología es el único campo que utiliza encuestas para analizar el lenguaje natural.

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!lY1-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6bf087b4-76cc-4272-a2f7-037d606ed2ba_726x682.png)Los PCs de encuestas no rotados son de uno de los [estudios](https://onlinelibrary.wiley.com/doi/10.1002/\(SICI\)1099-0984\(199603\)10:1%3C61::AID-PER246%3E3.0.CO;2-D) que definieron los Cinco Grandes. Los PCs de DeBERTa se extraen de vectores de palabras. Lee sobre ese proceso [aquí](https://psyarxiv.com/gdm5v/).

**Conclusión**

Thurstone fue pionero en métodos en estadística y álgebra lineal para explorar la Hipótesis Léxica en los años 30. Es notable que desarrolló una forma de representar palabras que luego fue redescubierta para la recuperación de información, que ahora impulsa la era de la información. La computación obligó a Thurstone a aplanar el rico paisaje del lenguaje a respuestas de encuestas. En los últimos 30 años, el PLN ha experimentado múltiples revoluciones. Si Thurstone inventó un telescopio con el cual observar la estructura del lenguaje, ahora tenemos el Hubble. ¡Muchos descubrimientos nos esperan!