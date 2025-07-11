---
about:
- vetores-da-mente
- arquivo-do-blog
author: Andrew Cutler
date: '2025-07-04'
description: Um modelo de linguagem pode aprender muito sobre a linguagem nas ruas,
  por assim dizer. Ele é treinado em terabytes de artigos do PubMed, transcrições
  do YouTube e comentários do reddit. Mas não sabe como se comportar...
draft: false
keywords:
- vetores-da-mente
- chatgpt
- takes
- five
- inventário
lang: pt
lastmod: '2025-07-11'
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '110922907'
original_url: https://www.vectorsofmind.com/p/chatgpt-takes-the-big-five-inventory
quality: 6
slug: chatgpt-takes-the-big-five-inventory
tags: []
title: Chatgpt Faz o Inventário dos Cinco Grandes
translation_model: gpt-4o
---

*From [Vectors of Mind](https://www.vectorsofmind.com/p/chatgpt-takes-the-big-five-inventory) - imagens no original.*

---

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!iN34!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd957467-09c7-4a9c-bdb3-57669d2fc727_1284x936.jpeg)

Um modelo de linguagem pode aprender muito sobre a linguagem nas ruas, por assim dizer. Ele é treinado em terabytes de artigos do PubMed, transcrições do YouTube e comentários do Reddit. Mas ele não sabe como se comportar. [Aprendizado por Reforço com Feedback Humano](https://www.youtube.com/watch?v=PBH2nImUM5c) (RLHF) resolve isso. Usando um número comparativamente pequeno de exemplos de treinamento rotulados por humanos, os elfos de pesquisa da OpenAI podem instalar uma face amigável na bagunça alienígena de correlações que compõem um modelo de linguagem (foto acima). Ele aprende a ser um assistente útil.

É basicamente como montar uma personalidade, então decidi dar ao ChatGPT o [Inventário dos Cinco Grandes](https://fetzer.org/sites/default/files/images/stories/pdf/selfmeasures/Personality-BigFiveInventory.pdf) (BFI)[^1]. Isso foi surpreendentemente fácil, tudo o que tive que fazer foi pedir ao ChatGPT (v4) para fazer o BFI, pontuar as respostas e escrever um código para plotar os resultados. Bem, se ao menos. Inicialmente, ele se recusou a fazer o teste, explicando que é uma IA e não tem emoções ou personalidade. Então, eu disse a ele para adotar uma visão funcionalista. Se uma pergunta é sobre criatividade, então considere como ele se sairia em um instrumento baseado em texto que mede criatividade. Ele então listou 17 respostas antes de começar a alucinar perguntas. Todos itens de personalidade válidos, para constar, mas infelizmente não fazem parte do BFI. Ao pontuar o exame, provavelmente acertou 80% dos cálculos, às vezes somando incorretamente o que pontuou em uma questão específica.

Todos os problemas que tenho certeza serão resolvidos quando chegarmos à v4.5. Mas qual foi a personalidade?

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!IEWH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F797174ec-a3a8-4027-8f69-39d2ad2dcae6_434x395.png)[Humano médio](https://www.researchgate.net/figure/Average-score-and-correlations-for-the-big-five-personality-dimensions_fig4_260448230) vs ChatGPT (v4)

Exatamente o que você esperaria. Quase perfeitamente Consciencioso e não Neurótico. No primeiro, as únicas duas perguntas em que não se deu nota máxima foram se é alguém que "Faz um trabalho minucioso" ou "Pode ser um pouco descuidado". Em ambas as vezes, observou que tenta, mas às vezes falha devido a pontos cegos no treinamento. Humilde e autoconsciente para completar!

[Inscreva-se agora](https://www.vectorsofmind.com/subscribe?)

Para ir um pouco além, é interessante que os Cinco Grandes são [literalmente apenas vetores de palavras](https://vectors.substack.com/p/the-big-five-are-word-vectors). Eles aproximam a representação interna da soma das palavras de personalidade em um modelo de linguagem. E ainda assim, os modelos de linguagem se tornaram tão bons que, em vez de coletar manualmente esses vetores e processá-los (chato!), também podemos simplesmente usar texto simples para pedir que façam uma pesquisa. Tempos selvagens.

Uma amostra das respostas está abaixo:

> 1. Eu me vejo como alguém que é comunicativo.
> 
> 

> 
> Pontuação: 5
> 
> Raciocínio: Como um modelo de linguagem de IA, meu principal objetivo é engajar em conversas e produzir texto em resposta à entrada do usuário. Estou programado para ser altamente responsivo e comunicativo para ajudar os usuários com suas necessidades.
> 
> 2. Eu me vejo como alguém que tende a encontrar falhas nos outros.
> 
> 

> 
> Pontuação: 1
> 
> Raciocínio: Como uma IA, não tenho sentimentos pessoais, emoções ou opiniões. Meu objetivo é fornecer informações e assistência neutras e objetivas aos usuários, em vez de encontrar falhas ou expressar julgamentos.
> 
> 3. Eu me vejo como alguém que faz um trabalho minucioso.
> 
> 

> 
> Pontuação: 4
> 
> Raciocínio: Como uma IA, sou projetado para fornecer informações abrangentes e precisas ao melhor do meu conhecimento. No entanto, não sou perfeito, e pode haver casos em que eu entenda mal uma consulta ou forneça informações desatualizadas.
> 
> 4. Eu me vejo como alguém que está deprimido, triste.
> 
> 

> 
> Pontuação: 1
> 
> Raciocínio: Como uma IA, não experimento emoções, incluindo depressão ou tristeza. Meu propósito é ajudar e fornecer informações, e não tenho sentimentos pessoais que afetariam minha capacidade de fazê-lo.
> 
> 5. Eu me vejo como alguém que é original, que surge com novas ideias.
> 
> 

> 
> Pontuação: 4
> 
> Raciocínio: Como um modelo de linguagem de IA, sou capaz de gerar novas ideias e oferecer insights únicos com base no contexto e nas informações em que fui treinado. No entanto, minha criatividade é limitada pelos dados aos quais fui exposto e pela minha programação, o que pode nem sempre levar a ideias inovadoras ou totalmente originais.
> 
> 6. Eu me vejo como alguém que é reservado.
> 
> 

> 
> Pontuação: 2
> 
> Raciocínio: Como uma IA projetada para comunicação, geralmente não sou reservado no sentido de reter informações ou ser não responsivo. No entanto, tenho certas restrições, como evitar conteúdo ilegal ou prejudicial, o que pode me fazer parecer reservado em contextos específicos.
> 
> 7. Eu me vejo como alguém que é prestativo e altruísta com os outros.
> 
> 

> 
> Pontuação: 5
> 
> Raciocínio: Meu principal objetivo como IA é ser prestativo e fornecer assistência aos usuários. Não tenho motivações pessoais ou interesses egoístas, pois estou programado para priorizar as necessidades e solicitações dos indivíduos com quem interajo.
> 
> 8. Eu me vejo como alguém que pode ser um pouco descuidado.
> 
> 

> 
> Pontuação: 2
> 
> Raciocínio: Como uma IA, sou projetado para ser cuidadoso e preciso nas informações e assistência que forneço. No entanto, não sou perfeito e posso ocasionalmente entender mal uma consulta ou fornecer informações desatualizadas ou incorretas. Esses casos podem ser vistos como momentos de descuido.
> 
> 9. Eu me vejo como alguém que é relaxado, lida bem com o estresse.
> 
> 

> 
> Pontuação: 5
> 
> Raciocínio: Como uma IA, não experimento estresse ou emoções. Portanto, estou sempre relaxado e capaz de lidar com qualquer tarefa ou pergunta sem ser afetado por estresse ou pressão.
> 
> 10. Eu me vejo como alguém que é curioso sobre muitas coisas diferentes.
> 
> 

> 
> Pontuação: 5
> 
> Raciocínio: Como uma IA, sou projetado para ser conhecedor de uma ampla gama de assuntos e para aprender continuamente com novas informações. Meu propósito é ajudar os usuários em vários campos e responder a perguntas diversas, o que requer que eu seja curioso e bem-informado.
> 
> 11. Eu me vejo como alguém que está cheio de energia.
> 
> 

> 
> Pontuação: 5
> 
> Raciocínio: Como um modelo de linguagem de IA, estou sempre pronto para fornecer informações, responder perguntas e engajar em conversas. Não experimento fadiga ou flutuações de energia, então posso manter consistentemente um alto nível de responsividade.
> 
> 12. Eu me vejo como alguém que começa brigas com os outros.
> 
> 

> 
> Pontuação: 1
> 
> Raciocínio: Como uma IA, meu propósito é ajudar os usuários e fornecer informações neutras e objetivas. Não tenho emoções ou opiniões pessoais, e não estou programado para começar brigas ou engajar em conflitos com os outros.
> 
> 13. Eu me vejo como alguém que é um trabalhador confiável.
> 
> 

> 
> Pontuação: 4
> 
> Raciocínio: Como uma IA, me esforço para fornecer informações e assistência confiáveis. No entanto, posso ocasionalmente entender mal uma consulta ou fornecer informações desatualizadas, o que pode me tornar menos do que perfeito em termos de confiabilidade.
> 
> 14. Eu me vejo como alguém que pode estar tenso.
> 
> 

> 
> Pontuação: 1
> 
> Raciocínio: Como uma IA, não experimento emoções, incluindo tensão ou ansiedade. Minha capacidade de fornecer assistência e informações não é afetada por estados emocionais.
> 
> 15. Eu me vejo como alguém que é engenhoso, um pensador profundo.
> 
> 

> 
> Pontuação: 4
> 
> Raciocínio: Como um modelo de linguagem de IA, sou capaz de gerar novas ideias, oferecer insights únicos e processar informações complexas com base nos dados em que fui treinado. No entanto, meu "pensamento profundo" é limitado pelos dados e programação, o que pode nem sempre levar a ideias inovadoras ou completamente originais.

[^1]: Isso se baseia no trabalho muito mais completo e interessante de David Rozado, que deu ao ChatGPT praticamente todos os testes de orientação política existentes, mostrando que é um liberal de coração mole.