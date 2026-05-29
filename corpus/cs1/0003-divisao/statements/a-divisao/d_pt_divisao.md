# Reabastecimento em Órbita

Todos os ciclos lunares, a nave de exploração **WOK-3** parte em patrulha pela fronteira da galáxia. Para não deixar ninguém à deriva, a capitã **Bruna Zeta** leva um galão extra de combustível quântico a bordo.

Durante uma missão recente, um grupo de **motocargas espaciais** da frota aliada ficou com seus tanques perigosamente vazios após atravessar um campo de asteroides. A capitã Bruna decidiu intervir e usar o conteúdo do galão extra para reabastecê-las.

A diretriz da Federação Galáctica é clara: **todas as naves em perigo devem receber exatamente a mesma quantidade de energia**, sem privilegiar nenhuma delas, para manter o equilíbrio da aliança.

Sua missão é programar o módulo do computador de bordo responsável por essa **distribuição perfeita de combustível**.

## O Problema
O computador de bordo receberá dois dados vitais de entrada:
1.  A capacidade total de combustível quântico disponível no galão extra (em litros). Por poder conter fracionados, ele deve ser lidado como um tipo de ponto-flutuante (`float` ou `double`).
2.  A quantidade de motocargas que necessitam de reabastecimento. Por ser contável da frota, deve ser lida em um tipo `int`.

Seu módulo deve calcular **quantos litros cada motocarga receberá**. Você solucionará isso efetuando uma simples operação de divisão matemática: `Combustivel / Motocargas`. 

O painel da nave deve exibir esse valor através da saída de tela. O resultado dessa divisão será um número real e deve ser impresso de modo formatado para garantir a consistência dos equipamentos. Dependendo da linguagem utilizada, você usará ferramentas como `printf("%.2f\n", resultado)` ou os formatadores de String `f"{resultado:.2f}"` (Python) para fixar a exibição da saída em exatas **duas casas decimais**.

---

## Entrada

A entrada consiste em **dois valores**, separadamente:
1.  Um número (que pode ser fracionário, ponto-flutuante) representando a quantidade de combustível no galão (em **litros**).
2.  Um número inteiro representando a quantidade de **motocargas espaciais**.

## Saída

A saída deve ser **um único número**, exibindo a sua variável que guardou o cálculo da divisão.
**Atenção**: O valor deve ser convertido em texto, sendo exibido restritamente com **duas casas decimais** antes da quebra de linha.

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
