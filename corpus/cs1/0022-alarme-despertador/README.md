# 0022 - Alarme Despertador | **Version**: 1.0
`alarme-despertador` | Difficulty: **D** | **Updated**: 2026-04-15 21:07:56


## Overview
Determina a defasagem temporal em minutos absolutos entre dois instantes isolados formatados em base 24h. O núcleo algorítmico requer modelagem aritmética cíclica combinada a varreduras contínuas (indeterminadas) terminadas por flags de limite estrito.

## Metadata
- **Author**: sbc
- **Editorial Author**: alessio
- **Editorial**: O problema alarme despertador é um problema que testa operações matemáticas de um controle condicional simples.
- **Success Msg**: Lógica consolidada com sucesso. Os intervalos temporais e as defasagens de limite cíclico foram avaliados perfeitamente.

| Time Limit | Memory Limit | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| 1s | 128MB | O(1) | O(1) |

## Stats
| Metric | Count |
| :--- | :--- |
| Test Scenarios | 11 |
| Solutions | 2 |

## Statements
| ID | Status | Level | Natural Languages | Skills |
| :--- | :--- | :--- | :--- | :--- |
| `a-alarme-despertador` | ✅ | A | pt | daily-life |

## Test Scenarios
| Name | Description | Count | Type | Level |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Teste de Desempenho (Carga Máxima)** | Cenário com milhares de casos de teste para validar a eficiência de input/output e o loop infinito de leitura. | 1 | TDD | A | loops, io |
| **Múltiplas Entradas por Arquivo** | Valida a leitura em laço de diversas entradas seguidas. | 1 | TDD | B | loops |
| **Dia Invertido (Meia-noite)** | Valida casos onde o horário de acordar é menor que o horário de dormir, exigindo uma adição de 1440 minutos. | 5 | TDD | B | math-computing, condicionais |
| **Testes Simples no Mesmo Dia** | Casos em que o alarme toca no mesmo dia: instante do final é maior que o instante inicial, sem troca de data. | 1 | TDD | C | math-computing |
| **Casos de Mesmo Horário** | Valida o caso especial onde o horário atual é igual ao horário de despertar (deve resultar em 1440 minutos). | 1 | TDD | C | math-computing, condicionais |
| **Testes de Exemplo do Problema (Sample)** | Cenário base contendo estritamente os exemplos demonstrados no PDF da competição. | 2 | TDD | D | io |

## Solutions
- **Solução Ótima** (`a-optimal`)
  - Languages: `c, py, cpp, por, java, java`
- **Solução Sub-ótima** (`b-suboptimal`)
  - Languages: `cpp, py`

## Components
- ✅ Statements
- ✅ Solutions
- ✅ Test Cases