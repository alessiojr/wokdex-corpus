# 0275 - DNA (Educational)

### Estratégia de Solução

Este problema é uma variação clássica do problema da Maior Subsequência Comum (LCS). A diferença principal é que cada caractere correspondente deve fazer parte de um bloco consecutivo de pelo menos $K$ caracteres. Isso sugere o uso de Programação Dinâmica (DP).

Em vez de apenas manter o comprimento da subsequência comum, precisamos controlar se o trecho atual em correspondência atinge ou supera o tamanho $K$. 
Uma matriz `dp[i][j]` armazenará o maior comprimento válido para os prefixos de tamanho `i` e `j`. Além disso, precisaremos calcular o tamanho do sufixo comum exato terminando nessas posições (uma matriz `match[i][j]`).

### Dicas de Implementação

- `match[i][j]` será `match[i-1][j-1] + 1` se os caracteres forem iguais, senão `0`.
- Se `match[i][j] >= K`, significa que podemos formar um bloco válido. Podemos então transitar do estado `dp[i-K][j-K] + K` (iniciando o bloco exato de tamanho K) ou estender um bloco já válido que termina em `i-1` e `j-1`.
- Para isso, uma matriz secundária `f[i][j]` para armazenar o valor máximo assumindo que o par atual é o fim de um bloco válido torna a solução elegante em `O(N^2)`.
