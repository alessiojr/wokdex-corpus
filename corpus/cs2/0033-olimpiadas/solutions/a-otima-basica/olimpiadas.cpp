#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

struct PathFlight { int o, d, s; };

struct Edge {
    int to;
    int cap;
    int flow;
    int rev;
};

bool check(int D, int N, int A, const vector<PathFlight>& flights) {
    auto nid = [&](int a, int t) { return t * N + a; };
    int SS = N * (D + 1);
    int TT = SS + 1;
    int total = TT + 1;
    
    vector<vector<Edge>> adj(total);
    
    auto add_edge = [&](int u, int v, int c) {
        adj[u].push_back({v, c, 0, (int)adj[v].size()});
        adj[v].push_back({u, 0, 0, (int)adj[u].size() - 1});
    };
    
    add_edge(SS, nid(0, 0), A);
    for(int t=0; t<D; ++t) {
        for(int a=0; a<N; ++a) add_edge(nid(a, t), nid(a, t+1), A);
        for(auto& f : flights) add_edge(nid(f.o, t), nid(f.d, t+1), f.s);
    }
    for(int t=0; t<=D; ++t) add_edge(nid(N-1, t), TT, A);
    
    int total_flow = 0;
    while(total_flow < A) {
        vector<int> parent_node(total, -1);
        vector<int> parent_edge(total, -1);
        parent_node[SS] = SS;
        queue<int> q;
        q.push(SS);
        while(!q.empty()) {
            int u = q.front(); q.pop();
            for(int i=0; i<(int)adj[u].size(); ++i) {
                Edge& e = adj[u][i];
                if(parent_node[e.to] == -1 && e.cap - e.flow > 0) {
                    parent_node[e.to] = u;
                    parent_edge[e.to] = i;
                    if(e.to == TT) {
                        while(!q.empty()) q.pop();
                        break;
                    }
                    q.push(e.to);
                }
            }
        }
        if(parent_node[TT] == -1) break;
        int path_flow = A - total_flow;
        int curr = TT;
        while(curr != SS) {
            int p = parent_node[curr];
            int e_idx = parent_edge[curr];
            Edge& e = adj[p][e_idx];
            path_flow = min(path_flow, e.cap - e.flow);
            curr = p;
        }
        curr = TT;
        while(curr != SS) {
            int p = parent_node[curr];
            int e_idx = parent_edge[curr];
            Edge& e = adj[p][e_idx];
            e.flow += path_flow;
            adj[curr][e.rev].flow -= path_flow;
            curr = p;
        }
        total_flow += path_flow;
    }
    return total_flow >= A;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N, M, A;
    while(cin >> N >> M >> A && (N || M || A)) {
        vector<PathFlight> flights(M);
        for(int i=0; i<M; ++i) {
            cin >> flights[i].o >> flights[i].d >> flights[i].s;
            flights[i].o--; flights[i].d--;
        }
        int lo = 1, hi = A + N;
        while(lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if(check(mid, N, A, flights)) hi = mid;
            else lo = mid + 1;
        }
        cout << lo << "\n";
    }
    return 0;
}
