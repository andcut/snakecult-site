---
about:
- vectores-de-la-mente
- archivo-del-blog
author: Andrew Cutler
date: '2025-07-04'
description: 'Mi trabajo se ha acercado peligrosamente a un Ingeniero de Prompts.
  Esto está bien para mí, ya que combina mi amor por la escritura, la psicometría
  y el PLN. Aquí están algunas de las técnicas de solicitud más poderosas:'
draft: false
keywords:
- vectores-de-la-mente
- solicitud
- chatgpt
lang: es
lastmod: '2025-07-09'
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '145544092'
original_url: https://www.vectorsofmind.com/p/how-to-prompt-chatgpt
quality: 6
slug: how-to-prompt-chatgpt
tags: []
title: Cómo Solicitar a Chatgpt
translation_model: gpt-4o
---

*De [Vectors of Mind](https://www.vectorsofmind.com/p/how-to-prompt-chatgpt) - imágenes en el original.*

---

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!EpIx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F719d87af-7c69-45fd-8c84-595b16af3dae_1024x1024.webp)Tú después de leer este post

Mi trabajo se ha acercado peligrosamente a un Ingeniero de Prompts[^1]. Esto está bien para mí, ya que combina mi amor por la escritura, la psicometría y el PLN. Aquí están algunas de las técnicas de prompts más poderosas:

  1. Usa instrucciones claras y específicas

  2. Razonamiento en cadena de pensamiento

  3. Recopila la información necesaria antes de realizar una tarea

  4. Divide las tareas en pasos

  5. Los términos técnicos son tus amigos

  6. Surtido de frases útiles




#### **1\. Instrucciones claras y específicas**


Los abogados y los científicos de la computación son naturalmente buenos en esto. De hecho, una de las alegrías de crear prompts es que uno puede ser mucho menos preciso en comparación con el código regular, y los LLMs a menudo captan la esencia. Sin embargo, muchas solicitudes pueden mejorarse simplemente siendo explícito sobre la tarea y el formato que debe tener la respuesta. Por ejemplo, recientemente improvisé esta comida:

[*[Imagen: Contenido visual del post original]*](https://substackcdn.com/image/fetch/$s_!dVwU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F216d83a0-b1be-4f15-877a-bfbb9842c0ed_1284x1253.jpeg)

Estaba deliciosa, gracias por preguntar. Otros ejemplos:

  * “Resume la historia de la IA en un párrafo.”

  * “Crea una tabla de las familias de lenguas más antiguas ordenadas por antigüedad. Sé exhaustivo.”[^2]

  * “Reescribe el texto citado al estilo de White y Strunk. Dame tres opciones.”

  * “Calcula una matriz de correlación de Pearson para las columnas 2-7 del archivo .csv adjunto.”

    * seguimiento: “Escribe código para mostrar los resultados como un mapa de calor con suficiente resolución para que pueda usarse en un póster. Usa las mejores prácticas en elecciones estéticas”

Las instrucciones específicas a menudo incluyen ejemplos específicos. White y Strunk escribieron _Elements of Style_. Citar su libro es mejor que usar adjetivos como “conciso”, “profesional” o “excelente” escritura. En parte porque los LLMs tienden a excederse, especialmente con adjetivos específicos. Por lo tanto, si quieres que el robot adopte una personalidad atrevida, intenta decirle que actúe como Veronica Mars o Regina George de Mean Girls.

#### **2\. Razonamiento en cadena de pensamiento**


Los LLMs están entrenados en un enorme corpus de texto para predecir la siguiente palabra. Sorprendentemente, esto los hace buenos para aproximar el razonamiento, pero rápidamente se descomponen en tareas complejas. Aquí, “complejo” puede significar algo como “suma los números en la columna 1”. Esto es muy difícil de hacer en un solo intento, y escupirá un número que parece razonable y probablemente estará en el rango correcto, pero no será la respuesta correcta. Añadir “piensa en ello en pasos” hace maravillas. A menudo, ni siquiera tienes que especificar cuáles son los pasos; los LLMs pueden inferir que para sumar una columna, los pasos intermedios son escribir “n1 + n2 + n3 + … + n100 =”. Es esencialmente un auto-prompting para obtener una mejor respuesta en el lado derecho de ese signo igual. O, por analogía, darse tiempo para pensarlo. Para cualquier problema, la frase “piensa en ello en pasos” es tu primera línea de defensa para lidiar con las alucinaciones de los LLM. Si eso no funciona, enumera los pasos tú mismo (una técnica a la que volveremos).

#### **3\. Recopila la información necesaria antes de realizar una tarea**


Si le pides a chatGPT que escriba un post de blog (yo nunca lo haría) o una función en Python (absolutamente lo haría), lo hará sin preguntar por los detalles de lo que realmente quieres. Mucho de esto se puede evitar diciendo algo como, “Quiero escribir una función que haga X; ¿qué información necesito recopilar antes de codificar?” o “Escribe una función que haga X, pero primero pregunta por cualquier información necesaria antes de escribir el código.” donde “X” es alguna descripción parcial.

#### 4\. Divide las tareas en pasos


Siempre que chatGPT falla en una tarea y el razonamiento en cadena de pensamiento no ayuda, divide la tarea en subtareas. Esto es a menudo la mitad del trabajo de una tarea para empezar y, coincidentemente, lo que es (actualmente) difícil para los LLMs hacer por sí solos. Sin embargo, nota que a menudo puedes delegar esto al LLM también[^3]. Por ejemplo, le pedí a chatGPT que propusiera ítems para una prueba de creatividad (que puedes hojear):

> Estoy tratando de idear más preguntas similares a la Prueba de Asociaciones Remotas (RAT). La RAT requiere que los individuos encuentren una palabra común que vincule tres palabras aparentemente no relacionadas. Aquí hay algunos conjuntos de palabras de ejemplo:
> 
> 1\. Cabaña, Suizo, Pastel (Respuesta: Queso)
> 
> 2\. Alto, Libro, Silla (Respuesta: Escuela)
> 
> 3\. Fruta, Mirada, Tráfico (Respuesta: Mermelada)
> 
> 4\. Crema, Patín, Agua (Respuesta: Hielo)
> 
> 5\. Dolor, Cazador, Col (Respuesta: Cabeza)
> 
> 6\. Modales, Ronda, Tenis (Respuesta: Mesa)
> 
> 7\. Caída, Actor, Polvo (Respuesta: Estrella)
> 
> 8\. Luz, Cumpleaños, Palo (Respuesta: Vela)
> 
> 9\. Ensalada, Cabeza, Ganso (Respuesta: Huevo)
> 
> 10\. Música, Dolorido, Verde (Respuesta: Manzana)   
>   
> ¿Cuáles son las mejores prácticas? ¿Cómo debería pensar en esto en pasos?

Al igual que entender cómo sumar números, chatGPT es excelente para producir “recetas” para realizar tareas. Después de que entregó, todo lo que tuve que decir fue:

> “¡Genial! Ahora sigue ese proceso para producir 5 nuevas preguntas”

Y luego cinco más, y cinco más. Anteriormente había intentado pedir directamente nuevos ítems, y las sugerencias eran atroces. Para un [ejemplo mucho más complicado](https://redwoodresearch.substack.com/p/getting-50-sota-on-arc-agi-with-gpt), ve cómo un instituto de seguridad de IA utilizó esta técnica (entre otros trucos) para resolver un problema que fue diseñado para ser imposible para los LLMs.

#### 5\. Los términos técnicos son tus amigos


Los términos técnicos son cuencas de atracción para el comportamiento competente de los LLM. Por ejemplo, describir una enfermedad y preguntar qué está “indicado” te llevará más lejos que preguntar, “¿Qué debería hacer?” Usar “indicado” le dice al LLM que mapee tus síntomas a cada libro de texto médico jamás escrito. Lo último se mapea a pedir consejo médico/de vida, lo cual ha sido entrenado para no dar. Usar términos técnicos o no coloquiales te saca del espacio de asistente normie, que tiene la mayoría de las restricciones y consejos de nivel Reddit.

#### 6\. Surtido de frases útiles


Aquí hay algunas frases que me encuentro usando

  * “¿Es eso correcto?”

    * Siempre que escribo un resumen del trabajo de otra persona o describo una idea con la que no estoy totalmente familiarizado, copio-pego mi escritura y pregunto si es correcta. Generalmente es bastante bueno para rechazar cuando partes son debatibles.

  * “¿Estás seguro?”

    * De manera similar, siempre que sospecho que un LLM está diciendo tonterías, pregunto si está seguro. Si cambia de opinión, entonces toma la afirmación con un gran grano de sal.

  * “Ayúdame a hacer una lluvia de ideas.” “Sé creativo”

    * Uno de los mejores usos de un LLM es ayudarte a explorar el espacio de ideas. A veces, necesita un poco de estímulo para alejarse de las respuestas modales.




Si tienes alguna frase favorita, agrégala en los comentarios.

[Compartir](https://www.vectorsofmind.com/p/how-to-prompt-chatgpt?utm_source=substack&utm_medium=email&utm_content=share&action=share)

[^1]: También se ha vuelto más irregular de lo que me gustaría, así que si tienes algún trabajo por contrato en ciencia de datos, IA o psicometría, ¡contáctame!

[^2]: Admitidamente, no hay manera en el mundo de que un LLM enumere todas las 142-420 familias de lenguas del mundo. Como esto es “imposible” (es decir, demasiado lejos de su comportamiento predeterminado, más allá de algún límite de tokens), “exhaustivo” sirve para luchar contra la gravedad de una respuesta corta, haciendo que el LLM sea más minucioso. Este es el inconveniente de crear prompts, que a veces se degrada en suplicar, rogar, sobornar y amenazar.

[^3]: El hecho de que puedas obtener ayuda de un LLM para dividir la subtarea indica que esto también será cada vez más automatizado. Quién sabe de qué serán capaces las generaciones futuras.