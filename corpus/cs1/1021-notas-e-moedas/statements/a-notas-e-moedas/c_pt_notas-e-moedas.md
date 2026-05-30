# Notas e Moedas — Estratégia de Solução

Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01.

### Dica Estratégica
Este problema pode ser resolvido de forma eficiente utilizando um **algoritmo guloso**. Como as denominações de notas e moedas no sistema monetário são canônicas, escolher sempre a maior denominação disponível garantirá o número mínimo de unidades.

> [!TIP]
> **Complexidade**: A complexidade de tempo é **$O(1)$**, pois o número de cédulas e moedas disponíveis é fixo, independentemente do valor de entrada $N$.
>
> **Atenção à Precisão**: O uso direto de tipos `double` ou `float` pode causar erros de arredondamento inerentes à representação binária. Considere converter o valor total para centavos (multiplicando por 100 e arredondando para o inteiro mais próximo) para realizar os cálculos com números inteiros.

### Entrada
O arquivo de entrada contém um valor de ponto flutuante $N$ ($0 \le N \le 1000000.00$).

### Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme o exemplo fornecido.

| Entrada |                  Saída |
|--------:|-----------------------:|
|  576.73 |                 NOTAS: |
|         | 5 nota(s) de R$ 100.00 |
|         |  1 nota(s) de R$ 50.00 |
|         |  1 nota(s) de R$ 20.00 |
|         |  0 nota(s) de R$ 10.00 |
|         |   1 nota(s) de R$ 5.00 |
|         |   0 nota(s) de R$ 2.00 |
|         |                MOEDAS: |
|         |  1 moeda(s) de R$ 1.00 |
|         |  1 moeda(s) de R$ 0.50 |
|         |  0 moeda(s) de R$ 0.25 |
|         |  2 moeda(s) de R$ 0.10 |
|         |  0 moeda(s) de R$ 0.05 |
|         |  3 moeda(s) de R$ 0.01 |
