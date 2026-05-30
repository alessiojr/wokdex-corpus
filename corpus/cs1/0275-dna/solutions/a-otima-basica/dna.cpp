#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

void solve() {
    int K;
    while (cin >> K && K != 0) {
        string s1, s2;
        cin >> s1 >> s2;

        int n = s1.length();
        int m = s2.length();

        vector<vector<int>> match(n + 1, vector<int>(m + 1, 0));
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
        vector<vector<int>> f(n + 1, vector<int>(m + 1, 0));

        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                if (s1[i - 1] == s2[j - 1]) {
                    match[i][j] = match[i - 1][j - 1] + 1;
                } else {
                    match[i][j] = 0;
                }

                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                f[i][j] = 0;

                if (match[i][j] >= K) {
                    f[i][j] = max(dp[i - K][j - K] + K, f[i - 1][j - 1] + 1);
                    dp[i][j] = max(dp[i][j], f[i][j]);
                }
            }
        }
        cout << dp[n][m] << "\n";
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    solve();
    return 0;
}
