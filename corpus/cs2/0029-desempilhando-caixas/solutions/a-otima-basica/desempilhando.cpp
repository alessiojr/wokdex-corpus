#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N, P;
    while (cin >> N >> P && (N || P)) {
        vector<vector<int>> piles(P);
        int target_pile = -1, target_row = -1;
        
        for (int i = 0; i < P; i++) {
            int Q;
            cin >> Q;
            piles[i].resize(Q);
            for (int j = 0; j < Q; j++) {
                cin >> piles[i][j];
                if (piles[i][j] == 1) {
                    target_pile = i;
                    target_row = j;
                }
            }
        }
        
        // Caixas acima da caixa 1 na mesma pilha
        int above = (int)piles[target_pile].size() - target_row - 1;
        
        // Custo indo pela esquerda (pilhas 0..target_pile-1)
        long long cost_left = above;
        for (int i = target_pile - 1; i >= 0; i--) {
            int h = (int)piles[i].size();
            if (h > target_row) {
                cost_left += h - target_row;
            } else {
                break; // lado livre encontrado, não precisa ir mais longe
            }
        }
        
        // Custo indo pela direita (pilhas target_pile+1..P-1)
        long long cost_right = above;
        for (int i = target_pile + 1; i < P; i++) {
            int h = (int)piles[i].size();
            if (h > target_row) {
                cost_right += h - target_row;
            } else {
                break; // lado livre encontrado
            }
        }
        
        cout << min(cost_left, cost_right) << "\n";
    }
    
    return 0;
}
