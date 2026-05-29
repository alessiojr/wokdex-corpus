# Reabastecimento em Órbita

Todos os ciclos lunares, a nave de exploração **WOK-3** parte em patrulha pela fronteira da galáxia. Para não deixar ninguém à deriva, a capitã **Bruna Zeta** leva um galão extra de combustível quântico a bordo.

Durante uma missão, várias **motocargas espaciais** da frota ficam com seus tanques quase vazios após atravessar um campo de asteroides. Bruna decide usar o combustível extra para que **todas as motocargas em pane recebam exatamente a mesma quantidade** de energia, sem privilegiar nenhuma delas.

Você recebeu a tarefa de programar o módulo do computador de bordo responsável por essa **distribuição perfeita de combustível**.  
O computador recebe:
- a capacidade total de combustível quântico no galão extra, em litros;
- a quantidade de motocargas que precisam receber combustível.

Seu módulo deve descobrir **quantos litros cada motocarga receberá**, se a capitã Bruna dividir o conteúdo do galão **de forma absolutamente uniforme** entre todas as que precisam ser ajudadas.

No final, o computador deve mostrar **um único valor real**, com exatamente **duas casas decimais**, representando a quantidade de litros destinada a **cada** motocarga da frota em dificuldade.

---

## Entrada

A entrada contém **dois valores inteiros**, que representam, respectivamente:
- a quantidade de combustível quântico no galão extra que Bruna trouxe nesta missão (em **litros**);
- a quantidade de **motocargas espaciais** que necessitam de combustível.

## Restrições

- \(a > 0\)  
- \(b > 0\)

onde:
- \(a\) é a quantidade de litros de combustível no galão extra;
- \(b\) é a quantidade de motocargas que receberão combustível.

## Saída

Seu programa deverá imprimir **um único número real**, usando **ponto** como separador decimal, informando **quantos litros cada motocarga deverá receber**, com **duas casas decimais**.

## Exemplos

|          Entrada |            Saída |
|           --:    |              --: |
|                5 |            2.50  | \
|                2 |                  |

|          Entrada |            Saída |
|           --:    |              --: |
|               10 |             5.00 | \
|               2  |                  |



