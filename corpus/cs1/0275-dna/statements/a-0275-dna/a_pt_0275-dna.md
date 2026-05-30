# 0275 - DNA

## Enunciado

Um biólogo está analisando sequências de DNA e deseja encontrar o grau de similaridade entre duas cadeias. A similaridade é medida pelo tamanho da maior subsequência comum entre as duas cadeias. No entanto, devido à natureza das mutações genéticas, o biólogo impôs uma restrição: a subsequência comum deve ser formada por **segmentos consecutivos** que correspondam em ambas as cadeias, e cada segmento deve ter um comprimento de **pelo menos $K$**.

Por exemplo, se $K=3$, as cadeias `lovxxelyxxxxx` e `xxxxxxxlovely` compartilham os segmentos `lov` e `ely`, que formam a subsequência comum `lovely` de tamanho 6. A sequência de caracteres `xxxxxxx` de tamanho 7 não é válida pois, embora existam os caracteres `x` soltos nas palavras, eles precisariam formar um bloco com tamanho mínimo de 3. Mas ao combiná-los, a estrutura dos blocos não obedece a ordem sem cruzar.

Escreva um programa que dadas duas sequências de DNA e um inteiro $K$, determine o tamanho da maior subsequência comum sob a restrição do biólogo.

### Entrada
A entrada consiste em vários casos de teste. Cada caso de teste é composto por três linhas:
1. A primeira linha contém o inteiro $K$ ($1 \le K \le 1000$).
2. A segunda linha contém a primeira sequência de DNA (apenas letras minúsculas e maiúsculas do alfabeto inglês), com comprimento entre 1 e 1000.
3. A terceira linha contém a segunda sequência de DNA, também com comprimento entre 1 e 1000.

O final da entrada é indicado por um caso onde $K = 0$, que não deve ser processado.

### Saída
Para cada caso de teste, imprima uma única linha contendo um inteiro que representa o tamanho máximo da subsequência comum formada por segmentos de tamanho no mínimo $K$.

### Exemplos
| Entrada | Saída |
|---|---|
| `3`<br>`lovxxelyxxxxx`<br>`xxxxxxxlovely` | `6` |
| `1`<br>`lovxxelyxxxxx`<br>`xxxxxxxlovely` | `7` |
| `3`<br>`lovxxxelxyxxxx`<br>`xxxlovelyxxxxxxx` | `10` |
| `4`<br>`lovxxxelyxxx`<br>`xxxxxxlovely` | `0` |
| `0` | (fim da entrada) |
