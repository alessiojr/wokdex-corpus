# 0339 - Ajuda | **Version**: 1.0
`ajuda` | Difficulty: **D** | **Updated**: 2026-04-15 21:26:11


## Overview
Dado um log de submissões de uma competição de programação, calcule a quantidade de problemas resolvidos e a penalidade total de tempo seguindo as regras do ICPC.

## Metadata
- **Author**: Unknown
- **Editorial Author**: alessio
- **Editorial**: O problema pede a implementação do sistema de pontuação padrão do ICPC. Para resolvê-lo, é necessário manter o estado de cada problema (de 'A' a 'Z'). Um array de booleanos pode indicar se o problema já foi resolvido, e um array de inteiros pode acumular as penalidades (20 min) de cada submissão incorreta. A regra crucial é que as penalidades de tempo de um problema só são somadas ao total geral se e quando o problema for resolvido ('correct'). Submissões após o primeiro 'correct' de um mesmo problema devem ser ignoradas.
- **Success Msg**: Parabéns! Você implementou a lógica básica de um corretor de maratona de programação.

| Time Limit | Memory Limit | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| -s | -MB | O(N) | - |

## Stats
| Metric | Count |
| :--- | :--- |
| Test Scenarios | 19 |
| Solutions | 2 |

## Statements
| ID | Status | Level | Natural Languages | Skills |
| :--- | :--- | :--- | :--- | :--- |
| `a-ajuda` | ✅ | A | pt | wok |

## Test Scenarios
| Name | Description | Count | Type | Level |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Limite Máximo (N=300)** | Log complexo com o número máximo de submissões e tempo limite. | 4 | TDD | A | loops, io |
| **Problemas Não Resolvidos** | Problemas com submissões incorretas que nunca foram resolvidos não devem somar penalidade. | 3 | TDD | B | arrays, condicionais |
| **Múltiplos Casos de Teste** | Vários conjuntos de submissões em uma única execução para testar o reset de variáveis. | 3 | TDD | B | loops, arrays |
| **Submissões Únicas** | Cada problema possui apenas uma submissão, facilitando a depuração inicial. | 3 | TDD | C | condicionais |
| **Submissões Pós-Acerto** | Verifica se o sistema ignora corretamente submissões (corretas ou incorretas) após o primeiro acerto. | 3 | TDD | C | condicionais |
| **Exemplos do Enunciado** | Casos de teste básicos fornecidos no problema original. | 3 | TDD | D | io |

## Solutions
- **Soluções Oficiais** (`a-optimal`)
  - Languages: `py, c, java`
- **Soluções Incorretas** (`c-wa`)
  - Languages: `py, java`

## Components
- ✅ Statements
- ✅ Solutions
- ✅ Test Cases