# Pedido de Desculpas

Cuca saiu para jogar futebol com os amigos e esqueceu do encontro que tinha com a namorada. Ciente da mancada, Cuca deseja elaborar um pedido especial de desculpas. Resolveu então enviar flores e usar o cartão da floricultura para escrever um pedido especial de desculpas.

Cuca buscou na internet um conjunto de frases bonitas contendo a palavra 'desculpe' (que pode ocorrer mais de uma vez na mesma frase). No entanto, o cartão da floricultura é pequeno, e nem todas as frases que Cuca colecionou poderão ser aproveitadas.

Cuca quer aproveitar o espaço do cartão, onde cabe um número limitado de caracteres, para escrever um sub-conjunto das frases coletadas de modo que apareça o máximo de vezes possível a palavra 'desculpe'.

## Dicas e Estratégia
Este é um problema clássico de **Programação Dinâmica**, conhecido especificamente como o **Problema da Mochila 0/1 (0/1 Knapsack Problem)**.
- A **capacidade da mochila** é o tamanho máximo do cartão ($C$).
- Os **itens** são as frases coletadas ($F$).
- O **peso de cada item** é o comprimento da frase ($N$).
- O **valor de cada item** é a quantidade de vezes que a palavra 'desculpe' aparece ($D$).

Como não podemos repetir frases (cada frase pode ser escolhida 0 ou 1 vez), você precisa construir uma matriz ou tabela onde o estado `PD[i][c]` representa o maior valor de "desculpes" que pode ser alcançado usando um subconjunto das `i` primeiras frases, com um cartão de capacidade `c`. Sua solução deve processar os estados de forma iterativa ou recursiva com memoização.
A complexidade ideal de tempo esperada é $O(F \times C)$.

## Tarefa
Escreva um programa que, dados o número de caracteres que cabem no cartão e a quantidade de frases coletadas (com os respectivos comprimentos e os números de ocorrências da palavra 'desculpe'), determine o número máximo de vezes que a palavra aparece, utilizando apenas as frases colecionadas, sem repeti-las.

## Entrada
A entrada é constituída de vários casos de teste. A primeira linha de um caso de teste contém dois números inteiros $C$ e $F$ indicando respectivamente o comprimento do cartão em caracteres ($8 \leq C \leq 1000$) e o número de frases coletadas ($1 \leq F \leq 50$). Cada uma das $F$ linhas seguintes descreve uma frase coletada. A descrição é composta por dois inteiros $N$ e $D$ que indicam respectivamente o número de caracteres na frase ($8 \leq N \leq 200$) e quantas vezes a palavra 'desculpe' ocorre na frase ($1 \leq D \leq 25$).
O final da entrada é indicado por $C = F = 0$.

A entrada deve ser lida do dispositivo de entrada padrão (normalmente o teclado).

## Saída
Para cada caso de teste seu programa deve produzir três linhas na saída. A primeira identifica o conjunto de teste no formato "Teste n", onde n é numerado a partir de 1. A segunda linha deve conter o máximo número de vezes que a palavra 'desculpe' pode aparecer no cartão, considerando que apenas frases coletadas podem ser utilizadas, e cada frase não é utilizada mais de uma vez. A terceira linha deve ser deixada em branco. A grafia mostrada no Exemplo de Saída, abaixo, deve ser seguida rigorosamente.

A saída deve ser escrita no dispositivo de saída padrão (normalmente a tela).

## Restrições
* $8 \leq C \leq 1000$ ($C = 0$ apenas para indicar o fim da entrada)
* $1 \leq F \leq 50$ ($F = 0$ apenas para indicar o fim da entrada)
* $8 \leq N \leq 200$
* $1 \leq D \leq 25$

## Exemplos

| Entrada | Saída |
| :-- | :-- |
| 200 4<br>100 4<br>100 1<br>120 2<br>80 5 | Teste 1<br>9<br> |

| Entrada | Saída |
| :-- | :-- |
| 40 3<br>10 1<br>10 1<br>20 2<br>0 0 | Teste 2<br>4<br> |
