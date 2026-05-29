# 0039 - Dama | **Version**: 0.5
`dama` | Difficulty: **E** | **Updated**: 2026-05-15 23:03:53


## Overview
Calcular o número mínimo de movimentos para uma dama ir de uma casa a outra em um tabuleiro 8x8.

## Metadata
- **Author**: beecrowd
- **Editorial**: A solução exige apenas o conhecimento de como a peça Dama se move no Xadrez. 
- Se a casa de destino for igual à origem, são 0 movimentos.
- Se estiver na mesma linha, coluna ou na mesma diagonal, será 1 movimento. (Para checar a diagonal, a diferença absoluta das coordenadas X será igual à diferença absoluta das coordenadas Y).
- Caso contrário, a Dama sempre alcança qualquer casa em 2 movimentos.

- **Success Msg**: Checkmate! Você dominou o tabuleiro!

| Time Limit | Memory Limit | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| -s | -MB | O(1) | - |

## Stats
| Metric | Count |
| :--- | :--- |
| Test Scenarios | 17 |
| Solutions | 2 |

## Statements
| ID | Status | Level | Natural Languages | Skills |
| :--- | :--- | :--- | :--- | :--- |
| `a-dama` | ✅ | A | pt | board-games |

## Test Scenarios
| Name | Description | Count | Type | Level |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Teste de Casos Finais** | Limites máximos de combinações do tabuleiro. | 5 | Performance | A | conditionals |
| **Fuzzing Aleatório** | 200 posições aleatórias no tabuleiro por arquivo. | 5 | TDD | B | logic |
| **Casos Extremos do Tabuleiro** | Movimentos de uma ponta a outra e movimentos zerados. | 5 | TDD | C | conditionals |
| **Exemplos do Enunciado** | Casos de teste do PDF original (ICPC 2010). | 2 | TDD | D | conditionals |

## Solutions
- **Solução Ótima (Condicionais)** (`a-otima-basica`)
  - Languages: `cpp, py, java`
- **Solução Sub-Ótima** (`b-subotima`)
  - Languages: `py`

## Components
- ✅ Statements
- ✅ Solutions
- ✅ Test Cases