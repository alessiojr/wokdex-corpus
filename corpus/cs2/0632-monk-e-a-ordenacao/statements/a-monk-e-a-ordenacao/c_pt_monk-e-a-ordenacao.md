# Monk e o Algoritmo de Ordenação

Monk recentemente teve uma conversa com Fredo sobre algoritmos de ordenação. Para testar se Fredo realmente compreendeu os conceitos, Monk propôs um desafio baseado em uma variante do **Radix Sort**.

### O Algoritmo

Considere o dígito mais à direita de um número como estando na **posição 1**, o segundo mais à direita na **posição 2**, e assim por diante.

Um **pedaço (chunk) de índice $i$** consiste nos dígitos localizados entre as posições $5 \times i$ (inclusive) e $1 + 5 \times (i - 1)$ (inclusive). Se um número não possuir dígitos em determinadas posições de um pedaço, assume-se o valor **0** para essas posições.

O algoritmo funciona da seguinte forma:
1. Começamos com $i = 1$.
2. Para cada número no array, extraímos o seu **$i$-ésimo pedaço**. O valor numérico desse pedaço é chamado de **peso** do número.
3. Se o peso de **todos** os números no array for igual a **0**, o algoritmo **para**.
4. Caso contrário, ordenamos o array de forma **estável** com base nos pesos calculados. (Ordenação estável significa que se dois números possuem o mesmo peso, sua ordem relativa original deve ser mantida).
5. Exibimos o estado atual do array após a ordenação.
6. Incrementamos $i$ em 1 ($i = i + 1$) e voltamos ao **passo 2**.

Sua tarefa é implementar esse algoritmo e exibir o estado do array após cada iteração de ordenação.

## Entrada

A primeira linha contém um inteiro $N$ ($1 \le N \le 10^6$), representando o número de elementos no array.
A segunda linha contém $N$ inteiros $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^{18}$), representando os elementos do array inicial.

## Saída

Para cada iteração em que o array é ordenado, imprima uma linha contendo os $N$ elementos do array separados por espaço, refletindo a ordem após aquela iteração.

## Restrições

- $1 \le N \le 10^6$
- $1 \le A_i \le 10^{18}$
- O tempo limite é rigoroso; use métodos de entrada/saída eficientes.

## Exemplos

### Exemplo de Entrada
```text
3
213456789 167890 123456789
```

### Exemplo de Saída
```text
213456789 123456789 167890 
167890 123456789 213456789 
```

**Explicação do Exemplo:**
- **Passo 1 ($i=1$):**
  - Blocos de 5 dígitos (posições 1 a 5):
    - `213456789` -> pedaço: `56789`
    - `167890` -> pedaço: `67890`
    - `123456789` -> pedaço: `56789`
  - Pesos: `56789, 67890, 56789`.
  - Ordenação estável: `213456789` e `123456789` têm o mesmo peso, então `213456789` vem primeiro. `67890` é o maior.
  - Resultado: `213456789 123456789 167890`

- **Passo 2 ($i=2$):**
  - Blocos de 5 dígitos (posições 6 a 10):
    - `213456789` -> pedaço: `02134` (ou `2134`)
    - `123456789` -> pedaço: `01234` (ou `1234`)
    - `167890` -> pedaço: `00001` (ou `1`)
  - Pesos: `2134, 1234, 1`.
  - Ordenação estável: `1` < `1234` < `2134`.
  - Resultado: `167890 123456789 213456789`

- **Passo 3 ($i=3$):**
  - Todos os pesos serão 0. O algoritmo para.
