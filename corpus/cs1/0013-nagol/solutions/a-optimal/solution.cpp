#include <iostream>

using namespace std;

int main() {
    long long l, c, x, y;
    while (cin >> l >> c >> x >> y) {
        long long index = x * c + y;
        if (index % 2 == 0) {
            cout << "Direita" << endl;
        } else {
            cout << "Esquerda" << endl;
        }
    }
    return 0;
}
