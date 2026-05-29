## Copa do Mundo 

Uma Copa do Mundo de futebol de botões está sendo realizada com times de todo o mundo. A classificação é baseada no número de pontos ganhos pelos times, e a distribuição de pontos é feita da forma usual. Ou seja, quando um time ganha um jogo, ele recebe 3 pontos;  se o jogo termina empatado, ambos os times recebem 1 ponto; e o perdedor não recebe nenhum ponto. 

Dada a classificação atual dos times e o número de times participantes na Copa do Mundo, sua tarefa é de determinar quantos jogos terminaram empatados até o momento. 

### Dica (Caminho para a Solução)
Para resolver esse problema de forma eficiente (em complexidade ótima $O(T)$ por caso de teste), preste atenção ao número total de pontos distribuídos em um jogo:
- Se houver uma vitória, um time ganha 3 e o outro 0. Total distribuído: 3.
- Se houver um empate, ambos ganham 1 ponto. Total distribuído: 2 (reduz em 1 ponto a soma máxima possível).

Assim, podemos focar na **soma total de pontos de todos os times**. Se não houvesse empates, a soma de pontos do torneio seria exatamente $3 \times N$, onde $N$ é o número de partidas. Cada ponto "faltante" para completar o máximo de pontos só pode ter sido perdido devido a empates!

### Entrada
A entrada é composta por diversos casos de teste.  A primeira linha de um caso de teste contém dois inteiros T e N, indicando respectivamente o número de times participantes e o número de partidas jogadas.  Cada uma das T linhas seguintes contém o nome de um time (uma cadeia de máximo 10 letras e dígitos), seguido de um espaço em branco, seguido do número de pontos que o time obteve até o momento. A entrada termina quando $T = 0$.

### Saída
Para cada um dos casos de teste seu programa deve imprimir uma única linha contendo um número inteiro, representando a quantidade de jogos que terminaram empatados até o momento. 

### Restrições
* $2 \le T \le 200$ 
* $0 \le N \le 10^4$ 
* Nome de time contém no máximo 10 carateres, que podem ser dígitos ou letras maiúsculas e minúsculas sem acento. 

---

### Exemplos

| Input       | Output |
|:------------|:-------|
| 3 3         | 0      |
| Brasil 3    | 2      |
| Australia 3 |        |
| Croacia 3   |        |
| 3 3         |        |
| Brasil 5    |        |
| Japao 1     |        |
| Australia 1 |        |
| 0 0         |        |
