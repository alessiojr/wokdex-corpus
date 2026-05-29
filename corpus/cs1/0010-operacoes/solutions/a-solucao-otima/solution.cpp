#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    char op;
    double a, b;
    
    if (!(cin >> op >> a >> b)) return 0;

    double res = 0;
    if (op == 'M') {
        res = a * b;
    } else if (op == 'D') {
        res = a / b;
    }

    cout << fixed << setprecision(2) << res << endl;

    return 0;
}
