# 0345 - Bakugan | **Version**: 1.0
`bakugan` | Difficulty: **C** | **Updated**: 2026-04-15 21:43:26


## Overview
Mark e Leti jogam bolas Bakugan em uma competição de R rodadas. O objetivo é calcular a pontuação total considerando um bônus de 30 pontos para o primeiro jogador a conseguir três monstros idênticos consecutivos, desde que o oponente não consiga o mesmo feito na mesma rodada.

## Metadata
- **Author**: unknown
- **Editorial Author**: alessio
- **Editorial**: A solução requer a simulação das R rodadas, acumulando os pontos de cada monstro. Deve-se monitorar sequências de três monstros iguais para ambos os jogadores. O bônus de 30 pontos é atribuído apenas ao primeiro jogador que completar a sequência, a menos que ambos completem na mesma rodada, caso em que ninguém recebe o bônus.
- **Success Msg**: Excelente! Você ajudou Mark e Leti a anunciar o vencedor!

| Time Limit | Memory Limit | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| 1s | 256MB | O(N) | - |

## Stats
| Metric | Count |
| :--- | :--- |
| Test Scenarios | 84 |
| Solutions | 2 |

## Statements
| ID | Status | Level | Natural Languages | Skills |
| :--- | :--- | :--- | :--- | :--- |
| `a-bakugan` | ✅ | A | pt | games |

## Test Scenarios
| Name | Description | Count | Type | Level |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Carga de Desempenho (R=10^5)** | Cenário com o limite máximo de rodadas para verificar a eficiência do processamento O(R). | 4 | TDD | A | arrays, loops |
| **Bônus Simultâneo** | Ambos os jogadores completam três monstros iguais na mesma rodada pela primeira vez. | 19 | TDD | B | condicionais, simulation-ad-hoc |
| **Corrida pelo Bônus** | Teste onde um jogador completa o trio logo antes do outro, garantindo a vantagem. | 23 | TDD | B | condicionais, simulation-ad-hoc |
| **Partida Curta (R < 3)** | Casos onde o número de rodadas não permite que ninguém complete um trio. | 33 | TDD | C | arrays, condicionais |
| **Exemplos do Enunciado** | Casos de teste básicos fornecidos no exemplo oficial. | 5 | TDD | D | loops, simulation-ad-hoc |

## Solutions
- **Solução Ótima** (`a-optimal`)
  - Languages: `py, cpp, java`
- **Busca Dinâmica Retrospectiva O(R^2)** (`b-suboptimal`)
  - Languages: `py`

## Components
- ✅ Statements
- ✅ Solutions
- ✅ Test Cases