#include <iostream>
#include <vector>

int main() {
    // Fast I/O
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n;
    if (!(std::cin >> n)) return 0;

    std::vector<int> colors(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> colors[i];
    }

    long long total_pairs = 0;
    // O(N^2) loop
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if (colors[i] == colors[j]) {
                total_pairs++;
            }
        }
    }

    std::cout << total_pairs << "\n";

    return 0;
}
