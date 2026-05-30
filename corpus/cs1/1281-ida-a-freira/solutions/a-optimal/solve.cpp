#include <iostream>
#include <string>
#include <unordered_map>
#include <iomanip>

using namespace std;

void solve() {
    int n;
    if (!(cin >> n)) return;

    while (n--) {
        int m;
        cin >> m;
        unordered_map<string, double> catalog;
        for (int i = 0; i < m; ++i) {
            string name;
            double price;
            cin >> name >> price;
            catalog[name] = price;
        }

        int p;
        cin >> p;
        double total = 0.0;
        for (int i = 0; i < p; ++i) {
            string name;
            int qty;
            cin >> name >> qty;
            if (catalog.count(name)) {
                total += catalog[name] * qty;
            }
        }

        cout << fixed << setprecision(2) << "R$ " << total << endl;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    solve();
    return 0;
}
