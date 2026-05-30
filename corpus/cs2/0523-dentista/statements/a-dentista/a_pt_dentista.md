# Dentista

O dentista que atende em uma pequena cidade tem apenas um consultório. Ele atende no máximo um paciente por vez e as consultas sempre iniciam e terminam no mesmo dia. Ele já tem marcadas as consultas para o dia de hoje. No entanto, por um erro de sua secretária, algumas consultas podem estar marcadas para horários que se sobrepõem.

O dentista deseja atender o maior número possível de pacientes e, para isso, ele pode desmarcar algumas consultas, desde que as consultas restantes não se sobreponham.

## Entrada

A primeira linha contém um inteiro $N$ ($1 \le N \le 10.000$) que indica o número de consultas que a secretária marcou. Cada uma das $N$ linhas seguintes contém um par de inteiros $X$ e $Y$ separados por um espaço em branco ($0 \le X < Y \le 1.000.000$) que representam, respectivamente, o horário de início e de término da consulta. Considere que se uma consulta inicia no exato instante em que outra termina não há sobreposição. Os horários de início são fornecidos em ordem, podendo haver mais de uma consulta que inicie no mesmo horário.

## Saída

Seu programa deve imprimir uma única linha, contendo um inteiro que representa a quantidade máxima de consultas que podem ser atendidas sem que haja qualquer sobreposição.

## Informações sobre a pontuação

- Em um conjunto de casos de teste que totaliza 40 pontos, ($0 \le X < Y \le 1.000$).

| Entrada | Saída |
|--------:|------:|
|       3 |     2 |
|  10 100 |       |
|  40 130 |       |
| 120 200 |       |

| Entrada | Saída |
|--------:|------:|
|       4 |     4 |
|   10 20 |       |
|   20 30 |       |
|   30 40 |       |
|   40 50 |       |

| Entrada | Saída |
|--------:|------:|
|       5 |     3 |
|   10 30 |       |
|   20 40 |       |
|   30 60 |       |
|   40 80 |       |
|  60 100 |       |
