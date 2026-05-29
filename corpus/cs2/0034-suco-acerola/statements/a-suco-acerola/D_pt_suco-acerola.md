# Manual de Distribuição de Suco

Na estação espacial WOK-42, a tripulação colheu frutas e precisa dividir o suco igualmente. Cada fruta produz **50 ml** de suco. O resultado deve ser exibido em **litros** com **duas casas decimais**.

Para resolver este problema, siga o passo a passo:

1.  Leia os dois valores inteiros $N$ (tripulantes) e $F$ (frutas) em um laço que se repete enquanto ambos forem diferentes de zero.
2.  Calcule o volume total de suco em mililitros: `total_ml = F * 50`.
3.  Divida o total pelo número de tripulantes: `por_pessoa_ml = total_ml / N`.
4.  Converta de mililitros para litros: `por_pessoa_litros = por_pessoa_ml / 1000`.
    *   Você pode combinar os passos 2, 3 e 4 em uma única expressão: `resultado = (F * 50.0) / (N * 1000.0)`.
5.  Imprima o resultado com exatamente **duas casas decimais**. Em C, use `printf("%.2f\n", resultado)`. Em Python, use `print(f"{resultado:.2f}")`.
6.  Repita até ler `0 0`.

## Entrada

A entrada contém vários casos de teste, cada um em uma única linha.

Cada linha contém dois inteiros $N$ e $F$ ($1 \leq N \leq 10^3$, $1 \leq F \leq 10^3$).

O final da entrada é indicado por `0 0`.

## Saída

Para cada caso de teste, imprima uma linha com o volume em litros, com duas casas decimais.

## Exemplos

| Entrada | Saída |
|:--- |:--- |
| 1 1 | 0.05 |
| 5 431 | 4.31 |
| 101 330 | 0.16 |
| 0 0 | |
