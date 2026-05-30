#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string s;
    if (cin >> s) {
        vector<char> piles;
        for (char c : s) {
            auto it = upper_bound(piles.begin(), piles.end(), c);
            if (it == piles.end()) {
                piles.push_back(c);
            } else {
                *it = c;
            }
        }
        cout << piles.size() << "\n";
    }
    return 0;
}
