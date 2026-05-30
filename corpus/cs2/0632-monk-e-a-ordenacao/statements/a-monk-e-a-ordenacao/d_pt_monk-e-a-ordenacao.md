# Editorial - Monk e o Algoritmo de Ordenação

Este problema é uma aplicação direta do algoritmo **Radix Sort**, mas com uma variação na base de processamento. Em vez de processar dígito a dígito (base 10), o problema solicita o processamento em blocos de 5 dígitos (base $10^5$).

## Lógica da Solução

O Radix Sort funciona ordenando os números com base em compartimentos de pesos (buckets). Para que o Radix Sort funcione globalmente, cada ordenação intermediária **deve ser estável**. Isso significa que elementos com o mesmo peso devem manter sua ordem relativa que tinham antes daquele passo de ordenação.

### 1. Extração do Pedaço (Peso)
Para extrair os dígitos da posição $5i$ até $5(i-1)+1$, podemos usar operações aritméticas simples:
- O $i$-ésimo pedaço de um número $X$ pode ser calculado como:
  $$\text{peso} = \left\lfloor \frac{X}{10^{5(i-1)}} \right\rfloor \mod 10^5$$

### 2. Escolha do Algoritmo de Ordenação
Como $N$ pode chegar a $10^6$ e o intervalo de pesos é fixo ($0$ a $99.999$), o algoritmo mais eficiente para a fase de ordenação estável é o **Counting Sort**.
- O Counting Sort executa em $O(N + K)$, onde $K=10^5$.
- Ordenar usando `sort()` nativo das linguagens (que costuma ser $O(N \log N)$) pode ser muito lento para $10^6$ elementos em múltiplas passagens, especialmente em linguagens como Python ou Java se houver muitos passos.

### 3. Condição de Parada
O algoritmo para quando todos os números, ao serem divididos por $10^{5i}$, resultarem em 0. Uma forma simples de implementar é verificar se o maior elemento do array ainda possui dígitos para as posições atuais.

## Complexidade
- **Tempo**: $O(D \times (N + K))$, onde $D$ é o número de passagens (máximo 4 para números até $10^{18}$ na base $10^5$), $N$ é o número de elementos e $K=10^5$. Resultando em uma complexidade linear $O(N)$.
- **Espaço**: $O(N + K)$ para armazenar o array auxiliar e as frequências do Counting Sort.

## Referências
- **HackerEarth**: Este problema faz parte da trilha *Codemonk* do HackerEarth, sob o título original *"Monk and Sorting Algorithm"*.
- **URI/Beecrowd**: Frequentemente encontrado em maratonas de programação como um exercício clássico de Radix Sort.