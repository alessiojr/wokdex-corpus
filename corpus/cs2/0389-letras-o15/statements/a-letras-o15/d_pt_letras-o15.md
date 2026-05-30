# Letras

Uma cadeia de caracteres é uma sequência de letras do alfabeto. Uma cadeia de caracteres crescente é uma sequência de letras onde a próxima letra (da esquerda para a direita) nunca ocorre antes no alfabeto do que a letra anterior. Por exemplo ABBD é crescente, enquanto ABBAD não é crescente. Uma subsequência de uma cadeia de caracteres é uma cadeia de caracteres que pode ser obtida a partir da remoção de zero ou mais caracteres da cadeia de caracteres original. Por exemplo ANNA é uma subsequência de BANANAS. Outro exemplo seria ANNS, que é uma subsequência crescente de BANANAS.

Dada uma cadeia de caracteres S, escreva um programa para determinar o tamanho da maior subsequência de S que é uma cadeia de caracteres crescente.

## Tutorial Passo a Passo

O problema pede para encontrarmos a Maior Subsequência "Crescente" (na verdade, não-decrescente, pois permite letras repetidas). Esse é um problema clássico de Programação Dinâmica chamado **LIS** (Longest Increasing Subsequence). 

A abordagem de força bruta ou programação dinâmica simples em $O(N^2)$ funciona bem para cadeias curtas, mas como $N$ pode chegar a $300.000$, precisaremos de uma abordagem ótima em $O(N \log N)$.

**Passo 1: Entendendo o LIS em O(N log N)**
A ideia principal é manter um vetor auxiliar, digamos `pilhas`, que representará os finais das melhores subsequências crescentes encontradas até o momento. O tamanho desse vetor `pilhas` no final do processamento será exatamente o tamanho da maior subsequência crescente.

**Passo 2: Construindo o vetor auxiliar**
Iteramos por cada caractere `c` da cadeia `S`, da esquerda para a direita. Para cada `c`:
1. Procuramos no vetor `pilhas` qual é o primeiro elemento que é **estritamente maior** que `c`.
2. Como o vetor `pilhas` estará sempre ordenado de forma não-decrescente, podemos usar **Busca Binária** para encontrar essa posição rapidamente. (Em linguagens como C++, usamos a função `upper_bound`).
3. Se o caractere `c` for maior ou igual a todos os elementos de `pilhas` (ou se o vetor estiver vazio), nós o adicionamos no final do vetor (isso aumenta o tamanho da subsequência).
4. Caso contrário, substituímos o elemento encontrado pelo caractere `c`. Isso não muda o tamanho máximo encontrado até agora, mas melhora o "potencial" da subsequência, pois terminar com uma letra "menor" facilita a adição de novas letras futuras.

**Passo 3: Exemplo Prático**
Dado `S = BANANAS`
1. `B` -> `pilhas = [B]`
2. `A` -> Primeiro maior que `A` é `B`. Substitui `B`. `pilhas = [A]`
3. `N` -> Nenhum maior que `N`. Adiciona ao final. `pilhas = [A, N]`
4. `A` -> Primeiro maior que `A` é `N`. Substitui `N`. `pilhas = [A, A]`
5. `N` -> Nenhum maior que `N`. Adiciona ao final. `pilhas = [A, A, N]`
6. `A` -> Primeiro maior que `A` é `N`. Substitui `N`. `pilhas = [A, A, A]`
7. `S` -> Nenhum maior que `S`. Adiciona ao final. `pilhas = [A, A, A, S]`

O tamanho final do vetor `pilhas` é 4. Essa é a resposta!

**Passo 4: Implementação**
A lógica é tão simples quanto iterar sobre a string, chamar `upper_bound` e fazer a substituição ou inserção (via `push_back`). No fim, basta imprimir o tamanho do vetor auxiliar. Essa solução executará no tempo $O(N \log N)$ utilizando uma memória adicional de $O(N)$, o que resolve o problema confortavelmente dentro dos limites.

## Entrada

A entrada consiste em uma única linha, contendo uma cadeia de caracteres S.

## Saída

Seu programa deve produzir uma única linha, contendo um único inteiro, o tamanho da maior subsequência de S que é uma cadeia de caracteres crescente.

## Restrições

- A cadeia de caracteres de entrada contém letras maiúsculas do alfabeto, de A até Z.
- 1 ≤ comprimento(S) ≤ 3 × 10^5.

## Informações sobre a pontuação

- Em um conjunto de casos de teste valendo 20 pontos: comprimento(S) ≤ 20.
- Em um conjunto de casos de teste valendo 30 pontos: comprimento(S) ≤ 3000.

## Exemplos

| Entrada | Saída |
| :-- | :-- |
| BANANAS | 4 |

| Entrada | Saída |
| :-- | :-- |
| AAXBBXZZX | 7 |

| Entrada | Saída |
| :-- | :-- |
| AAA | 3 |
