# Copa Galáctica de Pontos

Você foi contratado como desenvolvedor júnior pela **WOK League**, a liga
oficial de esportes da galáxia. Sua primeira tarefa é reconstruir uma estatística
da **Copa Galáctica de Pontos**.

Em cada duelo entre duas naves-times:

- **Vitória**: o time vencedor ganha 3 pontos e o perdedor ganha 0;  
- **Empate**: cada time ganha 1 ponto.

Ao final do campeonato em um certo setor da galáxia, o sistema central
armazenou:

- o número total de times participantes,  
- o número total de partidas disputadas, e  
- a pontuação final de cada time.

Essas informações foram preservadas, mas os registros detalhando se cada partida
teve vencedor ou empate se perderam. O comitê quer saber **quantos duelos
terminaram empatados** em cada setor.

## Ideia principal

Em cada setor, você sabe:

- `N` = número total de partidas disputadas;  
- para cada time, um total de pontos `P_i`.

Se **todas** as `N` partidas tivessem um vencedor, cada partida distribuiria
3 pontos no total, então o máximo de pontos somados seria:

```text
max_pontos = 3 * N
```

Na prática, alguns jogos podem ter acabado empatados, distribuindo apenas
2 pontos no total. Isso reduz a soma real de pontos.

Se:

- `S` = soma de todos os pontos de todos os times,  

então a diferença `max_pontos - S` é exatamente o número de partidas
que terminaram empatadas:

```text
empates = 3 * N - S
```

## Entrada

A entrada contém vários casos de teste, cada um representando um setor da Copa.

Para cada caso:

- Uma linha com dois inteiros `T` e `N`:
  - `T` — número de times participantes (`1 ≤ T ≤ 200`);
  - `N` — número total de partidas jogadas (`0 ≤ N ≤ T * (T - 1) / 2`).

- Em seguida, `T` linhas, cada uma contendo:
  - o nome de um time (string sem espaços, com até 10 caracteres), e
  - um inteiro `P` (`0 ≤ P ≤ 3 * N`), representando o total de pontos
    obtidos por esse time.

A entrada termina quando `T = 0`. Esse caso não deve ser processado.

## Saída

Para cada caso de teste, imprima uma única linha contendo um número inteiro:
o número total de partidas que terminaram em empate naquele setor da Copa Galáctica.

## Passo a passo sugerido

Para cada caso de teste:

1. Leia `T` e `N`.  
   - Se `T == 0`, encerre o programa.
2. Inicialize uma variável `S = 0` para acumular a soma dos pontos.
3. Repita `T` vezes:
   - Leia o nome do time (uma string) e o número de pontos `P` (um inteiro).
   - Some `P` em `S`.
4. Calcule:

   ```text
   empates = 3 * N - S
   ```

5. Imprima o valor de `empates` em uma linha.
6. Volte ao passo 1 para ler o próximo caso.

## Complexidade

Você apenas percorre a lista de times de cada setor uma vez:

- **Tempo**: `O(T)` por caso de teste;  
- **Memória extra**: `O(1)`, usando apenas variáveis simples para somar pontos.

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

