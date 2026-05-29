# Tutorial: Frequências das Etiquetas

Neste desafio da academia de código da plataforma WOK, simularemos o emparelhamento de etiquetas espaciais da mesma cor.

Como o limite de $N$ é enorme ($10^5$), um loop triplo ou duplo dará **TLE**! Para resolver o problema eficientemente:
1. Declare um Mapa/Dicionário/Hash para armazenar a contagem de cada cor ao longo do escaneamento do vetor (ex. `map<int, long long> counts;` em C++).
2. Para cada etiqueta que você lê, incremente sua contagem: `counts[cor]++`.
3. Sabemos que se uma cor apareceu $X$ vezes, ela forma exatamente $\frac{X \cdot (X-1)}{2}$ pares.
4. Faça um loop final iterando por cada chave do Mapa e adicione sua respectiva pontuação ao total de pares! Tenha a certeza de usar uma variável `long long` no total de pares para não ocasionar Overflow estourando limites de 32 bits.

## Entrada
* A 1ª linha tem o número total de amostras de etiquetas espaciais, $N$.
* A 2ª linha fornece as $N$ cores (inteiros de $1$ a $10^9$).

## Saída
* O total exato de pares possíveis dentro da equipe.

## Exemplos

### Exemplo 1

| Entrada       | Saída |
| :------------ | :---- |
| 5             | 2     |
| 1 2 1 3 2     |       |

### Exemplo 2

| Entrada   | Saída |
| :-------- | :---- |
| 4         | 6     |
| 1 1 1 1   |       |
