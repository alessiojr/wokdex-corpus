# Analysis Report: 0416-corredor
**Generated at:** 2026-05-07 08:37:38

# Analysis Report — 0416-corredor
**Generated at:** 2026-05-07 08:37:38

## 1) Structure Check
- **statements**: ✅ FOUND
- **solutions**: ✅ FOUND
- **test-cases**: ✅ FOUND

## 2) Statements Analysis
- **Total statements in metadata**: `1`
- **ID `a-corredor`** (Level `A`): ✅ FOUND (a-corredor)
  - Languages (`1`): pt

## 3) Statistics
- **Test cases**: `41`
- **Solutions**: `2`
- **Solution ID `a-otima-kadane`** (Level `A`): ✅ OK
- **Solution ID `b-forca-bruta`** (Level `B`): ✅ OK

## 4) Metadata Validation
- ✅ Schema valid

## 5) Test Scenarios Directory Check
- **ID `a-performance-load`** (Level `A`): ✅ FOUND (a-performance-load)
- **ID `b-fuzzing`** (Level `B`): ✅ FOUND (b-fuzzing)
- **ID `c-edge-cases`** (Level `C`): ✅ FOUND (c-edge-cases)
- **ID `c-patterns`** (Level `C`): ✅ FOUND (c-patterns)
- **ID `d-sample`** (Level `D`): ✅ FOUND (d-sample)

## 6) Test Scenarios Grid
| Scenario | TestType | Level | Count |
| :--- | :--- | :--- | :--- |
| a-performance-load | Performance | A | 14 |
| b-fuzzing | Input | B | 17 |
| c-edge-cases | TDD | C | 6 |
| c-patterns | TDD | C | 2 |
| d-sample | TDD | D | 2 |

## 7) Test Scenarios & Cases
- **Scenario `a-performance-load`** (`14` cases) — type: **Performance**
  - [Performance] `performance-load-01`: 🆕 New (Local Only) (ID: None)
  - [Performance] `performance-load-02`: ✅ Synced (ID: 5885)
  - [Performance] `performance-load-03`: ✅ Synced (ID: 5891)
  - [Performance] `performance-load-04`: ✅ Synced (ID: 5892)
  - [Performance] `performance-load-05`: ✅ Synced (ID: 5893)
  - [Performance] `performance-load-06`: ✅ Synced (ID: 5894)
  - [Performance] `performance-load-07`: ✅ Synced (ID: 5900)
  - [Performance] `performance-load-08`: ✅ Synced (ID: 5901)
  - [Performance] `performance-load-09`: ✅ Synced (ID: 5902)
  - [Performance] `performance-load-10`: ✅ Synced (ID: 5903)
  - [Performance] `performance-load-11`: ✅ Synced (ID: 5882)
  - [Performance] `performance-load-12`: ✅ Synced (ID: 5883)
  - [Performance] `performance-load-13`: ✅ Synced (ID: 15099)
  - [Performance] `performance-load-14`: ✅ Synced (ID: 15100)
- **Scenario `b-fuzzing`** (`17` cases) — type: **Input**
  - [Input] `fuzzing-01`: ✅ Synced (ID: 5887)
  - [Input] `fuzzing-02`: ✅ Synced (ID: 5888)
  - [Input] `fuzzing-03`: ✅ Synced (ID: 5889)
  - [Input] `fuzzing-04`: ✅ Synced (ID: 5890)
  - [Input] `fuzzing-05`: ✅ Synced (ID: 5896)
  - [Input] `fuzzing-06`: ✅ Synced (ID: 5897)
  - [Input] `fuzzing-07`: ✅ Synced (ID: 5898)
  - [Input] `fuzzing-08`: ✅ Synced (ID: 5899)
  - [Input] `fuzzing-09`: ✅ Synced (ID: 5878)
  - [Input] `fuzzing-10`: ✅ Synced (ID: 5879)
  - [Input] `fuzzing-11`: ✅ Synced (ID: 5880)
  - [Input] `fuzzing-12`: ✅ Synced (ID: 5881)
  - [Input] `fuzzing-13`: ✅ Synced (ID: 15101)
  - [Input] `fuzzing-14`: ✅ Synced (ID: 15102)
  - [Input] `fuzzing-15`: ✅ Synced (ID: 15103)
  - [Input] `fuzzing-16`: ✅ Synced (ID: 15104)
  - [Input] `fuzzing-17`: ✅ Synced (ID: 15105)
- **Scenario `c-edge-cases`** (`6` cases) — type: **TDD**
  - [TDD] `edge-cases-01`: ✅ Synced (ID: 15106)
  - [TDD] `edge-cases-02`: ✅ Synced (ID: 5895)
  - [TDD] `edge-cases-03`: ✅ Synced (ID: 5904)
  - [TDD] `edge-cases-04`: 🆕 New (Local Only) (ID: None)
  - [TDD] `edge-cases-05`: ✅ Synced (ID: 15107)
  - [TDD] `edge-cases-06`: ✅ Synced (ID: 15108)
- **Scenario `c-patterns`** (`2` cases) — type: **TDD**
  - [TDD] `patterns-01`: 🆕 New (Local Only) (ID: None)
  - [TDD] `patterns-02`: 🆕 New (Local Only) (ID: None)
- **Scenario `d-sample`** (`2` cases) — type: **TDD**
  - [TDD] `sample-01`: ✅ Synced (ID: 5875)
  - [TDD] `sample-02`: ✅ Synced (ID: 5876)

## 8) Phase 0 Quality Gate
- **Overall**: ❌ FAIL
- **Next recommended prompt**: `0.5`

| Prompt | Status | Reason |
| :--- | :--- | :--- |
| `0.1` | ✅ done | ok |
| `0.2` | ✅ done | ok |
| `0.3` | ✅ done | ok |
| `0.4` | ✅ done | ok |
| `0.5` | ❌ pending | not_implemented |

## Solutions Check Report (Detalhado / Debug)
**Generated**: 2026-05-07T08:49:42.341244
**Solution**: `solutions/a-otima-kadane/resolucao.c`

### Compilation
✅ /dados/projetos/mundoDoCodigo/problemas/pack-tecnicas/workspace/0416-corredor/solutions/a-otima-kadane/resolucao.out

### Resultados

<table class="results-table"><thead><tr><th>Test Case</th><th>Result</th><th>Time (s)</th></tr></thead><tbody>
<tr class="scenario-row"><td colspan="3"><strong>a-performance-load - Performance</strong></td></tr>
<tr id="row-a-performance-load-performance-load-01-in"><td>performance-load-01.in</td><td>✅ PASS</td><td>0.004</td></tr>
<tr id="row-a-performance-load-performance-load-02-in"><td>performance-load-02.in</td><td>✅ PASS</td><td>0.004</td></tr>
<tr id="row-a-performance-load-performance-load-03-in"><td>performance-load-03.in</td><td>✅ PASS</td><td>0.004</td></tr>
<tr id="row-a-performance-load-performance-load-04-in"><td>performance-load-04.in</td><td>✅ PASS</td><td>0.007</td></tr>
<tr id="row-a-performance-load-performance-load-05-in"><td>performance-load-05.in</td><td>✅ PASS</td><td>0.006</td></tr>
<tr id="row-a-performance-load-performance-load-06-in"><td>performance-load-06.in</td><td>✅ PASS</td><td>0.007</td></tr>
<tr id="row-a-performance-load-performance-load-07-in"><td>performance-load-07.in</td><td>✅ PASS</td><td>0.006</td></tr>
<tr id="row-a-performance-load-performance-load-08-in"><td>performance-load-08.in</td><td>✅ PASS</td><td>0.007</td></tr>
<tr id="row-a-performance-load-performance-load-09-in"><td>performance-load-09.in</td><td>✅ PASS</td><td>0.006</td></tr>
<tr id="row-a-performance-load-performance-load-10-in"><td>performance-load-10.in</td><td>✅ PASS</td><td>0.006</td></tr>
<tr id="row-a-performance-load-performance-load-11-in"><td>performance-load-11.in</td><td>✅ PASS</td><td>0.006</td></tr>
<tr id="row-a-performance-load-performance-load-12-in"><td>performance-load-12.in</td><td>✅ PASS</td><td>0.007</td></tr>
<tr id="row-a-performance-load-performance-load-13-in"><td>performance-load-13.in</td><td>✅ PASS</td><td>0.005</td></tr>
<tr id="row-a-performance-load-performance-load-14-in"><td>performance-load-14.in</td><td>✅ PASS</td><td>0.005</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>b-fuzzing - Input</strong></td></tr>
<tr id="row-b-fuzzing-fuzzing-01-in"><td>fuzzing-01.in</td><td>✅ PASS</td><td>0.001</td></tr>
<tr id="row-b-fuzzing-fuzzing-02-in"><td>fuzzing-02.in</td><td>✅ PASS</td><td>0.001</td></tr>
<tr id="row-b-fuzzing-fuzzing-03-in"><td>fuzzing-03.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr id="row-b-fuzzing-fuzzing-04-in"><td>fuzzing-04.in</td><td>✅ PASS</td><td>0.005</td></tr>
<tr id="row-b-fuzzing-fuzzing-05-in"><td>fuzzing-05.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr id="row-b-fuzzing-fuzzing-06-in"><td>fuzzing-06.in</td><td>✅ PASS</td><td>0.003</td></tr>
<tr id="row-b-fuzzing-fuzzing-07-in"><td>fuzzing-07.in</td><td>✅ PASS</td><td>0.003</td></tr>
<tr id="row-b-fuzzing-fuzzing-08-in"><td>fuzzing-08.in</td><td>✅ PASS</td><td>0.005</td></tr>
<tr id="row-b-fuzzing-fuzzing-09-in"><td>fuzzing-09.in</td><td>✅ PASS</td><td>0.001</td></tr>
<tr id="row-b-fuzzing-fuzzing-10-in"><td>fuzzing-10.in</td><td>✅ PASS</td><td>0.001</td></tr>
<tr id="row-b-fuzzing-fuzzing-11-in"><td>fuzzing-11.in</td><td>✅ PASS</td><td>0.003</td></tr>
<tr id="row-b-fuzzing-fuzzing-12-in"><td>fuzzing-12.in</td><td>✅ PASS</td><td>0.005</td></tr>
<tr id="row-b-fuzzing-fuzzing-13-in"><td>fuzzing-13.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr id="row-b-fuzzing-fuzzing-14-in"><td>fuzzing-14.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr id="row-b-fuzzing-fuzzing-15-in"><td>fuzzing-15.in</td><td>✅ PASS</td><td>0.001</td></tr>
<tr id="row-b-fuzzing-fuzzing-16-in"><td>fuzzing-16.in</td><td>✅ PASS</td><td>0.001</td></tr>
<tr id="row-b-fuzzing-fuzzing-17-in"><td>fuzzing-17.in</td><td>✅ PASS</td><td>0.001</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>c-edge-cases - TDD</strong></td></tr>
<tr id="row-c-edge-cases-edge-cases-01-in"><td>edge-cases-01.in</td><td>✅ PASS</td><td>0.005</td></tr>
<tr id="row-c-edge-cases-edge-cases-02-in"><td>edge-cases-02.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr id="row-c-edge-cases-edge-cases-03-in"><td>edge-cases-03.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr id="row-c-edge-cases-edge-cases-04-in"><td>edge-cases-04.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr id="row-c-edge-cases-edge-cases-05-in"><td>edge-cases-05.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr id="row-c-edge-cases-edge-cases-06-in"><td>edge-cases-06.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>c-patterns - TDD</strong></td></tr>
<tr id="row-c-patterns-patterns-01-in"><td>patterns-01.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr id="row-c-patterns-patterns-02-in"><td>patterns-02.in</td><td>✅ PASS</td><td>0.003</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>d-sample - TDD</strong></td></tr>
<tr id="row-d-sample-sample-01-in"><td>sample-01.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr id="row-d-sample-sample-02-in"><td>sample-02.in</td><td>✅ PASS</td><td>0.002</td></tr>
</tbody></table>
