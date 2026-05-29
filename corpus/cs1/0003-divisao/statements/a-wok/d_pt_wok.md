# Tutorial: Dividindo Combustível na Nave WOK

Na nave da capitã **Bruna Zeta**, existe um **galão extra de combustível quântico** usado para ajudar **motocargas espaciais** que ficam com pouco combustível durante as missões.

Você vai escrever um programa para o computador de bordo que faz a seguinte conta:
- recebe o total de litros de combustível no galão extra;
- recebe quantas motocargas precisam de combustível;
- calcula **quantos litros cada motocarga vai receber**, dividindo igualmente o combustível entre todas elas.

---

## Como resolver passo a passo

1. **Leia dois números inteiros** da entrada:
   - o primeiro inteiro é a quantidade de litros de combustível no galão extra (`a`);
   - o segundo inteiro é a quantidade de motocargas que precisam de combustível (`b`).

2. **Converta um dos valores para número real** (por exemplo, `double` ou `float`) para que a divisão não seja inteira.  
   - Em muitas linguagens, você pode fazer algo como:
     - `resultado = (double)a / b;`

3. **Calcule a divisão**:
   - `resultado = a / b` (usando tipo real), que representa quantos litros cada motocarga receberá.

4. **Imprima o resultado com duas casas decimais**:
   - Use **ponto** como separador decimal.
   - Em C, por exemplo, você pode usar:
     - `printf("%.2f\n", resultado);`
   - Em outras linguagens, use o formato equivalente para sempre mostrar duas casas decimais.

O importante é que:
- você faça a divisão usando um tipo real;
- a saída sempre tenha **exatamente duas casas decimais**.

---

## Entrada

A entrada contém **dois valores inteiros**, que representam, respectivamente:

- a quantidade de combustível quântico no galão extra que Bruna trouxe nesta missão (em **litros**);
- a quantidade de **motocargas espaciais** que necessitam de combustível.

## Restrições

- \(a > 0\);
- \(b > 0\).

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

