# Organizando o Estoque

A divisão de Suprimentos de Botas e Calçados do Exército está com problemas de inventário. Muitos pares caíram das caixas e estão misturados. Sua missão é ajudar a organizar essa bagunça.

Você recebeu uma lista com a descrição de cada bota que foi encontrada. Cada bota tem um número (tamanho) e um indicativo de pé (Direito ou Esquerdo). Para formar um par válido que possa ser usado por um soldado, você precisa encontrar duas botas que tenham o **mesmo tamanho**, mas sejam de **pés opostos** (uma Esquerda e uma Direita).

## Dicas de Implementação

Para resolver este problema eficientemente, você pode contar quantas botas de cada tipo (Tamanho e Pé) você possui.

*   Considere utilizar uma estrutura de dados para armazenar a contagem de botas para cada tamanho ($30 \leq M \leq 60$).
*   Para cada tamanho, você pode contar separadamente quantas botas são do pé Esquerdo e quantas são do pé Direito.
*   O número de pares que podem ser formados para um determinado tamanho é o mínimo entre a quantidade de botas esquerdas e direitas desse tamanho. Por exemplo, se você tem 5 botas tamanho 40 Esquerda e 3 botas tamanho 40 Direita, você só consegue formar 3 pares completos.

## Entrada

A entrada é composta por diversos casos de teste. A primeira linha de um caso de teste contém um inteiro **N** ($2 \leq N \leq 10^4$), **N** é par, indicando o número de botas individuais. Cada uma das **N** linhas seguintes descreve uma bota, contendo um número inteiro **M** ($30 \leq M \leq 60$) e uma letra **L**, separados por um espaço em branco. **M** indica o número da bota e **L** indica o pé da bota: **L = 'D'** indica que a bota é para o pé direito, **L = 'E'** indica que a bota é para o pé esquerdo.

## Saída

Para cada caso de teste imprima uma linha contendo um único número inteiro indicando o número total de pares corretos que podem ser formados somando-se os pares de todos os tamanhos.

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
