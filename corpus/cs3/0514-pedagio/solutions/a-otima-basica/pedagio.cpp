#include <iostream>

using namespace std;

int main() {
    int L, D, K, P;
    if (cin >> L >> D >> K >> P) {
        int cost = (L * K) + ((L / D) * P);
        cout << cost << "\n";
    }
    return 0;
}
