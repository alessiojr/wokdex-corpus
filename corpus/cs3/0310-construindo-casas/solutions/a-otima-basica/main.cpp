#include <iostream>
#include <cmath>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long a, b, c;
    while (cin >> a && a != 0) {
        cin >> b >> c;
        long long area = a * b;
        long long total = (area * 100) / c;
        long long side = sqrt(total);
        cout << side << "\n";
    }
    return 0;
}
