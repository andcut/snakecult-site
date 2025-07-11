---
about:
- vetores-da-mente
- arquivo-do-blog
author: Andrew Cutler
date: '2025-07-04'
description: 'Meu trabalho tornou-se perigosamente próximo de um Engenheiro de Prompt.
  Isso está bem para mim, pois combina meu amor pela escrita, psicometria e PLN. Aqui
  estão algumas das técnicas de prompt mais poderosas:'
draft: false
keywords:
- vetores-da-mente
- prompt
- chatgpt
lang: pt
lastmod: '2025-07-11'
license: https://creativecommons.org/licenses/by-sa/4.0/
original_id: '145544092'
original_url: https://www.vectorsofmind.com/p/how-to-prompt-chatgpt
quality: 6
slug: how-to-prompt-chatgpt
tags: []
title: Como Solicitar ao Chatgpt
translation_model: gpt-4o
---

*From [Vectors of Mind](https://www.vectorsofmind.com/p/how-to-prompt-chatgpt) - imagens no original.*

---

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!EpIx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F719d87af-7c69-45fd-8c84-595b16af3dae_1024x1024.webp)Você após ler este post

Meu trabalho tem se aproximado perigosamente de um Engenheiro de Prompt[^1]. Isso é bom para mim, pois combina meu amor pela escrita, psicometria e PLN. Aqui estão algumas das técnicas de prompting mais poderosas:

 1. Use instruções claras e específicas

 2. Raciocínio em cadeia

 3. Colete as informações necessárias antes de realizar uma tarefa

 4. Divida as tarefas em etapas

 5. Termos técnicos são seus amigos

 6. Conjunto de frases úteis




#### **1\. Instruções claras e específicas**


Advogados e cientistas da computação são naturalmente bons nisso. Na verdade, uma das alegrias do prompting é que se pode ser muito menos preciso em comparação com o código regular, e os LLMs frequentemente captam a essência. No entanto, muitos pedidos podem ser melhorados simplesmente sendo explícitos sobre a tarefa e o formato que a resposta deve ter. Por exemplo, recentemente preparei esta refeição:

[*[Imagem: Conteúdo visual do post original]*](https://substackcdn.com/image/fetch/$s_!dVwU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F216d83a0-b1be-4f15-877a-bfbb9842c0ed_1284x1253.jpeg)

Estava delicioso, obrigado por perguntar. Outros exemplos:

 * "Resuma a história da IA em um parágrafo."

 * "Crie uma tabela das famílias linguísticas mais antigas ordenadas por idade. Seja exaustivo."[^2]

 * "Reescreva o texto citado no estilo de White e Strunk. Dê-me três opções."

 * "Calcule uma matriz de correlação de Pearson para as colunas 2-7 do arquivo anexado.csv."

 * acompanhamento: "Escreva um código para exibir os resultados como um mapa de calor com resolução alta o suficiente para ser usado em um pôster. Use as melhores práticas em escolhas estéticas"




Instruções específicas frequentemente incluem exemplos específicos. White e Strunk escreveram _Elements of Style_. Citar seu livro é melhor do que usar adjetivos como "conciso", "profissional" ou "excelente" na escrita. Em parte porque os LLMs tendem a exagerar, especialmente em adjetivos específicos. Portanto, se você quer que o robô adote uma persona atrevida, tente dizer para ele agir como Veronica Mars ou Regina George de Meninas Malvadas.

#### **2\. Raciocínio em cadeia**


Os LLMs são treinados em um enorme corpus de texto para prever a próxima palavra. Surpreendentemente, isso os torna bons em aproximar o raciocínio, mas rapidamente falham em tarefas complexas. Aqui, "complexo" pode significar algo como "somar os números na coluna 1". Isso é muito difícil de fazer de uma só vez, e ele vai cuspir algum número que parece razoável e provavelmente estará na faixa certa, mas não será a resposta correta. Acrescentar "pense nisso em etapas" faz maravilhas. Muitas vezes, você nem precisa especificar quais são as etapas; os LLMs podem inferir que para somar a coluna, as etapas intermediárias são escrever "n1 + n2 + n3 + … + n100 =". É essencialmente um prompting para si mesmo para obter uma resposta melhor no lado direito desse sinal de igual. Ou, por analogia, dar a si mesmo tempo para pensar sobre isso. Para qualquer problema, a frase "pense nisso em etapas" é sua primeira linha de defesa ao lidar com alucinações de LLM. Se isso não funcionar, enumere as etapas você mesmo (uma técnica à qual retornaremos).

#### **3\. Colete as informações necessárias antes de realizar uma tarefa**


Se você pedir ao chatGPT para escrever um post de blog (eu nunca faria) ou uma função em Python (eu absolutamente faria), ele irá escrevê-lo sem perguntar os detalhes do que você realmente quer. Muito disso pode ser evitado dizendo algo como, "Quero escrever uma função que faça X; quais informações preciso reunir antes de codificar?" ou "Escreva uma função que faça X, mas primeiro pergunte por qualquer informação necessária antes de escrever o código." onde "X" é alguma descrição parcial.

#### 4\. Divida as tarefas em etapas


Sempre que o chatGPT falha em uma tarefa e o raciocínio em cadeia não ajuda, divida a tarefa em subtarefas. Isso é frequentemente metade do trabalho de uma tarefa para começar e, coincidentemente, o que é (atualmente) difícil para os LLMs fazerem por conta própria. No entanto, observe que você pode frequentemente terceirizar isso para o LLM também[^3]. Por exemplo, eu pedi ao chatGPT para criar itens para um teste de criatividade (que você pode ler por alto):

> Estou tentando criar mais perguntas semelhantes ao Teste de Associação Remota (RAT). O RAT exige que os indivíduos encontrem uma palavra comum que ligue três palavras aparentemente não relacionadas. Aqui estão alguns conjuntos de palavras de exemplo:
> 
> 1\. Cottage, Swiss, Cake (Resposta: Queijo)
> 
> 2\. High, Book, Chair (Resposta: Escola)
> 
> 3\. Fruit, Gaze, Traffic (Resposta: Jam)
> 
> 4\. Cream, Skate, Water (Resposta: Gelo)
> 
> 5\. Ache, Hunter, Cabbage (Resposta: Cabeça)
> 
> 6\. Manners, Round, Tennis (Resposta: Mesa)
> 
> 7\. Falling, Actor, Dust (Resposta: Estrela)
> 
> 8\. Light, Birthday, Stick (Resposta: Vela)
> 
> 9\. Salad, Head, Goose (Resposta: Ovo)
> 
> 10\. Music, Ached, Green (Resposta: Maçã) 
> 
> Quais são as melhores práticas? Como devo pensar nisso em etapas?

Como entender como somar números, o chatGPT é ótimo em produzir "receitas" para realizar tarefas. Depois que ele entregou, tudo o que eu tive que dizer foi:

> "Ótimo! Agora passe por esse processo para produzir 5 novas perguntas"

E então mais cinco, e mais cinco. Eu já havia tentado pedir diretamente por novos itens, e as sugestões foram atrozes. Para um [exemplo muito mais complicado](https://redwoodresearch.substack.com/p/getting-50-sota-on-arc-agi-with-gpt), veja como um instituto de segurança de IA usou essa técnica (entre outros truques) para resolver um problema que foi projetado para ser impossível para LLMs. 

#### 5\. Termos técnicos são seus amigos


Termos técnicos são bacias de atração para o comportamento competente dos LLMs. Por exemplo, descrever uma doença e perguntar o que é "indicado" levará você mais longe do que perguntar "O que devo fazer?" Usar "indicado" diz ao LLM para mapear seus sintomas para todos os livros de medicina já escritos. O último mapeia para pedir conselhos médicos/de vida, o que ele foi treinado para não dar. Usar termos técnicos ou não coloquiais move você para fora do espaço de assistente comum, que tem mais restrições e conselhos no nível do Reddit.

#### 6\. Conjunto de prompts úteis


Aqui estão algumas frases que costumo usar

 * "Isso está correto?"

 * Sempre que escrevo um resumo do trabalho de outra pessoa ou descrevo uma ideia com a qual não estou totalmente familiarizado, copio e colo minha escrita e pergunto se está correta. Geralmente é muito bom em contestar quando partes são discutíveis

 * "Você tem certeza?"

 * Da mesma forma, sempre que suspeito que um LLM está falando besteira, pergunto se ele tem certeza. Se ele mudar de ideia, então leve a afirmação com um grande grão de sal.

 * "Ajude-me a fazer um brainstorm." "Seja criativo"

 * Um dos melhores usos de um LLM é ajudá-lo a explorar o espaço de ideias. Às vezes, ele precisa de incentivo para se afastar das respostas modais.




Se você tiver algum favorito, adicione nos comentários!

[Compartilhar](https://www.vectorsofmind.com/p/how-to-prompt-chatgpt?action=share)

[^1]: Também se tornou mais irregular do que eu gostaria, então se você tiver algum trabalho por contrato em ciência de dados, IA ou psicometria, entre em contato!

[^2]: Admitidamente, não há como um LLM listar todas as 142-420 famílias linguísticas do mundo. Como isso é "impossível" (ou seja, muito longe de seu comportamento padrão, além de algum limite rígido de tokens), "exaustivo" serve para combater a gravidade de uma resposta curta, tornando o LLM mais minucioso. Este é o lado negativo do prompting, que às vezes se degrada em implorar, suplicar, subornar e ameaçar.

[^3]: O fato de você poder obter ajuda de um LLM na divisão da subtarefa indica que isso também será cada vez mais automatizado. Quem sabe do que as futuras gerações serão capazes.