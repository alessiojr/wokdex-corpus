"""
Olimpíadas - Beecrowd 2898
https://www.beecrowd.com.br/judge/en/problems/view/2898

Estratégia: grafo expandido no tempo + fluxo máximo (Edmonds-Karp) + busca binária.

A rede de voos é idêntica a cada dia, mas cada atleta só pode pegar UM voo por dia,
então rotas com escalas levam múltiplos dias — a fórmula simples ceil(A/max_flow) está
ERRADA nos casos com caminhos de comprimento > 1 hop.

A modelagem correta expande o grafo incluindo o tempo:
  - Nó (aeroporto a, dia t) representa "estar em a no início do dia t".
  - Aresta de voo: (O, t) → (D, t+1)  com capacidade S.
  - Aresta de espera: (a, t) → (a, t+1) com capacidade A (atleta aguarda no aeroporto).
  - SS → (aeroporto 1, dia 0)  com capacidade A  (ponto de partida).
  - (aeroporto N, t) → TT  para t=0..D  (chegada em Pequim em qualquer dia).

Busca binária sobre D ∈ [1, A+N]: verifica se max_flow(SS, TT) ≥ A.

Complexidade: O(log(A+N) × A × (N+M) × D), viável para N≤50, M≤2450, A≤50.
"""

import sys
from collections import deque


def solve():
    data = sys.stdin.read().split()
    idx = 0
    output = []

    while idx < len(data):
        N = int(data[idx]); M = int(data[idx+1]); A = int(data[idx+2])
        idx += 3
        if N == 0 and M == 0 and A == 0:
            break

        flights = []
        for _ in range(M):
            O  = int(data[idx])     - 1  # 0-indexed origin
            Ds = int(data[idx+1])   - 1  # 0-indexed destination
            S  = int(data[idx+2])        # seats available
            idx += 3
            flights.append((O, Ds, S))

        src = 0       # Tumbolia  = aeroporto 1 (0-indexed)
        snk = N - 1   # Pequim    = aeroporto N (0-indexed)

        def check(D):
            """Retorna True se todos os A atletas chegam em Pequim em até D dias."""
            def nid(a, t):
                return t * N + a          # node id para (aeroporto a, dia t)

            SS    = N * (D + 1)           # super-fonte
            TT    = SS + 1                # super-sumidouro
            total = TT + 1

            # Grafo de capacidades residuais como lista de dicionários
            cap = [dict() for _ in range(total)]

            def add_edge(u, v, c):
                cap[u][v] = cap[u].get(v, 0) + c
                if u not in cap[v]:      # garante existência da aresta reversa
                    cap[v][u] = 0

            # Fonte: todos os A atletas partem do aeroporto 1 no dia 0
            add_edge(SS, nid(src, 0), A)

            # Arestas de espera (atleta fica 1 dia em qualquer aeroporto)
            for t in range(D):
                for a in range(N):
                    add_edge(nid(a, t), nid(a, t + 1), A)

            # Arestas de voo para cada dia t = 0..D-1
            for t in range(D):
                for (o, d, s) in flights:
                    add_edge(nid(o, t), nid(d, t + 1), s)

            # Sumidouro: atleta chega a Pequim em qualquer dia
            for t in range(D + 1):
                add_edge(nid(snk, t), TT, A)

            # Edmonds-Karp (Ford-Fulkerson com BFS)
            flow = 0
            while flow < A:
                # BFS: encontra caminho aumentante de SS a TT
                parent = [-1] * total
                parent[SS] = SS
                queue = deque([SS])
                while queue:
                    u = queue.popleft()
                    for v, c in cap[u].items():
                        if parent[v] == -1 and c > 0:
                            parent[v] = u
                            if v == TT:
                                queue.clear()
                                break
                            queue.append(v)

                if parent[TT] == -1:
                    break  # não há mais caminhos aumentantes

                # Gargalo ao longo do caminho
                path_flow = A - flow   # nunca precisamos mais do que o restante
                v = TT
                while v != SS:
                    u = parent[v]
                    path_flow = min(path_flow, cap[u][v])
                    v = u

                # Atualiza grafo residual
                v = TT
                while v != SS:
                    u = parent[v]
                    cap[u][v] -= path_flow
                    cap[v][u] = cap[v].get(u, 0) + path_flow
                    v = u

                flow += path_flow

            return flow >= A

        # Busca binária sobre o número de dias
        # Limite superior: A atletas num pipeline de até N-1 scalas → A + N - 2 dias
        lo, hi = 1, A + N
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1

        output.append(str(lo))

    print('\n'.join(output))


solve()
