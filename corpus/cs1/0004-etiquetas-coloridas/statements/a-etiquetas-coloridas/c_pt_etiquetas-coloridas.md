# Pares de Cristais (Contagem Otimizada)

A bordo da Estação WOK, novos cristais minerais são minerados todos os dias. Você recebe uma lista de $N$ cristais coloridos. Cada cristal carrega uma etiqueta com um número representando sua cor.

O sistema da nave exige saber total de pares possíveis do mesmo tipo de cristal. Em vez de checar cada cristal contra todo o resto usando dois laços aninhados (uma abordagem O(N²) que causaria superaquecimento sistêmico, ou TLE), você pode registrar com que frequência cada cor de cristal aparece enquanto percorre a lista. 

Crie um programa eficiente que conte o total de pares de mesma cor.

## Entrada
* A 1ª linha tem o número total de cristais, $N$ ($1 \le N \le 10^5$).
* A 2ª linha fornece $N$ números (de $1$ a $10^9$) representando as cores.

## Saída
* Imprima a quantidade máxima de pares de mesma cor.

## Exemplos

### Exemplo 1

| Entrada       | Saída |
| :------------ | :---- |
| 5             | 2     |
| 1 2 1 3 2     |       |

### Exemplo 2

| Entrada   | Saída |
| :-------- | :---- |
| 4         | 6     |
| 1 1 1 1   |       |
