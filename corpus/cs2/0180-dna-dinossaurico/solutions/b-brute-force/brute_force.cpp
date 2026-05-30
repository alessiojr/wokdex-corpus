#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string s;
    if (!(cin >> s)) return 0;
    int n = s.length();
    
    int best_d = 1;
    for (int k = 1; k <= n; k++) {
        int d = n / k;
        bool valid = true;
        // Without early break and checking all K
        for (int i = 0; i < d / 2; i++) {
            for (int j = 0; j < k; j++) {
                if (s[i * k + j] != s[(d - 1 - i) * k + j]) {
                    valid = false;
                }
            }
        }
        if (n % k == 0 && valid) {
            best_d = max(best_d, d);
        }
    }
    cout << best_d << "\n";
    return 0;
}
