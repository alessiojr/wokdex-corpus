# Análise: 1194 — Prefixa, Infixa e Posfixa

## Paradigma Algorítmico
**Travessia de Árvores / Strings e Recursividade**

## Complexidade
| Etapa | Tempo | Espaço |
|-------|-------|--------|
| Achar raiz (Find/IndexOf) | O(N) | O(1) |
| Fatiamento (Slicing) | O(N) | O(N) |
| Chamadas Recursivas | O(N) de profundidade | O(N) call stack |
| **Total** | Pior caso **O(N^2)** | **O(N)** |

## Armadilhas
1. **Fatiamento Incorreto**: Obter a substring direita de Prefix a partir do final do Infix é o erro mais comum. O prefixo esquerdo na string *Prefix* possui o EXATO mesmo tamanho do infixo esquerdo na string *Infix*. 
   - `inLeft = in.substr(0, pos)`
   - `preLeft = pre.substr(1, pos)`
2. **String Vazia**: Não verificar se a string repassada é vazia (`pre.empty()`) causará erro de `IndexOutOfBounds` ao invocar `pre[0]`.

## Cenários de Teste
| Cenário | Objetivo | Tipo |
|---------|----------|------|
| a-performance | C=2000 e N=52, o máximo absoluto permitido pelo Beecrowd | PERFORMANCE |
| b-edge-cases | Casos com N=1, N=2, Árvores perfeitamente Skewed (Totalmente capengas para esquerda ou direita) | TDD |
| c-skewed | Árvores aleatórias pendendo propositalmente para um lado | TDD |
| d-sample | Exemplos Básicos do Site | TDD |
