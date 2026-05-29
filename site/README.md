# 🌐 Site — Frontend HTML/CSS/JS para GitHub Pages

## Propósito

Esta pasta contém o **site estático** que apresenta o corpus WOKDEX ao público. É a raiz de deploy do GitHub Pages.

## Arquitetura

O site é 100% client-side (sem servidor backend):

1. **HTML**: páginas estáticas com semântica SEO
2. **CSS**: Design system vanilla (sem frameworks)
3. **JS**: Carrega JSONs de `data/` via `fetch()` e renderiza dinamicamente
4. **Dados**: Cópia dos JSONs de `../data/` (gerados pelo Python)

```
site/
├── index.html          # Landing page + Dashboard
├── catalog.html        # Catálogo de exercícios (filtros + busca)
├── exercise.html       # Detalhe de exercício (query param: ?id=...)
├── about.html          # Sobre o WOKDEX + contexto do artigo
├── schema.html         # Documentação interativa do schema
├── .nojekyll           # Bypass Jekyll no GitHub Pages
│
├── css/
│   ├── main.css        # Design system: tokens, reset, layout, tipografia
│   ├── components.css  # Cards, badges, tabelas, botões, modais
│   └── pages.css       # Estilos específicos por página
│
├── js/
│   ├── app.js          # Core: loader de dados, navegação, utils
│   ├── charts.js       # Gráficos com Canvas API (barras, donut)
│   ├── catalog.js      # Filtros, busca, ordenação do catálogo
│   ├── exercise.js     # Renderização do detalhe do exercício
│   └── stats.js        # Animações de contagem e dashboard
│
├── data/               # Cópia dos JSONs (ver ../data/README.md)
│   ├── corpus.json
│   ├── stats.json
│   └── exercises/
│
└── assets/
    ├── logo.svg        # Logo WOKDEX
    ├── diagrams/       # Diagramas do artigo (SVG/PNG)
    └── icons/          # Ícones SVG inline
```

## Páginas

### `index.html` — Landing Page + Dashboard
- **Hero section**: Título do artigo, badge SBIE 2026, resumo em 1 parágrafo
- **Contribuições**: Cards animados com C1–C4 do artigo
- **Métricas**: Stat cards com count-up animation (exercícios, cenários, test cases)
- **Dashboard**: Gráficos de distribuição (dificuldade, testType, skills)
- **CTA**: Link para catálogo e documentação do schema

### `catalog.html` — Catálogo de Exercícios
- **Filtros**: Dificuldade (E–A), TestType (TDD, FALSE_GREEN, PERFORMANCE), Skills
- **Busca**: Full-text search no nome e overview
- **Grid**: Cards responsivos com badges, skills tags, métricas
- **Ordenação**: Por dificuldade, nome, número de cenários

### `exercise.html` — Detalhe do Exercício
- **Metadados**: Nome, dificuldade, complexidade, skills
- **Editorial**: Explicação pedagógica completa
- **Cenários**: Tabela com testType badge, level badge, helpTip, skills
- **Estrutura**: Visualização em árvore dos diretórios
- **Validação**: Status do ANALYSIS.md

### `about.html` — Sobre o Projeto
- **Problema**: Silêncio pedagógico dos juízes online
- **Solução**: Schema WOKDEX e tipologia de testes
- **Fluxo fail-fast**: Diagrama visual
- **Tabela comparativa**: ICPC vs Kattis vs Polygon vs WOKDEX
- **HCS**: Explicação do Hint Confidence Score

### `schema.html` — Documentação do Schema
- **Camadas**: Descritiva → Pedagógica → Avaliativa (diagrama interativo)
- **Campos**: Documentação de cada campo do metadata.yaml
- **Exemplo vivo**: YAML renderizado com syntax highlighting
- **Tipologia**: Tabela dos 4 tipos de teste com exemplos

## Design System

### Paleta de Cores

| Token | Cor | Uso |
|-------|-----|-----|
| `--bg-primary` | `#0f172a` | Background principal (dark mode) |
| `--bg-secondary` | `#1e293b` | Cards e seções |
| `--bg-tertiary` | `#334155` | Hover states |
| `--accent-cyan` | `#06b6d4` | Links, ações primárias |
| `--accent-orange` | `#f97316` | Alertas, FALSE_GREEN badges |
| `--accent-green` | `#22c55e` | Sucesso, TDD badges |
| `--accent-red` | `#ef4444` | PERFORMANCE badges |
| `--accent-purple` | `#a855f7` | SAMPLE badges |
| `--text-primary` | `#f8fafc` | Texto principal |
| `--text-secondary` | `#94a3b8` | Texto secundário |

### Tipografia

- **Corpo**: `Inter` (Google Fonts)
- **Código**: `JetBrains Mono` (Google Fonts)
- **Headings**: `Inter` weight 700

### Componentes-Chave

- **Stat Card**: Glassmorphism, border gradient, count-up animation
- **Exercise Card**: Hover scale, badge grid, skill tags
- **Badge**: Rounded pill com cor por tipo (TDD=green, FALSE_GREEN=orange, PERFORMANCE=red)
- **Table**: Striped, sticky header, responsive scroll
- **Chart**: Canvas API, animated draw, tooltips

## Desenvolvimento Local

```bash
# Servir localmente
cd site/
python3 -m http.server 8000

# Abrir no navegador
open http://localhost:8000
```

## SEO

Cada página inclui:
- `<title>` descritivo
- `<meta name="description">` com resumo
- `<h1>` único por página
- Schema.org `Dataset` metadata (para indexação acadêmica)
- Open Graph tags para compartilhamento
