# Analysis Report: 1281-ida-a-freira
**Generated at:** 2026-03-18 02:14:57

Analysis Report for: 1281-ida-a-freira
Generated at: 2026-03-18 02:14:57
========================================

[Structure Check]
  - statements: FOUND
  - solutions: FOUND
  - test-cases: FOUND

[Statements Analysis]
  - Total Statements in Metadata: 1
  - ID 'a-ida-a-feira' (Level A): ✅ FOUND (a-ida-a-feira)
    - Languages (1): pt

[Statistics]
  - Test Cases: 16
  - Solutions: 3
  - ID 'a-optimal' (Level A): 
  - ID 'b-suboptimal' (Level B): 
  - ID 'c-falso-duplicados' (Level C): 

[Metadata Validation]
  ✅ Schema Valid

[Test Scenarios Directory Check]
  - ID 'd-sample' (Level D): ✅ FOUND (d-sample)
  - ID 'c-simples' (Level C): ✅ FOUND (c-simples)
  - ID 'c-precos-zerados' (Level C): ✅ FOUND (c-precos-zerados)
  - ID 'b-volume-dados' (Level B): ✅ FOUND (b-volume-dados)
  - ID 'b-precisao-moeda' (Level B): ✅ FOUND (b-precisao-moeda)
  - ID 'a-itens-duplicados' (Level A): ✅ FOUND (a-itens-duplicados)
  - ID 'a-produtos-inexistentes' (Level A): ✅ FOUND (a-produtos-inexistentes)

## Test Scenarios (grid)
| Scenario | TestType | Level | Count |
| :--- | :--- | :--- | :--- |
| d-sample | TDD | D | 2 |
| c-simples | TDD | C | 3 |
| c-precos-zerados | TDD | C | 2 |
| b-volume-dados | TDD | B | 2 |
| b-precisao-moeda | TDD | B | 3 |
| a-itens-duplicados | False-Green | A | 2 |
| a-produtos-inexistentes | TDD | A | 2 |

[Test Scenarios & Cases]
  - **Scenario: a-itens-duplicados** (2 cases) — type: **False-Green**
    - [False-Green] itens-duplicados-01: ✅ Synced (ID: 14498)
    - [False-Green] itens-duplicados-02: ✅ Synced (ID: 14499)
  - **Scenario: a-produtos-inexistentes** (2 cases) — type: **TDD**
    - [TDD] produtos-inexistentes-01: ✅ Synced (ID: 14500)
    - [TDD] produtos-inexistentes-02: ✅ Synced (ID: 14501)
  - **Scenario: b-precisao-moeda** (3 cases) — type: **TDD**
    - [TDD] precisao-moeda-01: ✅ Synced (ID: 14493)
    - [TDD] precisao-moeda-02: ✅ Synced (ID: 14494)
    - [TDD] precisao-moeda-03: ✅ Synced (ID: 14495)
  - **Scenario: b-volume-dados** (2 cases) — type: **TDD**
    - [TDD] volume-dados-01: ✅ Synced (ID: 14496)
    - [TDD] volume-dados-02: ✅ Synced (ID: 14497)
  - **Scenario: c-precos-zerados** (2 cases) — type: **TDD**
    - [TDD] precos-zerados-01: ✅ Synced (ID: 14488)
    - [TDD] precos-zerados-02: ✅ Synced (ID: 14489)
  - **Scenario: c-simples** (3 cases) — type: **TDD**
    - [TDD] simples-01: ✅ Synced (ID: 14490)
    - [TDD] simples-02: ✅ Synced (ID: 14491)
    - [TDD] simples-03: ✅ Synced (ID: 14492)
  - **Scenario: d-sample** (2 cases) — type: **TDD**
    - [TDD] sample-01: ✅ Synced (ID: 14486)
    - [TDD] sample-02: ✅ Synced (ID: 14487)

## Solutions Check Report
**Generated**: 2026-04-15T23:53:34.978384

Found 5 solution(s) and 16 test case(s).

## Solution: `solutions/a-optimal/solve.py`
- **Compilation**: No compilation needed
| Test Case | Result | Time (s) |
| :--- | :--- | :--- |
| a-itens-duplicados - False-Green | | |
| itens-duplicados-01.in | ✅ WA (expected) | 0.017 |
| itens-duplicados-02.in | ✅ WA (expected) | 0.010 |
| a-produtos-inexistentes - TDD | | |
| produtos-inexistentes-01.in | ✅ PASS | 0.010 |
| produtos-inexistentes-02.in | ✅ PASS | 0.019 |
| b-precisao-moeda - TDD | | |
| precisao-moeda-01.in | ✅ PASS | 0.017 |
| precisao-moeda-02.in | ✅ PASS | 0.008 |
| precisao-moeda-03.in | ✅ PASS | 0.010 |
| b-volume-dados - TDD | | |
| volume-dados-01.in | ✅ PASS | 0.021 |
| volume-dados-02.in | ✅ PASS | 0.020 |
| c-precos-zerados - TDD | | |
| precos-zerados-01.in | ✅ PASS | 0.022 |
| precos-zerados-02.in | ✅ PASS | 0.022 |
| c-simples - TDD | | |
| simples-01.in | ✅ PASS | 0.016 |
| simples-02.in | ✅ PASS | 0.011 |
| simples-03.in | ✅ PASS | 0.010 |
| d-sample - TDD | | |
| sample-01.in | ✅ PASS | 0.010 |
| sample-02.in | ✅ PASS | 0.010 |

## Solution: `solutions/a-optimal/solve.cpp`
- **Compilation**: /dados/projetos/mundoDoCodigo/problemas/pack-tecnicas/workspace/1281-ida-a-freira/solutions/a-optimal/solve.out
| Test Case | Result | Time (s) |
| :--- | :--- | :--- |
| a-itens-duplicados - False-Green | | |
| itens-duplicados-01.in | ✅ WA (expected) | 0.002 |
| itens-duplicados-02.in | ✅ WA (expected) | 0.002 |
| a-produtos-inexistentes - TDD | | |
| produtos-inexistentes-01.in | ✅ PASS | 0.001 |
| produtos-inexistentes-02.in | ✅ PASS | 0.001 |
| b-precisao-moeda - TDD | | |
| precisao-moeda-01.in | ✅ PASS | 0.002 |
| precisao-moeda-02.in | ✅ PASS | 0.002 |
| precisao-moeda-03.in | ✅ PASS | 0.001 |
| b-volume-dados - TDD | | |
| volume-dados-01.in | ✅ PASS | 0.002 |
| volume-dados-02.in | ✅ PASS | 0.002 |
| c-precos-zerados - TDD | | |
| precos-zerados-01.in | ✅ PASS | 0.003 |
| precos-zerados-02.in | ✅ PASS | 0.002 |
| c-simples - TDD | | |
| simples-01.in | ✅ PASS | 0.002 |
| simples-02.in | ✅ PASS | 0.003 |
| simples-03.in | ✅ PASS | 0.003 |
| d-sample - TDD | | |
| sample-01.in | ✅ PASS | 0.003 |
| sample-02.in | ✅ PASS | 0.004 |

## Solution: `solutions/a-optimal/solve.java`
- **Compilation**: Compilation successful
| Test Case | Result | Time (s) |
| :--- | :--- | :--- |
| a-itens-duplicados - False-Green | | |
| itens-duplicados-01.in | ✅ WA (expected) | 0.077 |
| itens-duplicados-02.in | ✅ WA (expected) | 0.061 |
| a-produtos-inexistentes - TDD | | |
| produtos-inexistentes-01.in | ✅ PASS | 0.058 |
| produtos-inexistentes-02.in | ✅ PASS | 0.059 |
| b-precisao-moeda - TDD | | |
| precisao-moeda-01.in | ✅ PASS | 0.070 |
| precisao-moeda-02.in | ✅ PASS | 0.096 |
| precisao-moeda-03.in | ✅ PASS | 0.057 |
| b-volume-dados - TDD | | |
| volume-dados-01.in | ✅ PASS | 0.086 |
| volume-dados-02.in | ✅ PASS | 0.087 |
| c-precos-zerados - TDD | | |
| precos-zerados-01.in | ✅ PASS | 0.057 |
| precos-zerados-02.in | ✅ PASS | 0.068 |
| c-simples - TDD | | |
| simples-01.in | ✅ PASS | 0.060 |
| simples-02.in | ✅ PASS | 0.048 |
| simples-03.in | ✅ PASS | 0.044 |
| d-sample - TDD | | |
| sample-01.in | ✅ PASS | 0.046 |
| sample-02.in | ✅ PASS | 0.064 |

## Solution: `solutions/b-suboptimal/brute.py`
- **Compilation**: No compilation needed
| Test Case | Result | Time (s) |
| :--- | :--- | :--- |
| a-itens-duplicados - False-Green | | |
| itens-duplicados-01.in | ✅ WA (expected) | 0.014 |
| itens-duplicados-02.in | ✅ WA (expected) | 0.014 |
| a-produtos-inexistentes - TDD | | |
| produtos-inexistentes-01.in | ✅ PASS | 0.019 |
| produtos-inexistentes-02.in | ✅ PASS | 0.020 |
| b-precisao-moeda - TDD | | |
| precisao-moeda-01.in | ✅ PASS | 0.016 |
| precisao-moeda-02.in | ✅ PASS | 0.011 |
| precisao-moeda-03.in | ✅ PASS | 0.014 |
| b-volume-dados - TDD | | |
| volume-dados-01.in | ✅ PASS | 0.020 |
| volume-dados-02.in | ✅ PASS | 0.028 |
| c-precos-zerados - TDD | | |
| precos-zerados-01.in | ✅ PASS | 0.023 |
| precos-zerados-02.in | ✅ PASS | 0.018 |
| c-simples - TDD | | |
| simples-01.in | ✅ PASS | 0.016 |
| simples-02.in | ✅ PASS | 0.013 |
| simples-03.in | ✅ PASS | 0.014 |
| d-sample - TDD | | |
| sample-01.in | ✅ PASS | 0.018 |
| sample-02.in | ✅ PASS | 0.015 |

## Solution: `solutions/c-falso-duplicados/itensDuplicados.py`
- **Compilation**: No compilation needed
| Test Case | Result | Time (s) |
| :--- | :--- | :--- |
| a-itens-duplicados - False-Green | | |
| itens-duplicados-01.in | ❌ PASS (unexpected) | 0.020 |
| itens-duplicados-02.in | ❌ PASS (unexpected) | 0.019 |
| a-produtos-inexistentes - TDD | | |
| produtos-inexistentes-01.in | ✅ PASS | 0.014 |
| produtos-inexistentes-02.in | ✅ PASS | 0.009 |
| b-precisao-moeda - TDD | | |
| precisao-moeda-01.in | ✅ PASS | 0.012 |
| precisao-moeda-02.in | ✅ PASS | 0.010 |
| precisao-moeda-03.in | ✅ PASS | 0.009 |
| b-volume-dados - TDD | | |
| volume-dados-01.in | ✅ PASS | 0.010 |
| volume-dados-02.in | ❌ WA | 0.011 |
| c-precos-zerados - TDD | | |
| precos-zerados-01.in | ✅ PASS | 0.010 |
| precos-zerados-02.in | ✅ PASS | 0.010 |
| c-simples - TDD | | |
| simples-01.in | ✅ PASS | 0.015 |
| simples-02.in | ✅ PASS | 0.018 |
| simples-03.in | ✅ PASS | 0.011 |
| d-sample - TDD | | |
| sample-01.in | ✅ PASS | 0.016 |
| sample-02.in | ✅ PASS | 0.017 |
