# 0632 - Monk e a Ordenação | **Version**: 1.0
`monk-e-a-ordenacao` | Difficulty: **C** | **Updated**: 2026-03-23 09:21:04


## Overview
Implementação de Radix Sort baseado em blocos de 5 dígitos, exibindo o estado do array após cada passo de ordenação.

## Metadata
- **Author**: alessio
- **Editorial Author**: alessio
- **Editorial**: A ideia do Radix Sort é fazer a classificação dígito por dígito. Neste problema, classificamos os números em blocos de 5 dígitos (base 100.000) e exibimos o vetor após cada passagem.
- **Success Msg**: Parabéns! Você dominou a lógica do Radix Sort e a manipulação de dígitos em bases customizadas.

| Time Limit | Memory Limit | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| 1s | 128MB | O(N) | O(N) |

## Stats
| Metric | Count |
| :--- | :--- |
| Test Scenarios | 17 |
| Solutions | 1 |

## Statements
| ID | Status | Level | Natural Languages | Skills |
| :--- | :--- | :--- | :--- | :--- |
| `a-monk-e-a-ordenacao` | ✅ | A | en, pt | biologia |
| `a-wok-monk` | ✅ | A | pt | wok |

## Test Scenarios
| Name | Description | Count | Type | Level |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Teste de Estresse (N=10^6)** | Validar a eficiência da implementação com o limite máximo de elementos (1 milhão). | 4 | TDD | A | ordenacao |
| **Valores Altos (10^18)** | Validar se o algoritmo lida corretamente com números de até 18 dígitos, exigindo múltiplas passagens do Radix Sort. | 3 | TDD | B | radix-sort |
| **Números Pequenos** | Teste com números que possuem menos de 5 dígitos para validar o preenchimento com zeros à esquerda no cálculo do peso. | 8 | TDD | C | lacos |
| **Exemplo do Enunciado** | Caso básico fornecido no enunciado para validar a lógica inicial. | 2 | TDD | D | io, logica |

## Solutions
- **Solução Ótima (Radix Sort)** (`a-optimal`)
  - Languages: `py, cpp, java, java, java`

## Components
- ✅ Statements
- ✅ Solutions
- ✅ Test Cases