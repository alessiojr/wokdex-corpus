# Copa Galáctica de Pontos

Na galáxia WOK, a **Copa Galáctica de Pontos** reúne equipes de todos os cantos do universo:
times de planetas oceânicos, colônias em anéis asteroides e até federações de robôs.

Em uma edição especial, o comitê intergaláctico definiu a seguinte regra de pontuação
para cada confronto entre dois times:

- **Vitória**: 3 pontos para o time vencedor  
- **Empate**: 1 ponto para cada time  
- **Derrota**: 0 pontos

Ao final do torneio, o comitê tem acesso à **tabela final de classificação**:

- o número total de times que participaram,  
- o número total de partidas disputadas, e  
- a pontuação final de cada time.

Porém, os registros de telemetria dos jogos foram corrompidos por uma tempestade de raios cósmicos,
e ninguém sabe mais **quantos confrontos terminaram empatados**.

Sua missão é, a partir desses dados, descobrir **quantas partidas terminaram em empate** na Copa Galáctica.

## Entrada

A entrada contém vários casos de teste.

Em cada caso:

- A primeira linha contém dois inteiros `T` e `N`:
  - `T` — número de times participantes (`1 ≤ T ≤ 200`);
  - `N` — número total de partidas jogadas (`0 ≤ N ≤ T * (T - 1) / 2`).

- Em seguida, são dadas `T` linhas, cada uma contendo:
  - o nome de um time (string sem espaços, com até 10 caracteres), e
  - um inteiro `P` (`0 ≤ P ≤ 3 * N`), representando o total de pontos
    obtidos por esse time ao longo do torneio.

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

> Observação: o caso `0 0` indica o fim da entrada e **não** gera linha de saída.
