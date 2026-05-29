#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int B, N;
    while (cin >> B >> N && (B || N)) {
        vector<long long> saldo(B + 1);
        for (int i = 1; i <= B; i++) {
            cin >> saldo[i];
        }
        
        for (int j = 0; j < N; j++) {
            int D, C, V;
            cin >> D >> C >> V;
            saldo[D] -= V;
            saldo[C] += V;
        }
        
        bool ok = true;
        for (int i = 1; i <= B; i++) {
            if (saldo[i] < 0) {
                ok = false;
                break;
            }
        }
        
        cout << (ok ? "S" : "N") << "\n";
    }
    
    return 0;
}
