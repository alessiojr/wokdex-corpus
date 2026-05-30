# Labirinto

Sua missão, se você decidir aceitá-la, é criar um programa de desenho de labirinto. Um labirinto será composto de caracteres alfabéticos (A-Z), asterisco (`*`) e espaços.

## Entrada

Seu programa irá receber as informações para construir os labirintos do arquivo de entrada. Cada linha contém os caracteres que o programa deverá interpretar para desenhar um labirinto completo.

Uma linha de labirinto é descrita por uma série de números seguidos de um caractere. O número que precede o caractere informa quantas vezes ele deve ser repetido. Se houver vários números consecutivos antes de um caractere, a quantidade de repetições é a **soma** desses números.

A letra minúscula `b` é usada para representar um **espaço**. O caractere de exclamação (`!`) indica uma **única** quebra de linha dentro do labirinto (independentemente de haver números antes dele).

Cada linha da entrada representa um labirinto diferente. O arquivo de entrada termina com o fim de arquivo (EOF).

## Saída

Para cada labirinto da entrada, o programa deve desenhar o labirinto correspondente. Após o desenho de cada labirinto completo, deve ser impressa uma linha contendo exatamente **13 hifens** (`-------------`).

## Exemplos

|         Entrada | Saída             |
|----------------:|:------------------|
| 11X21b1X!4X1b1X | XX   X            |
|        dddddddd | XXXX X            |
|        dd2ddddd | ----------------- |
|                 | Entrada errada    |
|                 | ----------------- |
|                 | dd                |
|                 | ----------------- |

<br>

|                                                          Entrada | Saída         |
|-----------------------------------------------------------------:|:--------------|
| 1T1b5T!1T2b1T1b2T!1T1b1T2b2T!1T3b1T1b1T!3T3b1T!1T3b1T1b1T!5T1*1T | T TTTTT       |
|                                                                  | T  T TT       |
|                                                                  | T T  TT       |
|                                                                  | T   T T       |
|                                                                  | TTT   T       |
|                                                                  | T   T T       |
|                                                                  | TTTTT*T       |
|                                                                  | ------------- |
