# Cara ou Coroa — Tutorial Passo a Passo

João e Maria possuem um registro enorme das partidas anuais de Cara ou Coroa, datando da época do colégio. Sabendo que Maria sempre aposta na cara (0) e João aposta na coroa (1), precisamos escrever um programa tático que consiga não só varrer esse montante histórico rapidamente, como contar detalhadamente as vitórias agrupadas de cada um e imprimir esse placar.

## Estratégia de Processamento

A execução dessa contagem é um algoritmo canônico estruturado em complexidade $O(N)$ usando **Soma Simples Distribuída**. Você não precisa ordenar ou procurar padrões, basta escanear e incrementar sua contagem. Não faça alocações excessivas e nem instancie arrays bidimensionais. Cuidado para não reter valores da rodada anterior (reinicie os contadores)!

## Dicas e Lógica Central

1. **Sentinela do Main-Loop**:
Como você irá processar um número livre de rodadas que só cessa quando $N=0$, você precisará iniciar com um *Loop Infinito* (ex: `while True`). Logo na primeira instrução, capture o valor de `N`. Caso detecte `N == 0`, ative uma ruptura (`break`) encerrando imediatamente todo o processamento.

2. **Captura em Massa**:
Após ler a primeira linha com o total da rodada (`N`), efetue a varredura da segunda linha. Dependendo de sua linguagem, capture toda a string fatiando os espaços e convertendo para inteiros num bloco (como `list(map(int, input().split()))` no Python). 

3. **Loop Interno (Contabilização)**:
Declare duas variáveis logo após o sentinela: `mary = 0` e `john = 0`.
Atravesse a sequência inteira dos registros num `For`:
 - Caso o registro lido assuma o valor `0`, some $+1$ na variável `mary`.
 - Caso contrário (se o valor for `1`), some $+1$ na variável `john`.

4. **Saída Formatada**:
Emito o relatório ao final de cada laço usando concatenação rígida idêntica à solicitada sem pontuação terminal:
`Mary won X times and John won Y times`

## Entrada

A entrada contém vários casos de teste. A primeira linha de um caso de teste contém um único inteiro $N$ indicando o número de vezes jogadas ($1 \leq N \leq 10000$). A linha seguinte contém $N$ inteiros $R_i$, separados por um espaço, descrevendo a lista de resultados. Se $R_i = 0$ então Maria venceu, se $R_i = 1$ então João venceu. O fim da entrada é indicado por $N = 0$.

## Saída

Para cada caso de teste na entrada, seu programa deverá escrever uma linha contendo a sentença “Mary won X times and John won Y times”, onde $X$ e $Y$ são calculados via programação.

## Exemplos

| Entrada | Saída |
| :-- | :-- |
| 5 | Mary won 3 times and John won 2 times |
| 0 0 1 0 1 | |

| Entrada | Saída |
| :-- | :-- |
| 6 | Mary won 5 times and John won 1 times |
| 0 0 0 0 0 1 | |
| 0 | |
