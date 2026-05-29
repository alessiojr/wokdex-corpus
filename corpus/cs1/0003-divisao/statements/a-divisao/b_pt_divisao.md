# Reabastecimento em Órbita

Todos os ciclos lunares, a nave de exploração **WOK-3** parte em patrulha pela fronteira da galáxia. Para não deixar ninguém à deriva, a capitã **Bruna Zeta** leva um galão extra de combustível quântico a bordo.

Durante uma missão recente, um grupo de **motocargas espaciais** da frota aliada ficou com seus tanques perigosamente vazios após atravessar um campo de asteroides. A capitã Bruna decidiu intervir e usar o conteúdo do galão extra para reabastecê-las.

A diretriz da Federação Galáctica é clara: **todas as naves em perigo devem receber exatamente a mesma quantidade de energia**, sem privilegiar nenhuma delas, para manter o equilíbrio da aliança.

Sua missão é programar o módulo do computador de bordo responsável por essa **distribuição perfeita de combustível**.

## O Problema
O computador de bordo receberá dois dados vitais:
1.  A capacidade total de combustível quântico disponível no galão extra (em litros).
2.  A quantidade de motocargas que necessitam de reabastecimento.

Seu módulo deve calcular **quantos litros cada motocarga receberá** se o combustível for dividido de forma **absolutamente uniforme** entre elas.

O painel da nave deve exibir esse valor com precisão, pois o combustível quântico é instável. O resultado deve ser **um único número real**, formatado com exatamente **duas casas decimais**.

---

## Entrada

A entrada consiste em **dois valores**:
1.  Um número (que pode ser fracionário) representando a quantidade de combustível no galão (em **litros**).
2.  Um número inteiro representando a quantidade de **motocargas espaciais**.

## Saída

A saída deve ser **um único número**, representando a quantidade de litros destinada a cada motocarga.
**Atenção**: O valor deve ser exibido com **duas casas decimais**.

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
