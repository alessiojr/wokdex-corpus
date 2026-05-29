# 0005 - Concurso Contos | **Version**: 0.8
`concurso-contos` | Difficulty: **C** | **Updated**: 2026-04-06 09:45:06


## Overview
Calcule o número mínimo de páginas necessárias para um conto dadas as restrições de formatação.

## Metadata
- **Success Msg**: Conto formatado com sucesso!

| Time Limit | Memory Limit | Time Complexity | Space Complexity |
|:-----------|:-------------|:----------------|:-----------------|
| -s         | -MB          | O(N)            | -                |

## Stats
| Metric         | Count |
|:---------------|:------|
| Test Scenarios | 33    |
| Solutions      | 0     |

## Statements
| ID                  | Status | Level | Natural Languages | Skills  |
|:--------------------|:-------|:------|:------------------|:--------|
| `a-concurso-contos` | ✅      | A     | pt                | strings |

## Test Scenarios
| Name                             | Description                                                                                                    | Count | Type | Level |
|:---------------------------------|:---------------------------------------------------------------------------------------------------------------|:------|:-----|:------|:---------------------------------------------|
| **Performance e Carga Máxima**   | Teste com o número máximo de palavras (1000) para garantir a eficiência da solução.                            | 3     | TDD  | A     | complexity-analysis, lacos, algoritmo-guloso |
| **Verificação da Lógica Gulosa** | Garante o tratamento correto de espaços entre as palavras e as quebras de linha/página.                        | 25    | TDD  | B     | algoritmo-guloso, conditionals, basic-logic  |
| **Casos de Borda e Limites**     | Testa o comportamento com palavras de comprimento máximo (C) e contos que preenchem exatamente as páginas (L). | 1     | TDD  | C     | strings, basic-logic, algoritmo-guloso       |
| **Exemplos do Enunciado**        | Casos de teste básicos fornecidos na descrição do problema para verificação inicial.                           | 4     | TDD  | D     | entrada-saida, strings, algoritmo-guloso     |

## Components
- ✅ Statements
- ✅ Solutions
- ✅ Test Cases