#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Direções: N, L, S, O
// Mapeamento: 0, 1, 2, 3
// Direita (+1), Esquerda (-1 ou +3)

char get_direction_char(int dir) {
    if (dir == 0) return 'N';
    if (dir == 1) return 'L';
    if (dir == 2) return 'S';
    if (dir == 3) return 'O';
    return '?';
}

void solve() {
    int N;
    while (cin >> N && N != 0) {
        string commands;
        cin >> commands;
        
        int current_dir = 0; // Começa no Norte (0)
        
        for (char cmd : commands) {
            if (cmd == 'D') {
                current_dir = (current_dir + 1) % 4;
            } else if (cmd == 'E') {
                current_dir = (current_dir + 3) % 4;
            }
        }
        
        cout << get_direction_char(current_dir) << endl;
    }
}

int main() {
    solve();
    return 0;
}
