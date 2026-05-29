#include <stdio.h>
#include <stdlib.h>

typedef struct { int o, d, s; } Flight;
typedef struct { int to, cap, flow, rev, next; } Edge;

Edge pool[200000];
int pool_sz;
int head[6000];

void add_edge(int u, int v, int c) {
    int e1 = pool_sz++;
    int e2 = pool_sz++;
    pool[e1] = (Edge){v, c, 0, e2, head[u]}; head[u] = e1;
    pool[e2] = (Edge){u, 0, 0, e1, head[v]}; head[v] = e2;
}

int check(int D, int N, int A, Flight* flights, int M) {
    int SS = N * (D + 1);
    int TT = SS + 1;
    int total = TT + 1;
    
    pool_sz = 0;
    for(int i=0; i<total; i++) head[i] = -1;
    
    add_edge(SS, 0, A);
    for(int t=0; t<D; ++t) {
        for(int a=0; a<N; ++a) add_edge(t*N + a, (t+1)*N + a, A);
        for(int i=0; i<M; ++i) add_edge(t*N + flights[i].o, (t+1)*N + flights[i].d, flights[i].s);
    }
    for(int t=0; t<=D; ++t) add_edge(t*N + N - 1, TT, A);
    
    int total_flow = 0;
    int parent_node[6000];
    int parent_edge[6000];
    int q[6000];
    
    while(total_flow < A) {
        for(int i=0; i<total; i++) parent_node[i] = -1;
        parent_node[SS] = SS;
        int q_head = 0, q_tail = 0;
        q[q_tail++] = SS;
        
        while(q_head < q_tail) {
            int u = q[q_head++];
            for(int e = head[u]; e != -1; e = pool[e].next) {
                int v = pool[e].to;
                if(parent_node[v] == -1 && pool[e].cap - pool[e].flow > 0) {
                    parent_node[v] = u;
                    parent_edge[v] = e;
                    if(v == TT) { q_head = q_tail; break; }
                    q[q_tail++] = v;
                }
            }
        }
        if(parent_node[TT] == -1) break;
        
        int path_flow = A - total_flow;
        int curr = TT;
        while(curr != SS) {
            int e = parent_edge[curr];
            if (pool[e].cap - pool[e].flow < path_flow) {
                path_flow = pool[e].cap - pool[e].flow;
            }
            curr = parent_node[curr];
        }
        curr = TT;
        while(curr != SS) {
            int e = parent_edge[curr];
            pool[e].flow += path_flow;
            pool[pool[e].rev].flow -= path_flow;
            curr = parent_node[curr];
        }
        total_flow += path_flow;
    }
    return total_flow >= A;
}

int main() {
    int N, M, A;
    while(scanf("%d %d %d", &N, &M, &A) == 3 && (N || M || A)) {
        Flight flights[2500];
        for(int i=0; i<M; ++i) {
            scanf("%d %d %d", &flights[i].o, &flights[i].d, &flights[i].s);
            flights[i].o--; flights[i].d--;
        }
        int lo = 1, hi = A + N;
        while(lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if(check(mid, N, A, flights, M)) hi = mid;
            else lo = mid + 1;
        }
        printf("%d\n", lo);
    }
    return 0;
}
