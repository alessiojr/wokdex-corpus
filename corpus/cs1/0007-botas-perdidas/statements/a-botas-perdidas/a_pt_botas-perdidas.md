# Desafio do Sargento

O Sargento da divisão de suprimentos é conhecido por sua exigência extrema com a organização e eficiência. Recentemente, ele recebeu um carregamento caotico de equipamentos para os soldados e precisa apresentar um relatório de eficiência imediato ao General.

O carregamento consiste em diversos itens, onde cada item possui duas características fundamentais: um identificador numérico (tamanho) e uma lateralidade (esquerda ou direita). A eficiência do pelotão é medida estritamente pelo número máximo de conjuntos completos que podem ser formados. Um conjunto completo é formado por dois itens que possuem exatamente o mesmo identificador numérico, mas lateralidades opostas.

Sua tarefa, como o recruta mais proeminente em lógica, é calcular essa métrica de eficiência para os lotes recebidos. O Sargento não quer saber *quais* itens formam os pares, apenas o número total máximo de pares viáveis.

## Entrada

A entrada é composta por diversos casos de teste. A primeira linha de um caso de teste contém um número inteiro **N** ($2 \leq N \leq 10^4$), onde **N** é par, indicando a quantidade de itens individuais no lote.

Cada uma das **N** linhas seguintes descreve um item, contendo um número inteiro **M** ($30 \leq M \leq 60$) e uma letra **L**, separados por um espaço em branco. **M** indica o identificador do item (tamanho) e **L** indica a lateralidade:
*   **L = 'D'** indica que o item é do lado Direito.
*   **L = 'E'** indica que o item é do lado Esquerdo.

A entrada termina quando não houver mais casos de teste (EOF).

## Saída

Para cada caso de teste, imprima uma única linha contendo um único número inteiro indicando o número total de pares corretos (conjuntos completos) que podem ser formados.

## Exemplo

| Entrada | Saída |
|:--- |:--- |
| 4 | 2 |
| 40 D | |
| 41 E | |
| 41 D | |
| 40 E | |
| 6 | 1 |
| 38 E | |
| 38 E | |
| 40 D | |
| 38 D | |
| 40 D | |
| 37 E | |
