# Estatísticas de Consumo Orbital

Na arena espacial **HotDog Nexus**, os organizadores querem entender melhor
o perfil de consumo médio dos participantes. Para isso, precisam calcular a
**média de unidades de dogs cósmicos consumidas por competidor** em cada
edição do torneio.

Você receberá:

- o total consumido `H` (quantidade de dogs cósmicos devorados), e  
- o total de participantes `P`.

Matematicamente, a média que deve ser exibida nos painéis é:

$$ \text{Média} = \frac{H}{P} $$

Essa média precisa ser apresentada com **duas casas decimais**, pois os
auditores intergalácticos exigem um formato uniforme para todos os eventos.

### Dica sobre implementação

Em muitas linguagens, dividir dois inteiros faz uma **divisão inteira**
(por exemplo, `10 / 4 = 2`), descartando a parte decimal.  
Para obter um resultado como `2.50` ou `0.11`, você deve garantir que
pelo menos um dos operandos seja tratado como número de ponto flutuante
(`float`, `double`, etc.) antes da divisão.

Depois de calcular a média como número real, formate a saída para ter
**exatamente duas casas decimais**, usando a função de formatação
apropriada da linguagem (por exemplo, `printf("%.2f\n", x)` em C ou
`format(x, ".2f")` em muitas outras).

## Entrada

A entrada contém uma única linha com dois números inteiros `H` e `P`
(`1 ≤ H, P ≤ 1000`), representando o total de units de dogs cósmicos
consumidas e o total de participantes.

## Saída

Imprima o valor da média `H / P` com **exatamente dois dígitos** após
o ponto decimal.

## Exemplos

| Input | Output |
| :---- | -----: |
| `10 90` | `0.11` |

| Input | Output |
| :---- | -----: |
| `840 11` | `76.36` |

| Input | Output |
| :---- | -----: |
| `1 50` | `0.02` |

| Input | Output |
| :---- | -----: |
| `34 1000` | `0.03` |

| Input | Output |
| :---- | -----: |
| `35 1000` | `0.04` |

| Input | Output |
| :---- | -----: |
| `36 1000` | `0.04` |
