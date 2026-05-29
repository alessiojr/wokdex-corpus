# 🐍 Scripts — Pipeline Python de Extração de Dados

## Propósito

Esta pasta contém os scripts Python que leem o corpus de exercícios e geram os arquivos JSON estáticos consumidos pelo site.

## Arquivos

| Script | Função | Entrada | Saída |
|--------|--------|---------|-------|
| `extract_corpus.py` | Extrai metadados de cada exercício | `corpus/` | `data/corpus.json` + `data/exercises/*.json` |
| `generate_stats.py` | Gera estatísticas agregadas | `data/corpus.json` | `data/stats.json` |
| `requirements.txt` | Dependências Python | — | — |

## Uso

```bash
# Instalar dependências
pip install -r requirements.txt

# Extração principal (lê corpus, gera JSONs)
python extract_corpus.py ../corpus/ ../data/

# Estatísticas agregadas
python generate_stats.py ../data/
```

## Lógica de Extração (extract_corpus.py)

### Para cada exercício em `corpus/`:

1. **Lê `metadata.yaml`**
   - Extrai: `name`, `slug`, `difficultyLevelId`, `skills`, `timeComplexity`, `editorial`, `successmsg`
   - Processa `testScenarios[]`: conta cenários por `testType` e `level`
   - Processa `solutions[]`: conta soluções e linguagens
   - Processa `statements[]`: conta enunciados e idiomas

2. **Lê `README.md`**
   - Extrai: seção `Overview` (primeiro parágrafo após `## Overview`)
   - Extrai: tabela `Test Scenarios` (parseada como markdown table)
   - Conta: linhas da tabela = número real de cenários

3. **Lê `ANALYSIS.md`**
   - Extrai: status de validação (✅/❌)
   - Extrai: contagem de test cases, solutions

4. **Conta arquivos em `test-cases/`**
   - Para cada subdiretório: conta pares `.in/.out`
   - Gera contagem total de test cases por exercício

5. **Gera JSON individual** → `data/exercises/{id}.json`

6. **Consolida** → `data/corpus.json` (índice com todos exercícios)

### Schema de Saída (exercises/*.json)

```json
{
  "id": "0003-divisao",
  "name": "Divisão",
  "slug": "divisao",
  "difficulty": "E",
  "difficulty_label": "Iniciante",
  "time_complexity": "O(1)",
  "space_complexity": "O(1)",
  "skills": ["io", "io-formatacao-parsing", "operadores", "variables"],
  "editorial": "O problema consiste em...",
  "success_msg": "Além de trabalhar...",
  "overview": "O algorítimo deve ler...",
  "scenarios": [
    {
      "id": "d-sample",
      "name": "Exemplos",
      "description": "Entrada Básica...",
      "level": "D",
      "test_type": "TDD",
      "help_tip": "Você poderia verificar...",
      "skills": [{"skill": "io", "points": 1}],
      "test_case_count": 3
    },
    {
      "id": "c-falso-positivo-inteiros",
      "name": "Inteiros - Falso Positivo",
      "level": "C",
      "test_type": "TDD_FALSE_GREEN",
      "help_tip": "Erro na declaração de tipo de variável.",
      "skills": [{"skill": "variables", "points": 1}],
      "test_case_count": 3
    }
  ],
  "solutions": [...],
  "statements": [...],
  "stats": {
    "total_scenarios": 8,
    "total_test_cases": 26,
    "types": {"TDD": 6, "TDD_FALSE_GREEN": 2},
    "levels": {"A": 1, "B": 2, "C": 4, "D": 1}
  },
  "validation": {
    "statements_ok": true,
    "solutions_ok": true,
    "test_cases_ok": true
  }
}
```

## Dependências

- `pyyaml` — Parser de YAML
- `markdown` — Conversão de MD para HTML (opcional, para previews)

## Notas de Implementação

- O script é **idempotente**: pode ser executado múltiplas vezes sem efeitos colaterais
- Todos os caminhos são relativos à raiz do repositório
- Erros de parsing são logados mas não interrompem a extração de outros exercícios
- A contagem de test cases vem dos **arquivos físicos** (`.in/.out`), não apenas do YAML
