# Cara ou Coroa — Estratégia de Solução

João e Maria jogam Cara ou Coroa para decidir quem escolhe a brincadeira do dia. Maria sempre escolhe cara (representado por `0`) e João sempre escolhe coroa (representado por `1`). Seu objetivo é contar as vitórias de cada um dada uma lista de resultados.

### Dica Estratégica
Como a entrada contém múltiplos casos de teste, você precisará de uma estrutura de repetição que continue lendo enquanto o valor de $N$ não for zero.

> [!TIP]
> **Complexidade**: A complexidade de tempo ideal é **$O(N)$** para cada caso de teste, o que totaliza **$O(T \times N)$** onde $T$ é o número de casos. Basta percorrer a lista uma única vez incrementando dois contadores independentes.
>
> **Lógica de Contagem**: Utilize variáveis para armazenar o total de Mary e John. Se o valor lido for `0`, incremente o contador da Mary; se for `1`, incremente o do John.

### Entrada
Vários casos de teste. Cada um começa com $N$ ($1 \le N \le 10000$), seguido por $N$ valores (0 ou 1). A entrada termina com $N=0$.

### Saída
Para cada caso, imprima: `Mary won X times and John won Y times`.

| Entrada | Saída |
| :-- | :-- |
| 5 | Mary won 3 times and John won 2 times |
| 0 0 1 0 1 | |
