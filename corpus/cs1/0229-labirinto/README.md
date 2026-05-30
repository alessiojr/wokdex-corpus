# 0229 - Labirinto | **Version**: 1.0
`labirinto` | Difficulty: **D** | **Updated**: 2026-04-15 21:15:21


## Overview
Problema clássico de descompressão RLE (Run-Length Encoding) em stream de caracteres. O núcleo algorítmico exige uma acumulação iterativa de dígitos ASCII para computar multiplicadores lineares sobre os tokens não numéricos subsequentes associados, em conjunto com o tratamento específico de quebra e espaçamento ('b', '!').

## Metadata
- **Author**: unknown
- **Editorial Author**: alessio
- **Editorial**: A estratégia ótima consiste em percorrer a string de entrada caractere por caractere em uma única passagem (O(N)). Deve-se manter um acumulador para a soma dos dígitos encontrados; ao encontrar um caractere não-dígito, imprime-se o caractere (ou espaço se for 'b') o número de vezes acumulado e reseta-se o contador. O caractere '!' deve disparar uma quebra de linha imediata sem consumir o acumulador de dígitos. UVA 445 (Marvelous Mazes).
- **Success Msg**: Implementação concluída com sucesso. O seu parser processou com êxito as transições sintáticas contínuas no regime ótimo.

| Time Limit | Memory Limit | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| 1s | 128MB | O(N) | - |

## Stats
| Metric | Count |
| :--- | :--- |
| Test Scenarios | 23 |
| Solutions | 3 |

## Statements
| ID | Status | Level | Natural Languages | Skills |
| :--- | :--- | :--- | :--- | :--- |
| `a-labirinto` | ✅ | A | pt | games |

## Test Scenarios
| Name | Description | Count | Type | Level |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Teste de Carga e Performance** | Labirintos gigantes com milhares de caracteres para testar eficiência. | 3 | TDD | A | io, loops |
| **Caso de Entrada Errada** | Quando a entrada não contém dígitos que resultariam em saída impressa. | 4 | TDD | B | condicionais |
| **EOF e Múltiplos Labirintos** | Processamento de múltiplos casos de teste até o fim do arquivo. | 1 | TDD | B | io, loops |
| **Caracteres Especiais e Símbolos** | Garante que qualquer caractere não-dígito (como @, #, $, %) seja tratado como símbolo gráfico. | 2 | TDD | B | characters |
| **Soma de Múltiplos Dígitos** | Testa a soma de vários dígitos consecutivos antes de um caractere. | 3 | TDD | C | characters |
| **Espaços e Quebras de Linha** | Foco no tratamento de 'b' como espaço e '!' como quebra de linha interna. | 3 | TDD | C | condicionais |
| **Falso Positivo (Multiplicação de '!')** | Testa se o caractere '!' é multiplicado indevidamente quando precedido por dígitos. | 2 | False-Green | C | condicionais |
| **Dígitos Consecutivos e Zeros** | Testa o comportamento com vários dígitos seguidos e zeros à esquerda (ex: 007X ou 99X). | 2 | TDD | C | loops, characters |
| **Exemplos do Enunciado** | Casos de teste fornecidos no enunciado para verificação básica. | 3 | TDD | D | io |

## Solutions
- **Solução Ótima (Parsing Unitário)** (`a-optimal`)
  - Languages: `java, c, cpp, py`
- **Solução Sub-ótima (Concatenação Ineficiente)** (`b-suboptimal`)
  - Languages: `py`
- **Solução Incorreta (Multiplica Exclamação)** (`c-wa-multiplica-exclamacao`)
  - Languages: `py`

## Components
- ✅ Statements
- ✅ Solutions
- ✅ Test Cases