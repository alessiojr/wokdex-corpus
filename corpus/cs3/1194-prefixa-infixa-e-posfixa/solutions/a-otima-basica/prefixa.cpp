#include <iostream>
#include <string>

using namespace std;

string solve(string pre, string in) {
    if (pre.empty()) {
        return "";
    }
    
    char root = pre[0];
    int pos = in.find(root);
    
    string inLeft = in.substr(0, pos);
    string inRight = in.substr(pos + 1);
    
    string preLeft = pre.substr(1, pos);
    string preRight = pre.substr(pos + 1);
    
    return solve(preLeft, inLeft) + solve(preRight, inRight) + root;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int C;
    if (!(cin >> C)) return 0;
    
    while (C--) {
        int N;
        string pre, in;
        cin >> N >> pre >> in;
        
        cout << solve(pre, in) << "\n";
    }
    
    return 0;
}
