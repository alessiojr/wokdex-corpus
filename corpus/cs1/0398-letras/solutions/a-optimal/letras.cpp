#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    char target;
    if (!(cin >> target)) return 0;
    
    string word;
    int total = 0;
    int count = 0;
    
    while (cin >> word) {
        total++;
        if (word.find(target) != string::npos) {
            count++;
        }
    }
    
    if (total == 0) {
        cout << fixed << setprecision(1) << 0.0 << "\n";
    } else {
        double percent = (double)count / total * 100.0;
        cout << fixed << setprecision(1) << percent << "\n";
    }
    
    return 0;
}
