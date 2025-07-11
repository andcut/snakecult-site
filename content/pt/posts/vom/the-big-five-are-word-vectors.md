---
about:
- vetores-da-mente
- arquivo-do-blog
author: Andrew Cutler
date: '2025-07-04'
description: Estudos lexicais em psicologia e Análise Semântica Latente em ciência
  da computação foram introduzidos com meio século de diferença para resolver problemas
  distintos e, no entanto, são matematicamente equivalentes. Isto não é um meta...
draft: false
keywords:
- vetores-da-mente
- cinco
- palavra
- vetores
lang: pt
lastmod: '2025-07-11'
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '50351822'
original_url: https://www.vectorsofmind.com/p/the-big-five-are-word-vectors
quality: 6
slug: the-big-five-are-word-vectors
tags: []
title: '# Os Cinco Grandes São Vetores de Palavras'
translation_model: gpt-4o
---

*From [Vectors of Mind](https://www.vectorsofmind.com/p/the-big-five-are-word-vectors) - imagens no original.*

---

Estudos lexicais em psicologia e Análise Semântica Latente em ciência da computação foram introduzidos com meio século de diferença para resolver problemas distintos e, no entanto, são matematicamente equivalentes. Isso não é uma metáfora que funciona em um certo nível de abstração _;_ os Cinco Grandes são dimensões de [vetores de palavras](https://dzone.com/articles/introduction-to-word-vectors).

Mas primeiro, um pouco de contexto. A Hipótese Lexical afirma que a estrutura da personalidade será escrita na linguagem, pois os falantes precisam descrever os atributos mais salientes daqueles ao seu redor. A beleza dessa ideia é que, em vez de uma única pessoa sugerir um modelo de personalidade, a linguagem registra o que milhões de pessoas implicitamente concordam ser útil. O trabalho do psicometrista é simplesmente identificar essa estrutura. Isso geralmente é realizado convidando estudantes de psicologia a se autoavaliarem em listas de adjetivos e realizando análise fatorial na matriz de correlação. Em 1933, LL Thurstone administrou uma pesquisa com 60 adjetivos para 1300 pessoas. Em seu seminal [The Vectors of Mind](http://psych.colorado.edu/~carey/Courses/PSYC5112/Readings/VectorsOfMind_Thurstone.pdf), ele relata que "cinco fatores são suficientes" para explicar os dados. Nas décadas subsequentes, tais estudos, mais ou menos, resultaram em cinco componentes principais: Amabilidade, Extroversão, Conscienciosidade, Neuroticismo e Abertura/Intelecto. (Para um excelente tratamento do assunto, veja [Lexical Foundations of the Big Five](https://www.researchgate.net/profile/Boele-Raad-2/publication/282980275_The_Lexical_Foundation_of_the_Big_Five-Factor_Model/links/5626198508aed3d3f137e522/The-Lexical-Foundation-of-the-Big-Five-Factor-Model.pdf).)

A Análise Semântica Latente foi [introduzida](https://dl.acm.org/doi/abs/10.1145/57167.57214?casa_token=ogUyQ6VJeZgAAAAA:ksULYwu-Km_5Ap0wA2ho3tbwzTjsB0tHONfEEMIldNB6PJgkRyM7eFaa7uZ-XZJ3nYo0MbYFeJsBng) como uma técnica de recuperação de informação em 1988. Palavras podem ser representadas como vetores e documentos ou frases podem ser representados como a média de seus vetores de palavras. Se você quiser pesquisar em um grande banco de dados (por exemplo, Wikipedia), palavras-chave para cada página só te levarão até certo ponto. Uma maneira de contornar isso é representar tanto documentos (artigos wiki) quanto consultas (termos de busca) como a média de seus vetores de palavras. Encontrar documentos relevantes agora pode ser realizado com um simples produto escalar. (Neste post, trato LSA e vetores de palavras como sinônimos. Existem outras maneiras de vetorializar a linguagem e, mais especificamente, criar vetores de palavras, mas essas estão além do escopo por agora.)

Apesar de seus diferentes usos e histórias, os passos são os mesmos:

 1. Coletar uma matriz de contagem palavra x documento

 2. Transformação não linear

 3. Decomposição da matriz

 4. Rotação (Opcional)




O resultado é um conjunto de vetores de palavras que descrevem sucintamente cada palavra. Estes podem ser usados para uma série de tarefas subsequentes, desde análise de sentimento até previsão de narcisismo a partir de redações de estudantes. No caso de adjetivos de personalidade, as dimensões dos vetores de palavras foram analisadas, nomeadas e debatidas por décadas. O que se segue é uma discussão das diferenças em cada etapa.

**Matriz de contagem.** LSA geralmente envolve um grande número de documentos variados (por exemplo, milhões de avaliações de produtos da Amazon). Estes são transformados em matriz palavra x documento contando quantas vezes cada palavra aparece em cada documento. Em psicologia, um documento são as palavras que um sujeito concorda que o descrevem. Isso se estende a escalas de Likert também. Se alguém diz que uma palavra o descreve 5/7, então simplesmente repita a palavra cinco vezes no documento.

**Transformação não linear.** Estudos lexicais frequentemente ipsatizam os dados (pontuação z ao longo do eixo do sujeito) e então realizam uma correlação de Pearson. Thurstone usou uma correlação tetrárquica arcaica em seu estudo. Em LSA, a transformação mais comum é TF-IDF, seguida por um logaritmo. Isso garante que a matriz não seja dominada por termos comuns. Frequentemente, a transformação resulta em uma matriz de afinidade palavra x palavra (por exemplo, matriz de correlação). Esta etapa é praticamente muito importante, mas não tão teórica. A transformação a escolher é aquela que te dá um resultado razoável no final.

**Decomposição da Matriz.** Existem muitos métodos de decomposição de matriz. Alguns, como PCA, requerem uma matriz quadrada. Outros são robustos a dados ausentes. Com dados de personalidade, a escolha não importa muito; os resultados são muito semelhantes. Vetores de palavras gerais requerem ~300 dimensões para representar o significado de uma palavra, parte do discurso, gírias e muito mais que dá textura à linguagem. Como as pesquisas são projetadas para manter muito disso constante, apenas ~5 dimensões são necessárias. Thurstone justificou sua escolha de cinco olhando para o erro de reconstrução que ele relata como um histograma. Psicólogos posteriores justificaram 5 pelo erro de reconstrução (medido com autovalores), bem como considerando a interpretabilidade e reprodutibilidade.

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!Zw-J!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd562c1c2-1576-4fad-896c-52e799d4598b_1600x1066.png)Erro de reconstrução da matriz de correlação de palavras. Não obstante as restrições computacionais, sua amostra é uma ordem de magnitude maior do que muitos estudos modernos.

**Rotação.** Você já ouviu falar de superextração de componentes? Não é uma história que os psicólogos te contariam. É quando um pesquisador extrai muitos Componentes Principais e então rotaciona a variância dos PCs anteriores, válidos, para os PCs marginais posteriores. Isso é o que aconteceu com os Cinco Grandes, acredite ou não! O que agora é Amabilidade já foi um fator de 'Socialização' muito mais robusto e teoricamente satisfatório, que foi espalhado pelos PCs 3-5 para formar Conscienciosidade, Neuroticismo e Abertura. A rotação _pode_ ser justificada para produzir fatores interpretáveis. Mas se você se encontrar rotacionando e então discutindo sobre o número correto de fatores, verifique-se!

**Os Três Grandes a partir de vetores de palavras**

Comecei meu doutorado prevendo traços dos Cinco Grandes a partir de status do Facebook. Depois de ler como a "salsicha" da personalidade era feita, percebi que o projeto usava vetores de palavras (de status do Facebook) para prever aproximações ruidosas de onde os indivíduos viviam no espaço dos Cinco Grandes, que foi originalmente definido por vetores de palavras. Parecia mais interessante ir direto ao ponto e aprender algo fundamental sobre personalidade a partir de vetores de palavras. (Além disso, o conjunto de dados que eu estava usando se tornou tóxico após o Cambridge Analytica.) O restante do meu doutorado foi trabalhar para restringir vetores de palavras a fim de reproduzir os Cinco Grandes. Isso envolveu o uso de transformadores em vez de LSA (mais sobre isso em posts futuros). A correlação resultante entre fatores de vetores de palavras (DeBERTa) versus pesquisas está abaixo. Como você pode ver, há uma concordância muito próxima para os três primeiros fatores. Onde os resultados divergem, não está claro qual método está em erro. Talvez as pesquisas estejam certas, e todas as correlações irão para 1 quando chegarmos ao GPT-5. Talvez as pesquisas sejam apenas tendenciosas e ruidosas, e muitos PCs foram extraídos. Talvez estejam medindo coisas diferentes, e precisamos refinar nossa interpretação de ambos. De qualquer forma, não é óbvio para mim que as pesquisas devam ser consideradas o padrão-ouro entre os dois. A Hipótese Lexical é sobre a estrutura da linguagem, afinal, e a psicologia é o único campo que usa pesquisas para analisar a linguagem natural.

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!lY1-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6bf087b4-76cc-4272-a2f7-037d606ed2ba_726x682.png)Os PCs de pesquisa não rotacionados são de um dos [estudos](https://onlinelibrary.wiley.com/doi/10.1002/\(SICI\)1099-0984\(199603\)10:1%3C61::AID-PER246%3E3.0.CO;2-D) que definiram os Cinco Grandes. Os PCs DeBERTa são extraídos de vetores de palavras. Leia sobre esse processo [aqui](https://psyarxiv.com/gdm5v/).

**Conclusão**

Thurstone foi pioneiro em métodos de estatística e álgebra linear para investigar a Hipótese Lexical nos anos 30. É notável que ele desenvolveu uma maneira de representar palavras que foi posteriormente redescoberta para recuperação de informação, que agora alimenta a era da informação. A computação forçou Thurstone a achatar o rico panorama da linguagem para respostas de pesquisa. Nos últimos 30 anos, o PLN experimentou múltiplas revoluções. Se Thurstone inventou um telescópio com o qual visualizar a estrutura da linguagem, agora temos o Hubble. Muitos insights aguardam!