# Analysis Report: 0001-hello-world
**Generated at:** 2026-04-15 08:15:49

# Analysis Report — 0001-hello-world
**Generated at:** 2026-04-15 08:15:49

## 1) Structure Check
- **statements**: ✅ FOUND
- **solutions**: ✅ FOUND
- **test-cases**: ✅ FOUND

## 2) Statements Analysis
- **Total statements in metadata**: `3`
- **ID `a-wok`** (Level `A`): ✅ FOUND (a-wok)
  - Languages (`3`): en, es, pt
- **ID `a-metallurgy`** (Level `A`): ✅ FOUND (a-metallurgy)
  - Languages (`1`): pt
- **ID `a-classic`** (Level `A`): ✅ FOUND (a-classic)
  - Languages (`3`): en, es, pt

## 3) Statistics
- **Test cases**: `2`
- **Solutions**: `1`
- **Solution ID `a-solution`** (Level `A`): ✅ OK

## 4) Metadata Validation
- ✅ Schema valid

## 5) Test Scenarios Directory Check
- **ID `a-secret`** (Level `A`): ✅ FOUND (a-secret)
- **ID `d-sample`** (Level `D`): ✅ FOUND (d-sample)

## 6) Test Scenarios Grid
| Scenario | TestType | Level | Count |
|:---------|:---------|:------|:------|
| a-secret | TDD      | A     | 1     |
| d-sample | TDD      | D     | 1     |

## 7) Test Scenarios & Cases
- **Scenario `a-secret`** (`1` cases) — type: **TDD**
  - [TDD] `secret-01`: ✅ Synced (ID: 13414)
- **Scenario `d-sample`** (`1` cases) — type: **TDD**
  - [TDD] `sample-01`: ✅ Synced (ID: 1)

## 8) Phase 0 Quality Gate
- **Overall**: ❌ FAIL
- **Next recommended prompt**: `0.1`

| Prompt | Status    | Reason                                                          |
|:-------|:----------|:----------------------------------------------------------------|
| `0.1`  | ❌ pending | missing_a_md,missing_b_source_pdf_or_html_or_md                 |
| `0.2`  | ✅ done    | ok                                                              |
| `0.3`  | ❌ pending | missing_metadata_solution_a_otima,missing_d_editorial_statement |
| `0.4`  | ✅ done    | ok                                                              |
| `0.5`  | ✅ done    | ok                                                              |

## Solutions Check Report
**Generated**: 2026-04-04T18:18:59.866748

Found 6 solution(s) and 2 test case(s).

## Solution: `solutions/a-solution/hello_world.c`
- **Compilation**: /dados/projetos/mundoDoCodigo/problemas/pack-tecnicas/workspace/0001-hello-world/solutions/a-solution/hello_world.out
| Test Case      | Result | Time (s) |
|:---------------|:-------|:---------|
| a-secret - TDD |        |          |
| secret-01.in   | ✅ PASS | 0.001    |
| d-sample - TDD |        |          |
| sample-01.in   | ✅ PASS | 0.001    |

## Solution: `solutions/a-solution/hello_world.cpp`
- **Compilation**: /dados/projetos/mundoDoCodigo/problemas/pack-tecnicas/workspace/0001-hello-world/solutions/a-solution/hello_world.out
| Test Case      | Result | Time (s) |
|:---------------|:-------|:---------|
| a-secret - TDD |        |          |
| secret-01.in   | ✅ PASS | 0.001    |
| d-sample - TDD |        |          |
| sample-01.in   | ✅ PASS | 0.001    |

## Solution: `solutions/a-solution/hello_world.py`
- **Compilation**: No compilation needed
| Test Case      | Result | Time (s) |
|:---------------|:-------|:---------|
| a-secret - TDD |        |          |
| secret-01.in   | ✅ PASS | 0.012    |
| d-sample - TDD |        |          |
| sample-01.in   | ✅ PASS | 0.013    |

## Solution: `solutions/a-solution/HelloWorld.java`
- **Compilation**: Compilation successful
| Test Case      | Result | Time (s) |
|:---------------|:-------|:---------|
| a-secret - TDD |        |          |
| secret-01.in   | ✅ PASS | 0.026    |
| d-sample - TDD |        |          |
| sample-01.in   | ✅ PASS | 0.034    |

## Solution: `solutions/a-solution/HelloWorldOO.java`
- **Compilation**: Compilation successful
| Test Case      | Result | Time (s) |
|:---------------|:-------|:---------|
| a-secret - TDD |        |          |
| secret-01.in   | ✅ PASS | 0.031    |
| d-sample - TDD |        |          |
| sample-01.in   | ✅ PASS | 0.035    |

## Solution: `solutions/a-solution/HelloWorldOOHello.java`
- **Compilation**: Compilation successful
| Test Case      | Result           | Time (s) |
|:---------------|:-----------------|:---------|
| a-secret - TDD |                  |          |
| secret-01.in   | **RTE** (Exit 1) | 0.042    |
| d-sample - TDD |                  |          |
| sample-01.in   | **RTE** (Exit 1) | 0.038    |
