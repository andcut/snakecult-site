---
about:
- vetores-da-mente
- arquivo-do-blog
author: Andrew Cutler
date: '2025-07-04'
description: Certo, vamos dar uma pequena pausa nas questões de sapiência. Na verdade,
  eu tinha uma série de psicometria preparada antes de ser atraído pelo chamado claro
  da consciência. É tão difícil desviar o olhar...
draft: false
keywords:
- vetores-da-mente
- personalidade
- ao-redor
- mundo
lang: pt
lastmod: '2025-07-11'
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '108601152'
original_url: https://www.vectorsofmind.com/p/personality-around-the-world
quality: 6
slug: personality-around-the-world
tags: []
title: Personalidade Ao Redor do Mundo
translation_model: gpt-4o
---

*From [Vectors of Mind](https://www.vectorsofmind.com/p/personality-around-the-world) - imagens no original.*

---

Ok, vamos dar uma pequena pausa nas questões de sapiência. Eu na verdade tinha uma série de psicometria preparada antes de ser atraído pelo chamado da consciência. É simplesmente tão difícil desviar o olhar.

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!X2nA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F62106fb3-6e73-444d-96f1-07b95ec828f9_1024x506.jpeg)[Ulisses e as Sereias](https://en.wikipedia.org/wiki/Ulysses_and_the_Sirens_\(Waterhouse\)), pintura de [John William Waterhouse](https://en.wikipedia.org/wiki/John_William_Waterhouse)

Comecei este blog para explorar a Hipótese Lexical a partir de uma perspectiva de aprendizado de máquina. Modelos de personalidade definem os traços mais comentados em uma língua, e podemos medir isso muito melhor na era do GPT. Modelos de personalidade derivados de vetores de palavras ou de pesquisas tradicionais retornam aos mesmos poucos traços, especialmente os Dois Grandes: autorregulação social e dinamismo. Para uma revisão sobre isso, confira [Os Cinco Grandes são Vetores de Palavras](https://vectors.substack.com/p/the-big-five-are-word-vectors) e [O Fator Primário da Personalidade](https://vectors.substack.com/p/primary-factor-of-personality-part).

Os Cinco Grandes foram encontrados em muitas línguas de forma independente, mas a comparação entre línguas é sempre qualitativa. Pesquisadores aplicam uma pesquisa de adjetivos de personalidade em turco ou alemão, fatoram-na e meio que analisam os fatores para ver se são os mesmos. Esses dados não podem ser usados para dizer "A Extroversão está deslocada 15 graus em relação à Conscienciosidade em alemão comparado ao inglês." Para ser tão preciso, ambas as línguas teriam que compartilhar alguma base.

Se você aplicar perguntas em várias línguas, pode relacioná-las por 1) encontrar um grupo bilíngue que possa responder em ambas as línguas ou 2) assumir que as traduções das palavras são 1:1 (por exemplo, _fun_ é perfeitamente equivalente a _divertido_ em espanhol). No primeiro caso, há um forte efeito de seleção. E se pessoas bilíngues tendem a ser mais educadas? O último simplesmente não é verdade. Na verdade, o motivo para fatorar línguas juntas é entender como a estrutura de personalidade pode divergir entre elas. Assumir que as palavras são as mesmas derrota o propósito.

**[Minha pesquisa](https://arxiv.org/abs/2203.02092) mostrou que você pode extrair a estrutura de personalidade de modelos de linguagem em inglês. Uma questão natural é como isso muda quando você adiciona outras línguas.** Com modelos treinados em dezenas de línguas, isso se torna bastante fácil de explorar. Você pode mapear qualquer número de línguas para a mesma base.

## Os Dois Grandes, mais uma vez

Usei [XLM-RoBERTa](https://huggingface.co/xlm-roberta-base) para atribuir similaridade entre adjetivos de personalidade. Estranhamente, este modelo é um resultado do genocídio em Mianmar. A Meta está na posição ingrata de precisar remover conteúdo em lugares dos quais têm muito pouco entendimento. Tecnicamente, isso é o que se chama de problema de aprendizado por transferência. Eles gostariam de treinar um classificador de discurso de ódio em inglês (ou outra língua bem documentada) e então aplicá-lo a outras línguas. Nos tempos sombrios da modelagem de linguagem (2018), isso funcionava muito mal. A fala coloquial em birmanês para "vamos reunir os gays e matá-los" parecia para seus classificadores como "deveria haver menos arco-íris". Isso, é claro, passava pela moderação de conteúdo. O NYT explicou a consequência: _**[Um Genocídio Incitado no Facebook, Com Postagens do Exército de Mianmar](https://www.nytimes.com/2018/10/15/technology/myanmar-facebook-genocide.html)**_

A resposta da Meta foi construir um modelo de linguagem que pudesse mapear melhor qualquer língua (bem, 100 línguas) para vetores de palavras no mesmo espaço compartilhado. Dessa forma, um classificador de discurso de ódio treinado em inglês pode se estender melhor a outras línguas. (Menos birmanês é necessário para ajustá-lo.) Usando este modelo, incorporei palavras de personalidade em quatro línguas: inglês, espanhol, francês e turco. Abaixo estão os dois primeiros fatores:

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!eLVQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd3ff00d-d96d-4e3b-ada4-640e3cd66089_1245x954.png)

Estes servem para separar as diferentes línguas. O primeiro fator distingue o turco das línguas indo-europeias. No segundo fator, as línguas românicas são adjacentes (embora também próximas ao turco).

Isso faz sentido. O modelo é treinado para prever a próxima palavra de uma sentença, então naturalmente incluirá informações específicas da língua. Se alguém está falando em espanhol, não costuma mudar para turco. A esperança é que também existam direções no espaço vetorial que correspondam a informações de personalidade.

Se as línguas forem bastante independentes, você precisa de pelo menos 3 dimensões para separar 4 línguas em seus próprios grupos não sobrepostos. Vamos conferir os próximos componentes principais.

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!PRKA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5eb70bd2-8684-4844-94bd-aa12adc030bf_1256x954.png)

O Fator 4 é o primeiro fator que não foi aprendido para separar as línguas, e é o Fator Geral de Personalidade! Em inglês: _dominador, implacável, compulsivo_ e _egoísta_ **vs** _generoso, gentil_ e _atencioso_. [Eu argumentei](https://vectors.substack.com/p/primary-factor-of-personality-part) que este fator é melhor entendido como a tendência de viver a Regra de Ouro. A Teoria de Eva da Consciência foi na verdade um resultado de [imaginar o que isso selecionaria](https://vectors.substack.com/p/consequences-of-conscience) em nossa história evolutiva. O Fator 5 também é sobre personalidade, traçando-os juntos:

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!pD64!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F192dc8f4-db5e-4d96-b8a5-ce16c1cbf1f6_1264x954.png)

Temos os Dois Grandes! O Fator Cinco (ou dois, dos fatores de personalidade) é o Dinamismo: _aventureiro, imaginativo_ e _entusiástico_ **vs** _cauteloso, reservado_ e _covarde._ É incrível que isso surja tão regularmente. **Há [2.500 citações no artigo dos Dois Grandes](https://scholar.google.com/scholar?cites=11052969740325606797&as_sdt=2005&sciodt=0,5&hl=en), e ainda assim os pesquisadores não percebem que eles são simplesmente os dois primeiros fatores não rotacionados da personalidade geral.** A crença comum de que eles de alguma forma existem em uma relação hierárquica com os Cinco Grandes vem de pesquisadores abandonando o tratamento direto com a linguagem logo após fazerem os inventários dos Cinco Grandes. Desde então, qualquer tentativa de entender a personalidade básica ou geral deve ser feita em referência aos Cinco Grandes. Mas as palavras vieram primeiro, e os modelos de linguagem agora tornam fácil analisar a linguagem nesse nível fundamental.

[Compartilhar](https://www.vectorsofmind.com/p/personality-around-the-world?action=share)

## Precisamos ir mais fundo

Adicionar russo e farsi produz os mesmos fatores:

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!IIKx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F976f1c11-fd97-4184-a74a-a384a09b0579_2078x1715.png)Para ver melhor as palavras, baixe a imagem e amplie.

Pelos meus padrões de engenheiro preguiçoso, isso é bastante trabalhoso porque requer encontrar um bom prompt para cada língua. Trabalhei com o Google Translate e falantes nativos para acertar isso, e você pode ver que a distribuição do farsi ainda está errada no Fator 4. Meu palpite é que meu método de ignorar qualquer fator que não seja compartilhado é muito falho para tantas línguas. O Fator 4 provavelmente é usado como o GFP, e também para separar o farsi (apenas um pouco). Não há nada que mantenha esses fatores puros, somos realmente sortudos que a distribuição é tão bem comportada quanto é. Fazer algum pré-processamento (como zerar o significado de cada cluster de língua) pode resolver isso.

Até onde sei, esta é a primeira vez que várias línguas foram fatoradas juntas. Isso seria publicável com resultados apenas em inglês e espanhol, e aqui cheguei a seis, incluindo duas línguas não indo-europeias. Também lança luz sobre a natureza dos Dois Grandes, um dos construtos mais populares — e mal compreendidos — na psicometria.

## Deficiências

Fiz esta pesquisa da maneira mais tola possível. Encontrei 100 palavras de personalidade em um guia de ESL e depois traduzi essas palavras para outras línguas usando o Google Translate. Se houvesse duplicatas, eu as removia. Isso não é tão ruim quanto parece. Os dois primeiros fatores são virtualmente inalterados em inglês, quer você use 100 ou 500 palavras. Mas, se isso fosse um artigo real, você obviamente gostaria de desenvolver um conjunto de palavras em cada vocabulário de forma independente. Há várias outras deficiências:

**Não há línguas suficientes!** Se eu publicasse isso, gostaria de adicionar uma dúzia de outras línguas que não são tipicamente estudadas na ciência da personalidade. Isso é, de fato, o motivo pelo qual nunca cheguei a publicá-lo. É muito trabalho e exigiria falantes nativos de várias línguas asiáticas.

**Modelos multilíngues distorcidos pelos dados de treinamento.** Modelos de linguagem são treinados para prever a próxima palavra de uma sentença. Se você treina com várias línguas, o modelo tentará transferir parte do conhecimento. No entanto, para as línguas menores, isso pode parecer mais como seus significados sendo forçados a analogias dentro das línguas mais bem documentadas (inglês, chinês, russo, etc).

**As consultas são um grau de liberdade do pesquisador.** O método que uso para incorporar palavras é "Minha personalidade pode ser descrita como <máscara> e [palavra]" onde [palavra] é uma das palavras de personalidade. Por causa da forma como a sentença é escrita, o modelo carrega informações puras de personalidade no token de máscara e depois o incorpora. Em minha dissertação, descobri que isso funcionava melhor. Claro, há infinitas variações para isso, e você tem que selecionar uma. Teoricamente, um pesquisador poderia ter um resultado particular em mente e então encontrar uma consulta que apoie isso. Na minha opinião, não é muito arriscado, dado quão semelhante este resultado é ao que os métodos de pesquisa produzem. Temos um pré-conceito bastante forte sobre qual estrutura de personalidade encontramos com a análise fatorial. Este método recapitulando isso é evidência de que o método funciona.

**Modelo de linguagem desatualizado.** Fiz este trabalho há mais de 2 anos, muito antes do GPT-4 ser lançado. Tempos mais simples.

## Conclusão

Se eu ainda estivesse na academia, este seria meu plano de pesquisa. Adicionar o máximo de línguas possível e tentar entender todas as maneiras pelas quais o método pode ser tendencioso. No final, pode produzir um modelo universal de personalidade superior aos Cinco Grandes. Isso nos ajudaria a entender melhor quem somos e talvez até de onde viemos. Pois é a linguagem que define nossa espécie agora, e foi a linguagem que forjou nossa psique no passado distante. Somos habitualmente sociais porque milhares de anos atrás, falhar em gerenciar sua reputação era morrer. Modelos de personalidade são mapas da linguagem; são vetores na evolução de nossa mente.

[Inscreva-se agora](https://www.vectorsofmind.com/subscribe?)

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!MDwl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F935dcb92-8e91-41c3-9630-2a80f2bc9a06_1024x1024.png)