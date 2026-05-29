# 0029 - Desempilhando Caixas | **Version**: 0.5
`desempilhando-caixas` | Difficulty: **C** | **Updated**: 2026-05-15 22:52:54


## Overview
Dadas N caixas em P pilhas arrumadas em fila, determine o número mínimo de caixas a desempilhar para recuperar a caixa 1, respeitando as restrições de acesso (topo e lado livre).

## Metadata
- **Author**: Unknown
- **Editorial**: Localize a caixa 1 em sua pilha e posição. Para cada direção (esquerda/direita), calcule o custo: caixas acima na mesma pilha + excesso de altura das pilhas adjacentes até encontrar um lado livre. A resposta é o mínimo entre os dois lados. Complexidade O(N) por caso.
- **Success Msg**: Parabéns!

| Time Limit | Memory Limit | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| -s | -MB | O(N) | - |

## Stats
| Metric | Count |
| :--- | :--- |
| Test Scenarios | 16 |
| Solutions | 2 |

## Statements
| ID | Status | Level | Natural Languages | Skills |
| :--- | :--- | :--- | :--- | :--- |
| `a-desempilhando-caixas` | ✅ | A | pt | stacks, simulation-ad-hoc |

## Test Scenarios
| Name | Description | Count | Type | Level |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Teste de Carga Máxima** | 50 casos com N=1000 caixas por arquivo. | 5 | Performance | A | stacks |
| **Fuzzing Aleatório** | 100 casos aleatórios de tamanho variado por arquivo. | 5 | TDD | B | simulation-ad-hoc |
| **Casos Extremos** | Caixa sozinha, pilha única gigante, caixa 1 na borda, pilhas uniformes. | 5 | TDD | C | stacks |
| **Exemplos do Enunciado** | Casos de teste do PDF original (ICPC 2007). | 1 | TDD | D | stacks |

## Solutions
- **Solução Ótima O(N)** (`a-otima-basica`)
  - Languages: `cpp, py, java`
- **Simulação Bruta** (`b-subotima-basica`)
  - Languages: `py`

## Components
- ✅ Statements
- ✅ Solutions
- ✅ Test Cases