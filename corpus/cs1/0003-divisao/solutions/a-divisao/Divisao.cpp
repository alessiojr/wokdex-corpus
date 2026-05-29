#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    float a, b;
    cin >> a >> b;
    cout << fixed << setprecision(2) << (double)a / b << endl;
    return 0;
}
