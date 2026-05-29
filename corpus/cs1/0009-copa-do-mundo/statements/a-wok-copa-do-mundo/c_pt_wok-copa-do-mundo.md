# Copa Galáctica de Pontos

Nesta versão, o enunciado da **Copa Galáctica de Pontos** é o mesmo da versão padrão,
mas com dicas extras para te ajudar a modelar a solução no universo WOK.

## Descrição

Na galáxia WOK, times de diferentes planetas se enfrentam em uma grande liga espacial.
Cada partida segue a seguinte regra de pontuação:

- **Vitória**: 3 pontos para o time vencedor  
- **Empate**: 1 ponto para cada time  
- **Derrota**: 0 pontos

Ao final do campeonato, o comitê intergaláctico possui:

- o número total de times participantes,  
- o número total de partidas disputadas, e  
- a pontuação final de cada time (já somada ao longo de todo o torneio).

O que eles **não** sabem mais, por causa de uma pane nos registradores de partida,
é **quantas dessas partidas terminaram empatadas**.

Sua tarefa é ajudar o comitê a descobrir quantos empates ocorreram na Copa Galáctica.

## Entrada

A entrada contém vários casos de teste.

- A primeira linha de cada caso contém dois inteiros `T` e `N`:
  - `T` — número de times participantes (`1 ≤ T ≤ 200`);
  - `N` — número total de partidas jogadas (`0 ≤ N ≤ T * (T - 1) / 2`).

- Em seguida, há `T` linhas, cada uma contendo:
  - o nome de um time (uma sequência de até 10 caracteres, sem espaços), e
  - um inteiro `P` (`0 ≤ P ≤ 3 * N`), representando o total de pontos
    obtidos por esse time.

A entrada termina quando `T = 0`. Esse caso não deve ser processado.

## Saída

Para cada caso de teste, imprima uma única linha contendo um número inteiro:
o número total de partidas que terminaram em empate na Copa Galáctica.

## Exemplos

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
```

> Observação: o caso `0 0` indica o fim da entrada e **não** gera linha de saída.

## Dicas e Estratégia (Educacional)

Pense em quantos **pontos de energia** são distribuídos em cada confronto
entre dois times espaciais:

1. Se há um **vencedor**, a partida distribui `3` pontos de energia no total  
   (3 para o vencedor, 0 para o perdedor).
2. Se há um **empate**, a partida distribui apenas `2` pontos de energia no total  
   (1 para cada time).

Se todos os `N` jogos tivessem um vencedor, o campeonato distribuiria
`3 * N` pontos de energia no total.

Agora observe:

- Seja `S` a soma dos pontos de todos os times após o torneio.  
- Cada empate faz essa soma total ficar **1 ponto menor** do que o máximo
  possível (`3 * N`), pois distribui 2 em vez de 3.

Logo, se houver `E` empates:

- Pontos máximos possíveis: `3 * N`  
- Pontos efetivamente distribuídos: `S`  
- Diferença: `3 * N - S`  

Essa diferença é exatamente o número de empates:

```text
empates = 3 * N - S
```

### Passos sugeridos para a implementação

1. Leia `T` e `N`. Se `T == 0`, pare o programa.
2. Inicialize uma variável `S = 0`.
3. Repita `T` vezes:
   - Leia o nome do time (string) e o número de pontos `P` (inteiro).
   - Some `P` em `S`.
4. Calcule `empates = 3 * N - S`.
5. Imprima `empates`.
6. Volte ao passo 1 para ler o próximo caso de teste.

### Complexidade

Você faz apenas um laço simples sobre os `T` times de cada caso
e algumas operações aritméticas:

- **Complexidade de tempo**: `O(T)` por caso de teste.  
- **Complexidade de memória**: `O(1)` extra, além das variáveis de leitura.

