#include <iostream>
#include <string>

using namespace std;

void solve() {
    string line;
    while (getline(cin, line)) {
        if (line.empty()) continue;
        
        int i = 0;
        int len = line.length();
        bool tem_saida = false;
        
        while (i < len) {
            if (line[i] == '!') {
                cout << "\n";
                tem_saida = true;
                i++;
                continue;
            }
            
            int total = 0;
            while (i < len && isdigit(line[i])) {
                total += (line[i] - '0');
                i++;
            }
            
            if (i < len && line[i] == '!') {
                cout << "\n";
                tem_saida = true;
                i++;
            } else if (total > 0 && i < len) {
                char atual = line[i];
                if (atual == 'b') atual = ' ';
                for (int j = 0; j < total; j++) {
                    cout << atual;
                    tem_saida = true;
                }
                i++;
            } else if (i < len) {
                i++;
            }
        }
        
        if (!tem_saida) cout << "Entrada errada";
        cout << "\n-------------" << endl;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    solve();
    return 0;
}
