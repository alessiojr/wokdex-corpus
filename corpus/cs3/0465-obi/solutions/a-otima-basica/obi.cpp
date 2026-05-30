#include <iostream>

using namespace std;

int main() {
    int N, P;
    if (cin >> N >> P) {
        int pass_count = 0;
        for (int i = 0; i < N; ++i) {
            int X, Y;
            cin >> X >> Y;
            if (X + Y >= P) {
                pass_count++;
            }
        }
        cout << pass_count << "\n";
    }
    return 0;
}
