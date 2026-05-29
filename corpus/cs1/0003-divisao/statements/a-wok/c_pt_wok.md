# Algoritmo de Reabastecimento da Frota WOK

Na periferia da galáxia WOK, a capitã **Bruna Zeta** conduz uma patrulha em sua nave principal, acompanhada de várias **motocargas espaciais**. Para evitar que qualquer nave fique à deriva, ela leva um **galão extra de combustível quântico**.

Durante a missão, algumas motocargas ficam com pouco combustível e precisam ser reabastecidas. Bruna quer ser justa e **dividir o combustível extra igualmente entre todas as motocargas que precisam de ajuda**.

Seu objetivo é implementar um programa que calcule **quantos litros de combustível cada motocarga receberá**, considerando essa divisão uniforme.

---

## Dica de abordagem (nível educacional)

Para resolver este problema, você pode seguir estes passos:

1. **Leia dois inteiros**:
   - o total de litros de combustível quântico no galão extra;
   - a quantidade de motocargas espaciais que precisam ser reabastecidas.
2. Converta pelo menos um dos valores para um **tipo numérico real** (por exemplo, `double` ou `float`) para evitar divisão inteira.
3. **Calcule a divisão**: quantidade de combustível por motocarga = total de litros ÷ número de motocargas.
4. **Formate a saída** para exibir o resultado com **exatamente duas casas decimais**, usando ponto como separador decimal.

---

## Entrada

A entrada contém **dois valores inteiros**, que representam, respectivamente:

- a quantidade de combustível quântico no galão extra que Bruna trouxe nesta missão (em **litros**);
- a quantidade de **motocargas espaciais** que necessitam de combustível.

## Restrições

- \(a > 0\);
- \(b > 0\).

Onde:
- \(a\) é a quantidade total de litros de combustível no galão;
- \(b\) é o número de motocargas que serão reabastecidas.

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







