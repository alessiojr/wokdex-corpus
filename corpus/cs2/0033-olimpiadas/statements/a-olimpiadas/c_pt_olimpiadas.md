# Olimpíadas

Tumbólia é um pequeno país ao leste da América do Sul (ou ao sul da América do Leste) que irá participar dos Jogos Olímpicos pela primeira vez na sua história. Apesar de sua delegação ser muito pequena comparada ao total de atletas que estarão em Pequim (as estimativas oficiais são de mais de dez mil atletas), a participação será fundamental para a imagem e para o turismo de Tumbólia.

Após selecionar os atletas, o Comitê Olímpico Tumboliano (COT) precisa comprar as passagens para eles. A fim de economizar dinheiro, o COT decidiu comprar apenas passagens da Air Rock. No entanto, muitas das passagens da Air Rock já foram vendidas, uma vez que muitos tumbolianos desejam assistir aos Jogos. Sendo assim, o COT deverá comprar passagens de acordo com os assentos vagos em cada vôo.

Todos os voos da Air Rock partem diariamente antes do meio-dia e chegam após o meio-dia; por isso, um atleta pode tomar apenas um avião por dia. A Air Rock providenciou uma lista contendo todos os voos operados por ela e o número de assentos vagos em cada um (curiosamente, o número de assentos livres em um mesmo trecho é igual todos os dias).

O COT verificou que realmente é possível ir de Tumbólia para Pequim usando apenas voos da Air Rock mas, mesmo assim, o COT está tendo dificuldades para planejar a viagem de seus atletas. Por isso, o COT pediu para você escrever um programa que, dada a lista de voos da Air Rock, determina a menor quantidade de dias necessária para que todos os atletas cheguem em Pequim.

## Entrada

A entrada contém vários casos de teste. A primeira linha de cada caso de teste contém três inteiros **N**, **M** e **A** indicando respectivamente a quantidade de aeroportos em que a Air Rock opera (2 ≤ **N** ≤ 50), a quantidade de voos em que há assentos vagos (1 ≤ **M** ≤ 2.450) e quantos atletas a delegação tumboliana tem (1 ≤ **A** ≤ 50).

Cada uma das **M** linhas seguintes contém uma descrição de voo com três inteiros **O**, **D** e **S** que indicam respectivamente o aeroporto de origem (1 ≤ **O** ≤ **N**), o aeroporto de destino (1 ≤ **D** ≤ **N** e **O** ≠ **D**) e a quantidade de assentos vagos naquele voo (1 ≤ **S** ≤ 50). Os aeroportos são numerados de 1 a **N**; o Aeroporto Internacional de Tumbólia é o aeroporto 1, e o Aeroporto Internacional de Pequim é o aeroporto **N**.

A existência de um voo de **A** para **B** **não** implica a existência de um voo de **B** para **A** (mas sempre há no máximo um voo de um aeroporto para outro em cada direção).

O final da entrada é indicado por **N** = **M** = **A** = 0.

## Saída

Para cada caso de teste da entrada seu programa deve produzir uma linha na saída contendo um inteiro, indicando a quantidade mínima de dias necessária para que todos os atletas tumbolianos cheguem em Pequim (alguns atletas podem chegar depois de outros, e eles não precisam chegar na mesma ordem em que partiram).

## Dica de Estratégia

Este problema é um clássico de **fluxo máximo em grafos** combinado com **busca binária** (ou simulação iterativa sobre dias).

- Modele os aeroportos como nós de um grafo dirigido, onde cada aresta possui uma **capacidade** igual ao número de assentos vagos do voo correspondente.
- A cada dia, o número de atletas que conseguem viajar da origem ao destino corresponde ao **fluxo máximo** entre o aeroporto 1 (Tumbólia) e o aeroporto **N** (Pequim).
- Como os voos são idênticos todos os dias, o fluxo máximo diário é constante. Com isso, basta calcular o fluxo máximo **uma única vez** e então determinar o número de dias necessário para escoar todos os **A** atletas.
- Use **busca binária** sobre o número de dias para encontrar o mínimo, ou simplesmente calcule: `dias = ⌈A / fluxo_max⌉` (teto da divisão de A pelo fluxo diário máximo).

**Algoritmos recomendados**: Ford-Fulkerson com BFS (Edmonds-Karp), com complexidade **O(V · E²)** — adequado para os limites do problema (N ≤ 50, M ≤ 2.450).

## Exemplos

| Entrada | Saída |
|:--------|:------|
| 3 3 3   | 2     |
| 1 2 2   |       |
| 2 3 2   |       |
| 1 3 1   |       |
| 3 3 5   | 6     |
| 1 2 1   |       |
| 2 3 5   |       |
| 3 1 4   |       |
| 0 0 0   |       |

| Entrada | Saída |
|:--------|:------|
| 4 4 4   | 3     |
| 1 4 1   |       |
| 1 2 1   |       |
| 2 3 1   |       |
| 3 4 1   |       |
| 0 0 0   |       |
