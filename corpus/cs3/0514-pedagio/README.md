# 0514 - Pedágio | **Version**: 0.5
`pedagio` | Difficulty: **A** | **Updated**: 2026-05-15 23:43:09


## Overview
Calcule o custo total de uma viagem dado o tamanho da estrada, distância entre os pedágios, custo por quilômetro e valor do pedágio.

## Metadata
- **Author**: Unknown
- **Editorial**: Problema básico de aritmética. O custo total é a soma do custo dos quilômetros rodados
(`L * K`) e o custo dos pedágios. O número de pedágios é `L / D` (divisão inteira).
Portanto, `Custo = (L * K) + (L / D) * P`. O limite máximo `10^4 * 10^4 = 10^8`
cabe em um inteiro de 32 bits, sem perigo de overflow.

- **Success Msg**: Viagem tranquila e custo calculado certinho!

| Time Limit | Memory Limit | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| -s | -MB | O(1) | - |

## Stats
| Metric | Count |
| :--- | :--- |
| Test Scenarios | 18 |
| Solutions | 2 |

## Statements
| ID | Status | Level | Natural Languages | Skills |
| :--- | :--- | :--- | :--- | :--- |
| `a-pedagio` | ✅ | A | pt | math, basic-io |

## Test Scenarios
| Name | Description | Count | Type | Level |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Teste de Carga Máxima** | Casos com os maiores valores possíveis. | 5 | Performance | A | math |
| **Fuzzing Aleatório** | Casos aleatórios com valores intermediários. | 5 | TDD | B | math |
| **Casos Extremos** | Valores mínimos (1), distância menor que o espaço entre pedágios, exato múltiplo. | 5 | TDD | C | basic-io |
| **Exemplos do Enunciado** | Casos de teste do PDF original (OBI 2010). | 3 | TDD | D | basic-io |

## Solutions
- **Fórmula O(1)** (`a-otima-basica`)
  - Languages: `cpp, py, java`
- **Simulação Iterativa** (`b-subotima-basica`)
  - Languages: `py`

## Components
- ✅ Statements
- ✅ Solutions
- ✅ Test Cases