# 0010 - Operações | **Version**: 1.0
`operacoes` | Difficulty: **D** | **Updated**: 2026-02-12 15:39:49

## Overview
Implemente uma calculadora simples que realiza multiplicação ou divisão de dois números reais.

## Metadata
- **Author**: alessio
- **Editorial Author**: alessio
- **Editorial**: O problema exige o uso de estrutura condicional (`if/else` ou `switch`) para decidir qual operação matemática realizar.  

1. Leia um caractere que define a operação.
2. Leia dois números reais (A e B).
3. Se o caractere for 'M', calcule $R = A \times B$.
4. Se o caractere for 'D', calcule $R = A / B$.
5. Imprima $R$ formatado com duas casas decimais (ex: `%.2f` em C/Python ou `String.format` em Java).
- **Success Msg**: Ótimo trabalho! Você aprendeu a combinar entrada de caracteres com operações aritméticas condicionais.

| Time Limit | Memory Limit | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| 1s | 128MB | O(1) | O(1) |

## Stats
| Metric | Count |
| :--- | :--- |
| Test Scenarios | 17 |
| Solutions | 1 |

## Statements
| ID | Status | Level | Natural Languages | Skills |
| :--- | :--- | :--- | :--- | :--- |
| `pt-BR_easy` | ⚠️ Format | A | None | wok |

## Test Scenarios
| Name | Description | Count | Type | Level |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Exemplos** | Entrada básica de exemplo do exercício. | 4 | TDD | A | io, condicional |
| **Multiplicação Simples** | Testes apenas com operação de multiplicação. | 3 | TDD | B | aritmetica |
| **Divisão Simples** | Testes apenas com operação de divisão. | 3 | TDD | B | aritmetica |
| **Precisão Decimal** | Testes que exigem precisão na formatação float. | 3 | TDD | C | io |

## Solutions
- **Solução Ótima** (`A-optimal`)
  - Languages: `cpp, python, java`

## Components
- ✅ Statements
- ✅ Solutions
- ✅ Test Cases