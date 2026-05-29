// Optimal C++ solution for "Copa do Mundo" (Beecrowd 1414)
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

        long long sumPoints = 0;
        for (int i = 0; i < T; ++i) {
            string name;
            long long points;
            cin >> name >> points;
            sumPoints += points;
        }

        long long draws = 3LL * N - sumPoints;
        cout << draws << '\n';
    }

    return 0;
}

