#include <iostream>
#include <string>
#include <map>

int main() {
    // Fast I/O
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n;
    if (!(std::cin >> n)) return 0;

    std::map<int, long long> color_counts;
    for (int i = 0; i < n; ++i) {
        int color;
        std::cin >> color;
        color_counts[color]++;
    }

    long long total_pairs = 0;
    for (std::map<int, long long>::const_iterator it = color_counts.begin(); it != color_counts.end(); ++it) {
        long long count = it->second;
        if (count >= 2) {
            total_pairs += (count * (count - 1)) / 2;
        }
    }

    std::cout << total_pairs << "\n";

    return 0;
}
