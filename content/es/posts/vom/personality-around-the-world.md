---
about:
- vectors-of-mind
- blog-archive
author: Andrew Cutler
date: '2025-07-04'
description: Okay, let’s take a little reprieve from the sapience stuff. I actually
  had a bunch of psychometrics queued up before being pulled in by the clarion call
  of consciousness. It’s just so hard to look awa...
draft: false
keywords:
- vectors-of-mind
- personality
- around
- world
lang: es
lastmod: '2025-07-04'
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '108601152'
original_url: https://www.vectorsofmind.com/p/personality-around-the-world
quality: 6
slug: personality-around-the-world
tags: []
title: Personality Around The World
translation_model: gpt-4o
---

*De [Vectors of Mind](https://www.vectorsofmind.com/p/personality-around-the-world) - imágenes en el original.*

---

Bien, tomemos un pequeño respiro del tema de la sapiencia. En realidad, tenía un montón de psicometría preparada antes de ser atraído por el llamado clarion de la conciencia. Es simplemente tan difícil mirar hacia otro lado.

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!X2nA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F62106fb3-6e73-444d-96f1-07b95ec828f9_1024x506.jpeg)[Ulises y las sirenas](https://en.wikipedia.org/wiki/Ulysses_and_the_Sirens_\(Waterhouse\)), pintura de [John William Waterhouse](https://en.wikipedia.org/wiki/John_William_Waterhouse)

Comencé este blog para explorar la Hipótesis Léxica desde una perspectiva de aprendizaje automático. Los modelos de personalidad definen los rasgos más comentados en un idioma, y podemos medir eso mucho mejor en la era de GPT. Los modelos de personalidad derivados de vectores de palabras o encuestas tradicionales vuelven a los mismos pocos rasgos, especialmente los Dos Grandes: autorregulación social y dinamismo. Para refrescarte sobre esto, revisa [Los Cinco Grandes son Vectores de Palabras](https://vectors.substack.com/p/the-big-five-are-word-vectors) y [El Factor Primario de la Personalidad](https://vectors.substack.com/p/primary-factor-of-personality-part).

Los Cinco Grandes se han encontrado en muchos idiomas de manera independiente, pero la comparación entre idiomas siempre es cualitativa. Los investigadores administran una encuesta de adjetivos de personalidad en turco o alemán, la factorizan y más o menos observan los factores para ver si son los mismos. Estos datos no pueden usarse para decir "La extraversión está desplazada 15 grados de la conciencia en alemán comparado con el inglés". Para ser tan preciso, ambos idiomas tendrían que compartir alguna base.

Si administras preguntas en múltiples idiomas, puedes relacionarlas 1) encontrando un grupo bilingüe que pueda responder en ambos idiomas o 2) asumiendo que las traducciones de palabras son 1:1 (por ejemplo, _fun_ es perfectamente equivalente a _divertido_ en español). En el primer caso, hay un fuerte efecto de selección. ¿Qué pasa si las personas bilingües tienden a estar mejor educadas? El segundo simplemente no es cierto. De hecho, la razón para factorizar idiomas juntos es entender cómo la estructura de la personalidad puede divergir entre ellos. Asumir que las palabras son las mismas derrota el propósito.

**[Mi investigación](https://arxiv.org/abs/2203.02092) mostró que puedes extraer la estructura de la personalidad de los modelos de lenguaje en inglés. Una pregunta natural es cómo cambia eso cuando agregas otros idiomas.** Con modelos entrenados en docenas de idiomas, esto se vuelve bastante sencillo de explorar. Puedes mapear cualquier número de idiomas a la misma base.

## Los Dos Grandes, una vez más

Usé [XLM-RoBERTa](https://huggingface.co/xlm-roberta-base) para asignar similitud entre adjetivos de personalidad. Extrañamente, este modelo es un resultado del genocidio en Myanmar. Meta tiene la posición poco envidiable de necesitar eliminar contenido en lugares de los que tienen muy poco entendimiento. Técnicamente, esto es lo que se llama un problema de aprendizaje por transferencia. Les gustaría entrenar un clasificador de discurso de odio en inglés (u otro idioma bien documentado), y luego aplicarlo a otros idiomas. En la era oscura del modelado de lenguaje (2018), esto funcionaba muy mal. El habla coloquial en birmano para "vamos a reunir a los gays y matarlos" parecía a sus clasificadores como "debería haber menos arcoíris". Esto, por supuesto, pasaba por alto su moderación de contenido. El NYT explicó la consecuencia: _**[Un genocidio incitado en Facebook, con publicaciones del ejército de Myanmar](https://www.nytimes.com/2018/10/15/technology/myanmar-facebook-genocide.html)**_

La respuesta de Meta fue construir un modelo de lenguaje que pudiera mapear mejor cualquier idioma (bueno, 100 idiomas) a vectores de palabras en el mismo espacio compartido. De esa manera, un clasificador de discurso de odio entrenado en inglés puede extenderse mejor a otros idiomas. (Se necesita menos birmano para ajustarlo). Usando este modelo, incrusté palabras de personalidad en cuatro idiomas: inglés, español, francés y turco. A continuación se muestran los dos primeros factores:

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!eLVQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd3ff00d-d96d-4e3b-ada4-640e3cd66089_1245x954.png)

Estos sirven para separar los diferentes idiomas. El primer factor distingue el turco de los idiomas indoeuropeos. En el segundo factor, los idiomas romances están adyacentes (aunque también cerca del turco).

Esto tiene sentido. El modelo está entrenado para predecir la siguiente palabra de una oración, por lo que naturalmente incluirá información específica del idioma. Si alguien está hablando en español, no suele cambiar a turco. La esperanza es que también haya direcciones en el espacio vectorial que correspondan a información de personalidad.

Si los idiomas son bastante independientes, necesitas al menos 3 dimensiones para separar 4 idiomas en sus propios grupos no superpuestos. Veamos los siguientes componentes principales.

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!PRKA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5eb70bd2-8684-4844-94bd-aa12adc030bf_1256x954.png)

El Factor 4 es el primer factor que no se aprendió para separar los idiomas, ¡y es el Factor General de Personalidad! En inglés: _dominante, despiadado, compulsivo_ y _egoísta_ **vs** _generoso, amable_ y _considerado_. [He argumentado](https://vectors.substack.com/p/primary-factor-of-personality-part) que este factor se entiende mejor como la tendencia a vivir la Regla de Oro. La Teoría de Eva de la Conciencia fue en realidad un resultado de [preguntarse qué seleccionaría esto](https://vectors.substack.com/p/consequences-of-conscience) en nuestra historia evolutiva. El Factor 5 también trata sobre la personalidad, trazándolos juntos:

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!pD64!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F192dc8f4-db5e-4d96-b8a5-ce16c1cbf1f6_1264x954.png)

¡Obtenemos los Dos Grandes! El Factor Cinco (o dos, de los factores de personalidad) es el Dinamismo: _aventurero, imaginativo_ y _entusiasta_ **vs** _cauteloso, reservado_ y _cobarde._ Es sorprendente que esto surja tan regularmente. **Hay [2,500 citas en el artículo de los Dos Grandes](https://scholar.google.com/scholar?cites=11052969740325606797&as_sdt=2005&sciodt=0,5&hl=en), y aún así los investigadores no se dan cuenta de que son simplemente los dos primeros factores no rotados de la personalidad general.** La creencia común de que de alguna manera existen en una relación jerárquica con los Cinco Grandes proviene de que los investigadores abandonaron el trato directo con el lenguaje poco después de hacer los inventarios de los Cinco Grandes. Desde entonces, cualquier intento de entender la personalidad básica o general debe hacerse en referencia a los Cinco Grandes. Pero las palabras vinieron primero, y los modelos de lenguaje facilitan analizar el lenguaje en ese nivel fundamental ahora.

[Compartir](https://www.vectorsofmind.com/p/personality-around-the-world?utm_source=substack&utm_medium=email&utm_content=share&action=share)

## Tenemos que ir más profundo

Agregar ruso y farsi produce los mismos factores:

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!IIKx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F976f1c11-fd97-4184-a74a-a384a09b0579_2078x1715.png)Para ver mejor las palabras, descarga la imagen y haz zoom.

Según mis estándares de ingeniero perezoso, esto es bastante laborioso porque requiere encontrar un buen prompt para cada idioma. Trabajé con Google Translate y hablantes nativos para hacerlo bien, y puedes ver que la distribución del farsi todavía está desfasada en el Factor 4. Mi suposición es que mi método de ignorar cualquier factor que no sea compartido es demasiado rudimentario para tantos idiomas. El Factor 4 probablemente se usa como el GFP, y también para separar el farsi (solo un poco). No hay nada que mantenga estos factores puros, realmente tenemos suerte de que la distribución sea tan bien comportada como es. Hacer algún preprocesamiento (como dar un significado cero a cada grupo de idiomas) podría resolver esto.

Hasta donde sé, esta es la primera vez que múltiples idiomas se han factorizado juntos. Esto sería publicable con resultados solo en inglés y español, y aquí llegué hasta seis, incluyendo dos idiomas no indoeuropeos. También arroja luz sobre la naturaleza de los Dos Grandes, uno de los constructos más populares—y mal entendidos—en psicometría.

## Deficiencias

Hice esta investigación de la manera más tonta posible. Encontré 100 palabras de personalidad en una guía de ESL, y luego las traduje a otros idiomas usando Google Translate. Si había duplicados, los eliminaba. Esto no es tan malo como parece. Los dos primeros factores son prácticamente inalterados en inglés, ya sea que uses 100 o 500 palabras. Pero, si esto fuera un artículo real, obviamente querrías desarrollar un conjunto de palabras en cada vocabulario de manera independiente. Hay varias otras deficiencias:

**¡No hay suficientes idiomas!** Si publicara esto, me gustaría agregar una docena más de idiomas que no suelen estudiarse en la ciencia de la personalidad. De hecho, por eso nunca llegué a publicarlo. Es mucho trabajo y requeriría hablantes nativos de varios idiomas asiáticos.

**Modelos multilingües deformados por los datos de entrenamiento.** Los modelos de lenguaje están entrenados para predecir la siguiente palabra de una oración. Si entrenas con múltiples idiomas, el modelo intentará transferir parte del conocimiento. Sin embargo, para los idiomas más pequeños esto podría parecer más como que sus significados son forzados a analogías dentro de los idiomas mejor documentados (inglés, chino, ruso, etc.).

**Las consultas son un grado de libertad del investigador.** El método que uso para incrustar palabras es "Mi personalidad puede describirse como <mask> y [palabra]" donde [palabra] es una de las palabras de personalidad. Debido a la forma en que está escrita la oración, el modelo carga información de personalidad pura en el token de máscara y luego lo incrusta. En mi disertación, encontré que esto funcionaba mejor. Por supuesto, hay infinitas variaciones a esto, y tienes que seleccionar una. Teóricamente, un investigador podría tener un resultado particular en mente, y luego encontrar una consulta que lo respalde. En mi opinión, no es demasiado arriesgado, dado lo similar que es este resultado a lo que producen los métodos de encuesta. Tenemos un precedente bastante fuerte sobre qué estructura de personalidad encontramos con el análisis factorial. Este método que lo recapitula es evidencia de que el método funciona.

**Modelo de lenguaje desactualizado.** Hice este trabajo hace más de 2 años, mucho antes de que saliera GPT-4. Tiempos más simples.

## Conclusión

Si todavía estuviera en la academia, este sería mi agenda de investigación. Agregar tantos idiomas como sea posible, y tratar de entender todas las formas en que el método puede estar sesgado. Al final, puede producir un modelo universal de personalidad superior a los Cinco Grandes. Nos ayudaría a entender mejor quiénes somos, y tal vez incluso de dónde venimos. Porque es el lenguaje lo que define a nuestra especie ahora, y fue el lenguaje lo que forjó nuestra psique en el pasado. Somos habitualmente sociales porque hace miles de años, fallar en manejar tu reputación era morir. Los modelos de personalidad son mapas del lenguaje; son vectores en la evolución de nuestra mente.

[Suscríbete ahora](https://www.vectorsofmind.com/subscribe?)

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!MDwl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F935dcb92-8e91-41c3-9630-2a80f2bc9a06_1024x1024.png)