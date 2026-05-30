# 0523 - Dentista | **Version**: 1.0
`dentista` | Difficulty: **C** | **Updated**: 2026-04-15 21:44:18


## Overview
Otimização de agendamento (Interval Scheduling) utilizando paradigma guloso (Greedy). O fluxo lógico visa encontrar o subconjunto máximo de matrizes não-sobrepostas, exigindo ordenação prévia por limite de offset seguida por roteirização linear O(N).

## Metadata
- **Editorial Author**: alessio
- **Editorial**: Para resolver este problema de seleção de intervalos (Interval Scheduling), utilize uma abordagem gulosa. Primeiro, ordene todas as consultas pelo horário de término (Y). Em seguida, itere sobre elas, selecionando sempre a primeira consulta que não se sobrepõe ao término da última selecionada.
- **Success Msg**: Mapeamento validado. A estratégia gulosa maximizou com eficiência a seleção de intervalos O(N log N) e lidou estritamente com os limites condicionais.

| Time Limit | Memory Limit | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| 1s | 256MB | O(N logN) | - |

## Stats
| Metric | Count |
| :--- | :--- |
| Test Scenarios | 39 |
| Solutions | 2 |

## Statements
| ID | Status | Level | Natural Languages | Skills |
| :--- | :--- | :--- | :--- | :--- |
| `a-dentista` | ✅ | A | pt | daily-life |

## Test Scenarios
| Name | Description | Count | Type | Level |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Volume Máximo de Dados** | Testa a robustez da solução com o limite máximo de 10.000 consultas e dados aleatórios. | 22 | TDD | A | loops, sorting |
| **Teste de Performance e Carga** | Stress-test com 10.000 intervalos e padrões de sobreposição complexos (intervalos aninhados). | 6 | TDD | A | greedy-algorithms, sorting |
| **Caso Unitário** | Testa o limite inferior com apenas uma consulta agendada. | 0 | TDD | B | arrays |
| **Estratégia de Ordenação** | Testa casos onde ordenar por início ou duração falha, garantindo que o aluno ordenou por término. | 4 | TDD | B | greedy-algorithms, sorting |
| **Consultas Contíguas** | Testa o caso onde uma consulta termina exatamente no mesmo instante em que a próxima começa. | 4 | TDD | C | greedy-algorithms |
| **Caso Exemplo** | Valida a lógica básica com os exemplos fornecidos no enunciado. | 3 | TDD | D | arrays, loops |

## Solutions
- **A-Optimal** (`a-optimal`)
  - Languages: `cpp, java, py`
- **B-Sub-optimal** (`b-suboptimal`)
  - Languages: `py`

## Components
- ✅ Statements
- ✅ Solutions
- ✅ Test Cases