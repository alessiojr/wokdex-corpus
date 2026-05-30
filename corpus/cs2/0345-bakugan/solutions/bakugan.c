#include <stdio.h>

int main() {
    int r;

    while (1) {
        scanf("%d", &r);
        if (r == 0)
            break;

        int m[r], l[r];
        int mpontos = 0, lpontos = 0;

        for (int i = 0; i < r; i++) {
            scanf("%d", &m[i]);
        }
        for (int i = 0; i < r; i++) {
            scanf("%d", &l[i]);
        }

       
        for (int i = 0; i < r; i++) {
            mpontos += m[i];
            lpontos += l[i];
        }

        
        int mb = -1, lb = -1;

        for (int i = 2; i < r; i++) {
            if (m[i] == m[i - 1] && m[i - 1] == m[i - 2]) {
                mb = i; 
                break;
            }
        }

        for (int i = 2; i < r; i++) {
            if (l[i] == l[i - 1] && l[i - 1] == l[i - 2]) {
                lb = i; 
                break;
            }
        }

        if (mb != -1 && (lb == -1 || mb < lb)) {
            mpontos += 30; 
        } else if (lb != -1 && (mb == -1 || lb < mb)) {
            lpontos += 30; 
        }
        

        if (mpontos > lpontos)
            printf("M\n");
        else if (lpontos > mpontos)
            printf("L\n");
        else
            printf("T\n");
    } 

    return 0;
}
