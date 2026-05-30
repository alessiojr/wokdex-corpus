# 0458 - Pizza | **Version**: 1.0
`pizza` | Difficulty: **C** | **Updated**: 2026-05-07 09:38:25


## Overview
Nesta tarefa, você precisará ajudar o Rodrigo a encontrar a fatia contínua de pizza que possua a maior diferença a favor de cebolas em relação às azeitonas. Lembre-se de que a pizza tem formato circular e a fatia que você escolher pode dar a volta, conectando o final ao início!

## Metadata
- **Editorial Author**: alessio
- **Editorial**: **Briefing do Professor:**
Este problema é um excelente exercício intermediário para consolidar o entendimento de Programação Dinâmica unidimensional e raciocínio de vetores, focando no problema da Subsequência Contígua de Soma Máxima. O aluno precisa ter familiaridade com arrays e com o Algoritmo de Kadane básico. A transição para um array circular o torna um ótimo exemplo para exercitar a lógica espacial e de complementos, encaixando-se perfeitamente após a introdução de Algoritmos Gulosos ou DP.

**Resumo da Estratégia:**
A intuição chave é perceber que a maior fatia pode estar no centro do array ou cruzando as bordas. Para o centro, basta rodar o Kadane normal (buscando a maior soma). Para as bordas, a lógica é baseada em complementos matemáticos: o melhor pedaço pelas bordas equivale à pizza inteira menos o *pior* pedaço no meio. Portanto, calculamos o total do array e subtraímos o resultado de um Kadane invertido (que busca a menor soma contígua). O resultado final será o valor máximo entre o Kadane normal e a diferença (Total - Kadane Invertido). Cuidado especial com o edge case onde todos os elementos são negativos.
*Para os detalhes completos de implementação e dedução lógica, consulte o statement de nível D.*

- **Success Msg**: Incrível! Você encontrou a melhor fatia da pizza e maximizou as cebolas com sucesso!

| Time Limit | Memory Limit | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| 1s | -MB | O(N) | O(1) |

## Stats
| Metric | Count |
| :--- | :--- |
| Test Scenarios | 52 |
| Solutions | 1 |

## Statements
| ID | Status | Level | Natural Languages | Skills |
| :--- | :--- | :--- | :--- | :--- |
| `a-pizza` | ✅ | A | pt | daily-life |

## Test Scenarios
| Name | Description | Count | Type | Level |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Teste de Carga e Desempenho (O(N))** | Array máximo com N=100.000 forçando soluções quadráticas a TLE. | 13 | Performance | A | dynamic-programming |
| **Fatias Circulares (Kadane Invertido)** | Cenários que exigem obrigatoriamente que a solução dê a volta na pizza para encontrar a maior soma. | 20 | TDD | B | dynamic-programming, arrays |
| **Casos Extremos (Edge Cases)** | Apenas valores negativos, pequenos arrays, ou fatias puramente lineares sem elementos circulares. | 16 | TDD | C | arrays |
| **Exemplos** | Casos de teste de exemplo do enunciado. | 3 | TDD | D | dynamic-programming, arrays |

## Solutions
- **Solução Ótima (Python)** (`a-otima-basica`)
  - Languages: `py, cpp`

## Components
- ✅ Statements
- ✅ Solutions
- ✅ Test Cases