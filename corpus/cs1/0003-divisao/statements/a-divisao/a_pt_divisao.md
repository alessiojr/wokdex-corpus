# Reabastecimento em Órbita

Todos os ciclos lunares, a nave de exploração **WOK-3** parte em patrulha pela fronteira da galáxia. Para não deixar ninguém à deriva, a capitã **Bruna Zeta** leva um galão extra de combustível quântico a bordo.

Durante uma missão recente, um grupo de **motocargas espaciais** da frota aliada ficou com seus tanques perigosamente vazios após atravessar um campo de asteroides. A capitã Bruna decidiu intervir e usar o conteúdo do galão extra para reabastecê-las.

A diretriz da Federação Galáctica dita uma regra inquebrável para resgates: **a partilha de energia deve ser perfeitamente equânime**. Se houver qualquer flutuação ou diferença na quantidade de plasma transferida para cada nave, os motores quânticos entrarão em colapso gravitacional. 

Sua missão é desenvolver o subsistema de partilha do painel. A partir do volume bruto de combustível disponibilizado e o escopo da frota resgatada, determine com extrema precisão de duas sub-unidades o volume estabilizado que todos os motores receberão simultaneamente.

## Entrada

A entrada é composta por dois valores vitais recebidos pelos sensores:
1.  Um número (que pode ser fracionário) representando a reserva bruta de combustível no galão.
2.  Um número inteiro indicando a quantidade de motocargas integram a frota necessitada.

## Saída

Seu painel de controle deve projetar **um único valor numérico**, calibrado exatamente na escala de **duas casas decimais**, definindo a cota exata estabilizada.

## Restrições

- A quantidade de combustível é sempre maior que zero (\( A > 0 \)).
- A quantidade de motocargas é sempre maior que zero (\( B > 0 \)).

## Exemplos

|          Entrada |            Saída |
|           --:    |              --: |
|                5 |            2.50  | \
|                2 |                  |

|          Entrada |            Saída |
|           --:    |              --: |
|               10 |             5.00 | \
|               2  |                  |
