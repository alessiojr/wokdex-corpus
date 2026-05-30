# Prefixa, Infixa e Posfixa — Tutorial

## Como Resolver Passo a Passo

Você não precisa construir os nós em memória (com ponteiros `left` e `right`). Você pode gerar a string posfixa diretamente manipulando as strings!

### Passo 1: A Lógica da Raiz
Dado um percurso prefixo, por exemplo `ABCDEF`, o primeiro caractere `A` é obrigatoriamente a Raiz do problema inteiro. 
Dado o infixo correspondente `CBAEDF`, sabemos que tudo à esquerda do `A` é a sub-árvore esquerda (neste caso `CB`), e tudo à direita é a sub-árvore direita (`EDF`).

### Passo 2: A Função Recursiva

Crie uma função `posfixa(S_pre, S_in)`:

**Condição de Parada (Caso Base):**
Se as strings estiverem vazias, retorne uma string vazia `""`.

**Processamento:**
1. A raiz é `raiz = S_pre[0]`.
2. O índice da raiz em `S_in` é `pos = S_in.find(raiz)`. (Em C++, use `.find()`, em Java `.indexOf()`, em Python `.index()`).
3. Com o índice `pos`, podemos "fatiar" as strings:
   - Infixa Esquerda: `S_in[0 ... pos-1]` (tamanho `pos`)
   - Infixa Direita: `S_in[pos+1 ... fim]`
   - Prefixa Esquerda: `S_pre[1 ... pos]` (pega logo após a raiz, o mesmo tamanho `pos` caracteres)
   - Prefixa Direita: `S_pre[pos+1 ... fim]`
4. O resultado posfixo é construído chamando a função para o filho da esquerda, depois filho da direita, e colocando a raiz no final:
   `return posfixa(PrefixaEsq, InfixaEsq) + posfixa(PrefixaDir, InfixaDir) + raiz;`

### Passo 3: Executando no Código
Você fará a leitura da primeira linha contendo o número $C$.
Depois, fará um laço `C` vezes lendo as três variáveis: `N`, `S1` e `S2`. (Note que o `N` aqui é opcional, pois o tamanho das strings nos basta, mas é bom lê-lo para não perder sincronia do Scanner).

Chame `print( posfixa(S1, S2) )`!

**Dica de Python**: Fatiamento (slicing) é nativo e elegante.
`S_in[:pos]` é o esquerdo, `S_in[pos+1:]` é o direito.
`S_pre[1:pos+1]` é o esquerdo, `S_pre[pos+1:]` é o direito.
