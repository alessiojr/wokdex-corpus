# O Código das Nebulosas Gêmeas

Na vastidão da Galáxia de WOK, a frota de pesquisa interestelar coleta amostras de poeira cósmica. Cada amostra emite uma assinatura espectral única, representada por um número de identificação de cor. 

O comandante supremo precisa saber quantos pares de amostras (i, j) compartilham a exata mesma assinatura espectral (cor i = cor j), respeitando a ordem de coleta (i < j). Sua missão é programar o computador central da nave para contabilizar esse número de pares idênticos em toda a base de dados.

## Entrada

A primeira linha contém um inteiro N (1 <= N <= 10^5), o número total de amostras de poeira cósmica coletadas.
A segunda linha contém N inteiros C1, C2, ..., CN (1 <= Ci <= 10^9), representando a assinatura espectral de cada amostra sequencial.

## Saída

Imprima um único inteiro, o número total de pares de amostras cósmicas que possuem a mesma assinatura espectral.

## Restrições

*   1 <= N <= 10^5
*   1 <= Ci <= 10^9

## Exemplos

### Exemplo 1

| Entrada       | Saída |
| :------------ | :---- |
| 5             | 2     |
| 1 2 1 3 2     |       |

### Exemplo 2

| Entrada   | Saída |
| :-------- | :---- |
| 4         | 6     |
| 1 1 1 1   |       |
