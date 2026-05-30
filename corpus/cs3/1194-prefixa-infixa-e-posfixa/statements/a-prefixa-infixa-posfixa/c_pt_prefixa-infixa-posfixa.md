# Prefixa, Infixa e Posfixa

## Estratégia de Solução

O problema pede a reconstrução de uma árvore binária dados os seus percursos \textit{Prefixo} (Raiz-Esq-Dir) e \textit{Infixo} (Esq-Raiz-Dir), para então obtermos o percurso \textit{Posfixo} (Esq-Dir-Raiz). 

Podemos resolver isso de forma elegante através de **recursão**! O segredo está nas propriedades de cada string de percurso:
1. O **primeiro caractere** do percurso prefixo é *sempre* a Raiz daquela sub-árvore.
2. Se você encontrar essa Raiz dentro da string do percurso infixo, ela divide o infixo em duas partes: a metade esquerda (\textit{left}) contém exclusivamente os nós da sub-árvore esquerda, e a metade direita (\textit{right}) contém exclusivamente os nós da sub-árvore direita.

### O Algoritmo
1. A função recursiva receberá as strings `pre` e `in`.
2. Se o tamanho de `pre` ou `in` for 0, retorne uma string vazia (caso base).
3. Seja a Raiz = `pre[0]`.
4. Procure a posição `P` da Raiz dentro de `in`. A sub-string de `in` que vai do começo até antes de `P` é o percurso infixo esquerdo. A sub-string que vai após `P` até o final é o percurso infixo direito.
5. Pelo tamanho do infixo esquerdo (`P` caracteres), sabemos exatamente quais são os caracteres correspondentes na string `pre`: pegue do índice `1` ao `P` da string prefixa para obter o prefixo esquerdo. Os restantes serão o prefixo direito.
6. Chame a função recursivamente para o lado Esquerdo.
7. Chame a função recursivamente para o lado Direito.
8. Como a resposta desejada é \textit{Posfixa} (Esquerda, Direita, Raiz), concatene os retornos da seguinte forma:
   `resultado = resolver(esq_pre, esq_in) + resolver(dir_pre, dir_in) + Raiz`.
