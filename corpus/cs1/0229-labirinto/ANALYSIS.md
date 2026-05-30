# Analysis Report: 0229-labirinto
**Generated at:** 2026-04-15 21:14:49

# Analysis Report — 0229-labirinto
**Generated at:** 2026-04-15 21:14:49

## 1) Structure Check
- **statements**: ✅ FOUND
- **solutions**: ✅ FOUND
- **test-cases**: ✅ FOUND

## 2) Statements Analysis
- **Total statements in metadata**: `1`
- **ID `a-labirinto`** (Level `A`): ✅ FOUND (a-labirinto)
  - Languages (`1`): pt

## 3) Statistics
- **Test cases**: `23`
- **Solutions**: `3`
- **Solution ID `a-optimal`** (Level `A`): ✅ OK
- **Solution ID `b-suboptimal`** (Level `B`): ✅ OK
- **Solution ID `c-wa-multiplica-exclamacao`** (Level `C`): ✅ OK

## 4) Metadata Validation
- ✅ Schema valid

## 5) Test Scenarios Directory Check
- **ID `d-sample`** (Level `D`): ✅ FOUND (d-sample)
- **ID `c-soma-digitos`** (Level `C`): ✅ FOUND (c-soma-digitos)
- **ID `c-espacos-e-linhas`** (Level `C`): ✅ FOUND (c-espacos-e-linhas)
- **ID `b-entrada-errada`** (Level `B`): ✅ FOUND (b-entrada-errada)
- **ID `b-eof-e-multiplos`** (Level `B`): ✅ FOUND (b-eof-e-multiplos)
- **ID `c-exclamacao-unica`** (Level `C`): ✅ FOUND (c-exclamacao-unica)
- **ID `c-consecutive-digits`** (Level `C`): ✅ FOUND (c-consecutive-digits)
- **ID `b-special-handling`** (Level `B`): ✅ FOUND (b-special-handling)
- **ID `a-performance-load`** (Level `A`): ✅ FOUND (a-performance-load)

## 6) Test Scenarios Grid
| Scenario             | TestType    | Level | Count |
|:---------------------|:------------|:------|:------|
| d-sample             | TDD         | D     | 3     |
| c-soma-digitos       | TDD         | C     | 3     |
| c-espacos-e-linhas   | TDD         | C     | 3     |
| b-entrada-errada     | TDD         | B     | 4     |
| b-eof-e-multiplos    | TDD         | B     | 1     |
| c-exclamacao-unica   | False-Green | C     | 2     |
| c-consecutive-digits | TDD         | C     | 2     |
| b-special-handling   | TDD         | B     | 2     |
| a-performance-load   | TDD         | A     | 3     |

## 7) Test Scenarios & Cases
- **Scenario `a-performance-load`** (`3` cases) — type: **TDD**
  - [TDD] `performance-load-01`: ✅ Synced (ID: 14693)
  - [TDD] `performance-load-02`: ✅ Synced (ID: 14694)
  - [TDD] `performance-load-03`: ✅ Synced (ID: 3995)
- **Scenario `b-entrada-errada`** (`4` cases) — type: **TDD**
  - [TDD] `entrada-errada-01`: ✅ Synced (ID: 14686)
  - [TDD] `entrada-errada-02`: ✅ Synced (ID: 14687)
  - [TDD] `entrada-errada-03`: ✅ Synced (ID: 14688)
  - [TDD] `entrada-errada-04`: ✅ Synced (ID: 14689)
- **Scenario `b-eof-e-multiplos`** (`1` cases) — type: **TDD**
  - [TDD] `eof-e-multiplos-01`: ✅ Synced (ID: 14690)
- **Scenario `b-special-handling`** (`2` cases) — type: **TDD**
  - [TDD] `special-handling-01`: ✅ Synced (ID: 14691)
  - [TDD] `special-handling-02`: ✅ Synced (ID: 14692)
- **Scenario `c-consecutive-digits`** (`2` cases) — type: **TDD**
  - [TDD] `consecutive-digits-01`: ✅ Synced (ID: 14675)
  - [TDD] `consecutive-digits-02`: ✅ Synced (ID: 14676)
- **Scenario `c-espacos-e-linhas`** (`3` cases) — type: **TDD**
  - [TDD] `espacos-e-linhas-01`: ✅ Synced (ID: 14677)
  - [TDD] `espacos-e-linhas-02`: ✅ Synced (ID: 14678)
  - [TDD] `espacos-e-linhas-03`: ✅ Synced (ID: 14679)
- **Scenario `c-exclamacao-unica`** (`2` cases) — type: **False-Green**
  - [False-Green] `exclamacao-unica-02`: ✅ Synced (ID: 14681)
  - [False-Green] `exclamacao-unica-03`: ✅ Synced (ID: 14682)
- **Scenario `c-soma-digitos`** (`3` cases) — type: **TDD**
  - [TDD] `soma-digitos-01`: ✅ Synced (ID: 14683)
  - [TDD] `soma-digitos-02`: ✅ Synced (ID: 14684)
  - [TDD] `soma-digitos-03`: ✅ Synced (ID: 14685)
- **Scenario `d-sample`** (`3` cases) — type: **TDD**
  - [TDD] `sample-01`: ✅ Synced (ID: 14672)
  - [TDD] `sample-02`: ✅ Synced (ID: 14673)
  - [TDD] `sample-03`: ✅ Synced (ID: 14674)

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
**Generated**: 2026-04-06T12:44:34.237306
**Solution**: `solutions/a-optimal/Solution.java`

### Compilation
✅ Compilation successful

### Resultados

<table class="results-table"><thead><tr><th>Test Case</th><th>Result</th><th>Time (s)</th></tr></thead><tbody>
<tr class="scenario-row"><td colspan="3"><strong>a-performance-load - TDD</strong></td></tr>
<tr id="row-a-performance-load-performance-load-01-in"><td>performance-load-01.in</td><td>✅ PASS</td><td>0.106</td></tr>
<tr id="row-a-performance-load-performance-load-02-in"><td>performance-load-02.in</td><td>✅ PASS</td><td>0.123</td></tr>
<tr id="row-a-performance-load-performance-load-03-in"><td>performance-load-03.in</td><td>✅ PASS</td><td>0.098</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>b-entrada-errada - TDD</strong></td></tr>
<tr id="row-b-entrada-errada-entrada-errada-01-in"><td>entrada-errada-01.in</td><td>✅ PASS</td><td>0.101</td></tr>
<tr id="row-b-entrada-errada-entrada-errada-02-in"><td>entrada-errada-02.in</td><td>✅ PASS</td><td>0.095</td></tr>
<tr id="row-b-entrada-errada-entrada-errada-03-in"><td>entrada-errada-03.in</td><td>✅ PASS</td><td>0.074</td></tr>
<tr id="row-b-entrada-errada-entrada-errada-04-in"><td>entrada-errada-04.in</td><td>✅ PASS</td><td>0.069</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>b-eof-e-multiplos - TDD</strong></td></tr>
<tr id="row-b-eof-e-multiplos-eof-e-multiplos-01-in"><td>eof-e-multiplos-01.in</td><td>✅ PASS</td><td>0.105</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>b-special-handling - TDD</strong></td></tr>
<tr id="row-b-special-handling-special-handling-01-in"><td>special-handling-01.in</td><td>✅ PASS</td><td>0.101</td></tr>
<tr id="row-b-special-handling-special-handling-02-in"><td>special-handling-02.in</td><td>✅ PASS</td><td>0.119</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>c-consecutive-digits - TDD</strong></td></tr>
<tr id="row-c-consecutive-digits-consecutive-digits-01-in"><td>consecutive-digits-01.in</td><td>✅ PASS</td><td>0.082</td></tr>
<tr id="row-c-consecutive-digits-consecutive-digits-02-in"><td>consecutive-digits-02.in</td><td>✅ PASS</td><td>0.076</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>c-espacos-e-linhas - TDD</strong></td></tr>
<tr id="row-c-espacos-e-linhas-espacos-e-linhas-01-in"><td>espacos-e-linhas-01.in</td><td>✅ PASS</td><td>0.091</td></tr>
<tr id="row-c-espacos-e-linhas-espacos-e-linhas-02-in"><td>espacos-e-linhas-02.in</td><td>✅ PASS</td><td>0.089</td></tr>
<tr id="row-c-espacos-e-linhas-espacos-e-linhas-03-in"><td>espacos-e-linhas-03.in</td><td>✅ PASS</td><td>0.082</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>c-exclamacao-unica - False-Green</strong></td></tr>
<tr id="row-c-exclamacao-unica-exclamacao-unica-02-in"><td><a href="#detail-c-exclamacao-unica-exclamacao-unica-02-in" class="tc-link">exclamacao-unica-02.in</a></td><td>✅ WA (expected)</td><td>0.078</td></tr>
<tr id="row-c-exclamacao-unica-exclamacao-unica-03-in"><td><a href="#detail-c-exclamacao-unica-exclamacao-unica-03-in" class="tc-link">exclamacao-unica-03.in</a></td><td>✅ WA (expected)</td><td>0.085</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>c-soma-digitos - TDD</strong></td></tr>
<tr id="row-c-soma-digitos-soma-digitos-01-in"><td>soma-digitos-01.in</td><td>✅ PASS</td><td>0.077</td></tr>
<tr id="row-c-soma-digitos-soma-digitos-02-in"><td>soma-digitos-02.in</td><td>✅ PASS</td><td>0.067</td></tr>
<tr id="row-c-soma-digitos-soma-digitos-03-in"><td>soma-digitos-03.in</td><td>✅ PASS</td><td>0.085</td></tr>
<tr class="scenario-row"><td colspan="3"><strong>d-sample - TDD</strong></td></tr>
<tr id="row-d-sample-sample-01-in"><td>sample-01.in</td><td>✅ PASS</td><td>0.084</td></tr>
<tr id="row-d-sample-sample-02-in"><td>sample-02.in</td><td>✅ PASS</td><td>0.087</td></tr>
<tr id="row-d-sample-sample-03-in"><td>sample-03.in</td><td>✅ PASS</td><td>0.096</td></tr>
</tbody></table>

### Detalhes (WA) — Expected vs Actual

<p id="detail-c-exclamacao-unica-exclamacao-unica-02-in"><strong>c-exclamacao-unica/exclamacao-unica-02.in</strong> <a href="#row-c-exclamacao-unica-exclamacao-unica-02-in" class="back-to-table" title="Voltar à tabela">↑ voltar</a></p>

<div class="wa-diff-wrap"><table class="diff" id="difflib_chg_to2__top"
           cellspacing="0" cellpadding="0" rules="groups" >
        <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup>
        <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup>
        <thead><tr><th class="diff_next"><br /></th><th colspan="2" class="diff_header">Expected</th><th class="diff_next"><br /></th><th colspan="2" class="diff_header">Actual</th></tr></thead>
        <tbody>
            <tr><td class="diff_next" id="difflib_chg_to2__0"></td><td class="diff_header" id="from2_2">2</td><td nowrap="nowrap">B</td><td class="diff_next"></td><td class="diff_header" id="to2_2">2</td><td nowrap="nowrap">B</td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from2_3">3</td><td nowrap="nowrap">-------------</td><td class="diff_next"></td><td class="diff_header" id="to2_3">3</td><td nowrap="nowrap">-------------</td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from2_4">4</td><td nowrap="nowrap">A</td><td class="diff_next"></td><td class="diff_header" id="to2_4">4</td><td nowrap="nowrap">A</td></tr>
            <tr><td class="diff_next"><a href="#difflib_chg_to2__1">n</a></td><td class="diff_header" id="from2_5">5</td><td nowrap="nowrap"><span class="diff_sub">&nbsp;</span></td><td class="diff_next"><a href="#difflib_chg_to2__1">n</a></td><td class="diff_header"></td><td nowrap="nowrap"></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from2_6">6</td><td nowrap="nowrap"><span class="diff_sub">&nbsp;</span></td><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from2_7">7</td><td nowrap="nowrap"><span class="diff_sub">&nbsp;</span></td><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td></tr>
            <tr><td class="diff_next" id="difflib_chg_to2__1"></td><td class="diff_header" id="from2_8">8</td><td nowrap="nowrap"><span class="diff_sub">&nbsp;</span></td><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from2_9">9</td><td nowrap="nowrap">B</td><td class="diff_next"></td><td class="diff_header" id="to2_5">5</td><td nowrap="nowrap">B</td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from2_10">10</td><td nowrap="nowrap">-------------</td><td class="diff_next"></td><td class="diff_header" id="to2_6">6</td><td nowrap="nowrap">-------------</td></tr>
            <tr><td class="diff_next" id="difflib_chg_to2__2"><a href="#difflib_chg_to2__2">n</a></td><td class="diff_header" id="from2_11">11</td><td nowrap="nowrap"><span class="diff_sub">AB</span></td><td class="diff_next"><a href="#difflib_chg_to2__2">n</a></td><td class="diff_header" id="to2_7">7</td><td nowrap="nowrap"><span class="diff_add">A</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to2_8">8</td><td nowrap="nowrap"><span class="diff_add">B</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from2_12">12</td><td nowrap="nowrap">-------------</td><td class="diff_next"></td><td class="diff_header" id="to2_9">9</td><td nowrap="nowrap">-------------</td></tr>
            <tr><td class="diff_next"><a href="#difflib_chg_to2__top">t</a></td><td class="diff_header" id="from2_13">13</td><td nowrap="nowrap"><span class="diff_sub">&nbsp;</span></td><td class="diff_next"><a href="#difflib_chg_to2__top">t</a></td><td class="diff_header"></td><td nowrap="nowrap"></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from2_14">14</td><td nowrap="nowrap"><span class="diff_sub">&nbsp;</span></td><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from2_15">15</td><td nowrap="nowrap"><span class="diff_sub">&nbsp;</span></td><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from2_16">16</td><td nowrap="nowrap"><span class="diff_sub">&nbsp;</span></td><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from2_17">17</td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to2_10">10</td><td nowrap="nowrap"></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from2_18">18</td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to2_11">11</td><td nowrap="nowrap"></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from2_19">19</td><td nowrap="nowrap">-------------</td><td class="diff_next"></td><td class="diff_header" id="to2_12">12</td><td nowrap="nowrap">-------------</td></tr>
        </tbody>
    </table></div>

<p id="detail-c-exclamacao-unica-exclamacao-unica-03-in"><strong>c-exclamacao-unica/exclamacao-unica-03.in</strong> <a href="#row-c-exclamacao-unica-exclamacao-unica-03-in" class="back-to-table" title="Voltar à tabela">↑ voltar</a></p>

<div class="wa-diff-wrap"><table class="diff" id="difflib_chg_to3__top"
           cellspacing="0" cellpadding="0" rules="groups" >
        <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup>
        <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup>
        <thead><tr><th class="diff_next"><br /></th><th colspan="2" class="diff_header">Expected</th><th class="diff_next"><br /></th><th colspan="2" class="diff_header">Actual</th></tr></thead>
        <tbody>
            <tr><td class="diff_next" id="difflib_chg_to3__0"></td><td class="diff_header" id="from3_8">8</td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to3_8">8</td><td nowrap="nowrap"></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from3_9">9</td><td nowrap="nowrap">@@@&nbsp;&nbsp;&nbsp;############</td><td class="diff_next"></td><td class="diff_header" id="to3_9">9</td><td nowrap="nowrap">@@@&nbsp;&nbsp;&nbsp;############</td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from3_10">10</td><td nowrap="nowrap">@@@@@@@@@&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td><td class="diff_next"></td><td class="diff_header" id="to3_10">10</td><td nowrap="nowrap">@@@@@@@@@&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td></tr>
            <tr><td class="diff_next"><a href="#difflib_chg_to3__top">t</a></td><td class="diff_header" id="from3_11">11</td><td nowrap="nowrap"><span class="diff_sub">&nbsp;</span></td><td class="diff_next"><a href="#difflib_chg_to3__top">t</a></td><td class="diff_header"></td><td nowrap="nowrap"></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from3_12">12</td><td nowrap="nowrap"><span class="diff_sub">&nbsp;</span></td><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from3_13">13</td><td nowrap="nowrap"><span class="diff_sub">&nbsp;</span></td><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from3_14">14</td><td nowrap="nowrap"><span class="diff_sub">&nbsp;</span></td><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from3_15">15</td><td nowrap="nowrap"><span class="diff_sub">&nbsp;</span></td><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from3_16">16</td><td nowrap="nowrap"><span class="diff_sub">&nbsp;</span></td><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from3_17">17</td><td nowrap="nowrap"><span class="diff_sub">&nbsp;</span></td><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from3_18">18</td><td nowrap="nowrap"><span class="diff_sub">&nbsp;</span></td><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from3_19">19</td><td nowrap="nowrap">*****************</td><td class="diff_next"></td><td class="diff_header" id="to3_11">11</td><td nowrap="nowrap">*****************</td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from3_20">20</td><td nowrap="nowrap">-------------</td><td class="diff_next"></td><td class="diff_header" id="to3_12">12</td><td nowrap="nowrap">-------------</td></tr>
        </tbody>
    </table></div>
