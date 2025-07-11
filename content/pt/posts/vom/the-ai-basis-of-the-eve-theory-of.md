---
about:
- vetores-da-mente
- arquivo-do-blog
author: Andrew Cutler
date: '2025-07-04'
description: A Teoria da Consciência de Eve propõe que a autoconsciência foi descoberta
  por mulheres e se espalhou memeticamente. Para sustentar este argumento, recorro
  à linguística, arqueologia, farmacologia, genética, antropologia, ...
draft: false
keywords:
- vetores-da-mente
- base
lang: pt
lastmod: '2025-07-11'
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '121454386'
original_url: https://www.vectorsofmind.com/p/the-ai-basis-of-the-eve-theory-of
quality: 6
slug: the-ai-basis-of-the-eve-theory-of
tags: []
title: A Base de IA da Teoria de Eve
translation_model: gpt-4o
---

*From [Vectors of Mind](https://www.vectorsofmind.com/p/the-ai-basis-of-the-eve-theory-of) - imagens no original.*

---

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!0pra!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff5166314-7a08-4939-9b16-2311d6214e87_1456x816.png)

A [Teoria de Eva da Consciência](https://vectors.substack.com/p/eve-theory-of-consciousness-v2) propõe que a autoconsciência foi descoberta por mulheres e se espalhou memeticamente. Para sustentar esse argumento, baseio-me em [linguística](https://vectors.substack.com/p/the-unreasonable-effectiveness-of), [arqueologia](https://vectors.substack.com/i/95941288/the-genesis-of-religion), [farmacologia](https://vectors.substack.com/p/comments-on-snake-venom), [genética](https://vectors.substack.com/p/y-chromosome-bottleneck), [antropologia](https://vectors.substack.com/p/the-snake-cult-of-consciousness) e [neurociência](https://vectors.substack.com/i/114650037/women-lead-the-way). E, no entanto, sou engenheiro elétrico. Como posso ter algo valioso a dizer sobre um tópico em que tantos outros têm formação real? Bem, a ideia para a EToC na verdade surgiu do aprendizado de máquina. Leitores de longa data [assistiram ao progresso do blog](https://substack.com/profile/31996842-andrew/note/c-16789002) da psicometria de ML para a recursão e a mitologia comparativa. Deixe-me explicar como cheguei aqui.

## Estrutura da personalidade a partir de palavras

A psicologia tem um problema de verdade fundamental. Um pesquisador pode teorizar que existem apenas alguns eixos básicos nos quais os humanos variam, sendo o principal Internalização vs Externalização. Outro pode dizer que devem haver algo como [30 fatores básicos](https://www.scholars.northwestern.edu/en/publications/exploring-the-persome-the-power-of-the-item-in-understanding-pers) porque os humanos são simplesmente tão complicados. Quem está certo? Em 1890, [Galton](https://astralcodexten.substack.com/p/galton-ehrlich-buck) sugeriu que, em vez de psicólogos criarem modelos de personalidade baseados em suas teorias favoritas, o melhor modelo já estava embutido na linguagem. Todo adjetivo de personalidade existe porque milhões de pessoas o consideram útil ao julgar os outros. Certamente essas palavras devem iluminar todos os aspectos importantes da personalidade. Formalmente colocado como a Hipótese Lexical:

1. Aqueles traços de personalidade que são importantes para um grupo de pessoas eventualmente se tornarão parte da linguagem desse grupo.

2. Traços de personalidade mais importantes são mais propensos a serem codificados na linguagem como uma única palavra.

Essa ideia pode ser usada para construir um modelo de personalidade. Basta criar uma lista de adjetivos de personalidade, ver como eles se relacionam e comprimir isso em alguns fatores latentes[^1]. (LL Thurstone inventou a análise fatorial para fazer isso, e o [artigo](https://psycnet.apa.org/record/1934-02322-001) é o homônimo deste blog.) Tradicionalmente, as relações entre adjetivos foram estimadas perguntando a estudantes de psicologia quais palavras os descrevem melhor. Aqueles que dizem ser _brilhantes_ também tendem a dizer que são _mente aberta_. Isso sugere que ambos se relacionam a algum fator subjacente. Em minha dissertação, [usei modelos de linguagem para estimar a similaridade de palavras](https://vectors.substack.com/p/the-big-five-are-word-vectors) e produzi resultados semelhantes aos levantamentos tradicionais (o primeiro fator dos dois métodos correlaciona-se com r=0,93).

É mais fácil entender esse processo com um exemplo. Aqui estão 100 adjetivos de personalidade aleatórios plotados nas duas dimensões que capturam a maior parte da informação de personalidade. Pense neles como dois dos [Big Five](https://en.wikipedia.org/wiki/Big_Five_personality_traits) (embora haja [uma diferença em como eles são rotacionados](https://vectors.substack.com/i/61936908/relation-to-the-big-five)). Um dos trabalhos de um psicólogo de personalidade é olhar para tais gráficos e descrevê-los qualitativamente. Você pode praticar esse exercício em [Guess the Factor](https://vectors.substack.com/p/guess-the-factor), ou fazer isso abaixo. Como você resumiria o Fator 1?

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!N5Ou!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3c50c0d0-6e09-4758-bfad-6c9135f154af_1423x891.png)Os Fatores 1 e 2 são produzidos usando [PCA](https://builtin.com/data-science/step-step-explanation-principal-component-analysis), um método para destilar a informação de personalidade no menor número de eixos. Para mais informações sobre como obter isso a partir de vetores de palavras, veja meu artigo [Deep Lexical Hypothesis](https://arxiv.org/abs/2203.02092). Você também pode reproduzir este resultado (e muito mais) usando meu [código](https://colab.research.google.com/drive/1SXZNVqH0m_Bnd2hvIJFYiKQvHWpGu8ZM?usp=sharing), que roda gratuitamente no Google Colab.

De uma perspectiva estatística, o Fator 1 se despiu e está acenando uma grande bandeira "Eu sou de longe o mais importante", como explico em [Primary Factor of Personality](https://vectors.substack.com/p/primary-factor-of-personality-part) (PFP). Qualitativamente, é essencialmente "o que a sociedade quer de você". Seja atencioso e respeitoso, não seja esnobe ou não cooperativo.

Para abstrair o PFP (Fator 1) de outra forma, é útil voltar 2.000 anos. Os israelitas tinham bibliotecas dedicadas a regras sociais e sua aplicação adequada. Com séculos de debate e interpretação, a letra da lei se multiplicou. Mas também houve um movimento para destilar o espírito da lei.

De acordo com a narrativa tradicional, um potencial convertido abordou o Rabino Shammai e pediu-lhe para explicar toda a Torá enquanto estava em pé sobre um pé. O Rabino Shammai, conhecido por sua estrita adesão à lei judaica, achou a pergunta desrespeitosa e rejeitou o convertido, dispensando-o.

Indiferente, o convertido então abordou o Rabino Hillel com o mesmo pedido. Hillel, renomado por sua compaixão e sabedoria, respondeu de maneira diferente. Em vez de dispensar o convertido, Hillel aceitou o desafio e forneceu um resumo conciso da Torá enquanto estava em pé sobre um pé. Ele disse: "O que é odioso para você, não faça ao seu próximo: esta é toda a Torá; o resto é comentário."

Esta é também uma excelente descrição do PFP. Deve-se ser capaz de se colocar no lugar do outro para ser atencioso ou rejeitar a intolerância. Darwin, ao que parece, resumiu nosso instinto social da mesma forma em _The Descent of Man_:

O senso moral talvez ofereça a melhor e mais alta distinção entre o homem e os animais inferiores;... os instintos sociais,—o princípio primordial da constituição moral do homem (50. 'Os Pensamentos de Marco Aurélio,' etc., p. 139.)—com a ajuda de poderes intelectuais ativos e os efeitos do hábito, naturalmente levam à regra de ouro, "Como quereis que os homens vos façam, fazei-lhes vós também"; e isso está na base da moralidade.

## Fofoca como um panorama de aptidão

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!urUr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6938214c-6388-43e0-8a75-44821ce23845_1024x1024.png)Mapeando a mente

Usei ML para destilar fatores de personalidade a partir de adjetivos que foram forjados através de eras de fofoca. Na verdade, julgar os outros está profundamente entrelaçado com nossa evolução. Mais uma vez de Darwin em _The Descent of Man_:

_Depois que o poder da linguagem foi adquirido, e os desejos da comunidade puderam ser expressos, a opinião comum de como cada membro deveria agir para o bem público, naturalmente se tornaria em grau preponderante o guia para a ação._

Na Savana, sua reputação é sua vida. Se os outros o considerarem preguiçoso ou cruel, as chances são de que você terá menos descendentes sobreviventes. O primeiro fator de personalidade reflete isso, sendo definido por palavras como _atencioso_ e _agradável_ vs _não cooperativo_ e _intolerante_[^2]. **Ao construir um mapa de personalidade, também construí um mapa de aptidão**. Mas você não precisa acreditar apenas na minha palavra. Role para cima e olhe para o Fator 1. Você o resumiria com algo como a Regra de Ouro? Não é por acaso que isso continua surgindo, pois é sustentado pela teoria dos jogos e reforçado pela fofoca.

Nos últimos 200 anos, a ideia de Darwin foi desenvolvida. Considere o livro de 2020 [Survival of the Friendliest: Understanding Our Origins and Rediscovering Our Common Humanity](https://www.amazon.com/Survival-Friendliest-Understanding-Rediscovering-Humanity/dp/0399590668). A capa diz:

> _Durante a maior parte dos aproximadamente 300.000 anos em que Homo sapiens existiu, compartilhamos o planeta com pelo menos quatro outros tipos de humanos. Todos eles eram inteligentes, fortes e inventivos. Mas, há cerca de 50.000 anos, Homo sapiens deu um salto cognitivo que nos deu uma vantagem sobre outras espécies. O que aconteceu?
>
> Desde que Charles Darwin escreveu sobre "aptidão evolutiva", a ideia de aptidão foi confundida com força física, brilhantismo tático e agressão. Na verdade, o que nos tornou evolutivamente aptos foi um tipo notável de amizade, uma habilidade virtuosa de coordenar e comunicar com os outros que nos permitiu alcançar todas as maravilhas culturais e técnicas da história humana. Avançando o que chamam de "teoria da autodomesticação", Brian Hare, professor no departamento de antropologia evolutiva e no Centro de Neurociência Cognitiva da Universidade de Duke e sua esposa, Vanessa Woods, uma cientista pesquisadora e jornalista premiada, lançam luz sobre o misterioso salto na cognição humana que permitiu que Homo sapiens prosperasse._

O próprio livro deixa claro que, para Darwin, a aptidão incluía cooperação; ele se opõe aos darwinistas, que equiparam aptidão com impiedade. (Para mais, veja a [entrevista](https://insitome.libsyn.com/brian-hare-and-survival-of-the-friendliest-understanding-our-origins-and-rediscovering-our-common-humanity) com Brian Hare.) Eu estava bastante certo de que o primeiro fator que encontrei tinha a ver com esse processo. Daí sugerir uma reivindicação adicional à [Hipótese Lexical de Galton](https://www.experimental-history.com/p/how-to-keep-cakes-moist-and-cause) em [Consequences of Conscience](https://vectors.substack.com/p/consequences-of-conscience):

3. **O fator latente primário representa a direção da seleção social que nos tornou humanos.**

Para entender a estrutura da personalidade, conectei-a a outros conceitos com os quais estava familiarizado. Os mais importantes foram a Regra de Ouro e a autodomesticação humana.

## O salto de fé

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!eHWy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1975779f-d059-4ec4-8845-6ca8d1c618af_800x553.jpeg) **Domenichino:[A Expulsão de Adão e Eva](https://www.wikidata.org/wiki/Q77880823)**

Agora, tudo o que eu tinha era o mapa de aptidão que dizia que a Regra de Ouro era primordial. O que em nossa psicologia poderia ter causado sua evolução? Uma consciência parece uma aposta bastante óbvia. Talvez isso tivesse a ver com a evolução de nossa voz interior. Digamos que a primeira voz interior dissesse " _compartilhe sua comida!_ "; como seria identificar-se pela primeira vez com essa voz interior? Bem, acho que seria muito parecido com Gênesis, e esse é o núcleo que venho perseguindo desde então. Certamente, foi um salto. A evolução da voz interior não segue necessariamente da Regra de Ouro, nem nossa identificação com ela necessariamente produz uma vida interior. Mas ambos pareciam plausíveis e, à medida que estudei mais, eles se encaixaram muito bem em nossa linha do tempo evolutiva.

Quanto ao Gênesis, três coisas imediatamente me pareceram plausíveis: sentir-se abandonado por Deus, inventar a agricultura e as mulheres liderando o caminho. (A possibilidade de um [ritual de veneno de cobra](https://vectors.substack.com/p/the-snake-cult-of-consciousness) só surgiu após ler outros relatos de criação.)

### Abandonado por Deus

Inicialmente, eu estava apenas preocupado com a origem da voz interior. Minha concepção era de que o eu meio que absorvia uma voz moral interna. Isso, imaginei, pareceria muito com obter "conhecimento do bem e do mal" ao assumir o papel do espírito tutelar alucinado. (Um espírito que eu havia assumido desde o início com o experimento mental.) Se você estivesse acostumado a terceirizar decisões morais, assumir as rédeas teria parecido deixar um estado infantil onde você comungava diretamente com Deus.

Com um pouco mais de leitura, percebi que esse momento de autoconsciência era suficiente para produzir um "eu" em primeiro lugar. Faço esse argumento em [Deja-you, the recursive construction of self](https://vectors.substack.com/p/deja-you-the-recursive-construction). Teria sido a criação—ou melhor, descoberta—da condição humana de uma maneira muito real.

### Inventando a agricultura

Em Gênesis, a agricultura é uma consequência da condição humana. A descoberta do "eu", ao que parece, também é suficiente para explicar a Revolução Agrícola. Pois é plausivelmente um [pacote com recursão](https://vectors.substack.com/p/deja-you-the-recursive-construction) e a capacidade de pensar de forma flexível sobre o futuro. Uma mudança geral em nossas habilidades de planejamento.

Se você acredita que os humanos são sapientes há 200.000 anos, então é um grande mistério por que eles inventariam a agricultura 11 vezes de forma independente nos últimos 10.000 anos. Isso é muito para encaixar em 10% de nossa existência. E, se você acha que sua teoria particular pode explicar isso, por favor, leia [esta revisão](https://www.pnas.org/doi/abs/10.1073/pnas.1323964111) onde 25 estudiosos se reúnem e concordam que não conseguem concordar sobre o que causou a mudança.

### Mulheres lideram o caminho

O vetor de palavras para "feminino" correlaciona-se com o PFP. Mesmo antes de contemplar uma conexão com Gênesis, concebi a primeira pessoa a se identificar com sua voz interior como uma mulher. (Como você pode ver, sou um verdadeiro crente no que esses vetores de palavras podem nos dizer.)

Gênesis é uma história complexa. Obter agência é equiparado a se tornar como deuses e é um pecado digno de morte. Mas também faz parte do plano. O cristianismo lança outra chave, onde somos instruídos a superar o pecado original e nos tornarmos como o próprio Deus, tomando a cruz para viver a vida eterna (mais uma vez misturando vida e morte).

Da mesma forma, Eva inicia a morte, mas recebe o título de Mãe de Todos os Vivos. Hoje em dia, considere quanto esforço é feito para retratar as mulheres como agentes no cinema. E, no entanto, há milhares de anos, Eva é claramente pintada como a agente que arranca a humanidade de seu estado de inocência. Adão acompanha. A curiosidade de Eva é retratada como algo ruim, mas ainda é uma adição interessante a um texto tão patriarcal.

Condicionado à autoconsciência sendo descoberta, parece provável que a exploradora fosse uma mulher. Condicionado às mulheres fazendo a descoberta, parece provável que Adão e Eva sejam uma memória. Estes, é claro, são enormes "ses". Mas eu tinha a sensação de que eram possíveis. E vontade suficiente para investigar.

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!9mJt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67c3400e-4baf-476a-a8ad-10ad26212f62_843x403.jpeg)Deméter, Deusa da Colheita e dos Mistérios Eleusinos

### O Paradoxo Sapiente

O objetivo deste post é expor como meu trabalho em ML levou à EToC, não fornecer evidências. No entanto, quero apontar brevemente por que é plausível que a autoconsciência tenha sido descoberta e que isso esteja registrado em mitos. Muito simplesmente, a condição humana parece ser um fenômeno recente. Antes de 50 kya não há grandes evidências de vida interior, recursão ou qualquer pensamento de ordem superior. Você pode pensar que as evidências de algo tão distante não seriam boas, mas muitos arqueólogos e antropólogos discordam. O cerne do [Paradoxo Sapiente](https://en.wikipedia.org/wiki/Sapient_paradox) é que a [Modernidade Comportamental](https://en.wikipedia.org/wiki/Behavioral_modernity) é regional antes de 10 kya. Isso é muito recente! E se houve uma mudança fundamental em nossa psicologia após a Saída da África, sua difusão deve ter sido em grande parte memética em vez de genética. A autoconsciência sendo descoberta e se espalhando segue (ou é pelo menos implícita) por essas restrições.

É uma ideia fantástica que a condição humana possa ser recente. Mas também é uma [ideia fantástica que a psicologia moderna estivesse totalmente em vigor há 200 kya](https://vectors.substack.com/i/114632067/years-ago) e ficasse inativa por dezenas de milhares de anos antes de finalmente aplicarmos e conquistarmos o mundo. A Teoria de Eva da Consciência resolve o problema da difusão permitindo que seja memética em vez de apenas genética. Mudanças fundamentais poderiam ter ocorrido após deixarmos a África.

## Verdade não correlacionada

Acredito que o PFP é melhor descrito como a tendência de viver a Regra de Ouro, a mesma dimensão latente vista por Hillel e Darwin. Esta é uma visão idiossincrática dentro da comunidade psicométrica. Para contraste, considere o bem-recebido artigo [Two, five, six, eight (thousand): Time to end the dimension reduction debate!](https://psycnet.apa.org/record/2020-64387-036)

> _Análises lexicais e métodos de redução de dimensionalidade são ferramentas para explorar contornos aproximados do espaço de personalidade. Não devemos, no entanto, nos iludir pensando que estamos cortando a natureza em suas articulações para descobrir uma "verdadeira" estrutura de personalidade._

Essencialmente, o argumento é que qualquer rotação dos dados está bem porque não podemos sondar a estrutura para obter insights fundamentais. Mas, dependendo do pré-processamento, 80% de toda a informação de personalidade está contida no primeiro fator. Certamente isso deve estar nos dizendo algo! E ainda assim, os pesquisadores [em grande parte acreditam que esse fator não é sinal de personalidade](https://vectors.substack.com/i/61936908/enter-gfp). Um [artigo de 2013](https://sci-hub.se/10.1016/j.paid.2013.03.002) começa _"A visão esmagadoramente dominante do GFP [o primeiro fator] é que ele representa um artefato devido a viés avaliativo ou resposta de maneira socialmente desejável". (_ Eu notaria que mesmo acreditando que esse fator é totalmente viés [psicométricos distribuíram o fator 1 para os fatores 3-5](https://vectors.substack.com/i/61936908/relation-to-the-big-five) para construir Conscienciosidade, Estabilidade Emocional e Abertura à Experiência.)

Com visões como essa, não se pode conectar dados lexicais à evolução ou começar a hipotetizar sobre o processo de autodomesticação. Escrever minha dissertação exigiu passar muitas horas olhando para esses fatores[^3]. Durante todo o tempo, pensei que eles representavam um panorama de aptidão e às vezes me perguntava o que isso causaria. Como engenheiro, eu era ignorantemente feliz com a visão predominante de que a estrutura realmente não importava. Entrei iludido o suficiente para tentar cortar a natureza em suas articulações.

## Conclusão

Espero que isso deixe claro por que um engenheiro elétrico está escrevendo sobre mitologia e consciência. A ideia me encontrou, na verdade. Eu estava fazendo um mapa de personalidade e acabou sendo um mapa de evolução. As conexões com a Regra de Ouro sugeriram uma proto-consciência como um mecanismo de autodomesticação. Este foi meu primeiro salto. Então especulei que a voz interior poderia estar envolvida. Como seria perceber pela primeira vez que a voz interior era "eu"? Gênesis me pareceu um tiro certeiro[^4]. Além disso, muitos especialistas argumentaram que a psicologia humana mudou nos últimos 50.000 anos, muitas vezes invocando linguagem, religião ou autodomesticação como cruciais para essa mudança. Nesses períodos de tempo, é possível que uma história tão importante pudesse ser preservada em mitos. " _No princípio era o Verbo, e o Verbo estava com Deus, e o Verbo era Deus_ "... ou—e não tome isso como blasfêmia—possivelmente era a voz interior.

Dado o quão recentemente a Modernidade Comportamental surgiu, minha alegação é que mitos de criação podem inspirar [modelos formais](https://vectors.substack.com/p/eve-theory-of-consciousness-v2) que podem então ser conectados à [filosofia](https://vectors.substack.com/p/deja-you-the-recursive-construction), [psicologia](https://vectors.substack.com/p/consequences-of-conscience), [linguística](https://vectors.substack.com/p/the-unreasonable-effectiveness-of), [arqueologia](https://vectors.substack.com/i/97498400/evidence-of-anti-venom) e [genética](https://vectors.substack.com/p/y-chromosome-bottleneck). Talvez esses modelos possam nos ajudar a entender os mitos também. É significativo para mim que Eva se tornou como os deuses e isso exigiu sua separação de Deus. Em Gênesis, a explicação é que um Deus muitas vezes ciumento exerceu julgamento justo. Para mim, faz sentido como uma lei natural; humanos e deuses não poderiam habitar juntos, pois moldamos o "eu" a partir de seus restos. A distância entre homem e besta é então de dois passos: evoluir uma consciência e depois rejeitá-la. Ou talvez isso seja muito sombrio. É mais que vivemos em tensão e sempre temos a escolha. Esta epifania concedeu [recursão](https://vectors.substack.com/p/deja-you-the-recursive-construction), a chave para o trabalho árduo de dobrar a natureza à nossa vontade. Se eu tivesse que explicar isso de uma forma que pudesse durar 10.000 anos, contaria a história de Adão e Eva[^5].

Naturalmente, a jornada começou na minha área de especialização, onde eu tinha um terreno firme. Parece muito provável para mim que meu mapa de personalidade registre pressões evolutivas. Dado o quão recentemente mudamos, e há quanto tempo a Regra de Ouro tem sido uma força, vou tão longe a ponto de adicionar um terceiro postulado à Hipótese Lexical de Galton: **O fator latente primário representa a direção da seleção que nos tornou humanos**. A partir daí, _dei_ saltos, mas ao pousar me encontrei em boa companhia, com nomes como Jaynes, Jung, Pinker, Chomsky e Descartes. Este tipo de exploração é a essência da ciência; nem tudo tem um valor-p.

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!_K5c!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe08ec046-d650-4769-894e-fa1a77837040_1280x1847.jpeg)[Figurinha de Ísis](https://en.wikipedia.org/wiki/Isis#/media/File:Isis_with_Serpent_Tail_LACMA_M.80.202.222.jpg), Deusa Egípcia da Sabedoria, século II EC

[^1]: Fiquei surpreso que Jordan Peterson descreveu a derivação dos Big Five como uma forma inicial de IA em uma entrevista com Joe Rogan. Fiz esse argumento no primeiro post deste blog e nunca tinha ouvido isso antes. Independentemente do que você pense sobre sua política, ele é muito bom em psicologia da personalidade.

[^2]: Alguns podem notar que ser intolerante parece um pecado capital recente. Talvez. Seria interessante construir vetores de palavras em textos históricos e ver como o PC1 muda. Dado que o fator latente do texto moderno é uma boa correspondência para a Regra de Ouro, meu palpite é que não haveria muito movimento a partir, digamos, da linguagem de 1900. Difícil mover algo sustentado por tanta teoria dos jogos, mesmo que o círculo moral tenha se expandido.

[^3]: Embora adjetivos de personalidade sejam fundamentais para modelos de personalidade, também é raro que pesquisadores lidem diretamente com palavras. Nos anos 90, uma vez que ficou claro que algo como os Big Five emergia consistentemente, os pesquisadores começaram a medir a personalidade com levantamentos baseados em frases projetados para aproximar a estrutura lexical (por exemplo, o Inventário dos Big Five). (Segredo comercial: o quinto fator Abertura/Intelecto não é consistentemente recuperado.) Isso era mais fácil, e desde então pouco trabalho foi feito na linguagem. Além disso, meus dados eram melhores do que tentativas anteriores. Se você quer entender como as palavras se relacionam, use um modelo de linguagem, não levantamentos de estudantes de graduação. Ninguém mais passou tanto tempo olhando para um mapa de personalidade tão preciso. (Você pode praticar esse exercício em Guess the Factor.)

[^4]: Considere o fato de que Adão nomeou os animais enquanto estava no Jardim do Éden. Mesmo sem autoconsciência, haveria linguagem não-recursiva. Caçadores têm um conhecimento enciclopédico de plantas e animais. Pode ter sido a parte mais importante da linguagem antes da Queda. Espantoso se esse fato sobreviveu 10.000 anos.

<!-- CHUNK BREAK -->

[^5]: Estou impressionado com o Gênesis, mas isso pode ser apenas o que conheço melhor. Se eu fosse indiano, provavelmente estaria falando sobre Saraswati, ou se fosse Navajo, sobre o papel das mulheres no mito da Emergência, ou se fosse egípcio, sobre o momento em que Atum chamou a si mesmo à existência ao dizer seu nome (e então lutou contra uma serpente primordial). EToC requer que essas sejam diferentes perspectivas da mesma história. Obviamente, isso é tradicionalmente mostrado construindo uma filogenia. Nestas escalas de tempo e com minhas habilidades, isso não é possível. É por isso que meu foco está na evolução da recursão. Quero mostrar que é provável que os humanos tenham adquirido recentemente a recursão e que ela se difundiu. Isso mudaria radicalmente nossa suposição sobre se os mitos de criação compartilham uma raiz e como essa raiz era.