#include <cstdio>

int main() {
    int n, f;
    while (scanf("%d %d", &n, &f) == 2) {
        if (n == 0 && f == 0) break;
        double litros = (f * 50.0) / (n * 1000.0);
        printf("%.2f\n", litros);
    }
    return 0;
}
