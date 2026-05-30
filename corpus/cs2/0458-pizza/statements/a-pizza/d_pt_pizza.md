# Tutorial: Pizza

## O Problema
A tarefa é encontrar a fatia contígua em um array circular que tenha a maior soma possível (a maior diferença positiva entre cebolas e azeitonas). Se todas as fatias contiverem mais azeitonas do que cebolas (somas negativas), o enunciado nos garante que podemos simplesmente escolher **nenhuma** fatia, obtendo a soma `0`.

## A Estratégia
O problema pede a Subsequência Contígua de Soma Máxima, clássico para o **Algoritmo de Kadane**. A pegadinha é que o array é **circular**! A sublista de soma máxima pode "dar a volta" (começando perto do fim do array e terminando no início).

A solução circular pode ser dividida em dois casos:
1. **A fatia de soma máxima não dá a volta:** Podemos encontrá-la aplicando o Algoritmo de Kadane padrão sobre o vetor. Chamaremos essa resposta de `max_normal`.
2. **A fatia de soma máxima dá a volta:** Se ela passa pelas pontas, significa que ela engloba todo o array *exceto* um pequeno segmento negativo no meio. Para maximizar essa fatia, basta achar a "pior" (de menor soma) fatia contígua no meio usando um Kadane Invertido, e então subtraí-la da soma total de todos os elementos da pizza! Assim: `max_circular = soma_total - min_normal`.

Por fim, a resposta será o máximo entre `max_normal` e `max_circular`. O único **Edge Case** é quando todos os elementos do vetor são negativos. Nesse cenário, o nosso `soma_total` será exatamente igual ao `min_normal`, e subtrair um do outro daria 0, porém, o problema nos permite não escolher nada, que também resulta em 0! Como o `max_normal` pode retornar 0 para listas negativas, estamos seguros.

## Passo a Passo (O(N))
1. Inicialize variáveis para calcular as somas em uma única varredura. Precisaremos da `soma_total`, além das lógicas para `max_normal` e `min_normal`.
2. Para cada elemento no array, atualizamos o Kadane de valor máximo e o Kadane de valor mínimo de forma simétrica.
3. Se o array contiver apenas elementos negativos, a resposta correta é `0`.
4. Caso contrário, comparamos a soma `max_normal` (pedaço do meio) com a soma `max_circular` (pedaços das bordas: `soma_total - min_normal`). A maior soma encontrada será a resposta!

## Exemplos
| Entrada | Saída |
| :-- | :-- |
| `6` <br> `5 -3 -3 2 -1 3` | `9` |
| `7` <br> `1 -2 2 -1 4 1 -5` | `6` |
| `2` <br> `-3 -10` | `0` |
