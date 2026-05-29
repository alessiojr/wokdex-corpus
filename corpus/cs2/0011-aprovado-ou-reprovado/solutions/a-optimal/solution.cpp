#include <iostream>

using namespace std;

int main() {
    double a, b;
    if (cin >> a >> b) {
        double media = (a + b) / 2.0;
        
        if (media >= 7.0) {
            cout << "Aprovado\n";
        } else if (media >= 4.0) {
            cout << "Recuperacao\n";
        } else {
            cout << "Reprovado\n";
        }
    }
    return 0;
}
