// Suboptimal (O(T^2)) C++ solution for "Copa do Mundo"
// Logicamente correta, mas com soma feita via laço quadrático.
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T, N;
    while (cin >> T >> N) {
        if (T == 0) {
            break;
        }

        vector<long long> points(T);
        for (int i = 0; i < T; ++i) {
            string name;
            long long p;
            cin >> name >> p;
            points[i] = p;
        }

        // Soma dos pontos feita de forma propositalmente ineficiente: O(T^2)
        long long sumPoints = 0;
        for (int i = 0; i < T; ++i) {
            for (int j = 0; j < T; ++j) {
                if (j == 0) { // garante que cada time seja somado exatamente uma vez
                    sumPoints += points[i];
                }
            }
        }

        long long draws = 3LL * N - sumPoints;
        cout << draws << '\n';
    }

    return 0;
}

