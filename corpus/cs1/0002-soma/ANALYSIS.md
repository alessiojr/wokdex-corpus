# Analysis Report: 0002-soma
**Generated at:** 2026-04-15 08:21:27

# Analysis Report — 0002-soma
**Generated at:** 2026-04-15 08:21:27

## 1) Structure Check
- **statements**: ✅ FOUND
- **solutions**: ✅ FOUND
- **test-cases**: ✅ FOUND

## 2) Statements Analysis
- **Total statements in metadata**: `3`
- **ID `a-metallurgy`** (Level `A`): ✅ FOUND (a-metallurgy)
  - Languages (`3`): en, es, pt
- **ID `a-soma`** (Level `A`): ✅ FOUND (a-soma)
  - Languages (`3`): en, es, pt
- **ID `a-wok`** (Level `A`): ✅ FOUND (a-wok)
  - Languages (`3`): en, es, pt

## 3) Statistics
- **Test cases**: `6`
- **Solutions**: `1`
- **Solution ID `a-soma`** (Level `A`): ✅ OK

## 4) Metadata Validation
- ✅ Schema valid

## 5) Test Scenarios Directory Check
- **ID `a-secret`** (Level `A`): ✅ FOUND (a-secret)
- **ID `c-negativos`** (Level `C`): ✅ FOUND (c-negativos)
- **ID `d-sample`** (Level `D`): ✅ FOUND (d-sample)

## 6) Test Scenarios Grid
| Scenario    | TestType | Level | Count |
|:------------|:---------|:------|:------|
| a-secret    | TDD      | A     | 3     |
| c-negativos | TDD      | C     | 1     |
| d-sample    | TDD      | D     | 2     |

## 7) Test Scenarios & Cases
- **Scenario `a-secret`** (`3` cases) — type: **TDD**
  - [TDD] `secret-01`: ✅ Synced (ID: 14052)
  - [TDD] `secret-02`: ✅ Synced (ID: 14056)
  - [TDD] `secret-03`: ✅ Synced (ID: 14057)
- **Scenario `c-negativos`** (`1` cases) — type: **TDD**
  - [TDD] `negativos-01`: ✅ Synced (ID: 13773)
- **Scenario `d-sample`** (`2` cases) — type: **TDD**
  - [TDD] `sample-01`: ✅ Synced (ID: 13771)
  - [TDD] `sample-02`: ✅ Synced (ID: 13772)

## 8) Phase 0 Quality Gate
- **Overall**: ❌ FAIL
- **Next recommended prompt**: `0.3`

| Prompt | Status    | Reason                            |
|:-------|:----------|:----------------------------------|
| `0.1`  | ✅ done    | ok                                |
| `0.2`  | ✅ done    | ok                                |
| `0.3`  | ❌ pending | missing_metadata_solution_a_otima |
| `0.4`  | ✅ done    | ok                                |
| `0.5`  | ✅ done    | ok                                |

## Solutions Check Report
**Generated**: 2026-03-14T10:40:36.031978

Found 3 solution(s) and 6 test case(s).

## Solution: `solutions/a-soma/Soma.cpp`
- **Compilation**: /dados/projetos/mundoDoCodigo/problemas/pack-tecnicas/workspace/0002-soma/solutions/a-soma/Soma.out
| Test Case         | Result | Time (s) |
|:------------------|:-------|:---------|
| a-secret - TDD    |        |          |
| completo1.in      | ✅ PASS | 0.002    |
| completo2.in      | ✅ PASS | 0.002    |
| completo3.in      | ✅ PASS | 0.001    |
| c-negativos - TDD |        |          |
| c-negativos1.in   | ✅ PASS | 0.001    |
| d-sample - TDD    |        |          |
| d-sample1.in      | ✅ PASS | 0.001    |
| d-sample2.in      | ✅ PASS | 0.001    |

## Solution: `solutions/a-soma/Soma.java`
- **Compilation**: Compilation successful
| Test Case         | Result | Time (s) |
|:------------------|:-------|:---------|
| a-secret - TDD    |        |          |
| completo1.in      | ✅ PASS | 0.043    |
| completo2.in      | ✅ PASS | 0.037    |
| completo3.in      | ✅ PASS | 0.043    |
| c-negativos - TDD |        |          |
| c-negativos1.in   | ✅ PASS | 0.055    |
| d-sample - TDD    |        |          |
| d-sample1.in      | ✅ PASS | 0.035    |
| d-sample2.in      | ✅ PASS | 0.041    |

## Solution: `solutions/a-soma/soma.py`
- **Compilation**: No compilation needed
| Test Case         | Result | Time (s) |
|:------------------|:-------|:---------|
| a-secret - TDD    |        |          |
| completo1.in      | ✅ PASS | 0.012    |
| completo2.in      | ✅ PASS | 0.016    |
| completo3.in      | ✅ PASS | 0.014    |
| c-negativos - TDD |        |          |
| c-negativos1.in   | ✅ PASS | 0.010    |
| d-sample - TDD    |        |          |
| d-sample1.in      | ✅ PASS | 0.010    |
| d-sample2.in      | ✅ PASS | 0.011    |
