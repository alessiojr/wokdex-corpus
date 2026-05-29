## Copa do Mundo 

Uma Copa do Mundo de futebol de botões está sendo realizada com times de todo o mundo. A classificação é baseada no número de pontos ganhos pelos times, e a distribuição de pontos é feita da forma usual. Ou seja, quando um time ganha um jogo, ele recebe 3 pontos;  se o jogo termina empatado, ambos os times recebem 1 ponto; e o perdedor não recebe nenhum ponto. 

Dada a classificação atual dos times e o número de times participantes na Copa do Mundo, sua tarefa é de determinar quantos jogos terminaram empatados até o momento. 

### Tutorial Passo a Passo

Esse problema parece complicado quando olhamos o nome de cada time e a classificação, mas na verdade não precisamos simular partidas ou descobrir quem jogou contra quem! Podemos simplificar a lógica olhando **apenas para a soma global dos pontos conquistados por todos os times**.

**1º Passo: Compreendendo a Distribuição de Pontos**
- Em uma partida com Vencedor: Time Vencedor (recebe 3 pontos) + Perdedor (recebe 0 pontos) = Total de **3 pontos** distribuídos e somados à tabela.
- Em um Empate: Time 1 (recebe 1 ponto) + Time 2 (recebe 1 ponto) = Total de **2 pontos** distribuídos e somados à tabela.

**2º Passo: O Cenário Ideal sem Empates**
Se soubermos que foram disputadas exatamente $N$ partidas, e imaginarmos que **nenhum** jogo empatou, o campeonato teria distribuído o máximo absoluto de $3 \times N$ pontos na classificação geral.
Porém, como na realidade alguns jogos acabaram empatados, o campeonato, na verdade, distribuiu um total de $S$ pontos (sendo $S$ a soma de pontos agrupados de cada time listado na entrada).

**3º Passo: A Fórmula Matemática**
Se analisarmos, cada empate registrado em campo retira exatamente **1 ponto** do montante ideal que seria $3 \times N$. 
Portanto, a quantidade total de empates do campeonato é simplesmente a diferença entre o que 'deveria ter' se ninguém empatasse e a 'soma real' de pontos conquistados somando todas as equipes!

**Lógica de Implementação Mão na Massa:**
1. Leia seguidamente casos de uso ignorando sentinelas (repita até que a leitura de $T$ e $N$ seja $T = 0$).
2. Para cada bloco, ao ler o número de times $T$ e o total de jogos $N$, calcule a quantidade máxima possível de pontos: `Maximo = 3 * N`.
3. Inicie um acumulador `Soma_Pontos = 0` e repita $T$ vezes uma leitura para coletar a pontuação de cada time. Você deve jogar fora ou ignorar a *String* do nome da equipe e focar apenas em extrair e somar o inteiro da pontuação da equipe!
4. Ao final do laço das linhas de times, calcule e imprima em uma nova linha o balanço: `Maximo - Soma_Pontos`.

### Entrada
A entrada é composta por diversos casos de teste.  A primeira linha de um caso de teste contém dois inteiros T e N, indicando respectivamente o número de times participantes e o número de partidas jogadas.  Cada uma das T linhas seguintes contém o nome de um time (uma cadeia de máximo 10 letras e dígitos), seguido de um espaço em branco, seguido do número de pontos que o time obteve até o momento. A entrada acaba no sentinela `0 0`.

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
