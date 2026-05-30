# Editorial: DNA Dinossáurico

## Resumo do Problema
Dado um texto $S$ (DNA) de tamanho $N$ composto pelos caracteres C, D, F e T, precisamos encontrar o maior inteiro $d$ (a "palindromicidade") tal que:
1. $d$ seja um divisor de $N$.
2. Se dividirmos $S$ em $d$ blocos de tamanho igual a $k = \frac{N}{d}$, a sequência de blocos forma um palíndromo. Ou seja, o 1º bloco é igual ao último, o 2º é igual ao penúltimo, etc.

## Análise e Principais Percepções (Insights)

### 1. Relação Inversa entre $d$ e $k$
Como $d$ é o número de blocos e $k$ é o tamanho de cada bloco, temos a relação $N = d \times k$. 
Para **maximizar** $d$, precisamos **minimizar** $k$. Portanto, nosso objetivo é encontrar o menor divisor $k$ de $N$ para o qual a condição dos blocos palindrômicos seja verdadeira.

### 2. Espaço de Busca (Evitando TLE)
Uma abordagem "gulosa" ou de força bruta (nível B) tentaria iterar sobre todos os valores possíveis de $k$ de $1$ a $N$, extraindo substrings e comparando-as. Essa abordagem pode executar operações desnecessárias e chegar a complexidade $O(N^2)$, garantindo o estouro do limite de tempo (TLE) para $N = 500.000$.

A chave para o sucesso é **testar apenas os divisores** de $N$. 
Podemos encontrar todos os divisores iterando até $\sqrt{N}$ e ordená-los. Para $N \le 500.000$, o número máximo de divisores é 240 (quando $N=420.420$, um número altamente composto).

### 3. Validação In-Place (Sem Alocação de Memória)
Criar arrays de substrings custa muita memória e tempo (overhead de alocação). O correto é acessar os caracteres da string diretamente por seus índices.
Para um tamanho de bloco $k$, e iterando o bloco da esquerda $i$ (de $0$ a $\lfloor d/2 \rfloor - 1$):
- O bloco correspondente da direita terá índice $(d - 1 - i)$.
- O caractere na posição $j$ do bloco esquerdo está no índice global: `i * k + j`.
- O caractere na posição $j$ do bloco direito está no índice global: `(d - 1 - i) * k + j`.

Se encontrarmos qualquer diferença, usamos **early exit** (`break`) imediatamente para invalidar esse $k$. A probabilidade de dois blocos serem idênticos ao acaso é ínfima, fazendo com que a validação termine nos primeiros caracteres na esmagadora maioria dos casos inválidos.

## Solução Passo a Passo (Nível A - Optimal)

1. Calcular $N = |S|$.
2. Encontrar todos os divisores de $N$ e armazená-los numa lista. Isso custa $O(\sqrt{N})$.
3. Ordenar a lista de divisores em ordem crescente.
4. Para cada divisor $k$ da lista:
   - Calcular $d = N / k$.
   - Executar a verificação iterando os blocos espelhados.
   - Assim que um $k$ for considerado válido (todos os blocos testados forem idênticos a seus espelhos), a resposta procurada será esse $d$.
   - Como estamos iterando os divisores $k$ em ordem crescente, o primeiro $k$ válido garantirá o maior $d$ possível. Retornamos imediatamente!

## Complexidade

- **Tempo:** $O(\sqrt{N})$ para achar divisores + $O(N \cdot D(N))$ no pior caso para validar os blocos, onde $D(N)$ é a quantidade de divisores. Graças ao *early exit*, a prática atinge quase $O(N)$. Esta complexidade é extremamente segura.
- **Espaço:** $O(D(N))$ para guardar a lista de divisores da string, ou seja, estritamente limitado e na prática $O(1)$ constante em relação à memória auxiliar do processo. A string de tamanho máximo 500k é armazenada gastando $< 1\text{ MB}$.
