# 0389 - Letras | **Version**: 1.0
`letras-o15` | Difficulty: **B** | **Updated**: 2026-05-07 14:38:38


## Overview
Neste problema você recebe uma cadeia de caracteres (contendo letras de 'A' a 'Z') e precisa encontrar o tamanho da maior subsequência que forma uma sequência crescente de letras no alfabeto (permitindo letras iguais). Este é um desafio clássico que exige otimização para lidar com entradas grandes!

## Metadata
- **Editorial**: Pedagogicamente, este é um problema essencial para o ensino avançado de Programação Dinâmica, modelando o clássico algoritmo de Longest Increasing Subsequence (LIS). É recomendado para alunos que já dominam conceitos básicos de algoritmos e precisam explorar limites de tempo restritos, se encaixando bem em currículos de algoritmos avançados.

A chave do problema é notar que uma abordagem ingênua em O(N^2) será reprovada para N até 300.000. O estudante deve combinar Programação Dinâmica com Busca Binária, mantendo um vetor auxiliar que armazena a menor letra final possível para subsequências de cada comprimento. Usando busca binária (como `upper_bound`), atualiza-se o vetor em tempo O(log N) para cada caractere. Isso garante a complexidade final de O(N log N). Para detalhes completos de implementação, consulte o enunciado de nível D.

- **Success Msg**: Excelente! Você dominou o algoritmo LIS em O(N log N) e lidou perfeitamente com os limites rigorosos de tempo!

| Time Limit | Memory Limit | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| 2s | -MB | O(N logN) | - |

## Stats
| Metric | Count |
| :--- | :--- |
| Test Scenarios | 66 |
| Solutions | 2 |

## Statements
| ID | Status | Level | Natural Languages | Skills |
| :--- | :--- | :--- | :--- | :--- |
| `a-letras-o15` | ✅ | A | pt | wok |

## Test Scenarios
| Name | Description | Count | Type | Level |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Performance Máxima (N = 300.000)** | String de tamanho 300.000 para testar complexidade O(N log N). Um LIS em O(N^2) vai dar TLE. | 29 | Performance | A | binary-search |
| **Anti-Guloso** | String que pune soluções gulosas puras ou soluções que não lidam com reposição/backtracking adequado, como 'ZAAAAAA'. | 16 | False-Green | B | longest-increasing-subsequence |
| **Sequência Não-Decrescente (Letras Repetidas)** | Teste onde a sequência possui letras iguais, garantindo que o algoritmo calcula LIS não-decrescente em vez de LIS estrito. | 3 | TDD | C | longest-increasing-subsequence |
| **Casos Extremos Básicos** | Tamanho N=1, sequência já perfeitamente crescente e sequência inversamente ordenada. | 15 | TDD | C | longest-increasing-subsequence |
| **Sample** | Casos de teste de exemplo do enunciado. | 3 | TDD | D | longest-increasing-subsequence |

## Solutions
- **Solução Ótima** (`a-optimal`)
  - Languages: `py, cpp, java`
- **Solução Sub-ótima O(N^2)** (`b-suboptimal`)
  - Languages: `py, py`

## Components
- ✅ Statements
- ✅ Solutions
- ✅ Test Cases