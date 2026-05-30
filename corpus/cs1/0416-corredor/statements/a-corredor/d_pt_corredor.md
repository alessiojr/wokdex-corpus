# Corredor

Bruninho está programando um personagem virtual para o próximo desafio de um jogo de aventura em que, numa das fases, o personagem tem que entrar em um corredor, percorrer algumas salas e depois sair do corredor. Ele pode entrar apenas uma vez, e passar por cada sala apenas uma vez. Todas as salas possuem uma porta de entrada e uma de saída, como ilustra a parte (a) da figura abaixo. Ao passar por uma sala o jogador ganha um certo número de vidas (que pode ser negativo!). O objetivo é passar pelo corredor coletando a maior quantidade possível de vidas! Por sorte, sempre existe ao menos uma sala onde se ganha um número positivo de vidas.

No exemplo acima, o personagem de Bruninho pode ganhar, no máximo, 12 vidas, por exemplo, entrando pela sala 2 e saindo pela sala 4, como mostrado na parte (b) da figura. Nesta tarefa, você deve escrever um programa que, dados os números de vidas correspondentes a cada sala do corredor, calcule a quantidade máxima de vidas que será possível ganhar.

> **Tutorial:** Para maximizar as vidas de Bruninho, precisamos encontrar o trecho contíguo dentro do corredor com a maior soma possível de vidas. Devido à quantidade de salas ($N \le 50000$), precisamos de um algoritmo linear, $O(N)$.
>
> A solução ideal é usar o **Algoritmo de Kadane**. O raciocínio passo a passo é o seguinte:
> 1. Crie duas variáveis: `soma_atual` (que armazena a soma das salas que estamos percorrendo) e `soma_maxima` (que guardará a melhor soma encontrada).
> 2. Percorra as salas uma por uma, da esquerda para a direita.
> 3. Ao entrar em uma sala, some o seu valor de vida à `soma_atual`.
> 4. Se a `soma_atual` ficar negativa, significa que todo o trecho percorrido até agora nos deu mais prejuízo do que lucro. Como podemos escolher começar de qualquer sala, a melhor atitude é **zerar a `soma_atual`** e tentar começar um novo trecho a partir da próxima sala.
> 5. A cada passo, atualize a `soma_maxima` com o maior valor entre ela mesma e a `soma_atual`.
> 6. Ao terminar de percorrer todas as salas, a `soma_maxima` terá a resposta do problema.

## Entrada

A entrada é composta por duas linhas. A primeira linha contém um inteiro N, o número de salas no corredor. A segunda linha contém N números inteiros, positivos ou negativos, indicando a quantidade de vidas que se ganha em cada sala.

## Saída

Seu programa deve imprimir uma linha, com o número máximo de vidas que é possível ganhar.

## Observações

**Restrições:**
- $1 \leq N \leq 50000$; e o número de vidas nas salas está entre -100 e 100.

**Informações sobre a Pontuação:**
- Em um conjunto de casos de teste totalizando 30 pontos, $N \leq 1000$.

## Exemplos

| Entrada | Saída |
| :-- | :-- |
| 7 | 12 |
| -2 5 -1 8 -11 7 3 | |

| Entrada | Saída |
| :-- | :-- |
| 10 | 105 |
| 50 42 -35 2 -60 5 30 -1 40 31 | |
