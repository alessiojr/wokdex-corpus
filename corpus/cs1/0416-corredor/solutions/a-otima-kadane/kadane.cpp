#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    if (!(cin >> n)) return 0;
    
    long long max_so_far = -1e18;
    long long current_max = 0;
    
    for (int i = 0; i < n; i++) {
        long long val;
        cin >> val;
        current_max += val;
        if (current_max > max_so_far) {
            max_so_far = current_max;
        }
        if (current_max < 0) {
            current_max = 0;
        }
    }
    
    cout << max_so_far << "\n";
    return 0;
}
