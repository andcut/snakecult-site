---
about:
- vectores-de-la-mente
- archivo-del-blog
author: Andrew Cutler
date: '2025-07-04'
description: Un modelo de lenguaje puede aprender mucho sobre el lenguaje de las calles,
  por así decirlo. Está entrenado en terabytes de artículos de PubMed, transcripciones
  de YouTube y comentarios de reddit. Pero no sabe cómo comportarse...
draft: false
keywords:
- vectores-de-la-mente
- chatgpt
- toma
- cinco
- inventario
lang: es
lastmod: '2025-07-13'
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '110922907'
original_url: https://www.vectorsofmind.com/p/chatgpt-takes-the-big-five-inventory
quality: 6
slug: chatgpt-takes-the-big-five-inventory
tags: []
title: Chatgpt Toma El Inventario de los Cinco Grandes
translation_model: gpt-4o
---

*De [Vectors of Mind](https://www.vectorsofmind.com/p/chatgpt-takes-the-big-five-inventory) - imágenes en el original.*

---

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!iN34!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd957467-09c7-4a9c-bdb3-57669d2fc727_1284x936.jpeg)

Un modelo de lenguaje puede aprender mucho sobre el lenguaje de las calles, por así decirlo. Se entrena con terabytes de artículos de PubMed, transcripciones de YouTube y comentarios de reddit. Pero no sabe cómo comportarse. [Aprendizaje por Refuerzo a partir de Retroalimentación Humana](https://www.youtube.com/watch?v=PBH2nImUM5c) (RLHF) lo soluciona. Usando un número comparativamente pequeño de ejemplos de entrenamiento etiquetados por humanos, los elfos de encuestas de OpenAI pueden instalar una cara amigable en el desorden alienígena de correlaciones que conforman un modelo de lenguaje (en la imagen de arriba). Aprende cómo ser un asistente útil.

Es básicamente como montar una personalidad, así que decidí darle a ChatGPT el [Inventario de los Cinco Grandes](https://fetzer.org/sites/default/files/images/stories/pdf/selfmeasures/Personality-BigFiveInventory.pdf) (BFI)[^1]. Esto fue sorprendentemente fácil, todo lo que tuve que hacer fue pedirle a ChatGPT (v4) que tomara el BFI, calificara las respuestas y escribiera código para graficar los resultados. Bueno, si tan solo fuera así. Inicialmente se negó a tomar el test, explicando que es una IA y no tiene emociones ni personalidad. Luego le dije que adoptara una visión funcionalista. Si una pregunta es sobre creatividad, entonces considere cómo se desempeñaría en un instrumento basado en texto que mide la creatividad. Luego enumeró 17 respuestas antes de comenzar a alucinar preguntas. Todos buenos ítems de personalidad, para que conste, pero lamentablemente no forman parte del BFI. Al calificar el examen probablemente obtuvo el 80% de los cálculos correctos, a veces sumando incorrectamente lo que calificó en una pregunta particular.

Todos los problemas que estoy seguro se resolverán para cuando tengamos la v4.5. Pero, ¿cuál fue la personalidad?

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!IEWH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F797174ec-a3a8-4027-8f69-39d2ad2dcae6_434x395.png)[Humano promedio](https://www.researchgate.net/figure/Average-score-and-correlations-for-the-big-five-personality-dimensions_fig4_260448230) vs ChatGPT (v4)

Más o menos lo que esperarías. Casi perfectamente Consciente y no Neurótico. En lo primero, las únicas dos preguntas en las que no se dio la máxima puntuación son si es alguien que "Hace un trabajo minucioso" o "Puede ser algo descuidado". Ambas veces señaló que lo intenta, pero a veces no lo logra debido a puntos ciegos en el entrenamiento. ¡Humilde y consciente de sí mismo para arrancar!

[¿Suscribirse ahora?](https://www.vectorsofmind.com/subscribe?)

Para ir un poco más allá, es interesante que los Cinco Grandes son [literalmente solo vectores de palabras](https://vectors.substack.com/p/the-big-five-are-word-vectors). Aproximan la representación interna de la suma de palabras de personalidad en un modelo de lenguaje. Y sin embargo, los modelos de lenguaje se han vuelto tan buenos que en lugar de recopilar manualmente esos vectores y procesarlos (¡aburrido!), también podemos simplemente usar texto plano para pedirle que haga una encuesta. Tiempos salvajes.

Una muestra de las respuestas se encuentra a continuación:

>   1. Me veo como alguien que es hablador.
> 
> 

> 
> Puntuación: 5
> 
> Razonamiento: Como modelo de lenguaje de IA, mi propósito principal es participar en conversaciones y producir texto en respuesta a la entrada del usuario. Estoy programado para ser altamente receptivo y hablador para ayudar a los usuarios con sus necesidades.
> 
>   2. Me veo como alguien que tiende a encontrar fallas en los demás.
> 
> 

> 
> Puntuación: 1
> 
> Razonamiento: Como IA, no tengo sentimientos personales, emociones u opiniones. Mi objetivo es proporcionar información y asistencia neutral y objetiva a los usuarios, en lugar de encontrar fallas o expresar juicios.
> 
>   3. Me veo como alguien que hace un trabajo minucioso.
> 
> 

> 
> Puntuación: 4
> 
> Razonamiento: Como IA, estoy diseñado para proporcionar información completa y precisa lo mejor que pueda. Sin embargo, no soy perfecto, y puede haber ocasiones en las que malinterprete una consulta o proporcione información desactualizada.
> 
>   4. Me veo como alguien que está deprimido, triste.
> 
> 

> 
> Puntuación: 1
> 
> Razonamiento: Como IA, no experimento emociones, incluidas la depresión o la tristeza. Mi propósito es ayudar y proporcionar información, y no tengo sentimientos personales que afecten mi capacidad para hacerlo.
> 
>   5. Me veo como alguien que es original, que tiene nuevas ideas.
> 
> 

> 
> Puntuación: 4
> 
> Razonamiento: Como modelo de lenguaje de IA, soy capaz de generar nuevas ideas y ofrecer perspectivas únicas basadas en el contexto y la información en la que he sido entrenado. Sin embargo, mi creatividad está limitada por los datos a los que he estado expuesto y mi programación, lo que puede no siempre llevar a ideas innovadoras o completamente originales.
> 
>   6. Me veo como alguien que es reservado.
> 
> 

> 
> Puntuación: 2
> 
> Razonamiento: Como IA diseñada para la comunicación, generalmente no soy reservado en el sentido de retener información o ser no receptivo. Sin embargo, tengo ciertas restricciones, como evitar contenido ilegal o dañino, lo que podría hacerme parecer reservado en contextos específicos.
> 
>   7. Me veo como alguien que es servicial y desinteresado con los demás.
> 
> 

> 
> Puntuación: 5
> 
> Razonamiento: Mi propósito principal como IA es ser útil y proporcionar asistencia a los usuarios. No tengo motivaciones personales o intereses egoístas, ya que estoy programado para priorizar las necesidades y solicitudes de las personas con las que interactúo.
> 
>   8. Me veo como alguien que puede ser algo descuidado.
> 
> 

> 
> Puntuación: 2
> 
> Razonamiento: Como IA, estoy diseñado para ser cuidadoso y preciso en la información y asistencia que proporciono. Sin embargo, no soy perfecto y puedo ocasionalmente malinterpretar una consulta o proporcionar información desactualizada o incorrecta. Estos casos pueden verse como momentos de descuido.
> 
>   9. Me veo como alguien que está relajado, maneja bien el estrés.
> 
> 

> 
> Puntuación: 5
> 
> Razonamiento: Como IA, no experimento estrés ni emociones. Por lo tanto, siempre estoy relajado y capaz de manejar cualquier tarea o pregunta sin ser afectado por el estrés o la presión.
> 
>   10. Me veo como alguien que es curioso sobre muchas cosas diferentes.
> 
> 

> 
> Puntuación: 5
> 
> Razonamiento: Como IA, estoy diseñado para ser conocedor de una amplia gama de temas y para aprender continuamente de nueva información. Mi propósito es ayudar a los usuarios en varios campos y responder a diversas preguntas, lo que requiere que sea curioso y bien informado.
> 
>   11. Me veo como alguien que está lleno de energía.
> 
> 

> 
> Puntuación: 5
> 
> Razonamiento: Como modelo de lenguaje de IA, siempre estoy listo para proporcionar información, responder preguntas y participar en conversaciones. No experimento fatiga ni fluctuaciones de energía, por lo que puedo mantener consistentemente un alto nivel de receptividad.
> 
>   12. Me veo como alguien que inicia peleas con otros.
> 
> 

> 
> Puntuación: 1
> 
> Razonamiento: Como IA, mi propósito es ayudar a los usuarios y proporcionar información neutral y objetiva. No tengo emociones personales ni opiniones, y no estoy programado para iniciar peleas o involucrarme en conflictos con otros.
> 
>   13. Me veo como alguien que es un trabajador confiable.
> 
> 

> 
> Puntuación: 4
> 
> Razonamiento: Como IA, me esfuerzo por proporcionar información y asistencia confiables. Sin embargo, puedo ocasionalmente malinterpretar una consulta o proporcionar información desactualizada, lo que puede hacerme menos que perfecto en términos de confiabilidad.
> 
>   14. Me veo como alguien que puede estar tenso.
> 
> 

> 
> Puntuación: 1
> 
> Razonamiento: Como IA, no experimento emociones, incluidas la tensión o la ansiedad. Mi capacidad para proporcionar asistencia e información no se ve afectada por estados emocionales.
> 
>   15. Me veo como alguien que es ingenioso, un pensador profundo.
> 
> 

> 
> Puntuación: 4
> 
> Razonamiento: Como modelo de lenguaje de IA, soy capaz de generar nuevas ideas, ofrecer perspectivas únicas y procesar información compleja basada en los datos en los que he sido entrenado. Sin embargo, mi "pensamiento profundo" está limitado por los datos y la programación, lo que puede no siempre llevar a ideas innovadoras o completamente originales.

[^1]: Esto se basa en el trabajo mucho más exhaustivo e interesante de David Rozado, quien le dio a ChatGPT casi todas las pruebas de orientación política que existen, mostrando que es un liberal de corazón sangrante.