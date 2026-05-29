# 📦 Corpus — Exercícios Curados com Metadados WOKDEX

## Propósito

Esta pasta contém os **exercícios de programação** que compõem o corpus de referência do artigo SBIE 2026. Cada exercício é auto-contido e segue o schema WOKDEX.

## Estrutura por Exercício

Cada subdiretório `NNNN-slug/` contém:

```
NNNN-slug/
├── metadata.yaml       # Metadados WOKDEX (campo testType, skills, helpTip, etc.)
├── README.md           # Visão geral gerada: overview, stats, cenários, soluções
├── ANALYSIS.md         # Relatório de validação estrutural
├── statements/         # Enunciados (markdown e/ou HTML)
│   └── a-slug/
│       ├── A_pt_slug.md
│       └── A_en_slug.md
├── test-cases/         # Arquivos de entrada/saída por cenário
│   ├── d-sample/
│   │   ├── 1.in
│   │   └── 1.out
│   ├── c-tdd/
│   └── c-falso-positivo/
└── solutions/          # Soluções de referência
    └── a-solution/
        ├── Solution.java
        ├── Solution.py
        └── Solution.cpp
```

## Convenção de IDs

O prefixo de cada ID indica o **nível de severidade** do cenário:

| Prefixo | Nível | Significado |
|---------|-------|-------------|
| `d-` | D | Exemplos básicos (SAMPLE) |
| `c-` | C | Testes funcionais padrão (TDD) |
| `b-` | B | Testes de borda / stress |
| `a-` | A | Performance / corner cases extremos |

## Exercícios no Protótipo (0001–0009)

| ID | Nome | Dificuldade | Skills Principais | FALSE_GREEN? | PERFORMANCE? |
|----|------|:-----------:|-------------------|:------------:|:------------:|
| 0001 | Hello World! | E | io | ❌ | ❌ |
| 0002 | Soma | E | io, operadores | ❌ | ❌ |
| 0003 | Divisão | E | io, operadores, variables | ✅ | ❌ |
| 0004 | Etiquetas Coloridas | E | condicionais | ❌ | ❌ |
| 0005 | Concurso de Contos | D | condicionais, loops | ❌ | ❌ |
| 0006 | Cachorros Quentes | D | loops, operadores | ❌ | ❌ |
| 0007 | Botas Perdidas | D | arrays, loops | ❌ | ❌ |
| 0008 | Esquerda, Volver! | D | strings, condicionais | ❌ | ✅ |
| 0009 | Copa do Mundo | D | math, operadores | ❌ | ❌ |

## Como Adicionar Exercícios

1. Copie a pasta do exercício do workspace original
2. Certifique-se de que o `metadata.yaml` segue o schema WOKDEX
3. Remova informações de sync/API internas (campo `Sync Status` do README)
4. Execute o extrator: `python scripts/extract_corpus.py corpus/ data/`

## Campos-Chave do metadata.yaml para o Site

O script Python extrai estes campos prioritariamente:

- `name`, `slug`, `difficultyLevelId` — Identificação
- `skills` — Competências necessárias
- `timeComplexity`, `spaceComplexity` — Complexidade
- `editorial` — Explicação pedagógica
- `testScenarios[].testType` — **Tipo de teste** (TDD, TDD_FALSE_GREEN, PERFORMANCE)
- `testScenarios[].helpTip` — **Dica formativa** por cenário
- `testScenarios[].skills` — Skills específicas por cenário
- `testScenarios[].level` — Nível do cenário (A–D)
