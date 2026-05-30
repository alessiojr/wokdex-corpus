# OBI

O principal prêmio da Olimpíada Brasileira de Informática (OBI) é um convite para os cursos de programação na Unicamp. São convidados apenas os competidores que alcançam um número mínimo de pontos somando as duas fases de provas.

A Coordenação da OBI quer que você desenvolva um programa que, dadas as pontuações de cada competidor, conte quantos foram aprovados!
Se a pontuação mínima é 435, um competidor que fez 200 pontos na primeira fase e 235 na segunda será convidado ($200 + 235 = 435 \ge 435$). Mas quem fez 200 e 234, não será convidado.

## Entrada
A primeira linha da entrada contém dois inteiros $N$ e $P$, que são o número total de competidores e a pontuação mínima necessária, respectivamente.
Seguem $N$ linhas. Cada linha trará dois inteiros $X$ e $Y$, indicando a pontuação obtida nas Fases 1 e 2 por aquele aluno específico.

## Saída
Imprima um único inteiro indicando a quantidade de aprovados para a Unicamp.

## Exemplos

| Entrada | Saída |
| :-- | :-- |
| 3 435<br>200 235<br>200 234<br>400 40 | 2 |
