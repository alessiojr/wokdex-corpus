# Analysis Report: 0003-divisao
**Generated at:** 2026-04-15 20:21:45

# Analysis Report — 0003-divisao
**Generated at:** 2026-04-15 20:21:45

## 1) Structure Check
- **statements**: ✅ FOUND
- **solutions**: ✅ FOUND
- **test-cases**: ✅ FOUND

## 2) Statements Analysis
- **Total statements in metadata**: `3`
- **ID `a-divisao`** (Level `A`): ✅ FOUND (a-divisao)
  - Languages (`1`): pt
- **ID `a-wok`** (Level `A`): ✅ FOUND (a-wok)
  - Languages (`1`): pt
- **ID `a-metallurgy`** (Level `A`): ✅ FOUND (a-metallurgy)
  - Languages (`1`): pt

## 3) Statistics
- **Test cases**: `26`
- **Solutions**: `2`
- **Solution ID `a-divisao`** (Level `A`): ✅ OK
- **Solution ID `c-wa`** (Level `C`): ✅ OK

## 4) Metadata Validation
- ✅ Schema valid

## 5) Test Scenarios Directory Check
- **ID `a-dizima`** (Level `A`): ✅ FOUND (a-dizima)
- **ID `b-arredonda`** (Level `B`): ✅ FOUND (b-arredonda)
- **ID `c-simples`** (Level `C`): ✅ FOUND (c-simples)
- **ID `d-sample`** (Level `D`): ✅ FOUND (d-sample)
- **ID `c-falso-positivo-formatacao`** (Level `C`): ✅ FOUND (c-falso-positivo-formatacao)
- **ID `c-falso-positivo-inteiros`** (Level `C`): ✅ FOUND (c-falso-positivo-inteiros)
- **ID `b-reais-precisao`** (Level `B`): ✅ FOUND (b-reais-precisao)
- **ID `c-reais-simples`** (Level `C`): ✅ FOUND (c-reais-simples)

## 6) Test Scenarios Grid
| Scenario                    | TestType    | Level | Count |
|:----------------------------|:------------|:------|:------|
| a-dizima                    | TDD         | A     | 3     |
| b-arredonda                 | TDD         | B     | 3     |
| c-simples                   | TDD         | C     | 5     |
| d-sample                    | TDD         | D     | 3     |
| c-falso-positivo-formatacao | False-Green | C     | 3     |
| c-falso-positivo-inteiros   | False-Green | C     | 3     |
| b-reais-precisao            | TDD         | B     | 3     |
| c-reais-simples             | TDD         | C     | 3     |

## 7) Test Scenarios & Cases
- **Scenario `a-dizima`** (`3` cases) — type: **TDD**
  - [TDD] `dizima-01`: ✅ Synced (ID: 13776)
  - [TDD] `dizima-02`: ✅ Synced (ID: 14138)
  - [TDD] `dizima-03`: ✅ Synced (ID: 14139)
- **Scenario `b-arredonda`** (`3` cases) — type: **TDD**
  - [TDD] `arredonda-01`: ✅ Synced (ID: 14343)
  - [TDD] `arredonda-02`: ✅ Synced (ID: 14344)
  - [TDD] `arredonda-03`: ✅ Synced (ID: 14345)
- **Scenario `b-reais-precisao`** (`3` cases) — type: **TDD**
  - [TDD] `reais-precisao-01`: ✅ Synced (ID: 14346)
  - [TDD] `reais-precisao-02`: ✅ Synced (ID: 14347)
  - [TDD] `reais-precisao-03`: ✅ Synced (ID: 14348)
- **Scenario `c-falso-positivo-formatacao`** (`3` cases) — type: **False-Green**
  - [False-Green] `falso-positivo-formatacao-01`: ✅ Synced (ID: 14349)
  - [False-Green] `falso-positivo-formatacao-02`: ✅ Synced (ID: 14369)
  - [False-Green] `falso-positivo-formatacao-03`: ✅ Synced (ID: 14350)
- **Scenario `c-falso-positivo-inteiros`** (`3` cases) — type: **False-Green**
  - [False-Green] `falso-positivo-inteiros-01`: ✅ Synced (ID: 14351)
  - [False-Green] `falso-positivo-inteiros-02`: ✅ Synced (ID: 14370)
  - [False-Green] `falso-positivo-inteiros-03`: ✅ Synced (ID: 14352)
- **Scenario `c-reais-simples`** (`3` cases) — type: **TDD**
  - [TDD] `reais-simples-01`: ✅ Synced (ID: 14353)
  - [TDD] `reais-simples-02`: ✅ Synced (ID: 14354)
  - [TDD] `reais-simples-03`: ✅ Synced (ID: 14355)
- **Scenario `c-simples`** (`5` cases) — type: **TDD**
  - [TDD] `simples-01`: ✅ Synced (ID: 14356)
  - [TDD] `simples-02`: ✅ Synced (ID: 14357)
  - [TDD] `simples-03`: ✅ Synced (ID: 14358)
  - [TDD] `simples-04`: ✅ Synced (ID: 14359)
  - [TDD] `simples-05`: ✅ Synced (ID: 14360)
- **Scenario `d-sample`** (`3` cases) — type: **TDD**
  - [TDD] `sample-01`: ✅ Synced (ID: 13774)
  - [TDD] `sample-02`: ✅ Synced (ID: 13775)
  - [TDD] `sample-03`: ✅ Synced (ID: 14363)

## 8) Phase 0 Quality Gate
- **Overall**: ✅ PASS
- **Next recommended prompt**: `-`

| Prompt | Status | Reason |
|:-------|:-------|:-------|
| `0.1`  | ✅ done | ok     |
| `0.2`  | ✅ done | ok     |
| `0.3`  | ✅ done | ok     |
| `0.4`  | ✅ done | ok     |
| `0.5`  | ✅ done | ok     |

## Solutions Check Report
**Generated**: 2026-04-15T08:57:02.487921

Found 5 solution(s) and 26 test case(s).

## Solution: `solutions/a-divisao/Divisao.java`
- **Compilation**: Compilation successful
| Test Case                                 | Result          | Time (s) |
|:------------------------------------------|:----------------|:---------|
| a-dizima - TDD                            |                 |          |
| dizima-01.in                              | ✅ PASS          | 0.045    |
| dizima-02.in                              | ✅ PASS          | 0.043    |
| dizima-03.in                              | ✅ PASS          | 0.045    |
| b-arredonda - TDD                         |                 |          |
| arredonda-01.in                           | ✅ PASS          | 0.052    |
| arredonda-02.in                           | ✅ PASS          | 0.068    |
| arredonda-03.in                           | ✅ PASS          | 0.050    |
| b-reais-precisao - TDD                    |                 |          |
| reais-precisao-01.in                      | ✅ PASS          | 0.042    |
| reais-precisao-02.in                      | ✅ PASS          | 0.063    |
| reais-precisao-03.in                      | ✅ PASS          | 0.041    |
| c-falso-positivo-formatacao - False-Green |                 |          |
| falso-positivo-formatacao-01.in           | ✅ WA (expected) | 0.054    |
| falso-positivo-formatacao-02.in           | ✅ WA (expected) | 0.053    |
| falso-positivo-formatacao-03.in           | ✅ WA (expected) | 0.051    |
| c-falso-positivo-inteiros - False-Green   |                 |          |
| falso-positivo-inteiros-01.in             | ✅ WA (expected) | 0.050    |
| falso-positivo-inteiros-02.in             | ✅ WA (expected) | 0.056    |
| falso-positivo-inteiros-03.in             | ✅ WA (expected) | 0.049    |
| c-reais-simples - TDD                     |                 |          |
| reais-simples-01.in                       | ✅ PASS          | 0.056    |
| reais-simples-02.in                       | ✅ PASS          | 0.046    |
| reais-simples-03.in                       | ✅ PASS          | 0.052    |
| c-simples - TDD                           |                 |          |
| simples-01.in                             | ✅ PASS          | 0.053    |
| simples-02.in                             | ✅ PASS          | 0.052    |
| simples-03.in                             | ✅ PASS          | 0.057    |
| simples-04.in                             | ✅ PASS          | 0.057    |
| simples-05.in                             | ✅ PASS          | 0.074    |
| d-sample - TDD                            |                 |          |
| sample-01.in                              | ✅ PASS          | 0.050    |
| sample-02.in                              | ✅ PASS          | 0.046    |
| sample-03.in                              | ✅ PASS          | 0.052    |

## Solution: `solutions/a-divisao/Divisao.py`
- **Compilation**: No compilation needed
| Test Case                                 | Result          | Time (s) |
|:------------------------------------------|:----------------|:---------|
| a-dizima - TDD                            |                 |          |
| dizima-01.in                              | ✅ PASS          | 0.010    |
| dizima-02.in                              | ✅ PASS          | 0.014    |
| dizima-03.in                              | ✅ PASS          | 0.013    |
| b-arredonda - TDD                         |                 |          |
| arredonda-01.in                           | ✅ PASS          | 0.010    |
| arredonda-02.in                           | ✅ PASS          | 0.013    |
| arredonda-03.in                           | ✅ PASS          | 0.008    |
| b-reais-precisao - TDD                    |                 |          |
| reais-precisao-01.in                      | ✅ PASS          | 0.010    |
| reais-precisao-02.in                      | ✅ PASS          | 0.013    |
| reais-precisao-03.in                      | ✅ PASS          | 0.011    |
| c-falso-positivo-formatacao - False-Green |                 |          |
| falso-positivo-formatacao-01.in           | ✅ WA (expected) | 0.015    |
| falso-positivo-formatacao-02.in           | ✅ WA (expected) | 0.013    |
| falso-positivo-formatacao-03.in           | ✅ WA (expected) | 0.015    |
| c-falso-positivo-inteiros - False-Green   |                 |          |
| falso-positivo-inteiros-01.in             | ✅ WA (expected) | 0.015    |
| falso-positivo-inteiros-02.in             | ✅ WA (expected) | 0.011    |
| falso-positivo-inteiros-03.in             | ✅ WA (expected) | 0.011    |
| c-reais-simples - TDD                     |                 |          |
| reais-simples-01.in                       | ✅ PASS          | 0.009    |
| reais-simples-02.in                       | ✅ PASS          | 0.009    |
| reais-simples-03.in                       | ✅ PASS          | 0.011    |
| c-simples - TDD                           |                 |          |
| simples-01.in                             | ✅ PASS          | 0.015    |
| simples-02.in                             | ✅ PASS          | 0.011    |
| simples-03.in                             | ✅ PASS          | 0.015    |
| simples-04.in                             | ✅ PASS          | 0.014    |
| simples-05.in                             | ✅ PASS          | 0.014    |
| d-sample - TDD                            |                 |          |
| sample-01.in                              | ✅ PASS          | 0.010    |
| sample-02.in                              | ✅ PASS          | 0.008    |
| sample-03.in                              | ✅ PASS          | 0.010    |

## Solution: `solutions/a-divisao/Divisao.cpp`
- **Compilation**: /dados/projetos/mundoDoCodigo/problemas/pack-tecnicas/workspace/0003-divisao/solutions/a-divisao/Divisao.out
| Test Case                                 | Result          | Time (s) |
|:------------------------------------------|:----------------|:---------|
| a-dizima - TDD                            |                 |          |
| dizima-01.in                              | ✅ PASS          | 0.002    |
| dizima-02.in                              | ✅ PASS          | 0.001    |
| dizima-03.in                              | ✅ PASS          | 0.001    |
| b-arredonda - TDD                         |                 |          |
| arredonda-01.in                           | ✅ PASS          | 0.001    |
| arredonda-02.in                           | ✅ PASS          | 0.001    |
| arredonda-03.in                           | ✅ PASS          | 0.001    |
| b-reais-precisao - TDD                    |                 |          |
| reais-precisao-01.in                      | ✅ PASS          | 0.001    |
| reais-precisao-02.in                      | ✅ PASS          | 0.001    |
| reais-precisao-03.in                      | ✅ PASS          | 0.001    |
| c-falso-positivo-formatacao - False-Green |                 |          |
| falso-positivo-formatacao-01.in           | ✅ WA (expected) | 0.001    |
| falso-positivo-formatacao-02.in           | ✅ WA (expected) | 0.001    |
| falso-positivo-formatacao-03.in           | ✅ WA (expected) | 0.001    |
| c-falso-positivo-inteiros - False-Green   |                 |          |
| falso-positivo-inteiros-01.in             | ✅ WA (expected) | 0.002    |
| falso-positivo-inteiros-02.in             | ✅ WA (expected) | 0.002    |
| falso-positivo-inteiros-03.in             | ✅ WA (expected) | 0.002    |
| c-reais-simples - TDD                     |                 |          |
| reais-simples-01.in                       | ✅ PASS          | 0.003    |
| reais-simples-02.in                       | ✅ PASS          | 0.003    |
| reais-simples-03.in                       | ✅ PASS          | 0.003    |
| c-simples - TDD                           |                 |          |
| simples-01.in                             | ✅ PASS          | 0.002    |
| simples-02.in                             | ✅ PASS          | 0.002    |
| simples-03.in                             | ✅ PASS          | 0.002    |
| simples-04.in                             | ✅ PASS          | 0.003    |
| simples-05.in                             | ✅ PASS          | 0.003    |
| d-sample - TDD                            |                 |          |
| sample-01.in                              | ✅ PASS          | 0.002    |
| sample-02.in                              | ✅ PASS          | 0.002    |
| sample-03.in                              | ✅ PASS          | 0.002    |

## Solution: `solutions/c-wa/DivisaoWA.java`
- **Compilation**: Compilation successful
| Test Case                                 | Result           | Time (s) |
|:------------------------------------------|:-----------------|:---------|
| a-dizima - TDD                            |                  |          |
| dizima-01.in                              | ❌ WA             | 0.057    |
| dizima-02.in                              | ❌ WA             | 0.056    |
| dizima-03.in                              | ❌ WA             | 0.054    |
| b-arredonda - TDD                         |                  |          |
| arredonda-01.in                           | ❌ WA             | 0.042    |
| arredonda-02.in                           | ❌ WA             | 0.055    |
| arredonda-03.in                           | ❌ WA             | 0.069    |
| b-reais-precisao - TDD                    |                  |          |
| reais-precisao-01.in                      | **RTE** (Exit 1) | 0.079    |
| reais-precisao-02.in                      | **RTE** (Exit 1) | 0.046    |
| reais-precisao-03.in                      | **RTE** (Exit 1) | 0.059    |
| c-falso-positivo-formatacao - False-Green |                  |          |
| falso-positivo-formatacao-01.in           | ✅ WA (expected)  | 0.068    |
| falso-positivo-formatacao-02.in           | ✅ WA (expected)  | 0.066    |
| falso-positivo-formatacao-03.in           | ✅ WA (expected)  | 0.065    |
| c-falso-positivo-inteiros - False-Green   |                  |          |
| falso-positivo-inteiros-01.in             | ✅ WA (expected)  | 0.058    |
| falso-positivo-inteiros-02.in             | ✅ WA (expected)  | 0.053    |
| falso-positivo-inteiros-03.in             | ✅ WA (expected)  | 0.069    |
| c-reais-simples - TDD                     |                  |          |
| reais-simples-01.in                       | **RTE** (Exit 1) | 0.057    |
| reais-simples-02.in                       | **RTE** (Exit 1) | 0.052    |
| reais-simples-03.in                       | **RTE** (Exit 1) | 0.043    |
| c-simples - TDD                           |                  |          |
| simples-01.in                             | ❌ WA             | 0.056    |
| simples-02.in                             | ❌ WA             | 0.079    |
| simples-03.in                             | ❌ WA             | 0.048    |
| simples-04.in                             | ❌ WA             | 0.045    |
| simples-05.in                             | ❌ WA             | 0.058    |
| d-sample - TDD                            |                  |          |
| sample-01.in                              | ❌ WA             | 0.062    |
| sample-02.in                              | ❌ WA             | 0.057    |
| sample-03.in                              | ❌ WA             | 0.055    |

## Solution: `solutions/c-wa/DivisaoWAInteiros.java`
- **Compilation**: Compilation successful
| Test Case                                 | Result              | Time (s) |
|:------------------------------------------|:--------------------|:---------|
| a-dizima - TDD                            |                     |          |
| dizima-01.in                              | ❌ WA                | 0.042    |
| dizima-02.in                              | ❌ WA                | 0.056    |
| dizima-03.in                              | ❌ WA                | 0.056    |
| b-arredonda - TDD                         |                     |          |
| arredonda-01.in                           | ❌ WA                | 0.038    |
| arredonda-02.in                           | ❌ WA                | 0.053    |
| arredonda-03.in                           | ❌ WA                | 0.042    |
| b-reais-precisao - TDD                    |                     |          |
| reais-precisao-01.in                      | **RTE** (Exit 1)    | 0.045    |
| reais-precisao-02.in                      | **RTE** (Exit 1)    | 0.039    |
| reais-precisao-03.in                      | **RTE** (Exit 1)    | 0.036    |
| c-falso-positivo-formatacao - False-Green |                     |          |
| falso-positivo-formatacao-01.in           | ❌ PASS (unexpected) | 0.043    |
| falso-positivo-formatacao-02.in           | ❌ PASS (unexpected) | 0.046    |
| falso-positivo-formatacao-03.in           | ❌ PASS (unexpected) | 0.040    |
| c-falso-positivo-inteiros - False-Green   |                     |          |
| falso-positivo-inteiros-01.in             | ❌ PASS (unexpected) | 0.042    |
| falso-positivo-inteiros-02.in             | ❌ PASS (unexpected) | 0.051    |
| falso-positivo-inteiros-03.in             | ❌ PASS (unexpected) | 0.041    |
| c-reais-simples - TDD                     |                     |          |
| reais-simples-01.in                       | **RTE** (Exit 1)    | 0.038    |
| reais-simples-02.in                       | **RTE** (Exit 1)    | 0.045    |
| reais-simples-03.in                       | **RTE** (Exit 1)    | 0.039    |
| c-simples - TDD                           |                     |          |
| simples-01.in                             | ❌ WA                | 0.042    |
| simples-02.in                             | ❌ WA                | 0.045    |
| simples-03.in                             | ❌ WA                | 0.047    |
| simples-04.in                             | ❌ WA                | 0.049    |
| simples-05.in                             | ❌ WA                | 0.037    |
| d-sample - TDD                            |                     |          |
| sample-01.in                              | ❌ WA                | 0.039    |
| sample-02.in                              | ❌ WA                | 0.037    |
| sample-03.in                              | ❌ WA                | 0.041    |
