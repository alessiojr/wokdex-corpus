# Operações

## Descrição
Você deve implementar um programa simples que funcione como uma calculadora limitada. O programa deve ser capaz de realizar duas operações básicas: multiplicação e divisão.

O usuário fornecerá um caractere indicando a operação desejada, seguido de dois números reais. Seu programa deve calcular o resultado da operação aplicada aos dois números e exibi-lo.

### Dica
- **Entrada e Saída Básicas:** Este problema é um exercício fundamental de leitura de diferentes tipos de dados (um caractere e dois números de ponto flutuante) e impressão formatada.
- **Estruturas Condicionais:** Utilize uma estrutura condicional (como `if/else` ou `switch`) para verificar qual operação foi solicitada (`'M'` ou `'D'`).
- **Formatação:** Preste atenção à exigência de imprimir o resultado com exatamente duas casas decimais. Dependendo da linguagem, funções como `printf("%.2f", ...)` em C/C++, `f"{valor:.2f}"` em Python, ou `System.out.printf("%.2f", ...)` em Java serão úteis.
- **Complexidade:** As operações matemáticas são primitivas e executadas em tempo constante. A complexidade esperada de tempo é $O(1)$ e complexidade de espaço $O(1)$.

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
