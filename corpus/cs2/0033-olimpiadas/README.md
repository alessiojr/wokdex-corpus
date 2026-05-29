# 0033 - Olimpíadas | **Version**: 1.0
`olimpiadas` | Difficulty: **B** | **Updated**: 2026-04-17 09:32:26


## Overview
O pequeno país de Tumbólia vai às Olimpíadas de Pequim pela primeira vez! O Comitê Olímpico precisa transportar todos os seus atletas usando apenas os voos disponíveis da Air Rock — cada rota tem um número fixo de assentos livres por dia. Dado o mapa de voos e a quantidade de atletas, descubra o menor número de dias necessário para que toda a delegação chegue a Pequim.

## Metadata
- **Author**: gabriel
- **Editorial Author**: gabriel
- **Editorial**: **Briefing para o Professor:** Este problema é ideal para introduzir Fluxo Máximo em Grafos após os alunos já dominarem grafos dirigidos e BFS. O pré-requisito essencial é entender modelagem de redes de capacidade (fonte, sumidouro, arestas com peso). É classificado como nível B (Especialista): requer conhecimento do algoritmo de Ford-Fulkerson ou Edmonds-Karp, conceito que normalmente aparece no segundo semestre de um curso de Algoritmos em Grafos. Não há implementação de estrutura de dados exótica, mas exige maturidade para depurar grafos residuais.
**Resumo da Estratégia:** A chave do problema é perceber que a rede de voos é idêntica a cada dia — logo, o número máximo de atletas transportados por dia é constante e igual ao Fluxo Máximo do grafo (aeroporto 1 = fonte, aeroporto N = sumidouro, capacidades = assentos vagos por voo). A resposta é ⌈A / fluxo_max⌉. Implemente Edmonds-Karp (Ford-Fulkerson + BFS) para garantir O(V·E²) com V≤50, E≤2450 — suficiente para o limite de 1 segundo. Atenção ao grafo residual: arestas inversas com capacidade igual ao fluxo já enviado. Para detalhes completos de implementação, consulte o enunciado nível D.

- **Success Msg**: Excelente! Você dominou o transporte olímpico modelando a rede como fluxo máximo!

| Time Limit | Memory Limit | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| 1s | 64MB | O(V * E^2) | O(V + E) |

## Stats
| Metric | Count |
| :--- | :--- |
| Test Scenarios | 11 |
| Solutions | 2 |

## Statements
| ID | Status | Level | Natural Languages | Skills |
| :--- | :--- | :--- | :--- | :--- |
| `a-olimpiadas` | ✅ | A | pt | grafos |

## Test Scenarios
| Name | Description | Count | Type | Level |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Grafo Denso e Carga Máxima** | Teste de carga com limites máximos suportados (50 nós, 1000 arestas ativas com capacidades grandes) para verificar se o algoritmo atende a complexidade O(V * E^2). | 1 | Performance | A | max-flow, busca-largura |
| **Armadilha Golosa (Greedy)** | Grafo projetado onde o caminho mais comprido tem capacidade muito larga, mas caminhos curtos juntos fluem tudo num só passo, falhando heurísticas ingênuas ou `ceil(A/max_flow)`. | 1 | TDD | B | max-flow |
| **Gargalo na Chegada** | Elevadas capacidades nas primeiras arestas, com o gargalo limitante localizado exatamente na porta do destino final. | 1 | TDD | C | max-flow |
| **Grafo Cego e Fuzzing** | Casos randômicos desconexos contendo ilhas, arestas irrelevantes para o caminho final e cruzamentos. Quebra programações fixas de IF/ELSE focadas apenas nos exemplos de base. | 1 | False-Green | C | busca-largura |
| **Casos do Enunciado** | Exemplos oficiais fornecidos pela documentação para alinhamento rápido e warm-up da lógica básica. | 3 | TDD | D | grafos |

## Solutions
- **Solução Ótima — Grafo Expandido no Tempo + Fluxo Máximo (Edmonds-Karp)** (`a-otima-basica`)
  - Languages: `py`
- **Solução Incorreta (Ordenação)** (`c-wrong-ordem`)
  - Languages: `java, c, cpp`

## Components
- ✅ Statements
- ✅ Solutions
- ✅ Test Cases