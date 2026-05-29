# WOKDEX Corpus — Reference Dataset for Formative Assessment in Online Judges

[![GitHub Pages](https://img.shields.io/badge/Live_Site-GitHub_Pages-blue?style=for-the-badge&logo=github)](https://INSERIR_USUARIO.github.io/wokdex-corpus)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey?style=for-the-badge)](https://creativecommons.org/licenses/by/4.0/)
[![SBIE 2026](https://img.shields.io/badge/Paper-SBIE_2026-green?style=for-the-badge)](https://doi.org/INSERIR_DOI)

> **Quebrando o Silêncio Pedagógico: O Modelo WOKDEX para Feedback Formativo em Juízes Online**
>
> *Artigo submetido ao SBIE 2026 — Trilha de Pesquisa (TPIE)*

---

## 📋 Sobre

Este repositório contém o **corpus de referência** do modelo WOKDEX — um schema de metadados pedagógicos que organiza casos de teste com intenção formativa explícita para exercícios de programação.

O corpus é composto por **40 exercícios curados** (160 cenários de teste) abrangendo os níveis curriculares **CS1**, **CS2** e **CS3**, conforme os referenciais ACM CS2013 e CC2020.

### O que é o WOKDEX?

O WOKDEX é um schema de metadados que transforma a avaliação binária dos juízes online (*Accepted/Wrong Answer*) em **diagnóstico pedagógico contextualizado**, através de:

| Componente | Descrição |
|---|---|
| **Tipologia de Testes** | Classifica cenários em `SAMPLE`, `TDD`, `TDD_FALSE_GREEN` (detecção de misconceptions) e `PERFORMANCE` (complexidade algorítmica) |
| **Camadas de Metadados** | Organiza atributos em camadas Descritiva, Pedagógica e Avaliativa |
| **Hint Confidence Score (HCS)** | Modula a confiabilidade do feedback com base na consistência dos erros |
| **Mapeamento de Skills** | Vincula cada cenário a competências curriculares específicas |

## 🏗️ Estrutura do Repositório

```
wokdex-corpus/
├── corpus/          # Exercícios curados com metadados WOKDEX
├── scripts/         # Pipeline Python de extração de dados
├── data/            # JSONs gerados (consumidos pelo site)
├── site/            # Frontend HTML/CSS/JS (GitHub Pages)
└── docs/            # Documentação acadêmica e JSON Schema
```

## 🚀 Uso Rápido

### Visualizar o Site
Acesse: **https://INSERIR_USUARIO.github.io/wokdex-corpus**

### Regenerar Dados Localmente

```bash
# 1. Instalar dependências
pip install -r scripts/requirements.txt

# 2. Extrair dados do corpus
python scripts/extract_corpus.py corpus/ data/

# 3. Gerar estatísticas agregadas
python scripts/generate_stats.py data/

# 4. Copiar para o site
cp -r data/ site/data/

# 5. Servir localmente
cd site && python -m http.server 8000
```

## 📊 Estatísticas do Corpus (Protótipo)

| Métrica | Valor |
|---------|-------|
| Exercícios | 9 (protótipo) / 40 (corpus completo) |
| Cenários de teste | ~180 |
| Casos de teste (.in/.out) | ~450 |
| Níveis curriculares | CS1 (E, D), CS2 (C, D) |
| Tipos de teste | TDD, TDD_FALSE_GREEN, PERFORMANCE |

## 📖 Referência ao Artigo

Se utilizar este corpus em sua pesquisa, cite:

```bibtex
@inproceedings{wokdex2026,
  title     = {Quebrando o Silêncio Pedagógico: O Modelo WOKDEX para
               Feedback Formativo em Juízes Online},
  author    = {Omitido para revisão cega},
  booktitle = {Anais do XXXVII Simpósio Brasileiro de Informática
               na Educação (SBIE 2026)},
  year      = {2026},
  publisher = {SBC}
}
```

## 📜 Licença

- **Código** (scripts, site): MIT License
- **Dados** (corpus, artigo): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
