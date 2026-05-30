# Pizza

Rodrigo pediu uma pizza de mussarela de N fatias, uma parte somente com cebola e o resto somente com azeitonas. Entretanto, ao receber a pizza em casa, notou que o motoqueiro que a entregou não foi cuidadoso o suficiente, pois tanto as tiras de cebola quanto as azeitonas estavam espalhadas por toda a pizza. Para piorar, como a pizza era de mussarela, as tiras de cebola e as azeitonas estavam grudadas na pizza.

Como gosta mais de cebola do que de azeitona, Rodrigo deseja pegar fatias consecutivas da pizza de tal forma que estas contenham a maior diferença possível entre tiras de cebola e azeitonas. Para isso, ele contou quantas tiras e quantas azeitonas tinham em cada fatia e subtraiu os dois valores, nessa ordem. Assim, sempre que uma fatia contiver mais cebolas que azeitonas, ela recebe um número positivo, e caso contrário, um número negativo. Uma fatia cujo número seja zero contém o mesmo número de tiras de cebolas e azeitonas.

Por exemplo, supondo que as fatias contenham as seguintes diferenças: 5, -3, -3, 2, -1, 3, pode-se pegar uma fatia consecutiva com 9 cebolas a mais que azeitonas, utilizando as fatias com as diferenças 2, -1, 3, 5 (lembre-se de que estamos tratando de um círculo e, portanto, a fatia com diferença 5 é vizinha da fatia com diferença 3 e vice-versa).

Como Rodrigo não entende de programação, ele resolveu contar com seus serviços.

**OBS:** repare que é melhor não escolher nenhuma fatia caso somente seja possível escolher fatias consecutivas com mais azeitonas que cebolas.

## Dicas do Mestre

Para resolver esse desafio com eficiência máxima em tempo $O(N)$, você precisará aplicar e adaptar o clássico **Algoritmo de Kadane** (que encontra a subsequência contígua de soma máxima).

A "pegadinha" aqui é que o array é circular: a maior fatia pode dar a volta na pizza! Para resolver isso de forma inteligente, considere duas possibilidades:
1. A fatia ótima está inteiramente no "meio" do array (resolvido pelo Kadane normal).
2. A fatia ótima cruza a borda (começa no fim e termina no início). Nesse caso, a fatia ótima é, na verdade, a "pizza inteira" MENOS a "pior fatia contígua possível" no meio. Como você encontra essa "pior fatia"? Usando um Kadane invertido que busca a menor soma contígua!

## Entrada

A entrada contém um único conjunto de testes, que deve ser lido do dispositivo de entrada padrão (normalmente o teclado). A primeira linha da entrada contém um inteiro $N$ que indica o número de fatias de pizza ($1 \leq N \leq 100.000$). A segunda linha contém $N$ inteiros $K$ ($-100 \leq K \leq 100$) separados por um espaço em branco com as diferenças entre as quantidades de cebolas e de azeitonas.

## Saída

Seu programa deve imprimir, na saída padrão, uma única linha, contendo a maior quantidade de cebolas que Rodrigo pode comer a mais do que azeitonas.

| Entrada | Saída |
| :-- | :-- |
| 6 | 9 |
| 5 -3 -3 2 -1 3 | |

| Entrada | Saída |
| :-- | :-- |
| 7 | 6 |
| 1 -2 2 -1 4 1 -5 | |

| Entrada | Saída |
| :-- | :-- |
| 2 | 0 |
| -3 -10 | |
