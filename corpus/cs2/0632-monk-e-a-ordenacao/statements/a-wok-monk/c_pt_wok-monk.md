# Radix Sort Espacial: O Desafio de Monk

![Hangar da Estação Espacial](../assets/monk_logistics.png)

Neste desafio, você deve ajudar Monk a implementar uma variante do algoritmo **Radix Sort** para organizar códigos de identificação espacial. O sistema de arquivos da Estação Orbital K-06 processa números em blocos de 5 dígitos (equivalente a trabalhar na base $10^5$), em vez do tradicional dígito a dígito (base 10).

### O Algoritmo

1. Divida cada número em pedaços de 5 dígitos, começando da direita para a esquerda.
2. Para cada iteração $i = 1, 2, \dots$:
    a. Calcule o "peso" de cada número como o valor do seu $i$-ésimo pedaço de 5 dígitos.
    b. Se todos os pesos na iteração atual forem zero, o algoritmo deve parar.
    c. Caso contrário, realize uma **ordenação estável** de todos os números com base nos pesos calculados. É altamente recomendável utilizar o **Counting Sort** para garantir que a complexidade da ordenação seja linear $O(N)$.
    d. Exiba o estado atual do array.

A ordenação estável é fundamental para que o Radix Sort funcione corretamente ao final das passagens.

## Entrada

A primeira linha contém um inteiro $N$ ($1 \le N \le 10^6$).
A segunda linha contém $N$ inteiros $A_i$ ($-10^{18} \le A_i \le 10^{18}$).

## Saída

Imprima o array após cada passo de ordenação estável.

## Restrições

- $1 \le N \le 10^6$
- $-10^{18} \le A_i \le 10^{18}$
- Tempo limite: 2.0 segundos.

## Exemplos

| Entrada | Saída |
| :--- | :--- |
| `3`<br>`213456789 167890 123456789` | `213456789 123456789 167890 `<br>`167890 123456789 213456789 ` |
