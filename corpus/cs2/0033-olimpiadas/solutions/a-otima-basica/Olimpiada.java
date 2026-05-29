import java.io.*;
import java.util.*;

public class Olimpiada {
    static class Flight {
        int o, d, s;
        Flight(int o, int d, int s) { this.o = o; this.d = d; this.s = s; }
    }
    
    static class Edge {
        int to, cap, flow, rev;
        Edge(int to, int cap, int flow, int rev) {
            this.to = to; this.cap = cap; this.flow = flow; this.rev = rev;
        }
    }
    
    static boolean check(int D, int N, int A, List<Flight> flights) {
        int SS = N * (D + 1);
        int TT = SS + 1;
        int total = TT + 1;
        
        List<List<Edge>> adj = new ArrayList<>(total);
        for(int i=0; i<total; i++) adj.add(new ArrayList<>());
        
        java.util.function.Consumer<int[]> add_edge = (args) -> {
            int u = args[0], v = args[1], c = args[2];
            adj.get(u).add(new Edge(v, c, 0, adj.get(v).size()));
            adj.get(v).add(new Edge(u, 0, 0, adj.get(u).size() - 1));
        };
        
        add_edge.accept(new int[]{SS, 0, A});
        for(int t=0; t<D; ++t) {
            for(int a=0; a<N; ++a) add_edge.accept(new int[]{t*N + a, (t+1)*N + a, A});
            for(Flight f : flights) add_edge.accept(new int[]{t*N + f.o, (t+1)*N + f.d, f.s});
        }
        for(int t=0; t<=D; ++t) add_edge.accept(new int[]{t*N + N - 1, TT, A});
        
        int total_flow = 0;
        int[] parent_node = new int[total];
        int[] parent_edge = new int[total];
        
        while(total_flow < A) {
            Arrays.fill(parent_node, -1);
            Arrays.fill(parent_edge, -1);
            parent_node[SS] = SS;
            Queue<Integer> q = new LinkedList<>();
            q.add(SS);
            
            while(!q.isEmpty()) {
                int u = q.poll();
                List<Edge> edges = adj.get(u);
                for(int i=0; i<edges.size(); i++) {
                    Edge e = edges.get(i);
                    if(parent_node[e.to] == -1 && e.cap - e.flow > 0) {
                        parent_node[e.to] = u;
                        parent_edge[e.to] = i;
                        if(e.to == TT) {
                            q.clear();
                            break;
                        }
                        q.add(e.to);
                    }
                }
            }
            if(parent_node[TT] == -1) break;
            
            int path_flow = A - total_flow;
            int curr = TT;
            while(curr != SS) {
                int p = parent_node[curr];
                Edge e = adj.get(p).get(parent_edge[curr]);
                path_flow = Math.min(path_flow, e.cap - e.flow);
                curr = p;
            }
            
            curr = TT;
            while(curr != SS) {
                int p = parent_node[curr];
                Edge e = adj.get(p).get(parent_edge[curr]);
                e.flow += path_flow;
                adj.get(curr).get(e.rev).flow -= path_flow;
                curr = p;
            }
            total_flow += path_flow;
        }
        return total_flow >= A;
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNextInt()) {
            int N = sc.nextInt();
            int M = sc.nextInt();
            int A = sc.nextInt();
            if(N == 0 && M == 0 && A == 0) break;
            List<Flight> flights = new ArrayList<>();
            for(int i=0; i<M; i++) {
                flights.add(new Flight(sc.nextInt()-1, sc.nextInt()-1, sc.nextInt()));
            }
            int lo = 1, hi = A + N;
            while(lo < hi) {
                int mid = lo + (hi - lo) / 2;
                if(check(mid, N, A, flights)) hi = mid;
                else lo = mid + 1;
            }
            System.out.println(lo);
        }
        sc.close();
    }
}
