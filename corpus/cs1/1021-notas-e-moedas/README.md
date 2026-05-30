# 1021 - Notas e Moedas | **Version**: 0.8
`notas-e-moedas` | Difficulty: **B** | **Updated**: 2026-04-09 08:22:34


## Overview
O problema solicita a decomposição de um valor monetário em cédulas e moedas de denominações específicas, visando a menor quantidade total de unidades. É um exercício clássico de lógica e tratamento de precisão numérica.

## Metadata
- **Author**: unknown
- **Editorial Author**: alessio
- **Editorial**: A solução segue uma estratégia gulosa, processando as moedas da maior para a menor denominação. A principal dificuldade é a imprecisão inerente ao ponto flutuante; a melhor prática é multiplicar o valor por 100, arredondar para o inteiro mais próximo e realizar os cálculos em centavos usando divisores e o operador de módulo.
- **Success Msg**: Parabéns! Você resolveu o problema do troco com precisão total.

| Time Limit | Memory Limit | Time Complexity | Space Complexity |
|:-----------|:-------------|:----------------|:-----------------|
| 1s         | 256MB        | O(1)            | -                |

## Stats
| Metric         | Count |
|:---------------|:------|
| Test Scenarios | 10    |
| Solutions      | 1     |

## Statements
| ID                 | Status | Level | Natural Languages | Skills |
|:-------------------|:-------|:------|:------------------|:-------|
| `a-notas-e-moedas` | ✅      | A     | pt                | -      |

## Test Scenarios
| Name                             | Description                                                                                            | Count | Type | Level |
|:---------------------------------|:-------------------------------------------------------------------------------------------------------|:------|:-----|:------|:-------|
| **Teste de Carga e Performance** | Cenários com valores máximos (1.000.000,00) e diversas combinações para forçar a eficiência da lógica. | 2     | TDD  | A     | -      |
| **Casos de Precisão Crítica**    | Valores que costumam gerar erros de arredondamento em ponto flutuante (ex: 0.01, 2.00, 5.00).          | 4     | TDD  | B     | -      |
| **Extremos e Limites**           | Testa o programa com o valor mínimo (0.00) e outras entradas de borda.                                 | 3     | TDD  | C     | -      |
| **Exemplo do Enunciado**         | Caso de teste padrão fornecido no enunciado do problema.                                               | 1     | TDD  | D     | -      |

## Solutions
- **Solução Ótima (Python)** (`optimal`)

## Components
- ✅ Statements
- ✅ Solutions
- ✅ Test Cases