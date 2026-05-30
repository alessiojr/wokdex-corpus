# Tutorial: Pedido de Desculpas

## O Problema
Cuca precisa escrever um pedido de desculpas em um cartão com espaço restrito. Ele tem uma lista de frases e cada frase tem um custo em caracteres e um benefício (quantas vezes a palavra "desculpe" aparece). A tarefa é selecionar um conjunto de frases para maximizar o número total de "desculpes" sem exceder o espaço do cartão. Cada frase pode ser utilizada no máximo uma vez.

## A Estratégia: Mochila 0/1
Se tentarmos uma abordagem gulosa (escolhendo as frases com melhor custo-benefício primeiro), ela poderá falhar, pois o espaço restante pode ser mal aproveitado. Para garantir a resposta ótima para qualquer combinação, usamos **Programação Dinâmica**, especificamente o **Problema da Mochila 0/1**.

- **Capacidade ($C$)**: O limite de caracteres do cartão.
- **Peso ($N$)**: O tamanho da frase.
- **Valor ($D$)**: A quantidade de vezes que a palavra "desculpe" aparece.

### O Estado da Programação Dinâmica
Definiremos uma matriz `dp[i][j]`, que armazenará o **maior número de "desculpes"** que podemos obter considerando apenas as primeiras `i` frases disponíveis e possuindo um cartão com tamanho limite `j`.

### A Transição
Para cada frase `i` (com peso $N_i$ e valor $D_i$), e para cada capacidade `j` de $0$ até $C$:
1. **Não incluir a frase `i`:** Se escolhermos ignorá-la, a resposta será exatamente a mesma que tínhamos considerando apenas as `i-1` frases com a mesma capacidade `j`.
   `dp[i][j] = dp[i-1][j]`
2. **Incluir a frase `i`:** Se o peso da frase ($N_i$) couber no limite `j` atual ($N_i \leq j$), podemos tentar incluir a frase. O benefício será o valor dela ($D_i$) mais o melhor que podíamos fazer com o espaço que sobrar (`j - N_i`) usando as `i-1` frases anteriores.
   `dp[i][j] = max(dp[i-1][j], D_i + dp[i-1][j - N_i])`

A resposta final estará em `dp[F][C]`. O espaço de memória pode ser otimizado usando apenas um vetor unidimensional `dp[j]`, desde que você o atualize de trás para frente (de $C$ até $N_i$) a cada iteração de `i`. A complexidade de tempo será $O(F \times C)$.

## Passo a Passo
1. O problema contém múltiplos casos de teste, encerrando quando $C = F = 0$. Use um loop contínuo que trate essa condição de saída.
2. Para cada caso, leia os valores de $C$ e $F$. Mantenha também um contador de teste para imprimir "Teste n".
3. Inicialize uma estrutura de dados de DP preenchida com zeros, de tamanho `C + 1`.
4. Itere $F$ vezes lendo cada frase (tamanho $N$ e ocorrências $D$). E para cada frase recebida, atualize sua matriz (ou vetor 1D) da capacidade total $C$ regressando até o limite $N$, atualizando a mochila.
5. Imprima a formatação solicitada (pulando a linha em branco recomendada entre os casos, de acordo com o Output).

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
