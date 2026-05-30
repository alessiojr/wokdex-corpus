#include <iostream>

using namespace std;

int main() {
    int a;
    int soma = 0;
    while (cin >> a && a != -1) {
        soma += a;
    }
    cout << "A soma dos valores eh: " << soma << "\n";
    return 0;
}
