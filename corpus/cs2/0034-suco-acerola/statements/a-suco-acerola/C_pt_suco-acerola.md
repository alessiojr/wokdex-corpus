# Distribuição de Suco na Nave

Na estação espacial WOK-42, a tripulação cultiva **Acerola Cósmica** em estufas pressurizadas. Após cada colheita, as frutas são processadas para produzir suco, que é dividido igualmente entre os tripulantes.

Sabe-se que:

*   Cada unidade de fruta produz exatamente **50 ml** de suco.
*   O suco total é dividido igualmente entre todos os tripulantes.
*   O resultado deve ser exibido **em litros**.

Uma dica: o volume total de suco em mililitros é $F \times 50$. Para obter o volume por tripulante em litros, basta **dividir o total pelo número de tripulantes** e depois **converter de mililitros para litros** (dividindo por 1000). Ou seja, a fórmula pode ser simplificada para:

$$\text{resultado} = \frac{F \times 50}{N \times 1000}$$

Lembre-se de usar **divisão real** (ponto flutuante) e formatar a saída com duas casas decimais.

## Entrada

A entrada contém vários casos de teste, cada um em uma única linha.

Cada linha contém dois inteiros $N$ e $F$ ($1 \leq N \leq 10^3$, $1 \leq F \leq 10^3$): o número de tripulantes e a quantidade de frutas.

O final da entrada é indicado por uma linha contendo `0 0`.

## Saída

Para cada caso de teste, imprima uma linha contendo um número real com exatamente **duas casas decimais**.

## Exemplos

| Entrada | Saída |
|:--- |:--- |
| 1 1 | 0.05 |
| 5 431 | 4.31 |
| 101 330 | 0.16 |
| 0 0 | |
