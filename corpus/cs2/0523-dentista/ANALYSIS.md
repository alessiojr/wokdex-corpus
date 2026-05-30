# Analysis Report: 0523-dentista
**Generated at:** 2026-03-27 02:17:14

Analysis Report for: 0523-dentista
Generated at: 2026-03-27 02:17:14
========================================

[Structure Check]
  - statements: FOUND
  - solutions: FOUND
  - test-cases: FOUND

[Statements Analysis]
  - Total Statements in Metadata: 1
  - ID 'a-dentista' (Level A): ✅ FOUND (a-dentista)
    - Languages (1): pt

[Statistics]
  - Test Cases: 39
  - Solutions: 2
  - ID 'a-optimal' (Level A): 
  - ID 'b-suboptimal' (Level B): 

[Metadata Validation]
  ✅ Schema Valid

[Test Scenarios Directory Check]
  - ID 'd-sample' (Level D): ✅ FOUND (d-sample)
  - ID 'c-contiguity' (Level C): ✅ FOUND (c-contiguity)
  - ID 'b-single-case' (Level B): ✅ FOUND (b-single-case)
  - ID 'b-wrong-sorting' (Level B): ✅ FOUND (b-wrong-sorting)
  - ID 'a-max-volume' (Level A): ✅ FOUND (a-max-volume)
  - ID 'a-performance-load' (Level A): ✅ FOUND (a-performance-load)

## Test Scenarios (grid)
| Scenario | TestType | Level | Count |
| :--- | :--- | :--- | :--- |
| d-sample | TDD | D | 3 |
| c-contiguity | TDD | C | 4 |
| b-single-case | TDD | B | 0 |
| b-wrong-sorting | TDD | B | 4 |
| a-max-volume | TDD | A | 22 |
| a-performance-load | TDD | A | 6 |

[Test Scenarios & Cases]
  - **Scenario: a-max-volume** (22 cases) — type: **TDD**
    - [TDD] max-volume-01: ✅ Synced (ID: 9280)
    - [TDD] max-volume-02: ✅ Synced (ID: 9289)
    - [TDD] max-volume-03: ✅ Synced (ID: 9291)
    - [TDD] max-volume-04: ✅ Synced (ID: 9283)
    - [TDD] max-volume-05: ✅ Synced (ID: 9293)
    - [TDD] max-volume-06: ✅ Synced (ID: 9267)
    - [TDD] max-volume-07: ✅ Synced (ID: 9285)
    - [TDD] max-volume-08: ✅ Synced (ID: 9286)
    - [TDD] max-volume-09: ✅ Synced (ID: 9287)
    - [TDD] max-volume-10: ✅ Synced (ID: 9288)
    - [TDD] max-volume-11: ✅ Synced (ID: 9298)
    - [TDD] max-volume-12: ✅ Synced (ID: 9281)
    - [TDD] max-volume-15: ✅ Synced (ID: 9302)
    - [TDD] max-volume-18: ✅ Synced (ID: 9305)
    - [TDD] max-volume-19: ✅ Synced (ID: 9306)
    - [TDD] max-volume-21: ✅ Synced (ID: 9309)
    - [TDD] max-volume-22: ✅ Synced (ID: 9310)
    - [TDD] max-volume-23: ✅ Synced (ID: 9282)
    - [TDD] max-volume-24: ✅ Synced (ID: 9312)
    - [TDD] max-volume-25: ✅ Synced (ID: 9313)
    - [TDD] max-volume-26: ✅ Synced (ID: 9314)
    - [TDD] max-volume-30: ✅ Synced (ID: 9284)
  - **Scenario: a-performance-load** (6 cases) — type: **TDD**
    - [TDD] performance-load-01: ✅ Synced (ID: 9274)
    - [TDD] performance-load-02: ✅ Synced (ID: 9275)
    - [TDD] performance-load-03: ✅ Synced (ID: 9276)
    - [TDD] performance-load-04: ✅ Synced (ID: 9277)
    - [TDD] performance-load-05: ✅ Synced (ID: 9278)
    - [TDD] performance-load-06: ✅ Synced (ID: 9273)
  - **Scenario: b-wrong-sorting** (4 cases) — type: **TDD**
    - [TDD] wrong-sorting-01: ✅ Synced (ID: 9265)
    - [TDD] wrong-sorting-02: ✅ Synced (ID: 9279)
    - [TDD] wrong-sorting-03: ✅ Synced (ID: 9271)
    - [TDD] wrong-sorting-04: ✅ Synced (ID: 9272)
  - **Scenario: c-contiguity** (4 cases) — type: **TDD**
    - [TDD] contiguity-01: ✅ Synced (ID: 9290)
    - [TDD] contiguity-03: ✅ Synced (ID: 9307)
    - [TDD] contiguity-05: ✅ Synced (ID: 9269)
    - [TDD] contiguity-06: ✅ Synced (ID: 9317)
  - **Scenario: d-sample** (3 cases) — type: **TDD**
    - [TDD] sample-01: ✅ Synced (ID: 9266)
    - [TDD] sample-02: ✅ Synced (ID: 9268)
    - [TDD] sample-03: ✅ Synced (ID: 9270)

## Solutions Check Report (Detalhado / Debug)
**Generated**: 2026-03-27T09:52:37.252601
**Solution**: `solutions/a-optimal/solution.cpp`

### Compilation
✅ /dados/projetos/mundoDoCodigo/problemas/pack-tecnicas/workspace/0523-dentista/solutions/a-optimal/solution.out

### Resultados

<table class="results-table"><thead><tr><th>Test Case</th><th>Result</th><th>Time (s)</th></tr></thead><tbody>
<tr class="scenario-row"><td colspan="3"><strong>a-max-volume - TDD</strong></td></tr>
<tr id="row-a-max-volume-max-volume-01-in"><td>max-volume-01.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr id="row-a-max-volume-max-volume-02-in"><td>max-volume-02.in</td><td>✅ PASS</td><td>0.003</td></tr>
<tr id="row-a-max-volume-max-volume-03-in"><td>max-volume-03.in</td><td>✅ PASS</td><td>0.004</td></tr>
<tr id="row-a-max-volume-max-volume-04-in"><td>max-volume-04.in</td><td>✅ PASS</td><td>0.005</td></tr>
<tr id="row-a-max-volume-max-volume-05-in"><td>max-volume-05.in</td><td>✅ PASS</td><td>0.005</td></tr>
<tr id="row-a-max-volume-max-volume-06-in"><td>max-volume-06.in</td><td>✅ PASS</td><td>0.003</td></tr>
<tr id="row-a-max-volume-max-volume-07-in"><td>max-volume-07.in</td><td>✅ PASS</td><td>0.005</td></tr>
<tr id="row-a-max-volume-max-volume-08-in"><td>max-volume-08.in</td><td>✅ PASS</td><td>0.006</td></tr>
<tr id="row-a-max-volume-max-volume-09-in"><td>max-volume-09.in</td><td>✅ PASS</td><td>0.008</td></tr>
<tr id="row-a-max-volume-max-volume-10-in"><td>max-volume-10.in</td><td>✅ PASS</td><td>0.005</td></tr>
<tr id="row-a-max-volume-max-volume-11-in"><td>max-volume-11.in</td><td>✅ PASS</td><td>0.007</td></tr>
<tr id="row-a-max-volume-max-volume-12-in"><td>max-volume-12.in</td><td>✅ PASS</td><td>0.006</td></tr>
<tr id="row-a-max-volume-max-volume-15-in"><td>max-volume-15.in</td><td>✅ PASS</td><td>0.007</td></tr>
<tr id="row-a-max-volume-max-volume-18-in"><td>max-volume-18.in</td><td>✅ PASS</td><td>0.007</td></tr>
<tr id="row-a-max-volume-max-volume-19-in"><td>max-volume-19.in</td><td>✅ PASS</td><td>0.007</td></tr>
<tr id="row-a-max-volume-max-volume-21-in"><td>max-volume-21.in</td><td>✅ PASS</td><td>0.005</td></tr>
<tr id="row-a-max-volume-max-volume-22-in"><td>max-volume-22.in</td><td>✅ PASS</td><td>0.005</td></tr>
<tr id="row-a-max-volume-max-volume-23-in"><td>max-volume-23.in</td><td>✅ PASS</td><td>0.007</td></tr>
<tr id="row-a-max-volume-max-volume-24-in"><td>max-volume-24.in</td><td>✅ PASS</td><td>0.006</td></tr>
<tr id="row-a-max-volume-max-volume-25-in"><td>max-volume-25.in</td><td>✅ PASS</td><td>0.008</td></tr>
<tr id="row-a-max-volume-max-volume-26-in"><td>max-volume-26.in</td><td>✅ PASS</td><td>0.008</td></tr>
<tr id="row-a-max-volume-max-volume-30-in"><td>max-volume-30.in</td><td>✅ PASS</td><td>0.007</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>a-performance-load - TDD</strong></td></tr>
<tr id="row-a-performance-load-performance-load-01-in"><td>performance-load-01.in</td><td>✅ PASS</td><td>0.009</td></tr>
<tr id="row-a-performance-load-performance-load-02-in"><td>performance-load-02.in</td><td>✅ PASS</td><td>0.009</td></tr>
<tr id="row-a-performance-load-performance-load-03-in"><td>performance-load-03.in</td><td>✅ PASS</td><td>0.010</td></tr>
<tr id="row-a-performance-load-performance-load-04-in"><td>performance-load-04.in</td><td>✅ PASS</td><td>0.009</td></tr>
<tr id="row-a-performance-load-performance-load-05-in"><td>performance-load-05.in</td><td>✅ PASS</td><td>0.008</td></tr>
<tr id="row-a-performance-load-performance-load-06-in"><td>performance-load-06.in</td><td>✅ PASS</td><td>0.006</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>b-wrong-sorting - TDD</strong></td></tr>
<tr id="row-b-wrong-sorting-wrong-sorting-01-in"><td>wrong-sorting-01.in</td><td>✅ PASS</td><td>0.004</td></tr>
<tr id="row-b-wrong-sorting-wrong-sorting-02-in"><td>wrong-sorting-02.in</td><td>✅ PASS</td><td>0.004</td></tr>
<tr id="row-b-wrong-sorting-wrong-sorting-03-in"><td>wrong-sorting-03.in</td><td>✅ PASS</td><td>0.003</td></tr>
<tr id="row-b-wrong-sorting-wrong-sorting-04-in"><td>wrong-sorting-04.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>c-contiguity - TDD</strong></td></tr>
<tr id="row-c-contiguity-contiguity-01-in"><td>contiguity-01.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr id="row-c-contiguity-contiguity-03-in"><td>contiguity-03.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr id="row-c-contiguity-contiguity-05-in"><td>contiguity-05.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr id="row-c-contiguity-contiguity-06-in"><td>contiguity-06.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>d-sample - TDD</strong></td></tr>
<tr id="row-d-sample-sample-01-in"><td>sample-01.in</td><td>✅ PASS</td><td>0.002</td></tr>
<tr id="row-d-sample-sample-02-in"><td>sample-02.in</td><td>✅ PASS</td><td>0.003</td></tr>
<tr id="row-d-sample-sample-03-in"><td>sample-03.in</td><td>✅ PASS</td><td>0.003</td></tr>
</tbody></table>
