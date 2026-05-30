# DNA Dinossáurico

Um grupo de pesquisadores recentemente descobriu um método eficiente para sequenciar DNA Dinossáurico a partir de fósseis. Isto nos permite agora entender melhor esses animais tão fascinantes que habitaram nosso planeta antes de nós. Semelhante ao caso humano, o DNA Dinossáurico também era armazenado no núcleo da célula dinossáurica, levado ao citoplasma por RNA mensageiro dinossáurico e interpretado por ribossomos, que contém a codificação do código genético dinossáurico (que pode ser representado por uma tabela que mapeia uma sequência de aminoácidos de entrada para outra sequência de aminoácidos de saída) e produzem com ele enzimas cuja estrutura terciária é bastante interessante. Para sua sorte, nenhuma dessas informações é relevante para este problema.

Uma sequência de DNA Dinossáurico é basicamente uma sequência com 4 aminoácidos possíveis: cretacina (representado pela letra C), dinossaurina (representado pela letra D), fossilina (F), e tirrexina (T). Por exemplo, uma sequência possível de DNA Dinossáurico é CDDFTFC. ACAATG é DNA humano, certamente não dinossáurico.

O que é importante é que os pesquisadores descobriram uma propriedade do DNA do dinossauro muito correlacionada com quão perigoso ele era. Ou seja, dado o DNA de dois dinossauros e tempo suficiente, os pesquisadores sabem dizer qual deles sairia vencedor em uma partida de MMA Dinossáurico (ou, mais realisticamente, qual deles mais provavelmente teria o outro como presa). Isto é de extrema valia para entender os fatores que afetaram a sobrevivência de cada espécie.

Esta propriedade de ouro é a palindromicidade do DNA. Você já deve saber que uma sequência de caracteres é palíndrome se ela é a mesma se lida da esquerda para a direita ou da direita para a esquerda. Por exemplo, DFTFD é uma sequência palíndrome, mas DFTTT não é. Nem toda sequência de DNA é palíndrome; contudo, todas possuem um número associado que é sua palindromicidade. A palindromicidade de uma sequência de DNA $s$ é o maior inteiro $d$ que satisfaz as seguintes propriedades:

* $d$ é um divisor do tamanho de $s$ ($|s|$);
* Se dividimos $s$ em $d$ subsequências contíguas de caracteres de igual tamanho $\frac{|s|}{d}$, a primeira subsequência é igual à última; a segunda é igual à penúltima, e assim por diante. Mais precisamente, se as subsequências são numeradas da esquerda para a direita de 1 a $\frac{|s|}{d}$, a subsequência de índice $i$ é igual à subsequência de índice $\frac{|s|}{d}+1-i$.

Note que, por definição, toda cadeia de caracteres tem palindromicidade no mínimo 1, porque ela sempre pode ser dividida apenas em um bloco. Já a cadeia DFDF não é palíndrome, mas tem palindromicidade 2, porque se a dividimos em dois blocos de igual tamanho, eles são iguais (DF e DF). Uma cadeia de tamanho $n$ que seja palíndrome (no sentido tradicional) tem palindromicidade $n$ (podemos colocar cada caractere em seu próprio bloco).

Dada uma sequência de DNA dinossáurico, calcule a sua palindromicidade.

## Tutorial e Solução Passo a Passo

Para determinar a palindromicidade de uma cadeia de DNA dinossáurico, nosso objetivo é achar o maior número $d$ de blocos em que a cadeia pode ser dividida de forma que a sequência resultante de blocos forme um palíndromo. 

### Passo 1: Entendendo o Tamanho dos Blocos
A cadeia original tem tamanho $N = |S|$. Se a dividirmos em $d$ blocos de tamanhos iguais, o tamanho de cada bloco será $L = \frac{N}{d}$. Como queremos maximizar o número de blocos ($d$), isso é o mesmo que **minimizar o tamanho de cada bloco ($L$)**.

Portanto, podemos procurar o valor de $L$ testando os tamanhos de bloco do menor para o maior (de $L = 1$ até $L = N$).

### Passo 2: Verificando as Condições
Para um dado tamanho de bloco $L$, ele só é válido se:
1. Ele for um divisor exato do tamanho total da cadeia (ou seja, `N % L == 0`).
2. Se verificarmos os blocos do início e do final caminhando em direção ao centro, os pares de blocos opostos devem ser idênticos.

Para verificar se os blocos são idênticos, podemos usar um laço de repetição. Como o tamanho do bloco é $L$, o bloco da extremidade esquerda de índice $k$ (onde $k$ varia de $0$ até metade da quantidade de blocos) começa na posição `k * L`. O bloco correspondente na extremidade direita começa na posição `N - (k + 1) * L`. Basta comparar se a substring de tamanho $L$ na posição esquerda é igual à substring de tamanho $L$ na posição direita (ou comparar caractere por caractere).

### Passo 3: O Algoritmo
1. Leia a string de DNA $S$ e determine seu tamanho $N$.
2. Para cada $L$ começando de $1$ até $N$:
   - Se `N % L != 0`, vá para o próximo $L$.
   - Caso contrário, a quantidade de blocos seria $d = \frac{N}{L}$. Assuma temporariamente que os blocos formam um palíndromo (ex: crie uma variável booleana `eh_palindrome = true`).
   - Use um laço com $k$ variando de $0$ até $\frac{d}{2} - 1$:
     - Se o trecho da string de tamanho $L$ começando em `k * L` for diferente do trecho começando em `N - (k + 1) * L`, então defina `eh_palindrome = false` e interrompa a checagem (break).
   - Se ao final da checagem `eh_palindrome` permanecer verdadeiro, achamos o menor tamanho de bloco válido!
   - A resposta ótima será o número de blocos, que é $\frac{N}{L}$. Imprima esse valor e encerre o programa.
3. Este algoritmo sempre terá uma resposta garantida, visto que, no pior dos casos, quando $L = N$, a string inteira é dividida em $d=1$ bloco, e um bloco único sempre é palíndrome de si mesmo.

### Entrada
A entrada consiste de uma única linha contendo uma sequência $S$ de DNA dinossaurico, composta apenas pelos caracteres C, D, F e T.

### Saída
Imprima uma única linha contendo um inteiro: a palindromicidade da sequência de DNA dinossáurico dada na entrada.

**Restrições:**
* $1 \le |S| \le 5 \times 10^5$
* $S_i \in \{C, D, F, T\}$

### Exemplos

| Entrada | Saída |
|:--------|:------|
| CDCD    | 2     |

| Entrada | Saída |
|:--------|:------|
| CDFTFDC | 7     |

| Entrada  | Saída |
|:---------|:------|
| CDFTFDCC | 1     |
