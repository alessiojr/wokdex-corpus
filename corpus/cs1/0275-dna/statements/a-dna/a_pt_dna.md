# DNA

O DNA é o repositório de informações genéticas de todos os seres vivos e de alguns vírus. Ele é composto por quatro bases nitrogenadas: Adenina (A), Timina (T), Guanina (G) e Citosina (C). Uma cadeia de DNA pode ser representada como uma sequência dessas letras.

Seu desafio é encontrar a subsequência comum mais longa entre duas cadeias de DNA fornecidas.

## Entrada

A entrada consiste de duas linhas. Cada linha contém uma string representando uma cadeia de DNA. As cadeias serão compostas apenas pelos caracteres 'A', 'T', 'G', 'C'.
O comprimento de cada cadeia será entre 1 e 1000 caracteres.

## Saída

A saída deve ser uma única linha contendo a subsequência comum mais longa. Se houver múltiplas subsequências com o mesmo comprimento máximo, qualquer uma delas será aceita.

## Restrições

*   Tempo Limite: 1 segundo
*   Memória Limite: 256 MB
*   Comprimento da cadeia N: 1 <= N <= 1000

## Exemplos

| Entrada   | Saída |
| :-- | :-- |
| AGGTAB    | GTAB  |
| GXTXAYB   |       |

| Entrada | Saída |
| :-- | :-- |
| ABCD    | ACD   |
| ACDF    |       |

| Entrada | Saída |
| :-- | :-- |
| ABC     |       |
| XYZ     |       |
