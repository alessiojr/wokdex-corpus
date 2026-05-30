# 1329 - Cara ou Coroa | **Version**: 1.0
`cara-ou-coroa` | Difficulty: **D** | **Updated**: 2026-04-16 09:04:23


## Overview
O problema requer o processamento iterativo de rodadas binárias delimitadas por blocos dimensionais (N) e finalizadas por sentinela (N=0). O raciocínio central é aplicar uma contagem linear sequencial sobre a entrada O(N), acumulando ocorrências escalares distintas parciais.

## Metadata
- **Author**: sbc
- **Editorial**: A estratégia ótima demanda um modelo iterativo While gerido pelo limite sentinela (0). Lida-se estaticamente iterando no laço interno o scan do I/O, incrementando quantificadores locais via Switch/If condicional e emitindo sem alocar arrays massivos na memória.
- **Success Msg**: Contagem linear validada. Tratamento serial de buffer e laços aninhados foi corretamente implementado preservando a eficiência computacional mínima necessária.

| Time Limit | Memory Limit | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| 1s | 256MB | O(N) | - |

## Stats
| Metric | Count |
| :--- | :--- |
| Test Scenarios | 18 |
| Solutions | 1 |

## Statements
| ID | Status | Level | Natural Languages | Skills |
| :--- | :--- | :--- | :--- | :--- |
| `a-cara-ou-coroa` | ✅ | A | pt | daily-life |

## Test Scenarios
| Name | Description | Count | Type | Level |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Supercarga no Juiz (O(N*M))** | Teste agressivo limitando execuções precaristas que escalam acúmulos a O(N^2) forçando N no teto de 10000 laços. | 6 | Performance | A | io, loops |
| **Hegemonia de Único Ganhador** | Rodadas contendo zero diversidade estática (apenas seqüências maciçamente uníssonas de Mary 0 ou John 1 ininterruptos). | 3 | TDD | B | loops, condicionais |
| **Vetor Minúsculo N=1** | Menor fronteira permitida onde as condicionais estalam apenas uma vez e exigem o flush da saída correto na primeira passagem local sem estourar index. | 3 | TDD | C | condicionais |
| **Exemplo do Enunciado** | Casos de teste padrão da documentação original. | 3 | TDD | D | io, simulation-ad-hoc |
| **Fuzzing Cego Massivo** | Variações estocásticas impuras aleatórias para quebrar heurísticas fracas atadas ao Sample de mesa primário. | 3 | TDD | F | io, simulation-ad-hoc, loops |

## Solutions
- **Solução Ótima (Python e CPP)** (`a-otima-basica`)
  - Languages: `py, cpp`

## Components
- ✅ Statements
- ✅ Solutions
- ✅ Test Cases