# 📚 Docs — Documentação Acadêmica e Schema

## Propósito

Esta pasta contém a documentação acadêmica complementar ao corpus, incluindo o JSON Schema oficial do WOKDEX e materiais de referência do artigo.

## Arquivos

| Arquivo | Descrição |
|---------|-----------|
| `schema-wokdex.json` | JSON Schema oficial para validação do `metadata.yaml` |
| `artigo-resumo.md` | Resumo estendido do artigo SBIE 2026 (para README do GitHub) |
| `tipologia-testes.md` | Documentação detalhada da tipologia de testes |
| `hcs-formula.md` | Formalização do Hint Confidence Score |

## JSON Schema

O arquivo `schema-wokdex.json` é o schema oficial que valida os arquivos `metadata.yaml` de cada exercício. Ele define:

- **Campos obrigatórios**: `id`, `name`, `slug`, `version`, `origin`, `difficultyLevelId`, etc.
- **Enums**: Valores permitidos para `testType`, `difficultyLevelId`, `paradigm`, `language`
- **Estrutura aninhada**: `testScenarios[]`, `solutions[]`, `statements[]`

### Uso

```yaml
# No topo do metadata.yaml:
# yaml-language-server: $schema=./docs/schema-wokdex.json
```

## Tipologia de Testes

Os 4 tipos de teste do WOKDEX, extraídos da Tabela 4 do artigo:

| Tipo | Visível? | Propósito |
|------|----------|-----------|
| `SAMPLE` | ✅ Sim | Exemplos do enunciado — depuração local |
| `TDD` | ❌ Não | Validação funcional — comportamento secreto |
| `TDD_FALSE_GREEN` | ❌ Não | Detecção de misconceptions — código acidentalmente correto |
| `PERFORMANCE` | ❌ Não | Complexidade algorítmica — separada da corretude lógica |

### Subtipos de TDD_FALSE_GREEN

| Subtipo | Misconception | Exemplo | Nível |
|---------|---------------|---------|-------|
| `TYPE` | Tipo de dado inadequado | `int` em vez de `double` para divisão | CS1 |
| `FORMAT` | Formatação de saída incorreta | `println` em vez de `printf("%.2f")` | CS1 |
| `STRATEGY` | Estratégia algorítmica insuficiente | QuickSort instável para ordenação com empate | CS2–CS3 |

## Hint Confidence Score (HCS)

Fórmula: `HCS = falhas_no_cenário / total_casos_do_cenário`

| Faixa | HCS | Ação |
|-------|-----|------|
| Alta confiança | 1.0 (todos falharam) | Emite helpTip diretamente |
| Confiança moderada | ≥ 0.5 | Emite "Possível causa: {helpTip}" |
| Baixa confiança | < 0.5 | Delega a dica genérica ou IA |
