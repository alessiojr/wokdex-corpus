# 📊 Data — Dados Gerados pelo Pipeline

## Propósito

Esta pasta contém os **arquivos JSON estáticos** gerados pelo script Python de extração. Estes arquivos são consumidos diretamente pelo site (HTML/JS) via `fetch()`.

> ⚠️ **Não edite manualmente!** Estes arquivos são gerados automaticamente. Para atualizá-los, execute o pipeline Python.

## Arquivos

| Arquivo | Descrição | Tamanho Típico |
|---------|-----------|---------------|
| `corpus.json` | Índice consolidado de todos os exercícios | ~50 KB |
| `stats.json` | Estatísticas agregadas (para dashboard) | ~5 KB |
| `exercises/` | JSON individual por exercício | ~2-5 KB cada |

## corpus.json

Contém o índice completo do corpus com:

- **Metadados do artigo**: título, venue, autores
- **Sumário**: totais de exercícios, cenários, test cases
- **Lista de exercícios**: resumo de cada exercício com dados chave

O site usa este arquivo para:
- Renderizar o catálogo de exercícios (`catalog.html`)
- Popular o dashboard de estatísticas (`index.html`)
- Navegação e busca

## stats.json

Contém estatísticas pré-computadas:

- Distribuição por dificuldade (E, D, C, B, A)
- Distribuição por tipo de teste (TDD, FALSE_GREEN, PERFORMANCE)
- Frequência de skills
- Cobertura de cenários FALSE_GREEN e PERFORMANCE
- Cenários por nível (A–D)

O site usa este arquivo para renderizar gráficos sem processamento pesado client-side.

## exercises/*.json

Um arquivo por exercício com metadados completos:

- Todos os campos do `metadata.yaml`
- Overview extraído do `README.md`
- Resultados de validação do `ANALYSIS.md`
- Contagem real de arquivos `.in/.out`
- Cenários detalhados com helpTip e skills

O site carrega estes arquivos sob demanda na página de detalhe (`exercise.html?id=0003-divisao`).

## Como Regenerar

```bash
# Da raiz do repositório:
python scripts/extract_corpus.py corpus/ data/
python scripts/generate_stats.py data/

# Copiar para o site:
cp -r data/ site/data/
```
