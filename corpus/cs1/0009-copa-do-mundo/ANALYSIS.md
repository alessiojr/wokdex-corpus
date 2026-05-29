# Analysis Report: 0009-copa-do-mundo
**Generated at:** 2026-04-15 20:47:29

# Analysis Report — 0009-copa-do-mundo
**Generated at:** 2026-04-15 20:47:29

## 1) Structure Check
- **statements**: ✅ FOUND
- **solutions**: ✅ FOUND
- **test-cases**: ✅ FOUND

## 2) Statements Analysis
- **Total statements in metadata**: `2`
- **ID `a-copa-do-mundo`** (Level `A`): ✅ FOUND (a-copa-do-mundo)
  - Languages (`1`): pt
- **ID `a-wok-copa-do-mundo`** (Level `A`): ✅ FOUND (a-wok-copa-do-mundo)
  - Languages (`1`): pt

## 3) Statistics
- **Test cases**: `26`
- **Solutions**: `2`
- **Solution ID `a-optimal`** (Level `A`): ✅ OK
- **Solution ID `b-suboptimal`** (Level `B`): ✅ OK

## 4) Metadata Validation
- ✅ Schema valid

## 5) Test Scenarios Directory Check
- **ID `c-edge-no-matches`** (Level `C`): ✅ FOUND (c-edge-no-matches)
- **ID `c-single-team`** (Level `C`): ✅ FOUND (c-single-team)
- **ID `b-all-wins-no-draws`** (Level `B`): ✅ FOUND (b-all-wins-no-draws)
- **ID `b-all-draws`** (Level `B`): ✅ FOUND (b-all-draws)
- **ID `b-mixed-results`** (Level `B`): ✅ FOUND (b-mixed-results)
- **ID `c-multi-cases-with-terminator`** (Level `C`): ✅ FOUND (c-multi-cases-with-terminator)
- **ID `a-stress-max-teams`** (Level `A`): ✅ FOUND (a-stress-max-teams)
- **ID `c-formatting-robust-io`** (Level `C`): ✅ FOUND (c-formatting-robust-io)
- **ID `d-sample`** (Level `D`): ✅ FOUND (d-sample)

## 6) Test Scenarios Grid
| Scenario                      | TestType | Level | Count |
|:------------------------------|:---------|:------|:------|
| c-edge-no-matches             | TDD      | C     | 2     |
| c-single-team                 | TDD      | C     | 1     |
| b-all-wins-no-draws           | TDD      | B     | 4     |
| b-all-draws                   | TDD      | B     | 3     |
| b-mixed-results               | TDD      | B     | 10    |
| c-multi-cases-with-terminator | TDD      | C     | 1     |
| a-stress-max-teams            | TDD      | A     | 1     |
| c-formatting-robust-io        | TDD      | C     | 1     |
| d-sample                      | TDD      | D     | 3     |

## 7) Test Scenarios & Cases
- **Scenario `a-stress-max-teams`** (`1` cases) — type: **TDD**
  - [TDD] `stress-max-teams-01`: ✅ Synced (ID: 14541)
- **Scenario `b-all-draws`** (`3` cases) — type: **TDD**
  - [TDD] `all-draws-01`: ✅ Synced (ID: 14538)
  - [TDD] `all-draws-02`: ✅ Synced (ID: 165)
  - [TDD] `all-draws-03`: ✅ Synced (ID: 166)
- **Scenario `b-all-wins-no-draws`** (`4` cases) — type: **TDD**
  - [TDD] `all-wins-no-draws-01`: ✅ Synced (ID: 14539)
  - [TDD] `all-wins-no-draws-02`: ✅ Synced (ID: 156)
  - [TDD] `all-wins-no-draws-03`: ✅ Synced (ID: 167)
  - [TDD] `all-wins-no-draws-04`: ✅ Synced (ID: 168)
- **Scenario `b-mixed-results`** (`10` cases) — type: **TDD**
  - [TDD] `mixed-results-01`: ✅ Synced (ID: 14540)
  - [TDD] `mixed-results-02`: ✅ Synced (ID: 169)
  - [TDD] `mixed-results-03`: ✅ Synced (ID: 170)
  - [TDD] `mixed-results-04`: ✅ Synced (ID: 157)
  - [TDD] `mixed-results-05`: ✅ Synced (ID: 159)
  - [TDD] `mixed-results-06`: ✅ Synced (ID: 160)
  - [TDD] `mixed-results-07`: ✅ Synced (ID: 161)
  - [TDD] `mixed-results-08`: ✅ Synced (ID: 162)
  - [TDD] `mixed-results-09`: ✅ Synced (ID: 163)
  - [TDD] `mixed-results-10`: ✅ Synced (ID: 164)
- **Scenario `c-edge-no-matches`** (`2` cases) — type: **TDD**
  - [TDD] `edge-no-matches-01`: ✅ Synced (ID: 14534)
  - [TDD] `edge-no-matches-02`: ✅ Synced (ID: 158)
- **Scenario `c-formatting-robust-io`** (`1` cases) — type: **TDD**
  - [TDD] `formatting-robust-io-01`: ✅ Synced (ID: 14535)
- **Scenario `c-multi-cases-with-terminator`** (`1` cases) — type: **TDD**
  - [TDD] `multi-cases-with-terminator-01`: ✅ Synced (ID: 14536)
- **Scenario `c-single-team`** (`1` cases) — type: **TDD**
  - [TDD] `single-team-01`: ✅ Synced (ID: 14537)
- **Scenario `d-sample`** (`3` cases) — type: **TDD**
  - [TDD] `sample-01`: ✅ Synced (ID: 14531)
  - [TDD] `sample-02`: ✅ Synced (ID: 14532)
  - [TDD] `sample-03`: ✅ Synced (ID: 14533)

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
**Generated**: 2026-03-24T23:13:39.751860
**Solution**: `solutions/a-optimal/Copa.cpp`

### Compilation
✅ /dados/projetos/mundoDoCodigo/problemas/pack-tecnicas/workspace/0009-copa-do-mundo/solutions/a-optimal/Copa.out

### Resultados

<table class="results-table"><thead><tr><th>Test Case</th><th>Result</th><th>Time (s)</th></tr></thead><tbody>
<tr class="scenario-row"><td colspan="3"><strong>a-stress-max-teams - TDD</strong></td></tr>
<tr id="row-a-stress-max-teams-stress-max-teams-01-in"><td>stress-max-teams-01.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>b-all-draws - TDD</strong></td></tr>
<tr id="row-b-all-draws-all-draws-01-in"><td>all-draws-01.in</td><td>✅ PASS</td><td>0.001</td></tr>
<tr id="row-b-all-draws-all-draws-02-in"><td>all-draws-02.in</td><td>✅ PASS</td><td>0.001</td></tr>
<tr id="row-b-all-draws-all-draws-03-in"><td>all-draws-03.in</td><td>✅ PASS</td><td>0.001</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>b-all-wins-no-draws - TDD</strong></td></tr>
<tr id="row-b-all-wins-no-draws-all-wins-no-draws-01-in"><td>all-wins-no-draws-01.in</td><td>✅ PASS</td><td>0.001</td></tr>
<tr id="row-b-all-wins-no-draws-all-wins-no-draws-02-in"><td>all-wins-no-draws-02.in</td><td>✅ PASS</td><td>0.001</td></tr>
<tr id="row-b-all-wins-no-draws-all-wins-no-draws-03-in"><td>all-wins-no-draws-03.in</td><td>✅ PASS</td><td>0.001</td></tr>
<tr id="row-b-all-wins-no-draws-all-wins-no-draws-04-in"><td>all-wins-no-draws-04.in</td><td>✅ PASS</td><td>0.001</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>b-mixed-results - TDD</strong></td></tr>
<tr id="row-b-mixed-results-mixed-results-01-in"><td>mixed-results-01.in</td><td>✅ PASS</td><td>0.001</td></tr>
<tr id="row-b-mixed-results-mixed-results-02-in"><td>mixed-results-02.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr id="row-b-mixed-results-mixed-results-03-in"><td>mixed-results-03.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr id="row-b-mixed-results-mixed-results-04-in"><td>mixed-results-04.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr id="row-b-mixed-results-mixed-results-05-in"><td>mixed-results-05.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr id="row-b-mixed-results-mixed-results-06-in"><td>mixed-results-06.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr id="row-b-mixed-results-mixed-results-07-in"><td>mixed-results-07.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr id="row-b-mixed-results-mixed-results-08-in"><td>mixed-results-08.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr id="row-b-mixed-results-mixed-results-09-in"><td>mixed-results-09.in</td><td>✅ PASS</td><td>0.003</td></tr>
<tr id="row-b-mixed-results-mixed-results-10-in"><td>mixed-results-10.in</td><td>✅ PASS</td><td>0.003</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>c-edge-no-matches - TDD</strong></td></tr>
<tr id="row-c-edge-no-matches-edge-no-matches-01-in"><td>edge-no-matches-01.in</td><td>✅ PASS</td><td>0.004</td></tr>
<tr id="row-c-edge-no-matches-edge-no-matches-02-in"><td>edge-no-matches-02.in</td><td>✅ PASS</td><td>0.004</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>c-formatting-robust-io - TDD</strong></td></tr>
<tr id="row-c-formatting-robust-io-formatting-robust-io-01-in"><td>formatting-robust-io-01.in</td><td>✅ PASS</td><td>0.004</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>c-multi-cases-with-terminator - TDD</strong></td></tr>
<tr id="row-c-multi-cases-with-terminator-multi-cases-with-terminator-01-in"><td>multi-cases-with-terminator-01.in</td><td>✅ PASS</td><td>0.004</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>c-single-team - TDD</strong></td></tr>
<tr id="row-c-single-team-single-team-01-in"><td>single-team-01.in</td><td>✅ PASS</td><td>0.003</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>d-sample - TDD</strong></td></tr>
<tr id="row-d-sample-sample-01-in"><td>sample-01.in</td><td>✅ PASS</td><td>0.004</td></tr>
<tr id="row-d-sample-sample-02-in"><td>sample-02.in</td><td>✅ PASS</td><td>0.003</td></tr>
<tr id="row-d-sample-sample-03-in"><td>sample-03.in</td><td>✅ PASS</td><td>0.003</td></tr>
</tbody></table>
