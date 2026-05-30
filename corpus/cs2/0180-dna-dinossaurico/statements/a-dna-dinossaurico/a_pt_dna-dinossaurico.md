#  DNA Dinossáurico

Um grupo de pesquisadores recentemente descobriu um método eficiente para sequenciar DNA Dinossáurico a partir de fósseis. Isto nos permite agora entender melhor esses animais tão fascinantes que habitaram nosso planeta antes de nós. Semelhante ao caso humano, o DNA Dinossáurico também era armazenado no núcleo da célula dinossáurica, levado ao citoplasma por RNA mensageiro dinossáurico e interpretado por ribossomos, que contém a codificação do código genético dinossáurico (que pode ser representado por uma tabela que mapeia uma sequência de aminoácidos de entrada para outra sequência de aminoácidos de saída) e produzem com ele enzimas cuja estrutura terciária é bastante interessante. Para sua sorte, nenhuma dessas informações é relevante para este problema.

Uma sequência de DNA Dinossáurico é basicamente uma sequência com 4 aminoácidos possíveis: cretacina (representado pela letra C), dinossaurina (representado pela letra D), fossilina (F), e tirrexina (T). Por exemplo, uma sequência possível de DNA Dinossáurico é CDDFTFC. ACAATG é DNA humano, certamente não dinossáurico.

O que é importante é que os pesquisadores descobriram uma propriedade do DNA do dinossauro muito correlacionada com quão perigoso ele era. Ou seja, dado o DNA de dois dinossauros e tempo suficiente, os pesquisadores sabem dizer qual deles sairia vencedor em uma partida de MMA Dinossáurico (ou, mais realisticamente, qual deles mais provavelmente teria o outro como presa). Isto é de extrema valia para entender os fatores que afetaram a sobrevivência de cada espécie.

Esta propriedade de ouro é a palindromicidade do DNA. Você já deve saber que uma sequência de caracteres é palíndrome se ela é a mesma se lida da esquerda para a direita ou da direita para a esquerda. Por exemplo, DFTFD é uma sequência palíndrome, mas DFTTT não é. Nem toda sequência de DNA é palíndrome; contudo, todas possuem um número associado que é sua palindromicidade. A palindromicidade de uma sequência de DNA $s$ é o maior inteiro $d$ que satisfaz as seguintes propriedades:

* $d$ é um divisor do tamanho de $s$ ($|s|$);
* Se dividimos $s$ em $d$ subsequências contíguas de caracteres de igual tamanho $\frac{|s|}{d}$, a primeira subsequência é igual à última; a segunda é igual à penúltima, e assim por diante. Mais precisamente, se as subsequências são numeradas da esquerda para a direita de 1 a $\frac{|s|}{d}$, a subsequência de índice $i$ é igual à subsequência de índice $\frac{|s|}{d}+1-i$.

Note que, por definição, toda cadeia de caracteres tem palindromicidade no mínimo 1, porque ela sempre pode ser dividida apenas em um bloco. Já a cadeia DFDF não é palíndrome, mas tem palindromicidade 2, porque se a dividimos em dois blocos de igual tamanho, eles são iguais (DF e DF). Uma cadeia de tamanho $n$ que seja palíndrome (no sentido tradicional) tem palindromicidade $n$ (podemos colocar cada caractere em seu próprio bloco).

Dada uma sequência de DNA dinossáurico, calcule a sua palindromicidade.

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