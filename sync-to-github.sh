#!/bin/bash
# =============================================================================
# WOKDEX Corpus — Sync para GitHub
# Sincroniza o repo local (GitLab origin) com o GitHub público.
#
# Pré-requisito: configurar o remote "github"
#   git remote add github https://github.com/USUARIO/wokdex-corpus.git
# =============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "🔄 WOKDEX Corpus — Sync GitLab → GitHub"
echo "=========================================="

# 1. Verificar que o remote 'github' existe
if ! git remote | grep -q '^github$'; then
  echo "❌ Remote 'github' não configurado."
  echo "   Execute: git remote add github https://github.com/USUARIO/wokdex-corpus.git"
  exit 1
fi

# 2. Rodar o pipeline (garante dados atualizados)
echo ""
echo "📦 Fase 1: Rodando pipeline..."
./run.sh

# 3. Commit se há mudanças
echo ""
echo "📝 Fase 2: Commit de mudanças..."
git add -A
if ! git diff --cached --quiet; then
  git commit -m "chore: atualiza corpus e dados $(date +%Y-%m-%d)"
  echo "  ✅ Commit criado"
else
  echo "  ℹ️  Nenhuma mudança para commit"
fi

# Detect branch from config or current
BRANCH=$(python3 -c "
import yaml
c = yaml.safe_load(open('config.yaml'))
print(c.get('repositories',{}).get('gitlab',{}).get('branch','master'))
" 2>/dev/null || echo "master")

# 4. Push para GitLab (origin)
echo ""
echo "🔼 Fase 3: Push para GitLab (origin/$BRANCH)..."
git push origin "$BRANCH" 2>&1 || echo "  ⚠️  Falha no push para GitLab (verifique as credenciais)"

# 5. Push para GitHub
echo ""
echo "🔼 Fase 4: Push para GitHub ($BRANCH)..."
git push github "$BRANCH" 2>&1 || echo "  ⚠️  Falha no push para GitHub (verifique as credenciais)"

echo ""
echo "=========================================="
echo "✅ Sync completo!"

# Extrair URL do Pages da config
PAGES_URL=$(python3 -c "
import yaml
c = yaml.safe_load(open('config.yaml'))
print(c.get('repositories',{}).get('github',{}).get('pages_url','(não configurado)'))
" 2>/dev/null || echo "(não configurado)")

echo "🌐 GitHub Pages: ${PAGES_URL}"
echo "=========================================="
