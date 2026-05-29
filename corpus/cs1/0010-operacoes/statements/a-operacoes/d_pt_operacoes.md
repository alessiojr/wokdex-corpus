# Operações

## Descrição
Você deve implementar um programa simples que funcione como uma calculadora limitada. O programa deve ser capaz de realizar duas operações básicas: multiplicação e divisão.

O usuário fornecerá um caractere indicando a operação desejada, seguido de dois números reais. Seu programa deve calcular o resultado da operação aplicada aos dois números e exibi-lo.

### Tutorial passo a passo
1.  **Lendo a operação:** A primeira coisa a fazer é ler o caractere que define a operação (`'M'` para multiplicação, ou `'D'` para divisão). Cuidado com os espaços em branco ou quebras de linha que podem estar na entrada, dependendo de como sua linguagem lida com leitura de caracteres únicos.
2.  **Lendo os valores:** Em seguida, leia os dois números com pontos flutuantes (que vamos chamar de $A$ e $B$).
3.  **Decidindo a operação:** Utilize uma estrutura condicional (ex: `if-else`).
    *   Se o caractere lido for `'M'`, multiplique $A$ por $B$ e armazene o resultado.
    *   Se o caractere lido for `'D'`, divida $A$ por $B$ e armazene o resultado.
4.  **Imprimindo a saída:** Imprima o resultado da operação garantindo que o número exibido possua exatamente as **duas casas decimais** exigidas pelo problema. Você deve usar os recursos da sua linguagem de escolha para forçar a formatação, sem fazer o arredondamento manual a não ser que necessário.
    *   **Python:** `print(f"{resultado:.2f}")`
    *   **C / C++:** `printf("%.2f\n", resultado);`
    *   **Java:** `System.out.printf("%.2f\n", resultado);`

## Formato de Entrada
A entrada consiste de duas partes:
1.  A primeira linha contém um único caractere:
    *   `'M'` para multiplicação.
    *   `'D'` para divisão.
2.  A segunda linha contém dois números reais (ponto flutuante), $A$ e $B$.

## Formato de Saída
A saída deve consistir de uma única linha contendo o resultado da operação, formatado com **duas casas decimais**.

## Exemplos

| Exemplo de Entrada | Exemplo de Saída |
| :- | :- |
| M<br>10 2.5 | 25.00 |
| D<br>10 4 | 2.50 |
