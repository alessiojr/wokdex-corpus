# Analysis Report: 0022-alarme-despertador
**Generated at:** 2026-04-10 18:05:52

# Analysis Report — 0022-alarme-despertador
**Generated at:** 2026-04-10 18:05:52

## 1) Structure Check
- **statements**: ✅ FOUND
- **solutions**: ✅ FOUND
- **test-cases**: ✅ FOUND

## 2) Statements Analysis
- **Total statements in metadata**: `1`
- **ID `a-alarme-despertador`** (Level `A`): ✅ FOUND (a-alarme-despertador)
  - Languages (`1`): pt

## 3) Statistics
- **Test cases**: `11`
- **Solutions**: `1`
- **Solution ID `a-optimal`** (Level `A`): ✅ OK

## 4) Metadata Validation
- ✅ Schema valid

## 5) Test Scenarios Directory Check
- **ID `a-performance-load`** (Level `A`): ✅ FOUND (a-performance-load)
- **ID `b-multiplas-entradas`** (Level `B`): ✅ FOUND (b-multiplas-entradas)
- **ID `b-dia-invertido`** (Level `B`): ✅ FOUND (b-dia-invertido)
- **ID `c-mesmo-dia`** (Level `C`): ✅ FOUND (c-mesmo-dia)
- **ID `d-sample`** (Level `D`): ✅ FOUND (d-sample)
- **ID `c-mesmo-horario`** (Level `C`): ✅ FOUND (c-mesmo-horario)

## 6) Test Scenarios Grid
| Scenario             | TestType | Level | Count |
|:---------------------|:---------|:------|:------|
| a-performance-load   | TDD      | A     | 1     |
| b-multiplas-entradas | TDD      | B     | 1     |
| b-dia-invertido      | TDD      | B     | 5     |
| c-mesmo-dia          | TDD      | C     | 1     |
| d-sample             | TDD      | D     | 2     |
| c-mesmo-horario      | TDD      | C     | 1     |

## 7) Test Scenarios & Cases
- **Scenario `a-performance-load`** (`1` cases) — type: **TDD**
  - [TDD] `performance-load-01`: ✅ Synced (ID: 14698)
- **Scenario `b-dia-invertido`** (`5` cases) — type: **TDD**
  - [TDD] `dia-invertido-01`: ✅ Synced (ID: 280)
  - [TDD] `dia-invertido-02`: ✅ Synced (ID: 281)
  - [TDD] `dia-invertido-03`: ✅ Synced (ID: 282)
  - [TDD] `dia-invertido-04`: ✅ Synced (ID: 283)
  - [TDD] `dia-invertido-05`: ✅ Synced (ID: 284)
- **Scenario `b-multiplas-entradas`** (`1` cases) — type: **TDD**
  - [TDD] `multiplas-entradas-01`: ✅ Synced (ID: 14697)
- **Scenario `c-mesmo-dia`** (`1` cases) — type: **TDD**
  - [TDD] `mesmo-dia-01`: ✅ Synced (ID: 14696)
- **Scenario `c-mesmo-horario`** (`1` cases) — type: **TDD**
  - [TDD] `mesmo-horario-01`: ✅ Synced (ID: 14880)
- **Scenario `d-sample`** (`2` cases) — type: **TDD**
  - [TDD] `sample-01`: ✅ Synced (ID: 279)
  - [TDD] `sample-02`: ✅ Synced (ID: 14695)

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

## Solutions Check Report (Detalhado / Debug)
**Generated**: 2026-04-10T18:05:20.614126
**Solution**: `solutions/a-optimal/alarme.c`

### Compilation
✅ /dados/projetos/mundoDoCodigo/problemas/pack-tecnicas/workspace/0022-alarme-despertador/solutions/a-optimal/alarme.out

### Resultados

<table class="results-table"><thead><tr><th>Test Case</th><th>Result</th><th>Time (s)</th></tr></thead><tbody>
<tr class="scenario-row"><td colspan="3"><strong>a-performance-load - TDD</strong></td></tr>
<tr id="row-a-performance-load-performance-load-01-in"><td>performance-load-01.in</td><td>✅ PASS</td><td>0.031</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>b-dia-invertido - TDD</strong></td></tr>
<tr id="row-b-dia-invertido-dia-invertido-01-in"><td>dia-invertido-01.in</td><td>✅ PASS</td><td>0.001</td></tr>
<tr id="row-b-dia-invertido-dia-invertido-02-in"><td>dia-invertido-02.in</td><td>✅ PASS</td><td>0.001</td></tr>
<tr id="row-b-dia-invertido-dia-invertido-03-in"><td>dia-invertido-03.in</td><td>✅ PASS</td><td>0.001</td></tr>
<tr id="row-b-dia-invertido-dia-invertido-04-in"><td>dia-invertido-04.in</td><td>✅ PASS</td><td>0.001</td></tr>
<tr id="row-b-dia-invertido-dia-invertido-05-in"><td>dia-invertido-05.in</td><td>✅ PASS</td><td>0.001</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>b-multiplas-entradas - TDD</strong></td></tr>
<tr id="row-b-multiplas-entradas-multiplas-entradas-01-in"><td>multiplas-entradas-01.in</td><td>✅ PASS</td><td>0.001</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>c-mesmo-dia - TDD</strong></td></tr>
<tr id="row-c-mesmo-dia-mesmo-dia-01-in"><td>mesmo-dia-01.in</td><td>✅ PASS</td><td>0.001</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>c-mesmo-horario - TDD</strong></td></tr>
<tr id="row-c-mesmo-horario-mesmo-horario-01-in"><td>mesmo-horario-01.in</td><td>✅ PASS</td><td>0.001</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>d-sample - TDD</strong></td></tr>
<tr id="row-d-sample-sample-01-in"><td>sample-01.in</td><td>✅ PASS</td><td>0.001</td></tr>
<tr id="row-d-sample-sample-02-in"><td>sample-02.in</td><td>✅ PASS</td><td>0.001</td></tr>
</tbody></table>
