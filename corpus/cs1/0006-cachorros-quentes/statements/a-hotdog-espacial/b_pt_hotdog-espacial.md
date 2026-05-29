# Média de Consumo na Arena Orbital

Na órbita de WOK-6 existe a arena gastronômica **HotDog Nexus**, onde
competidores de toda a galáxia participam de disputas de quem consome mais
unidades de *dogs cósmicos* em poucos minutos.

Os organizadores querem registrar em seus painéis holográficos a **média de
consumo por participante** em cada edição do evento, para comparar temporadas
e atrair novos patrocinadores interplanetários.

Para isso, depois de cada competição, o sistema central registra apenas dois
valores importantes:

- `H`: o número total de unidades de dogs cósmicos consumidas;  
- `P`: o número total de participantes que competiram naquela edição.

Sua tarefa é escrever um programa que calcule a média de unidades consumidas
por participante, com a precisão exigida pelos auditores da HotDog Nexus.

## Entrada

A entrada consiste de uma única linha contendo dois inteiros `H` e `P`
(`1 ≤ H, P ≤ 1000`), indicando respectivamente:

- `H` — o total de unidades de dogs cósmicos consumidas no evento;  
- `P` — o número de participantes.

## Saída

Seu programa deve produzir uma única linha contendo um número racional
representando a média de consumo por participante.  
O resultado deve ser escrito com **exatamente dois dígitos** após o ponto
decimal, arredondado se necessário.

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