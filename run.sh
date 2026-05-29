#!/bin/bash
# =============================================================================
# WOKDEX Corpus — Pipeline Completo
# Extrai dados do corpus, gera estatísticas e prepara o site para deploy.
# =============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "🔍 WOKDEX Corpus — Pipeline de Extração"
echo "=========================================="

# 1. Extract corpus data (reads config.yaml)
echo ""
echo "📄 Fase 1: Extraindo dados do corpus..."
python3 scripts/extract_corpus.py --config config.yaml

# 2. Generate stats
echo ""
echo "📊 Fase 2: Gerando estatísticas..."
python3 scripts/generate_stats.py data/

# 3. Copy data to site
echo ""
echo "📦 Fase 3: Copiando dados para o site..."
mkdir -p site/data/exercises
cp data/corpus.json site/data/
cp data/stats.json site/data/
cp data/exercises/*.json site/data/exercises/

echo ""
echo "✅ Pipeline concluído!"
echo ""
echo "🌐 Para servir localmente:"
echo "   cd site/ && python3 -m http.server 8000"
echo "   Abra: http://localhost:8000"
