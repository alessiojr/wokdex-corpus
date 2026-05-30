# Ida à Feira

Dona Parcinova é uma ávida compradora de supermercado. A cada ida dela ao centro da cidade, o seu pequeno caderninho conta com dezenas de itens minuciosamente anotados para a colorida salada da tarde! A sua missão como aspirante a engenheiro será exatamente automatizar de forma virtual a "calculadora mental" da feira.

A feira oferece $M$ produtos únicos na calçada principal, variando de exóticos como "mamao" para os rotineiros "brocolis". Seu sistema deve memorizar de maneira inteligente e rastreável todos esses preços para não perdê-los após andarem pela feira! Em seguida, as escolhas diretas para aquele final de semana virão, somando formalmente $P$ produtos e suas respectivas ordens de quantidade. A conta não pode falhar no caixa, pois no final, ela deve exibir com integridade absoluta exatamente os centavos exatos no lado direto do prefixo monetário. Cuidado com erros de troco decorrentes das limitadas casas decimais das linguagens e processadores virtuais!

## Tutorial Passo a Passo

Para este nível elementar é muito custoso e arriscado realizar varreduras exaustivas nos produtos a cada checagem individual. A implementação mais amigável previne percalços em feiras gigantes configurando estruturas baseadas em Dicionário de Correlação (**HashMap** / **Dictionary** / **Map**). O catálogo converte instantaneamente o nome em valor contábil.

1. **Laço de Múltiplos Casos Inteiros:** Existe uma bateria principal totalizando globalmente iteradores para "idas à feira" parametrizadas pela variável total $N$. Englobe adequadamente essa estrutura máxima ativando sua codificação inteira até consumir inteiramente os níveis.
2. **Leitura e Precificação de Identificadores ($M$):** 
   - Receba incialmente qual será a contagem de produtos isolados do sistema $M$.
   - Zere e re-instancie o objeto referencial de catálogo/tabela na memória para não vazar memórias lixo das feiras anteriores!
   - Execute num escopo simples de $M$ passagens uma leitura dual: colete a string rotular (o _Nome em Sí_) e amarre definitivamente ele como Chave Mestra junto na extração do ponto-flutuante associado (o _Preço na forma de Objeto Value/Double_).
3. **Povoar e Somar do Cesto ($P$):**
   - Aloque e inicialize um valor totalizador decimal neutro isoladamente (como `float soma_total = 0.0`).
   - Realoque seu olhar ao terminal processando a última barreira formal que contem exatos ciclos de pedidos de $P$ itens desejados.
   - Sua lógica lerá em mãos nome e quantidade atuais. Passe essa credencial nominal limpa dentro da função de busca do seu mapa sem o auxílio de For-Loops arcaicos. Se constar as laranjas de R$2,50, ela multiplicará os dois itens lidos garantindo logo a somatória real in-place. Adiciona no `soma_total`.
4. **Fechamento e Saída Restrita:** Terminado as coletas das $P$ restrições do carrinho de compras, valide os pontos fixos de 2 casas após o encerramento do printf (`%.2f`) assegurando que seu script sempre pule uma linha. Imprima literalmente `R$ ` (R + $ + espaço) de respiro!

---

## Entrada

A primeira linha de entrada contém um inteiro $N$ que indica a quantidade de idas à feira de dona Parcinova (que nada mais é do que o número de casos de teste que vem a seguir). Cada caso de teste inicia com um inteiro $M$ que indica a quantidade de produtos que estão disponíveis para venda na feira. Seguem os $M$ produtos com seus preços respectivos por unidade ou Kg. A próxima linha de entrada contém um inteiro $P$ ($1 \leq P \leq M$) que indica a quantidade de diferentes produtos que dona Parcinova deseja comprar. Seguem $P$ linhas contendo cada uma delas um texto (com até 50 caracteres) e um valor inteiro, que indicam respectivamente o nome de cada produto e a quantidade deste produto.

## Saída

Para cada caso de teste, imprima o valor que será gasto por dona Parcinova no seguinte formato: `R$` seguido de um espaço e seguido do valor, com 2 casas decimais, conforme o exemplo abaixo.

## Exemplos

| Entrada | Saída |
| :-- | :-- |
| 2<br>4<br>mamao 2.19<br>cebola 3.10<br>tomate 2.80<br>uva 2.73<br>3<br>mamao 2<br>tomate 1<br>uva 3<br>5<br>morango 6.70<br>repolho 1.12<br>brocolis 1.71<br>tomate 2.80<br>cebola 2.81<br>4<br>brocolis 2<br>tomate 1<br>cebola 1<br>morango 1 | R$ 15.37<br>R$ 15.73 |
