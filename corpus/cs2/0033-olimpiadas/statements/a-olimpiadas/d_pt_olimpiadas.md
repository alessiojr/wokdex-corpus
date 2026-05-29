# Olimpíadas

O Comitê Olímpico Tumboliano (COT) precisa transportar todos os seus atletas de Tumbólia (aeroporto 1) até Pequim (aeroporto N) usando apenas voos da Air Rock. Cada voo tem um número fixo de assentos disponíveis por dia, e um atleta só pode pegar **um voo por dia** — percursos com escalas levam múltiplos dias.

## Entrada

A entrada contém vários casos de teste. A primeira linha de cada caso de teste contém três inteiros **N**, **M** e **A** indicando respectivamente a quantidade de aeroportos (2 ≤ **N** ≤ 50), a quantidade de voos com assentos vagos (1 ≤ **M** ≤ 2.450) e quantos atletas a delegação tem (1 ≤ **A** ≤ 50).

Cada uma das **M** linhas seguintes contém **O**, **D** e **S**: aeroporto de origem, destino e número de assentos vagos (1 ≤ **S** ≤ 50). O final da entrada é **N** = **M** = **A** = 0.

## Saída

Para cada caso de teste, uma linha com o número mínimo de dias para todos os atletas chegarem a Pequim.

## Exemplos

| Entrada | Saída |
|:--------|:------|
| 3 3 3   | 2     |
| 1 2 2   |       |
| 2 3 2   |       |
| 1 3 1   |       |
| 3 3 5   | 6     |
| 1 2 1   |       |
| 2 3 5   |       |
| 3 1 4   |       |
| 0 0 0   |       |

| Entrada | Saída |
|:--------|:------|
| 4 4 4   | 3     |
| 1 4 1   |       |
| 1 2 1   |       |
| 2 3 1   |       |
| 3 4 1   |       |
| 0 0 0   |       |

## Tutorial

### Por que a abordagem ingênua falha

A ideia inicial é calcular o **fluxo máximo** da rede de aeroportos — quantos atletas conseguem avançar por dia — e então calcular ⌈A / fluxo_max⌉.

**Essa fórmula está errada** quando existem rotas com escalas. Exemplo: A=5 atletas, única rota 1→2→3 com capacidade 1 por trecho. O fluxo máximo do grafo original é 1, e ⌈5/1⌉ = 5, mas a resposta correta é **6**.

A razão: a rota tem 2 saltos, então o primeiro atleta só chega no **dia 2**. Cada atleta sai um dia após o anterior, e o quinto parte no dia 5, chegando no dia 6. A informação de "quantos saltos" a rota tem é perdida quando se calcula o fluxo no grafo estático.

### Modelagem correta: grafo expandido no tempo

Para um horizonte de **D dias**, criamos um grafo onde cada nó representa um par (aeroporto, dia):

- **Aresta de voo**: `(O, t) → (D, t+1)` com capacidade S, para `t = 0..D-1`
- **Aresta de espera**: `(a, t) → (a, t+1)` com capacidade A, para todo aeroporto a
- **SS → (aeroporto 1, dia 0)**: capacidade A (todos os atletas partem de Tumbólia)
- **(aeroporto N, t) → TT**: capacidade A, para `t = 0..D` (chegada em qualquer dia)

A pergunta vira: **o fluxo máximo de SS a TT é ≥ A?**  
Se sim, D dias são suficientes.

```
Exemplo (D=2, N=3, voos: 1→2 cap 2, 2→3 cap 2, 1→3 cap 1):

SS ──cap 3──► (1,0) ──cap 2──► (2,1) ──cap 2──► (3,2) ──► TT
                │                                    ↑
                └───cap 1────────────────────────► (3,1) ──► TT
     (arestas de espera omitidas por clareza)
```

Fluxo: 2 atletas via 1→2→3 (chegam dia 2) + 1 atleta via 1→3 (chega dia 1) = 3 = A. ✓

### Algoritmo: busca binária + fluxo máximo

```
busca binária sobre D em [1, A+N]:
    para cada D candidato:
        montar grafo expandido no tempo (N×(D+1) nós + SS + TT)
        calcular fluxo máximo de SS a TT com Edmonds-Karp
        se fluxo ≥ A → D é viável (tentar D menor)
        senão → D insuficiente (tentar D maior)
```

**Limite superior seguro**: D ≤ A + N − 2, pois em pior caso (capacidade 1, rota com N−1 saltos) temos pipeline de A + N − 2 dias.

**Complexidade**: O(log(A+N) × A × (N+M) × D). Com N≤50, M≤2450, A≤50, D≤100, cada checagem é rápida o suficiente para o limite de 1 segundo.

### Verificação com os exemplos

**Exemplo 1** (N=3, A=3, voos: 1→2 cap 2, 2→3 cap 2, 1→3 cap 1):
- Com D=2: 2 atletas via 1→2→3 + 1 via 1→3 = 3. ✓ Resposta: 2.

**Exemplo 2** (N=3, A=5, voos: 1→2 cap 1, 2→3 cap 5, 3→1 cap 4):
- Única rota válida: 1→2→3 (2 saltos, gargalo 1).
- Com D=5: 4 caminhos encadeados (t=0,1,2,3), total=4 < 5. ✗
- Com D=6: 5 caminhos (t=0..4), total=5 = A. ✓ Resposta: 6.

**Exemplo 3** (N=4, A=4, voos: 1→4 cap 1, 1→2 cap 1, 2→3 cap 1, 3→4 cap 1):
- Com D=3: 3 atletas via 1→4 (dias 1,2,3) + 1 atleta via 1→2→3→4 (3 saltos, chega dia 3). ✓ Resposta: 3.

### Notas de implementação

- Use dicionários para o grafo residual (grafo expandido tem muitos nós mas poucas arestas úteis).
- No Edmonds-Karp, limite o fluxo por augmentação a `A - fluxo_atual` para terminar assim que atingir A.
- Arestas reversas devem ser inicializadas com capacidade 0 para garantir que o BFS as descubra ao longo das augmentações.
- Para implementação em Python ou C++, consulte o arquivo `solutions/a-otima-basica/olimpiada.py`.
