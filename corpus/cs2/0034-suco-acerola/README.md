# 0034 - Suco Acerola | **Version**: 0.5
`suco-acerola` | Difficulty: **C** | **Updated**: 2026-02-22 17:20:50

## Overview
O problema Suco de Acerola envolve cálculos aritméticos simples com divisão real e conversão de unidades. Dado o número de amigos e a quantidade de frutas (cada uma produzindo 50ml), deve-se calcular o volume em litros que cada amigo receberá, com duas casas decimais de precisão.

## Metadata

| Time Limit | Memory Limit | Time Complexity | Space Complexity |
|:-----------|:-------------|:----------------|:-----------------|
| -s         | -MB          | O(N)            | O(1)             |

## Stats
| Metric         | Count |
|:---------------|:------|
| Test Scenarios | 19    |
| Solutions      | 1     |

## Statements
| ID               | Status | Level | Natural Languages | Skills |
|:-----------------|:-------|:------|:------------------|:-------|
| `a-suco-acerola` | ✅      | A     | pt                | -      |

## Test Scenarios
| Name                               | Description                                                                                                                                                               | Count | Type        | Level |
|:-----------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------|:------------|:------|:---------------------------|
| **Muitos Casos de Teste**          | Grande quantidade de casos de teste consecutivos para verificar robustez do loop de leitura e ausência de vazamento de memória ou acúmulo de erro.                        | 2     | Performance | A     | while, io                  |
| **Múltiplos Casos Variados**       | Vários casos de teste com combinações variadas de N e F, incluindo N > F (resultado menor que 0.05), N = F, e F muito maior que N.                                        | 2     | TDD         | B     | operadores, while          |
| **Resultados Próximos de Zero**    | Casos onde N é grande e F é pequeno, resultando em valores muito pequenos (ex: 0.00 ou 0.01). Testa se a divisão real e a precisão decimal funcionam para valores baixos. | 2     | TDD         | B     | operadores, arredondamento |
| **Valores nos Limites Máximos**    | N e F nos valores máximos (1000). Testa N=1000, F=1000 e combinações extremas como N=1, F=1000 e N=1000, F=1.                                                             | 2     | TDD         | B     | operadores, while          |
| **Caso Único e Mínimos**           | Apenas um caso de teste antes do 0 0. Inclui valores mínimos (N=1, F=1) para verificar se o loop de leitura processa corretamente um único caso.                          | 3     | TDD         | C     | while, io                  |
| **Divisão Exata e Arredondamento** | Casos onde a divisão resulta em valores exatos (ex: 0.50, 1.00) e casos onde o truncamento/arredondamento na segunda casa decimal é relevante.                            | 2     | TDD         | C     | arredondamento, operadores |
| **Exemplos do Enunciado**          | Casos de teste fornecidos diretamente no enunciado. Valida se a leitura, o cálculo básico e a formatação estão corretos.                                                  | 1     | TDD         | D     | io, operadores             |

## Solutions
- **Solução Ótima** (`A-optimal`)
  - Languages: `cpp, py, java`

## Components
- ✅ Statements
- ✅ Solutions
- ✅ Test Cases