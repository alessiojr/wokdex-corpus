# Crônicas da Copa Galáctica

Nos anéis externos da galáxia WOK, acontece a **Copa Galáctica**, um torneio
onde naves-times de diferentes sistemas estelares duelam em arenas de gravidade
variável. Cada confronto rende pontos ao longo da tabela interplanetária.

Após vários ciclos de jogos, um problema surge: parte dos registros de batalha
foi perdida em uma tempestade de partículas cósmicas. Restaram apenas:

- a lista de todas as naves-times participantes, e  
- a pontuação final de cada uma na tabela da liga,  
- além do número total de confrontos que ocorreram naquele setor.

Os árbitros gravitacionais sabem que cada duelo entre duas naves
sempre termina com uma dessas possibilidades:

- uma nave sai vitoriosa,  
- as duas naves encerram o duelo em equilíbrio perfeito.

Você recebe, para vários setores da galáxia, o resumo final de cada mini-liga:
os nomes das naves-times, a pontuação total atingida por cada uma e o
número total de confrontos disputados naquele setor.

O Conselho Galáctico quer saber, para **cada setor**, algo muito específico
sobre esses duelos — algo que não está mais gravado em nenhum painel de controle.

## Entrada

Vários setores da Copa Galáctica são descritos em sequência.

Para cada setor:

- Uma linha com dois inteiros `T` e `N`  
  (número de naves-times e número de confrontos disputados naquele setor).

- Em seguida, `T` linhas descrevem cada nave-time:
  - o identificador da nave (string curta, sem espaços), seguido
  - de um inteiro que representa a pontuação total acumulada por aquela nave
    em todos os duelos que disputou nesse setor.

Os valores numéricos obedecem a limites razoáveis para uma liga galáctica
com até algumas centenas de naves.

A entrada termina quando um setor é descrito com `T = 0`.  
Esse setor não deve ser analisado.

## Saída

Para cada setor descrito, seu programa deve imprimir uma única linha com
um número inteiro, respondendo à pergunta do Conselho para aquele setor.

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

> Observação: o setor final `0 0` indica apenas o fim da transmissão
> e **não** gera linha de saída.

