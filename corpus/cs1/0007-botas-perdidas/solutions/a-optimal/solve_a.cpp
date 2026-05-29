#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    while (cin >> n) {
        vector<int> left(65, 0);
        vector<int> right(65, 0);

        for (int i = 0; i < n; ++i) {
            int size;
            char side;
            cin >> size >> side;
            if (side == 'E') {
                left[size]++;
            } else {
                right[size]++;
            }
        }

        int pairs = 0;
        for (int i = 30; i <= 60; ++i) {
            pairs += min(left[i], right[i]);
        }
        cout << pairs << endl;
    }
    return 0;
}
