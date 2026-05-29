# 0004 - Etiquetas Coloridas | **Version**: 1.0
`etiquetas-coloridas` | Difficulty: **D** | **Updated**: 2026-04-15 09:02:28


## Overview
Um problema sobre atribuir cores a etiquetas.

## Metadata
- **Author**: felipe-mendes
- **Editorial Author**: alessio
- **Editorial**: O problema pode ser resolvido com uma abordagem baseada na contagem das frequências de cada etiqueta e utilizando
map/dict. Alternativamente, ordenar e contar.

- **Success Msg**: Cores atribuídas e etiquetas contadas com perfeição. Parabéns!

| Time Limit | Memory Limit | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| 2s | 256MB | O(N logN) | - |

## Stats
| Metric | Count |
| :--- | :--- |
| Test Scenarios | 14 |
| Solutions | 2 |

## Statements
| ID | Status | Level | Natural Languages | Skills |
| :--- | :--- | :--- | :--- | :--- |
| `a-etiquetas-coloridas` | ✅ | A | en, pt | daily-life |

## Test Scenarios
| Name | Description | Count | Type | Level |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Carga Máxima O(N log N)** | Array randômico gigante com limites estourados. | 1 | Performance | A | complexity-analysis, hashing |
| **Casos Imenso Iguais** | Array imenso estourando int se não usar long long. | 1 | Performance | A | complexity-analysis, hashing |
| **Arrays Imensos Distintos** | Array com muitos números diferentes | 1 | Performance | A | complexity-analysis, hashing |
| **Testes Aleatórios** | Arrays randômicos blindados. | 5 | Performance | A | arrays, hashing |
| **Array Curto Todos Iguais** | Cenário cirúrgico onde todos os elementos são exatamente os mesmos. | 2 | TDD | B | arrays |
| **Array Curto Totalmente Distinto** | Cenário cirúrgico onde nada forma pares. | 2 | TDD | C | arrays |
| **Exemplo Básico** | Teste do exemplo do enunciado. | 2 | TDD | D | arrays, io |

## Solutions
- **Solução Ótima Básica** (`a-otima-basica`)
  - Languages: `cpp`
- **Solução Sub-ótima Força Bruta** (`b-forca-bruta`)
  - Languages: `cpp`

## Components
- ✅ Statements
- ✅ Solutions
- ✅ Test Cases