#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main() {
    double n;
    if (cin >> n) {
        int cents = round(n * 100.0);
        
        int notes[] = {10000, 5000, 2000, 1000, 500, 200};
        int coins[] = {100, 50, 25, 10, 5, 1};
        
        cout << "NOTAS:\n";
        for (int note : notes) {
            int qty = cents / note;
            cents %= note;
            cout << qty << " nota(s) de R$ " << fixed << setprecision(2) << (note / 100.0) << "\n";
        }
        
        cout << "MOEDAS:\n";
        for (int coin : coins) {
            int qty = cents / coin;
            cents %= coin;
            cout << qty << " moeda(s) de R$ " << fixed << setprecision(2) << (coin / 100.0) << "\n";
        }
    }
    return 0;
}
