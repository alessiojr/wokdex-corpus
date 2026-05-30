# 0275 - DNA (Tutorial)

**Passo a Passo**

1. Este é um problema de Programação Dinâmica em duas dimensões (similar ao clássico Longest Common Subsequence - LCS).
2. Para resolver eficientemente em $O(N^2)$, criaremos três matrizes (ou vetores otimizados) de tamanho $(N+1) \times (M+1)$:
   - `match[i][j]`: guarda o comprimento exato do sufixo em comum terminando no índice $i$ da primeira string e $j$ da segunda.
   - `dp[i][j]`: o tamanho da maior subsequência válida encontrada processando os prefixos de tamanho $i$ e $j$.
   - `f[i][j]`: guarda a maior subsequência válida assumindo que ela **obrigatoriamente** usa o caractere na posição $i$ e $j$ como o fim de um bloco válido (ou seja, foi estendido de um bloco existente ou é o caractere $K$ de um novo bloco).

3. Laço principal para $i$ de $1$ a $N$ e $j$ de $1$ a $M$:
   - Se os caracteres forem iguais: `match[i][j] = match[i-1][j-1] + 1`
   - O valor base de `dp[i][j]` herda do melhor caso ignorando o caractere atual: `max(dp[i-1][j], dp[i][j-1])`.
   - Se `match[i][j] >= K`:
     - Podemos formar um bloco de tamanho $K$: o valor seria `dp[i-K][j-K] + K`.
     - Podemos estender um bloco que já era válido no caractere anterior: `f[i-1][j-1] + 1`.
     - Assim, `f[i][j] = max(dp[i-K][j-K] + K, f[i-1][j-1] + 1)`.
     - Atualize o `dp[i][j]` como o máximo entre seu valor atual e `f[i][j]`.

**Explicação Lógica**
Quando `match[i][j] >= K`, temos certeza que os últimos $K$ caracteres casam perfeitamente. O valor `dp[i-K][j-K] + K` considera que pegamos um bloco exatamente de tamanho $K$ e somamos ao que já tínhamos montado antes deste bloco. O valor `f[i-1][j-1] + 1` apenas incrementa a resposta caso o bloco continue crescendo além do tamanho $K$. Essa fórmula resolve o problema cobrindo todos os tamanhos de blocos sem precisar de um laço extra.

**Exemplo**
No caso com $K=3$ e as strings `xxxx` e `xxxx`.
- Na posição 3, `match` é 3. `f` recebe `dp[0][0] + 3 = 3`. Então `dp = 3`.
- Na posição 4, `match` é 4. `f` recebe `max(dp[1][1] + 3, f[3][3] + 1) = max(0+3, 3+1) = 4`. Então `dp = 4`.
Isso escala perfeitamente e encontra o máximo sem complexidades extras.
