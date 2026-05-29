# Alarme Despertador

Daniela é enfermeira em um grande hospital, e tem os horários de trabalho muito variáveis. Para piorar, ela tem sono pesado, e uma grande dificuldade para acordar com relógios despertadores.

![Daniela acordando](daniela.png "Daniela acordando"){width=200px align=right}

Recentemente ela ganhou de presente um relógio digital, com alarme com vários tons, e tem esperança que isso resolva o seu problema. No entanto, ela anda muito cansada e quer aproveitar cada momento de descanso. Por isso, carrega seu relógio digital despertador para todos os lugares, e sempre que tem um tempo de descanso procura dormir, programando o alarme despertador para a próxima ocorrência do horário em que tem que acordar. O problema é que, como está muito cansada, ela tem dificuldade para calcular o tempo de descanso que teria com uma certa programação do alarme.

Você deve escrever um programa que, dada a hora e minuto atuais, e a hora e minuto para os quais o alarme despertador foi programado, calcule o tempo de sono que ela terá, em minutos.

### Entrada

A entrada contém vários casos de teste. Cada caso de teste é descrito em uma linha e contém quatro números inteiros $H_1$, $M_1$, $H_2$ e $M_2$, com $H_1:M_1$ representando a hora e minuto atuais, e $H_2:M_2$ representando a hora e minuto para os quais o alarme despertador foi programado (0 $\leq$ $H_1$ $\leq$ 23, 0 $\leq$ $M_1$ $\leq$ 59, 0 $\leq$ $H_2$ $\leq$ 23, 0 $\leq$ $M_2$ $\leq$ 59).

O final da entrada é indicado por uma linha que contém apenas quatro zeros, separados por espaços em branco. O seu programa não deve processar esta linha.

### Saída

Para cada caso de teste da entrada, seu programa deve imprimir uma linha, cada uma contendo um número inteiro, indicando o número de minutos que Daniela tem para dormir.

### Observações

<br>

| Entrada | Saída |
|:--------|:------|
| 1 5 3 5 | 120   |

| Entrada     | Saída |
|:------------|:------|
| 21 33 21 10 | 1417  |
| 23 59 0 34  | 35    |
| 0 0 0 0     |       |
