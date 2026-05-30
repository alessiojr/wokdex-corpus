#include <iostream>
#include <vector>

using namespace std;

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> grid(n + 2, vector<int>(m + 2, 0));
    int x = -1, y = -1;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            cin >> grid[i][j];
            if (grid[i][j] == 3) {
                x = i;
                y = j;
            }
        }
    }

    int passos = 1;
    while (grid[x][y] != 2) {
        grid[x][y] = 0;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (grid[nx][ny] > 0) {
                passos++;
                x = nx;
                y = ny;
                break;
            }
        }
    }

    cout << passos << "\n";
    return 0;
}
