# Letras

Uma cadeia de caracteres é uma sequência de letras do alfabeto. Uma cadeia de caracteres crescente é uma sequência de letras onde a próxima letra (da esquerda para a direita) nunca ocorre antes no alfabeto do que a letra anterior. Por exemplo ABBD é crescente, enquanto ABBAD não é crescente. Uma subsequência de uma cadeia de caracteres é uma cadeia de caracteres que pode ser obtida a partir da remoção de zero ou mais caracteres da cadeia de caracteres original. Por exemplo ANNA é uma subsequência de BANANAS. Outro exemplo seria ANNS, que é uma subsequência crescente de BANANAS.

Dada uma cadeia de caracteres S, escreva um programa para determinar o tamanho da maior subsequência de S que é uma cadeia de caracteres crescente.

## Dicas e Estratégia

Este é um problema clássico conhecido como **Maior Subsequência Crescente** (ou *Longest Increasing Subsequence* - LIS). Note que a definição de "crescente" neste problema permite letras iguais (ou seja, é uma subsequência não-decrescente).

Como o comprimento de S pode chegar a $3 \times 10^5$, um algoritmo de programação dinâmica básico em $O(N^2)$ será muito lento e só passaria nos casos parciais. Para obter a pontuação total, você precisará de uma abordagem mais eficiente.
- Tente usar Programação Dinâmica aliada à **Busca Binária** (Binary Search).
- Você pode manter um vetor auxiliar que armazena a menor letra final possível para uma subsequência não-decrescente de cada tamanho encontrado até o momento. A cada nova letra processada, use a busca binária (`upper_bound` em C++) para encontrar a posição correta de substituição ou adição nesse vetor.
- Essa estratégia reduzirá a complexidade para $O(N \log N)$, o que é rápido o suficiente para passar no tempo limite.

## Entrada

A entrada consiste em uma única linha, contendo uma cadeia de caracteres S.

## Saída

Seu programa deve produzir uma única linha, contendo um único inteiro, o tamanho da maior subsequência de S que é uma cadeia de caracteres crescente.

## Restrições

- A cadeia de caracteres de entrada contém letras maiúsculas do alfabeto, de A até Z.
- 1 ≤ comprimento(S) ≤ 3 × 10^5.

## Informações sobre a pontuação

- Em um conjunto de casos de teste valendo 20 pontos: comprimento(S) ≤ 20.
- Em um conjunto de casos de teste valendo 30 pontos: comprimento(S) ≤ 3000.

## Exemplos

| Entrada | Saída |
| :-- | :-- |
| BANANAS | 4 |

| Entrada | Saída |
| :-- | :-- |
| AAXBBXZZX | 7 |

| Entrada | Saída |
| :-- | :-- |
| AAA | 3 |
