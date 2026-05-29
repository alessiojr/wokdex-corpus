# Alarme Despertador

Daniela é enfermeira em um grande hospital, e tem os horários de trabalho muito variáveis. Para piorar, ela tem sono pesado, e uma grande dificuldade para acordar com relógios despertadores.

![Daniela acordando](daniela.png "Daniela acordando"){width=200px align=right}

Recentemente ela ganhou de presente um relógio digital, com alarme com vários tons, e tem esperança que isso resolva o seu problema. No entanto, ela anda muito cansada e quer aproveitar cada momento de descanso. Por isso, carrega seu relógio digital despertador para todos os lugares, e sempre que tem um tempo de descanso procura dormir, programando o alarme despertador para a hora em que tem que acordar. O problema é que, como está muito cansada, ela tem dificuldade para calcular o tempo de descanso que teria com uma certa programação do alarme.

Você deve escrever um programa que, dada a hora e minuto atuais, e a hora e minuto para os quais o alarme despertador foi programado, calcule o tempo de sono que ela terá, em minutos.

### Dica D (Tutorial Passo-a-Passo)

Neste problema, o objetivo é descobrir quanto tempo se passou entre dois instantes no relógio digital informados, podendo ser no mesmo dia ou invadir o dia seguinte. A modelagem mais prática não lida com horas e minutos separados, mas unifica o horário daquele mesmo dia convertendo tudo para "quantos minutos se passaram desde o início do dia" (00:00). 

**Passo a passo da implementação:**

1. **Laço Principal**: Crie um loop de leitura de múltiplos casos (por exemplo, `while True:` em Python, ou `while (cin >> h1 >> m1 >> h2 >> m2)` em C++).
2. **Condição de Parada**: Imediatamente após ler os 4 valores `h1, m1, h2, m2`, verifique se todos são zero: `if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0`. Em caso positivo, quebre o laço de repetição (`break`).
3. **Conversão para Minutos Absolutos**: 
   Converta a hora atual e do alarme num intervalo de minutos transcorridos desde a zero-hora.
   - `instante_atual = (h1 * 60) + m1`
   - `instante_alarme = (h2 * 60) + m2`
4. **Subtração Simples**: Encontre a diferença total de duração: `tempo_sono = instante_alarme - instante_atual`.
5. **Ajuste de Dia Seguinte**: E se "instante do alarme" for menor ou igual ao "instante atual"? Isso significa que o alarme tocará apenas na próxima ocorrência daquele horário (no dia seguinte). Para corrigir o tempo de sono, adicione 1440 minutos (24 horas) ao resultado: `se tempo_sono <= 0, então tempo_sono = tempo_sono + 1440`.
6. **Saída**: Imprima a variável contendo o `tempo_sono` na tela, com a respectiva quebra de linha exigida.

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
