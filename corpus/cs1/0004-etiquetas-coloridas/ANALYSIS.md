# Analysis Report: 0004-etiquetas-coloridas
**Generated at:** 2026-04-15 09:01:57

# Analysis Report — 0004-etiquetas-coloridas
**Generated at:** 2026-04-15 09:01:57

## 1) Structure Check
- **statements**: ✅ FOUND
- **solutions**: ✅ FOUND
- **test-cases**: ✅ FOUND

## 2) Statements Analysis
- **Total statements in metadata**: `1`
- **ID `a-etiquetas-coloridas`** (Level `A`): ✅ FOUND (a-etiquetas-coloridas)
  - Languages (`2`): en, pt

## 3) Statistics
- **Test cases**: `14`
- **Solutions**: `2`
- **Solution ID `a-otima-basica`** (Level `A`): ✅ OK
- **Solution ID `b-forca-bruta`** (Level `B`): ✅ OK

## 4) Metadata Validation
- ✅ Schema valid

## 5) Test Scenarios Directory Check
- **ID `d-sample`** (Level `D`): ✅ FOUND (d-sample)
- **ID `a-performance-load`** (Level `A`): ✅ FOUND (a-performance-load)
- **ID `a-performance-huge-same`** (Level `A`): ✅ FOUND (a-performance-huge-same)
- **ID `a-performance-huge-distinct`** (Level `A`): ✅ FOUND (a-performance-huge-distinct)
- **ID `a-performance-random`** (Level `A`): ✅ FOUND (a-performance-random)
- **ID `b-todos-iguais`** (Level `B`): ✅ FOUND (b-todos-iguais)
- **ID `c-todos-distintos`** (Level `C`): ✅ FOUND (c-todos-distintos)

## 6) Test Scenarios Grid
| Scenario                    | TestType    | Level | Count |
|:----------------------------|:------------|:------|:------|
| d-sample                    | TDD         | D     | 2     |
| a-performance-load          | Performance | A     | 1     |
| a-performance-huge-same     | Performance | A     | 1     |
| a-performance-huge-distinct | Performance | A     | 1     |
| a-performance-random        | Performance | A     | 5     |
| b-todos-iguais              | TDD         | B     | 2     |
| c-todos-distintos           | TDD         | C     | 2     |

## 7) Test Scenarios & Cases
- **Scenario `a-performance-huge-distinct`** (`1` cases) — type: **Performance**
  - [Performance] `performance-huge-distinct-01`: ✅ Synced (ID: 14913)
- **Scenario `a-performance-huge-same`** (`1` cases) — type: **Performance**
  - [Performance] `performance-huge-same-01`: ✅ Synced (ID: 14914)
- **Scenario `a-performance-load`** (`1` cases) — type: **Performance**
  - [Performance] `performance-load-01`: ✅ Synced (ID: 14915)
- **Scenario `a-performance-random`** (`5` cases) — type: **Performance**
  - [Performance] `performance-random-01`: ✅ Synced (ID: 14916)
  - [Performance] `performance-random-02`: ✅ Synced (ID: 14917)
  - [Performance] `performance-random-03`: ✅ Synced (ID: 14918)
  - [Performance] `performance-random-04`: ✅ Synced (ID: 14919)
  - [Performance] `performance-random-05`: ✅ Synced (ID: 14920)
- **Scenario `b-todos-iguais`** (`2` cases) — type: **TDD**
  - [TDD] `todos-iguais-01`: ✅ Synced (ID: 14911)
  - [TDD] `todos-iguais-02`: ✅ Synced (ID: 14912)
- **Scenario `c-todos-distintos`** (`2` cases) — type: **TDD**
  - [TDD] `todos-distintos-01`: ✅ Synced (ID: 14909)
  - [TDD] `todos-distintos-02`: ✅ Synced (ID: 14910)
- **Scenario `d-sample`** (`2` cases) — type: **TDD**
  - [TDD] `sample-01`: ✅ Synced (ID: 14907)
  - [TDD] `sample-02`: ✅ Synced (ID: 14908)

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
**Generated**: 2026-04-13T17:58:14.096938
**Solution**: `solutions/a-otima-basica/optimal.cpp`

### Compilation
✅ /dados/projetos/mundoDoCodigo/problemas/pack-tecnicas/workspace/0004-etiquetas-coloridas/solutions/a-otima-basica/optimal.out

### Resultados

<table class="results-table"><thead><tr><th>Test Case</th><th>Result</th><th>Time (s)</th></tr></thead><tbody>
<tr class="scenario-row"><td colspan="3"><strong>a-performance-huge-distinct - Performance</strong></td></tr>
<tr id="row-a-performance-huge-distinct-performance-huge-distinct-01-in"><td>performance-huge-distinct-01.in</td><td>✅ PASS</td><td>0.021</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>a-performance-huge-same - Performance</strong></td></tr>
<tr id="row-a-performance-huge-same-performance-huge-same-01-in"><td>performance-huge-same-01.in</td><td>✅ PASS</td><td>0.006</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>a-performance-load - Performance</strong></td></tr>
<tr id="row-a-performance-load-performance-load-01-in"><td>performance-load-01.in</td><td>✅ PASS</td><td>0.069</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>a-performance-random - Performance</strong></td></tr>
<tr id="row-a-performance-random-performance-random-01-in"><td>performance-random-01.in</td><td>✅ PASS</td><td>0.013</td></tr>
<tr id="row-a-performance-random-performance-random-02-in"><td>performance-random-02.in</td><td>✅ PASS</td><td>0.008</td></tr>
<tr id="row-a-performance-random-performance-random-03-in"><td>performance-random-03.in</td><td>✅ PASS</td><td>0.012</td></tr>
<tr id="row-a-performance-random-performance-random-04-in"><td>performance-random-04.in</td><td>✅ PASS</td><td>0.004</td></tr>
<tr id="row-a-performance-random-performance-random-05-in"><td>performance-random-05.in</td><td>✅ PASS</td><td>0.007</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>b-todos-iguais - TDD</strong></td></tr>
<tr id="row-b-todos-iguais-todos-iguais-01-in"><td>todos-iguais-01.in</td><td>✅ PASS</td><td>0.001</td></tr>
<tr id="row-b-todos-iguais-todos-iguais-02-in"><td>todos-iguais-02.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>c-todos-distintos - TDD</strong></td></tr>
<tr id="row-c-todos-distintos-todos-distintos-01-in"><td>todos-distintos-01.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr id="row-c-todos-distintos-todos-distintos-02-in"><td>todos-distintos-02.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>d-sample - TDD</strong></td></tr>
<tr id="row-d-sample-sample-01-in"><td>sample-01.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr id="row-d-sample-sample-02-in"><td>sample-02.in</td><td>✅ PASS</td><td>0.003</td></tr>
</tbody></table>
