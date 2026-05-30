#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int r;
    while (cin >> r && r != 0) {
        vector<int> m(r);
        for (int i = 0; i < r; ++i) {
            cin >> m[i];
        }
        
        vector<int> l(r);
        for (int i = 0; i < r; ++i) {
            cin >> l[i];
        }
        
        int score_m = 0, score_l = 0;
        bool bonus_given = false;
        
        for (int i = 0; i < r; ++i) {
            score_m += m[i];
            score_l += l[i];
            
            if (!bonus_given && i >= 2) {
                bool m_consec = (m[i] == m[i-1] && m[i-1] == m[i-2]);
                bool l_consec = (l[i] == l[i-1] && l[i-1] == l[i-2]);
                
                if (m_consec && l_consec) {
                    bonus_given = true;
                } else if (m_consec) {
                    score_m += 30;
                    bonus_given = true;
                } else if (l_consec) {
                    score_l += 30;
                    bonus_given = true;
                }
            }
        }
        
        if (score_m > score_l) cout << "M\n";
        else if (score_l > score_m) cout << "L\n";
        else cout << "T\n";
    }
    
    return 0;
}
