# 0048 - Sub-prime | **Version**: 0.5
`sub-prime` | Difficulty: **C** | **Updated**: 2026-05-15 23:15:20


## Overview
Dados B bancos com reservas monetárias e N debêntures entre eles, determinar se todos conseguem liquidar suas dívidas usando reservas e créditos.

## Metadata
- **Author**: Unknown
- **Editorial**: Para cada banco, calcule o saldo líquido: reserva + soma dos créditos - soma das dívidas.
Se todos os saldos forem ≥ 0, a resposta é S; caso contrário, N.
A chave é perceber que a ordem de pagamento não importa: basta verificar o balanço final.

- **Success Msg**: Parabéns! O sistema financeiro foi salvo!

| Time Limit | Memory Limit | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| -s | -MB | O(B+N) | - |

## Stats
| Metric | Count |
| :--- | :--- |
| Test Scenarios | 16 |
| Solutions | 2 |

## Statements
| ID | Status | Level | Natural Languages | Skills |
| :--- | :--- | :--- | :--- | :--- |
| `a-sub-prime` | ✅ | A | pt | simulation-ad-hoc, arrays |

## Test Scenarios
| Name | Description | Count | Type | Level |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Teste de Carga Máxima** | 100 casos com B=20, N=20 por arquivo. | 5 | Performance | A | arrays |
| **Fuzzing Aleatório** | 50 casos aleatórios de tamanho variado por arquivo. | 5 | TDD | B | simulation-ad-hoc |
| **Casos Extremos** | Reservas zeradas, ciclos perfeitos, dívidas desbalanceadas, B máximo. | 5 | TDD | C | conditionals |
| **Exemplos do Enunciado** | Casos de teste do PDF original (ICPC 2009). | 1 | TDD | D | conditionals |

## Solutions
- **Solução Ótima O(B+N)** (`a-otima-basica`)
  - Languages: `cpp, py, java`
- **Simulação Iterativa (WA intencional)** (`b-subotima-basica`)
  - Languages: `py`

## Components
- ✅ Statements
- ✅ Solutions
- ✅ Test Cases