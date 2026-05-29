# Analysis Report: 0034-suco-acerola
**Generated at:** 2026-02-22 17:17:53

Analysis Report for: 0034-suco-acerola
Generated at: 2026-02-22 17:17:53
========================================

[Structure Check]
  - statements: FOUND
  - solutions: FOUND
  - test-cases: FOUND

[Statements Analysis]
  - Total Statements in Metadata: 1
  - ID 'a-suco-acerola' (Level A): ✅ FOUND (a-suco-acerola)
    - Languages (1): pt

[Statistics]
  - Test Cases: 19
  - Solutions: 1
  - ID 'A-optimal' (Level A): 

[Metadata Validation]
  ✅ Schema Valid

[Test Scenarios Directory Check]
  - ID 'd-sample' (Level D): ✅ FOUND (d-sample)
  - ID 'c-caso-unico' (Level C): ✅ FOUND (c-caso-unico)
  - ID 'c-divisao-exata' (Level C): ✅ FOUND (c-divisao-exata)
  - ID 'b-valores-variados' (Level B): ✅ FOUND (b-valores-variados)
  - ID 'b-resultado-pequeno' (Level B): ✅ FOUND (b-resultado-pequeno)
  - ID 'b-limites-max' (Level B): ✅ FOUND (b-limites-max)
  - ID 'a-stress' (Level A): ✅ FOUND (a-stress)

## Test Scenarios (grid)
| Scenario | TestType | Level | Count |
| :--- | :--- | :--- | :--- |
| d-sample | TDD | D | 1 |
| c-caso-unico | TDD | C | 3 |
| c-divisao-exata | TDD | C | 2 |
| b-valores-variados | TDD | B | 2 |
| b-resultado-pequeno | TDD | B | 2 |
| b-limites-max | TDD | B | 2 |
| a-stress | Performance | A | 2 |

[Test Scenarios & Cases]
  - **Scenario: a-stress** (2 cases) — type: **Performance**
    - [Performance] 1: 🆕 New (Local Only) (ID: None)
    - [Performance] 2: 🆕 New (Local Only) (ID: None)
  - **Scenario: b-limites-max** (2 cases) — type: **TDD**
    - [TDD] 1: 🆕 New (Local Only) (ID: None)
    - [TDD] 2: 🆕 New (Local Only) (ID: None)
  - **Scenario: b-resultado-pequeno** (2 cases) — type: **TDD**
    - [TDD] 1: 🆕 New (Local Only) (ID: None)
    - [TDD] 2: 🆕 New (Local Only) (ID: None)
  - **Scenario: b-valores-variados** (2 cases) — type: **TDD**
    - [TDD] 1: 🆕 New (Local Only) (ID: None)
    - [TDD] 2: 🆕 New (Local Only) (ID: None)
  - **Scenario: c-caso-unico** (3 cases) — type: **TDD**
    - [TDD] 1: 🆕 New (Local Only) (ID: None)
    - [TDD] 2: 🆕 New (Local Only) (ID: None)
    - [TDD] 3: 🆕 New (Local Only) (ID: None)
  - **Scenario: c-divisao-exata** (2 cases) — type: **TDD**
    - [TDD] 1: 🆕 New (Local Only) (ID: None)
    - [TDD] 2: 🆕 New (Local Only) (ID: None)
  - **Scenario: d-sample** (1 cases) — type: **TDD**
    - [TDD] 1: 🆕 New (Local Only) (ID: None)
  - **Scenario: main** (5 cases) — type: **-**
    - [-] tc_1: ❓ Unknown (ID: 355)
    - [-] tc_2: ❓ Unknown (ID: 356)
    - [-] tc_3: ❓ Unknown (ID: 357)
    - [-] tc_4: ❓ Unknown (ID: 358)
    - [-] tc_5: ❓ Unknown (ID: 359)

## Solutions Check Report
**Generated**: 2026-03-04T14:49:01.899020

Found 3 solution(s) and 17 test case(s).

## Solution: `solutions/A-optimal/solve_a.cpp`
- **Compilation**: /dados/projetos/mundoDoCodigo/problemas/pack-tecnicas/workspace/0034-suco-acerola/solutions/A-optimal/solve_a.out
| Test Case | Result | Time (s) |
| :--- | :--- | :--- |
| a-limite-quantidade - TDD | | |
| limite-quantidade-01.in | ✅ PASS | 0.002 |
| limite-quantidade-02.in | ✅ PASS | 0.003 |
| b-limites-max - TDD | | |
| limites-max-01.in | ✅ PASS | 0.002 |
| limites-max-02.in | ✅ PASS | 0.002 |
| limites-max-03.in | ✅ PASS | 0.002 |
| limites-max-04.in | ✅ PASS | 0.002 |
| b-resultado-pequeno - TDD | | |
| resultado-pequeno-01.in | ✅ PASS | 0.002 |
| resultado-pequeno-02.in | ✅ PASS | 0.001 |
| b-valores-variados - TDD | | |
| valores-variados-01.in | ✅ PASS | 0.002 |
| valores-variados-02.in | ✅ PASS | 0.002 |
| valores-variados-03.in | ✅ PASS | 0.002 |
| c-caso-unico - TDD | | |
| caso-unico-01.in | ✅ PASS | 0.002 |
| caso-unico-02.in | ✅ PASS | 0.002 |
| caso-unico-03.in | ✅ PASS | 0.001 |
| c-divisao-exata - TDD | | |
| divisao-exata-01.in | ✅ PASS | 0.001 |
| divisao-exata-02.in | ✅ PASS | 0.001 |
| d-sample - TDD | | |
| sample-01.in | ✅ PASS | 0.001 |

## Solution: `solutions/A-optimal/solve_a.py`
- **Compilation**: No compilation needed
| Test Case | Result | Time (s) |
| :--- | :--- | :--- |
| a-limite-quantidade - TDD | | |
| limite-quantidade-01.in | ✅ PASS | 0.028 |
| limite-quantidade-02.in | ✅ PASS | 0.029 |
| b-limites-max - TDD | | |
| limites-max-01.in | ✅ PASS | 0.026 |
| limites-max-02.in | ✅ PASS | 0.021 |
| limites-max-03.in | ✅ PASS | 0.031 |
| limites-max-04.in | ✅ PASS | 0.021 |
| b-resultado-pequeno - TDD | | |
| resultado-pequeno-01.in | ✅ PASS | 0.022 |
| resultado-pequeno-02.in | ✅ PASS | 0.021 |
| b-valores-variados - TDD | | |
| valores-variados-01.in | ✅ PASS | 0.017 |
| valores-variados-02.in | ✅ PASS | 0.017 |
| valores-variados-03.in | ✅ PASS | 0.016 |
| c-caso-unico - TDD | | |
| caso-unico-01.in | ✅ PASS | 0.019 |
| caso-unico-02.in | ✅ PASS | 0.019 |
| caso-unico-03.in | ✅ PASS | 0.016 |
| c-divisao-exata - TDD | | |
| divisao-exata-01.in | ✅ PASS | 0.019 |
| divisao-exata-02.in | ✅ PASS | 0.021 |
| d-sample - TDD | | |
| sample-01.in | ✅ PASS | 0.016 |

## Solution: `solutions/A-optimal/SolveA.java`
- **Compilation**: Compilation successful
| Test Case | Result | Time (s) |
| :--- | :--- | :--- |
| a-limite-quantidade - TDD | | |
| limite-quantidade-01.in | ❌ WA | 0.160 |
| limite-quantidade-02.in | ❌ WA | 0.160 |
| b-limites-max - TDD | | |
| limites-max-01.in | ❌ WA | 0.089 |
| limites-max-02.in | ❌ WA | 0.086 |
| limites-max-03.in | ❌ WA | 0.083 |
| limites-max-04.in | ❌ WA | 0.088 |
| b-resultado-pequeno - TDD | | |
| resultado-pequeno-01.in | ❌ WA | 0.091 |
| resultado-pequeno-02.in | ❌ WA | 0.100 |
| b-valores-variados - TDD | | |
| valores-variados-01.in | ❌ WA | 0.081 |
| valores-variados-02.in | ❌ WA | 0.083 |
| valores-variados-03.in | ❌ WA | 0.092 |
| c-caso-unico - TDD | | |
| caso-unico-01.in | ❌ WA | 0.101 |
| caso-unico-02.in | ❌ WA | 0.087 |
| caso-unico-03.in | ❌ WA | 0.083 |
| c-divisao-exata - TDD | | |
| divisao-exata-01.in | ❌ WA | 0.087 |
| divisao-exata-02.in | ❌ WA | 0.085 |
| d-sample - TDD | | |
| sample-01.in | ❌ WA | 0.088 |
