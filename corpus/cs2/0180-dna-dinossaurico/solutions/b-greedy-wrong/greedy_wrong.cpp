#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string s;
    if (!(cin >> s)) return 0;
    int n = s.length();
    
    vector<int> divisors;
    for (int i = 1; i * i <= n; i++) {
        if (n % i == 0) {
            divisors.push_back(i);
            if (i * i != n) {
                divisors.push_back(n / i);
            }
        }
    }
    sort(divisors.begin(), divisors.end());
    
    for (int k : divisors) {
        int d = n / k;
        bool valid = true;
        
        // ERRO GULOSO/PREGUIÇOSO:
        // Verifica apenas o primeiro e o último bloco (extremidades)
        // Ignora totalmente os blocos do miolo (onde d > 2)
        for (int j = 0; j < k; j++) {
            if (s[j] != s[(d - 1) * k + j]) {
                valid = false;
                break;
            }
        }
        
        // Se as pontas baterem, ele assume (erroneamente) que tudo é palíndromo
        if (valid) {
            cout << d << "\n";
            return 0;
        }
    }
    return 0;
}
