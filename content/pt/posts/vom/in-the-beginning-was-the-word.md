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
lang: pt
lastmod: '2025-07-11'
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '51210419'
original_url: https://www.vectorsofmind.com/p/in-the-beginning-was-the-word
quality: 6
slug: in-the-beginning-was-the-word
tags: []
title: No princípio era o Verbo
translation_model: gpt-4o
---

*From [Vectors of Mind](https://www.vectorsofmind.com/p/in-the-beginning-was-the-word) - imagens no original.*

---

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!5qwE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9f7c2505-9587-4daa-aac2-648b8bf16efb_1200x544.png)

_"No princípio era a Palavra, e a Palavra estava com a Psicologia, e a Palavra era Psicologia" ~Nova Tradução Vetorial_

Todos os construtos de personalidade são primeiramente descritos por palavras. Dos modelos alimentados por cocaína de Freud ao sóbrio Big Five, todos são em algum momento palavras. Grande parte da psicologia acadêmica se preocupa em comparar construtos. Para isso, eles devem compartilhar uma base, tipicamente um conjunto de sujeitos. Os sujeitos recebem um instrumento (geralmente um questionário) que aproxima onde eles vivem no espaço dos construtos. Com base em como as respostas dos sujeitos covariam, são feitas afirmações gerais sobre os construtos. Neste post, exploramos outra maneira. Avanços em PLN permitem a comparação quantitativa de construtos em seu habitat natural: a linguagem.

### Roteiro

No [último post](https://vectors.substack.com/p/the-big-five-are-word-vectors?s=w) argumentei que o Big Five são vetores de palavras. Este post faz a mesma afirmação sobre escalas independentes, o que então permite que os construtos sejam comparados sem envolver sujeitos. Para demonstrar isso, um modelo amplo de personalidade é introduzido, bem como um método para representar construtos no espaço das palavras. O esboço segue:

 1. Comparar construtos no espaço de sujeitos vs espaço de palavras

 2. Problemas com o espaço de sujeitos

 3. Relacionar altruísmo de parentesco e altruísmo recíproco ao Big Five usando sujeitos

 4. A mesma comparação no espaço de palavras

 1. Introduzir um modelo de cinco fatores (temporário) identificado usando PLN

 2. Projetar palavras de altruísmo nesse espaço

 3. Código disponível [aqui](https://colab.research.google.com/drive/13DA2IKQ9zRimGedww_09iGT6ehuYriVz?usp=sharing).

 5. Discussão, limitações, trabalhos futuros

### **Um caminho tortuoso**

Para comparar altruísmo com o Big Five, o sinal deve passar por muitas transformações: Altruísmo (ideal) → descrito por palavras → questionário desenvolvido (e, esperançosamente, validado) para aproximar esse construto → administrado ao sujeito que interpreta essas palavras e busca em sua alma → pontuação de altruísmo do sujeito → **correlação no espaço de sujeitos** ← pontuação do Inventário Big Five (BFI) do sujeito ← sujeito interpreta os itens do BFI e busca em sua alma ← desenvolver BFI para medir aproximadamente isso ← construto definido/comunicado por descrição qualitativa ← Big Five (definido por cargas de palavras). Então, são feitas afirmações sobre os dois ideais, Altruísmo e o Big Five.

### **O caminho reto e estreito**

Por que não usar vetores de palavras como a base compartilhada em vez de sujeitos? O caminho é muito mais direto: Altruísmo (ideal) → descrito por palavras → vetorizado para o espaço de palavras → **comparação no espaço de palavras** ← Big Five, que já existem no espaço de palavras, como discutido no [post anterior](https://vectors.substack.com/p/the-big-five-are-word-vectors?s=w). Para aqueles que estão acompanhando, são 4 vs 10 transformações. (É pontuado como golfe.)

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!tbb9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb8b6c50-e94e-4462-8772-78359189f70e_1600x1305.png)Realidades estatísticas visitando o campo da psicologia. Tem sido alguns anos difíceis.

### **Tal, o Revelador**

A dificuldade de usar sujeitos para fazer afirmações sobre construtos verbais não é segredo.

> _"A maioria das teorias e hipóteses em psicologia são de natureza verbal, mas sua avaliação depende esmagadoramente de procedimentos estatísticos inferenciais. A validade da transição da análise qualitativa para quantitativa depende de as expressões verbais e estatísticas de uma hipótese estarem intimamente alinhadas – isto é, que as duas devem se referir a aproximadamente o mesmo conjunto de observações hipotéticas. Aqui, argumento que muitas aplicações de inferência estatística em psicologia não atendem a essa condição básica." ~Tal Yarkoni,_ A [crise de generalização](https://psyarxiv.com/jqw35/)

Validade aqui refere-se a uma pontuação capturando o construto que se pretende medir. Vale a pena ler os argumentos e exemplos na íntegra. Mas para nós, a lição é o que pode ser feito, dadas essas realidades. Ele sugere:

 1. Fazer outra coisa (entrar em outros campos).

 2. Abraçar a pesquisa qualitativa

 3. Adotar melhores padrões (incluindo 7 sugestões).

> _"Sempre se pode fingir que pequenos valores de p obtidos de operacionalizações estatísticas extremamente estreitas podem fornecer uma base adequada para inferências verbais abrangentes sobre construtos psicológicos complexos. Mas ninguém mais—nem seus pares, nem seus financiadores, nem o público, e certamente não o registro científico de longo prazo—é obrigado a honrar a farsa."_

Mesmo que sua visão da pesquisa em psicologia não seja tão sombria, certamente os leitores já foram enganados por artigos que fazem afirmações, mas empregam experimentos que estão apenas tenuemente relacionados. Todas as soluções disponíveis são dolorosas. O campo pode ter que adotar uma visão mais restrita e deixar as grandes questões para aqueles que estudam história, literatura e álgebra linear. Proponho outro caminho a seguir.

### **Converter para o espaço de palavras**. 4. Usar vetores de palavras como base compartilhada

Os construtos vivem juntos no espaço de palavras, e ainda assim, quando comparações são feitas, os arrastamos para o espaço de sujeitos. Isso é um enorme, dispendioso, incômodo. E se eles pudessem permanecer com segurança no espaço de palavras? O conceito de processamento de linguagem natural é que as palavras são vetores em um espaço contínuo. Analisar esses vetores funciona bem o suficiente para ser um [processo](https://youtu.be/SGzMElJ11Cc?t=6667) [de sustentação](https://www.amazon.jobs/en/search?base_query=natural+language+processing&loc_query=&latitude=&longitude=&loc_group_id=&invalid_location=false&country=&city=&region=&county=) [de carga](https://blog.google/products/search/search-language-understanding-bert/) em indústrias de trilhões de dólares, e está atualmente sendo ([re](https://vectors.substack.com/p/the-big-five-are-word-vectors?s=w))introduzido à psicologia.

### **Pratique o que prega**

Aqui, vamos olhar para um estudo tradicional feito no espaço de sujeitos e tentar melhorá-lo movendo-o para o espaço de palavras. Para evitar um espantalho, o objeto é [Altruísmo de Parentesco, Altruísmo Recíproco e os Fatores de Personalidade do Big Five](https://www.sciencedirect.com/science/article/abs/pii/S1090513898000099?casa_token=05bTreOjGKUAAAAA:nLHTWhK3z45xUbN5nTVd7a3-Qaz9No22rQtVY6vpUjYpeZ1bkPy-cBig9UgRbn-GnqJScTCPpSY), que foi citado centenas de vezes e cujo primeiro autor tem um índice h de 70.

Os sujeitos são medidos usando três instrumentos: Big Five (via um questionário de adjetivos), Empatia/Apego e Perdão/Não-Retaliação (questionário de frases) e altruísmo em um jogo de divisão de dinheiro. Como os autores hipotetizam que o espaço intersticial entre Amabilidade e Estabilidade Emocional (também conhecido como Neuroticismo) diferencia os dois altruísmos, algumas palavras são adicionadas para medir melhor essa área. Da mesma forma, um novo questionário é projetado para medir Empatia/Apego e Perdão/Não-Retaliação, que são teorizados como relacionados ao altruísmo de parentesco vs recíproco. Além do esperado para este tipo de estudo, um jogo é usado para medir altruísmo.

> _"Na versão da tarefa de alocação de dinheiro usada para medir altruísmo de parentesco, a outra pessoa foi descrita como um amigo próximo—alguém com quem o participante tinha uma longa história de amizade e com quem o participante tinha muito em comum. Esperávamos que, ao descrever a amizade como antiga e o amigo como alguém muito semelhante ao participante, a amizade se assemelhasse muito à relação que se tem com um parente. A razão pela qual não usamos um parente como o potencial objeto de altruísmo foi para evitar introduzir variância nas respostas devido ao parente específico envolvido; por exemplo, muitas pessoas podem estar mais dispostas a se comportar altruisticamente em relação a um irmão do que a outro."_

Em outras palavras, para não manchar os dados com sentimentos do mundo real em relação aos parentes, o altruísmo recíproco é medido.

> _"Na versão da tarefa de alocação de dinheiro usada para medir altruísmo recíproco, a outra pessoa foi descrita como um não-cooperador—alguém que foi rude, desagradável e inconsiderado com o participante."_

E para medir altruísmo recíproco, eles medem... altruísmo não-reciproco? Naturalmente, há correlações e os autores concluem:

> _"Os resultados deste estudo apoiam a sugestão de que traços de personalidade envolvendo empatia e apego facilitam o altruísmo que é principalmente direcionado a parentes (ou seja, altruísmo de parentesco), e que traços de personalidade envolvendo perdão e não-retaliação facilitam o altruísmo que é principalmente direcionado a não-parentes (ou seja, altruísmo recíproco)."_

Mas se o altruísmo recíproco nunca foi medido, como os resultados podem apoiar essa afirmação? Estatísticas em artigos de psicologia são, como Tal aponta, muitas vezes um floreio retórico. Mas não precisamos jogar junto! Vamos ver o que o espaço de palavras tem a dizer.

### **Uma terra de leite e mel (bem-vindo ao espaço de palavras)**

Em estudos tradicionais, devido aos custos de mapear sujeitos no espaço de personalidade, a resolução só pode ser alta em algumas áreas de personalidade por vez. É por isso que os autores sondaram Empatia e Não-Retaliação e o espaço entre Amabilidade e Estabilidade Emocional. Todos esses eixos [existem no espaço regular do Big Five](https://psyarxiv.com/vebtm/), mas são medidos de forma bastante granular. No espaço de palavras, podemos comparar altruísmo com o Big Five completo em toda a sua glória de alta resolução. No meu github, há 2819 vetores de palavras fatorados em cinco PCs. Podemos usá-los para conveniência. A primeira ordem de negócios é selecionar conjuntos de palavras que descrevam cada altruísmo. Para palavras de parentesco, escolhi aquelas que incorporam papéis familiares: _fraternal, sororal, maternal, materno, paterno, avó, avô, conjugal, maternal, paternal._ Para altruísmo recíproco, sigo a definição de Trivers.

> _"Em relação ao altruísmo recíproco humano, é mostrado que os detalhes do sistema psicológico que regula esse altruísmo podem ser explicados pelo modelo. Especificamente, **amizade, antipatia, agressão moralista, gratidão, simpatia, confiança, suspeita, confiabilidade, aspectos de culpa e algumas formas de desonestidade e hipocrisia** podem ser explicados como adaptações importantes para regular o sistema altruísta. Cada ser humano é visto como possuindo **tendências altruístas e de trapaça**, cuja expressão é sensível a variáveis de desenvolvimento que foram selecionadas para definir as tendências em um equilíbrio apropriado ao ambiente social e ecológico local." _[A Evolução do Altruísmo Recíproco](https://www.journals.uchicago.edu/doi/abs/10.1086/406755), Robert Trivers (negrito adicionado)

Considerando isso, escolhi: _discriminador, implacável, vingativo, leal, amigável, cooperativo, confiável,_ e _justo._ Isso é mais ou menos igual a errar para a cooperação, mas seguir com agressão moralista quando as coisas dão errado. Além disso, tenta capturar esse altruísmo como a antítese da trapaça (por exemplo, _justo_, _confiável_).

(Para uma excelente explicação da evolução da confiança, veja [esta](https://ncase.me/trust/) demonstração interativa.)

#### Posso apresentar a você o desconhecido Modelo de Cinco Fatores?

Teoricamente, poderíamos usar cargas de palavras do Big Five produzidas via questionários, mas a maioria dessas palavras são raras o suficiente para não serem incluídas. Isso é para o melhor, pois não se obteria uma boa estimativa de _avó_ por auto-relato entre estudantes de psicologia. Como tal, vetores de palavras são computados usando o modelo de linguagem RoBERTa. Derivado de uma lista grande e [bem caracterizada](https://openpsychologydata.metajnl.com/articles/10.5334/jopd.57/) de palavras de personalidade, os cinco fatores resultantes são, em resumo:

 1. Afiliação (ou Socialização). Quanto você quer essa pessoa em sua equipe? Semelhante à Amabilidade, mas exclui ser um capacho. _Ingênuo_, por exemplo, carrega de forma neutra na Afiliação, mas positivamente na Amabilidade.

 2. Dinamismo. Muito próximo do Extroversão, mas mais sobre um senso de aventura e menos sobre confiança.

 3. Ordem. Conscienciosidade com um toque. Capacidade de alcançar seus próprios objetivos. _Exigente_ vs _indeciso_.

 4. Apego Emocional. Enquanto o Neuroticismo está preocupado com a instabilidade, isso é sobre apego; tanto _carinhoso_ quanto _rancoroso_ são altamente carregados.

 5. Transcendência. Este fator é caracterizado por _único, complicado, fadado, prejudicado, místico, de coração partido, de outro mundo_ vs. _não filosófico, despreocupado, teimoso, rude, materialista, egocêntrico, superficial_. Envolve olhar além de si mesmo e do mundano. Esse processo está, aparentemente, envolvido em dor. Na verdade, "perturbado" carrega mais em Transcendência do que Apego Emocional (o fator relacionado ao Neuroticismo).

Os nomes para os três primeiros fatores são emprestados do trabalho [pan cultural](https://journals.sagepub.com/doi/10.1002/per.1953) de De Raad porque, qualitativamente, a correspondência é mais próxima do que com o Big Five. Cada fator merece seu próprio post. (Para aqueles na psicologia industrial, suspeito que Ordem está mais correlacionada com sucesso nos negócios do que Conscienciosidade, pois é mais calculista do que apenas chegar na hora certa.) Mas propor modelos não é meu forte, e estudos de linguagem mais refinados estão por vir, o que pode gerar uma estrutura diferente. Por enquanto, esses fatores são suficientes. Aqui está sua correlação com o Big Five:

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!Sxlw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F63c86f00-e0cc-4854-bd8a-e6ba3fc55449_366x374.png)

#### Resultados

Cargas de palavras de altruísmo nos primeiros quatro fatores (Transcendência não é importante neste estudo):

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!Q5sr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4efdfb85-197d-4d57-8a8b-3675eaf2b162_955x735.png)É pró-social ter laços familiares fortes (alta Afiliação), se um pouco entediante (neutro a baixo Dinamismo). Todas as palavras mapeiam para um lugar semelhante.

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!f7oe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb08b529e-7443-4f5b-af1e-ce080e36a4b7_961x735.png)Palavras familiares carregam fortemente no apego emocional. Observe que as relações de pais e avós são bastante marcadas por gênero. Os homens são menos apegados, como a teoria de [investimento parental](http://joelvelasco.net/teaching/3330/trivers72-parentalinvestment.pdf) de Trivers prevê, e as [estatísticas](https://www.pewresearch.org/social-trends/2013/07/02/the-rise-of-single-fathers/) confirmam. Irmãos e irmãs, no entanto, são igualmente apegados, e em menor grau do que os pais. Pensando bem, _conjugal_ não deveria ter sido incluído no altruísmo sobre parentes de sangue. Em concordância com [programas de televisão diurnos](https://www.youtube.com/watch?v=jXZB0FeTyE8), carrega menos no apego do que materno ou avó.

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!FYnd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa40e5562-577f-4b55-bd16-d34ccec1c388_955x735.png)Palavras recíprocas tentam capturar o comportamento ideal de tit for tat quando um parceiro está cooperando ou trapaceando. Como tal, essas palavras estão muito mais espalhadas, embora ainda principalmente positivas. Mesmo 'discriminador' é ligeiramente positivo, o que significa que não acho que a palavra esteja sendo codificada como algo como 'discriminador racial'—às vezes esses modelos de linguagem se confundem com similaridade fonética (por exemplo, excêntrico e etnocêntrico).

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!lGox!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6eb4b7d2-4728-4f66-83ce-cd95e2346144_961x735.png)Cooperação e vizinhança implicam ligeiramente que os próprios objetivos estão ficando em segundo plano. Implacáveis e discriminadores são para aqueles que querem dizer negócios.

Para comparar os altruísmos, gostaríamos de reduzir cada um desses conjuntos de palavras a apenas um vetor. (Há espaço para debate se isso faz sentido, dado que o recíproco—e em menor medida o parentesco—requer respostas diferentes para diferentes cenários.) A solução barata e suja é tratar cada construto como um [Saco de Palavras](https://en.wikipedia.org/wiki/Bag-of-words_model) e tirar a média. As médias das cargas são:

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!TMN7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe3aaf685-9bb3-4dbf-974f-0ab994f40a88_356x238.png)Estas são pontuadas em z contra todas as 2819 palavras. Em média, palavras de parentesco estão de 1 a 1,5 DP em Afiliação e Apego Emocional.

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!mDHG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fba83d4f1-2f47-42e8-a158-368c7681a2db_356x238.png)O altruísmo recíproco também envolve Ordem, alcançando seus próprios objetivos.

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!48eW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd912d107-48f4-4d5e-bb23-fe24dd932b78_356x238.png)Diferença: Cargas de Parentesco menos Recíproco. Dominado por Ordem.

### **Discussão**

Não acho que o artigo no espaço de sujeitos inclua uma medida válida de altruísmo de parentesco ou recíproco e, como tal, não adiciona ao nosso entendimento de como ele se relaciona com a personalidade. Este é um modo de falha surpreendentemente comum. O espaço de palavras fornece alguma proteção contra comparações inválidas. Temos uma melhor intuição de onde uma palavra deve estar no espaço de palavras do que de como o sujeito 112 deve responder a um questionário. É mais fácil identificar erros.

Do ponto de vista bayesiano, algo diferente está acontecendo no espaço de sujeitos vs espaço de palavras. Experimentos que incluem sujeitos buscam trazer novas informações à mesa. A esperança é que isso atualize a visão dos leitores sobre o mundo. Mas os pesquisadores (e leigos) têm muita experiência social e uma percepção mais aguçada dos processos psicológicos do que o instantâneo fornecido por um questionário. É difícil mover muito o ponteiro. O espaço de palavras é mais parecido com visualizar nossos priors do que produzir novo conhecimento. Essa visão é valiosa porque a linguagem é onde a borracha encontra a estrada, por assim dizer. Como JL Austin colocou:

> _"Nosso estoque comum de palavras incorpora todas as distinções que os homens acharam que valia a pena desenhar, e as conexões que acharam que valia a pena marcar, na vida de muitas gerações: Estas certamente são mais numerosas, mais sólidas, já que resistiram ao longo teste de sobrevivência do mais apto, e mais sutis, pelo menos em todas as questões práticas ordinárias e razoáveis, do que qualquer que você ou eu provavelmente pensaríamos em nossa poltrona de uma tarde—a alternativa mais favorita." [Um apelo por desculpas](https://sites.ualberta.ca/~francisp/NewPhil448/AustinPlea56.pdf)_

A análise no espaço de palavras é comparativamente direta. Em vez de tabelas de correlações e valores de p, as palavras são simplesmente plotadas nos eixos de interesse e julgamentos visuais são feitos. Palavras de altruísmo de parentesco se agrupam fortemente tanto em Afiliação quanto em Apego Emocional, os únicos dois fatores com cargas consideráveis. Pais, mas não irmãos, são menos apegados do que suas contrapartes femininas, em linha com a teoria de investimento parental de Trivers. Irmãos e irmãs têm tanto motivo para cuidar de seus irmãos. Pais, no entanto, têm menos motivo do que mães. O esperma é barato. Ovos e gravidez são caros.

Palavras recíprocas estão mais espalhadas, refletindo traços ideais para responder a diferentes cenários: cooperação ou deserção do parceiro. A diferença mais saliente é a carga média mais alta em Ordem—alcançando seus próprios objetivos. Inicialmente chamado de _altruísmo de retorno adiado_, o altruísmo recíproco não é sobre sacrificar-se por um estranho, mas sim investir em seu próprio futuro por meio de meios pró-sociais. Por outro lado, o altruísmo de parentesco refere-se a ajudar a família mesmo às suas próprias custas por causa dos genes egoístas puxando suas cordas do coração. Isso é aparente em cargas mais altas de palavras de altruísmo de parentesco em Apego Emocional, apoiando a hipótese de Ashton. Mas a principal ação está em Ordem, longe de onde os instrumentos do espaço de sujeitos foram projetados para detectar. Os custos de amostragem no espaço de sujeitos tornam os resultados mais dependentes dos priors dos pesquisadores.

Interpretar esses gráficos pode parecer ler folhas de chá, mas estou cerca de 70% certo do que está aqui. Uma coisa que me faz hesitar é que os dois altruísmos são representados de maneiras diferentes. Palavras de parentesco descrevem todas as relações (por exemplo, _mãe, pai, irmão_), enquanto palavras recíprocas são uma mistura de relações (por exemplo, _vizinho_) e traços adequados em jogos de soma positiva repetidos (por exemplo, _vingativo, discriminador, cooperativo_). Incertezas à parte, não seria legal se em uma tarde eu realizasse um experimento que combina a experiência vivida de altruísmo de milhões de pessoas? O que gerações concordaram que faz alguém paternal, fraternal ou vizinho. Como sempre com uma nova fonte de sinal, começa-se atirando do quadril. Eventualmente, o Velho Oeste é domado; métodos e heurísticas emergem. Há muito espaço para melhorias. Os leitores podem ajustar os conjuntos de palavras e obter novos resultados em questão de minutos usando este [notebook colab](https://colab.research.google.com/drive/13DA2IKQ9zRimGedww_09iGT6ehuYriVz?usp=sharing). Por favor, façam isso!

#### Vantagens do espaço de palavras

 1. Conectado à Hipótese Lexical. Baseado na realidade social descentralizada.

 2. Menos transformações. Cada etapa é dispendiosa e introduz viés.

 3. Menos intensivo estatisticamente após a conversão para o espaço de palavras. (Barreira de entrada mais baixa.)

 4. O tamanho efetivo da amostra (aqueles que contribuíram para o modelo de linguagem via comentários no reddit, escrevendo livros ou artigos no pubMed) é muito maior e mais diverso do que a maioria dos estudos.

 5. Melhores perspectivas de emprego para PhDs em psicologia que conhecem PLN.

 6. Mais fácil de fazer trabalho multilíngue/multicultural. Alguns modelos são treinados em 100 idiomas simultaneamente (que é como a Meta treina [filtros de discurso de ódio](https://ai.facebook.com/blog/how-ai-is-getting-better-at-detecting-hate-speech/) em idiomas com poucos exemplos).

 7. Modelos de linguagem [continuam](https://openai.com/blog/introducing-text-and-code-embeddings/) [melhorando](https://say-can.github.io) [cada vez mais](https://ai.googleblog.com/2022/04/pathways-language-model-palm-scaling-to.html).

 8. Ciência aberta.

 9. [Evitar o IRB](https://slatestarcodex.com/2017/08/29/my-irb-nightmare/).

#### Desvantagens

 1. Mais partes móveis. Existem bilhões de parâmetros em um modelo de linguagem! No entanto, mesmo bilhões de neurônios e dezenas de decisões de treinamento podem resultar em uma representação estável. Qualquer modelo de linguagem que se preze pode completar a analogia "marido está para esposa assim como rei está para ____".

 2. Não é possível dividir os resultados por demografia. Às vezes é interessante saber a personalidade de professores do ensino fundamental entre 25-30 anos. Ou saber como algum construto se correlaciona com o histórico de prisões. Impossível no espaço de palavras.

 3. Os modelos de linguagem não são tendenciosos? Bem, não mais do que auto-relato.

 4. Definir altruísmo como a soma de um monte de vetores de palavras (ou seja, um saco de palavras) é um pouco improvisado. Há espaço substancial para melhorias aqui.

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!ctzj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F455fdb70-3c84-4dfe-81bf-6bf6e676fd44_1600x1128.jpeg)Psicólogos felizes com mais 40 anos vagando pelo espaço de sujeitos.

### **Deuses estrangeiros**

_"Acho que Kafka estava certo quando disse que, para um homem moderno, a burocracia estatal é o único contato restante com a dimensão do divino."_ ~Zizek, Um Guia do Pervertido para a Ideologia

Ele está descrevendo aqui, é claro, a sensação transcendente de apresentar um recurso ao IRB. Tenho uma previsão. O espaço de palavras é a coisa boa e certa a fazer do ponto de vista do processamento de sinal, mas sua adoção será impulsionada tanto pela conveniência de não ser regulamentado. O corolário é que o IRB será o primeiro órgão governamental a declarar modelos de linguagem sencientes.

<!-- CHUNK BREAK -->

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!6nGN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fedfc8bac-cf78-40f9-88d3-9a30066ff108_817x1600.jpeg)John espalhando a boa nova espacial

### **Preparando o caminho**

Gostaríamos de extrair relações entre construtos a partir de modelos de linguagem. Fazer isso de uma maneira que adicione sinal em vez de mais ruído requer muito trabalho de validação. Inicialmente, isso significa comparar com resultados de pesquisas bem estabelecidas. Eles podem ser recuperados usando vetores de palavras? Onde eles falham? Uma vez que isso tenha sido estabelecido, todo artigo que termina com "mais pesquisas necessárias" deve encontrar uma maneira de fazer a pergunta no espaço das palavras.

Passei mais de um ano ajustando um [método](https://psyarxiv.com/gdm5v/) para extrair relações de personalidade do [RoBERTa](https://arxiv.org/abs/1907.11692), o modelo de ponta na época. Logo após, o GPT-3 foi lançado e teve um desempenho melhor logo de cara. Que o poder de computação supera o conhecimento de domínio é uma [lição amarga](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) recorrente dentro da IA. O poder de computação aumenta exponencialmente. Se você pode obter ganhos de 30% sobre uma solução geral de ML usando conhecimento de domínio, você também pode simplesmente esperar que o [poder de computação alcance](https://twitter.com/russelljkaplan/status/1513128016452337667) e obter os mesmos resultados usando métodos gerais. Encontrar maneiras de relacionar questões de psicologia a modelos de PNL prontos para uso é, portanto, um bom caminho a seguir. Um novo modelo com desempenho visivelmente melhor é tornado público a cada seis meses ou mais. Aqueles que validam o espaço das palavras estão preparando o caminho para inteligências maiores—[PaLM](https://ai.googleblog.com/2022/04/pathways-language-model-palm-scaling-to.html), GPT-7, OSCar (**O** ptimal **S** entience **Car** tography)—para chover verdades psicológicas.

A linguagem natural está repleta de teorias compartilhadas sobre o mundo. Agora que podemos quantificá-las, elas não podem ser usadas como evidência?

Se você achou isso interessante, por favor, compartilhe!

[Compartilhar](https://www.vectorsofmind.com/p/in-the-beginning-was-the-word?action=share)