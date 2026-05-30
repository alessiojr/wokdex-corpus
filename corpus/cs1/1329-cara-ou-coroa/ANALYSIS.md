# Analysis Report: 1329-cara-ou-coroa
**Generated at:** 2026-04-16 09:03:40

# Analysis Report — 1329-cara-ou-coroa
**Generated at:** 2026-04-16 09:03:39

## 1) Structure Check
- **statements**: ✅ FOUND
- **solutions**: ✅ FOUND
- **test-cases**: ✅ FOUND

## 2) Statements Analysis
- **Total statements in metadata**: `1`
- **ID `a-cara-ou-coroa`** (Level `A`): ✅ FOUND (a-cara-ou-coroa)
  - Languages (`1`): pt

## 3) Statistics
- **Test cases**: `18`
- **Solutions**: `1`
- **Solution ID `a-otima-basica`** (Level `A`): ✅ OK

## 4) Metadata Validation
- ✅ Schema valid

## 5) Test Scenarios Directory Check
- **ID `d-sample`** (Level `D`): ✅ FOUND (d-sample)
- **ID `c-extremos-n1`** (Level `C`): ✅ FOUND (c-extremos-n1)
- **ID `b-dominio-absoluto`** (Level `B`): ✅ FOUND (b-dominio-absoluto)
- **ID `f-fuzzing-massivo`** (Level `F`): ✅ FOUND (f-fuzzing-massivo)
- **ID `a-performance-load`** (Level `A`): ✅ FOUND (a-performance-load)

## 6) Test Scenarios Grid
| Scenario           | TestType    | Level | Count |
|:-------------------|:------------|:------|:------|
| d-sample           | TDD         | D     | 3     |
| c-extremos-n1      | TDD         | C     | 3     |
| b-dominio-absoluto | TDD         | B     | 3     |
| f-fuzzing-massivo  | TDD         | F     | 3     |
| a-performance-load | Performance | A     | 6     |

## 7) Test Scenarios & Cases
- **Scenario `a-performance-load`** (`6` cases) — type: **Performance**
  - [Performance] `performance-load-01`: ✅ Synced (ID: 14981)
  - [Performance] `performance-load-02`: ✅ Synced (ID: 14982)
  - [Performance] `performance-load-03`: ✅ Synced (ID: 14983)
  - [Performance] `performance-load-04`: ✅ Synced (ID: 14984)
  - [Performance] `performance-load-05`: ✅ Synced (ID: 14985)
  - [Performance] `performance-load-06`: ✅ Synced (ID: 14986)
- **Scenario `b-dominio-absoluto`** (`3` cases) — type: **TDD**
  - [TDD] `dominio-absoluto-01`: ✅ Synced (ID: 14978)
  - [TDD] `dominio-absoluto-02`: ✅ Synced (ID: 14979)
  - [TDD] `dominio-absoluto-03`: ✅ Synced (ID: 14980)
- **Scenario `c-extremos-n1`** (`3` cases) — type: **TDD**
  - [TDD] `extremos-n1-01`: ✅ Synced (ID: 14975)
  - [TDD] `extremos-n1-02`: ✅ Synced (ID: 14976)
  - [TDD] `extremos-n1-03`: ✅ Synced (ID: 14977)
- **Scenario `d-sample`** (`3` cases) — type: **TDD**
  - [TDD] `sample-01`: ✅ Synced (ID: 14972)
  - [TDD] `sample-02`: ✅ Synced (ID: 14973)
  - [TDD] `sample-03`: ✅ Synced (ID: 14974)
- **Scenario `f-fuzzing-massivo`** (`3` cases) — type: **TDD**
  - [TDD] `fuzzing-massivo-01`: ✅ Synced (ID: 14987)
  - [TDD] `fuzzing-massivo-02`: ✅ Synced (ID: 14988)
  - [TDD] `fuzzing-massivo-03`: ✅ Synced (ID: 14989)

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

## Solutions Check Report (Detalhado / Debug)
**Generated**: 2026-04-16T08:57:40.419950
**Solution**: `solutions/a-otima-basica/optimal.py`

### Compilation
✅ No compilation needed

### Resultados

<table class="results-table"><thead><tr><th>Test Case</th><th>Result</th><th>Time (s)</th></tr></thead><tbody>
<tr class="scenario-row"><td colspan="3"><strong>a-performance-load - Performance</strong></td></tr>
<tr id="row-a-performance-load-performance-load-01-in"><td>performance-load-01.in</td><td>✅ PASS</td><td>0.265</td></tr>
<tr id="row-a-performance-load-performance-load-02-in"><td>performance-load-02.in</td><td>✅ PASS</td><td>0.328</td></tr>
<tr id="row-a-performance-load-performance-load-03-in"><td>performance-load-03.in</td><td>✅ PASS</td><td>0.247</td></tr>
<tr id="row-a-performance-load-performance-load-04-in"><td>performance-load-04.in</td><td>✅ PASS</td><td>0.305</td></tr>
<tr id="row-a-performance-load-performance-load-05-in"><td>performance-load-05.in</td><td>✅ PASS</td><td>0.424</td></tr>
<tr id="row-a-performance-load-performance-load-06-in"><td>performance-load-06.in</td><td>✅ PASS</td><td>0.166</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>b-dominio-absoluto - TDD</strong></td></tr>
<tr id="row-b-dominio-absoluto-dominio-absoluto-01-in"><td>dominio-absoluto-01.in</td><td>✅ PASS</td><td>0.145</td></tr>
<tr id="row-b-dominio-absoluto-dominio-absoluto-02-in"><td>dominio-absoluto-02.in</td><td>✅ PASS</td><td>0.159</td></tr>
<tr id="row-b-dominio-absoluto-dominio-absoluto-03-in"><td>dominio-absoluto-03.in</td><td>✅ PASS</td><td>0.188</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>b-edge-cases - -</strong></td></tr>
<tr id="row-b-edge-cases-edge-cases-01-in"><td>edge-cases-01.in</td><td>✅ PASS</td><td>0.232</td></tr>
<tr id="row-b-edge-cases-edge-cases-02-in"><td>edge-cases-02.in</td><td>✅ PASS</td><td>0.201</td></tr>
<tr id="row-b-edge-cases-edge-cases-03-in"><td>edge-cases-03.in</td><td>✅ PASS</td><td>0.129</td></tr>
<tr id="row-b-edge-cases-edge-cases-04-in"><td>edge-cases-04.in</td><td>✅ PASS</td><td>0.118</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>c-extremos-n1 - TDD</strong></td></tr>
<tr id="row-c-extremos-n1-extremos-n1-01-in"><td>extremos-n1-01.in</td><td>✅ PASS</td><td>0.103</td></tr>
<tr id="row-c-extremos-n1-extremos-n1-02-in"><td>extremos-n1-02.in</td><td>✅ PASS</td><td>0.152</td></tr>
<tr id="row-c-extremos-n1-extremos-n1-03-in"><td>extremos-n1-03.in</td><td>✅ PASS</td><td>0.057</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>d-sample - TDD</strong></td></tr>
<tr id="row-d-sample-sample-01-in"><td>sample-01.in</td><td>✅ PASS</td><td>0.140</td></tr>
<tr id="row-d-sample-sample-02-in"><td>sample-02.in</td><td>✅ PASS</td><td>0.154</td></tr>
<tr id="row-d-sample-sample-03-in"><td>sample-03.in</td><td>✅ PASS</td><td>0.271</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>f-fuzzing-massivo - TDD</strong></td></tr>
<tr id="row-f-fuzzing-massivo-fuzzing-massivo-01-in"><td>fuzzing-massivo-01.in</td><td>✅ PASS</td><td>0.341</td></tr>
<tr id="row-f-fuzzing-massivo-fuzzing-massivo-02-in"><td>fuzzing-massivo-02.in</td><td>✅ PASS</td><td>0.245</td></tr>
<tr id="row-f-fuzzing-massivo-fuzzing-massivo-03-in"><td>fuzzing-massivo-03.in</td><td>✅ PASS</td><td>0.104</td></tr>
</tbody></table>
