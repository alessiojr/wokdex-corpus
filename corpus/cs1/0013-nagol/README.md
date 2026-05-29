# 0013 - Nagol | **Version**: 0.8
`nagol` | Difficulty: **D** | **Updated**: 2026-04-08 23:51:05


## Overview
Nagol é um designer de azulejos que aplica um padrão de riscos alternando entre as mãos direita e esquerda. O objetivo é calcular qual mão será utilizada em uma coordenada específica (X, Y) de uma grade L x C, seguindo uma ordem de preenchimento por linhas.

## Metadata
- **Author**: dami-henrique
- **Editorial Author**: alessio
- **Editorial**: O problema pode ser resolvido mapeando a coordenada bidimensional (X, Y) para um índice linear k em uma grade de C colunas, usando a fórmula k = X * C + Y. Como Nagol começa com a mão direita no índice 0 (par) e alterna a cada azulejo, a paridade de k define o resultado: se k for par, a mão é 'Direita'; se for ímpar, é 'Esquerda'. Devido aos limites de L e C (10^5), o uso de inteiros de 64 bits é essencial para calcular k antes da operação de módulo.
- **Success Msg**: Parabéns! Você desvendou a técnica milenar de Nagol com precisão matemática!

| Time Limit | Memory Limit | Time Complexity | Space Complexity |
|:-----------|:-------------|:----------------|:-----------------|
| 1s         | 128MB        | O(1)            | O(1)             |

## Stats
| Metric         | Count |
|:---------------|:------|
| Test Scenarios | 48    |
| Solutions      | 2     |

## Statements
| ID        | Status | Level | Natural Languages | Skills      |
|:----------|:-------|:------|:------------------|:------------|
| `a-nagol` | ✅      | A     | pt                | pop-culture |

## Test Scenarios
| Name                              | Description                                                                                                                                      | Count | Type | Level |
|:----------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------|:------|:-----|:------|:--------------------------------------|
| **Carga e Performance (O(1))**    | Gera grades de tamanho máximo (10^5 x 10^5) para forçar o uso de cálculos matemáticos no lugar de simulações. Também testa overflow de inteiros. | 2     | TDD  | A     | complexity-analysis, math-computing   |
| **Paridade e Transição de Linha** | Testa se a alternância de mão persiste corretamente ao mudar de linha, especialmente em grades com número de colunas par vs ímpar.               | 40    | TDD  | B     | basic-logic, mathematical-abstraction |
| **Limites de Coordenadas**        | Testa as posições de início (0,0) e fim (L-1, C-1) em grades médias.                                                                             | 1     | TDD  | B     | basic-logic                           |
| **Logica em Grades Pequenas**     | Testa grades mínimas (1x1, 1x2, 2x1) para validar o comportamento em limites de dimensões.                                                       | 3     | TDD  | C     | basic-logic                           |
| **Exemplos do Enunciado**         | Cenários básicos fornecidos no PDF para validação inicial.                                                                                       | 2     | TDD  | D     | io, basic-logic                       |

## Solutions
- **Solução Matemática O(1)** (`a-optimal`)
  - Languages: `java, py, cpp`
- **Simulação por Laços O(L*C)** (`b-bruteforce`)
  - Languages: `py`

## Components
- ✅ Statements
- ✅ Solutions
- ✅ Test Cases