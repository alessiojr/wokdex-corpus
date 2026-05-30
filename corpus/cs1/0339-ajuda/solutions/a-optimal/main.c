/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include <string.h>

int main() {
    int N;

    while (scanf("%d", &N) == 1 && N != 0) {
        int S = 0; 
        int P = 0; 
        int resolvido[26];       
        int tempo[26];   
        int tempoAjuda[26];      

        for (int i = 0; i < 26; i++) {
            resolvido[i] = 0;
            tempo[i] = 0;
            tempoAjuda[i] = 0;
        }

        char letra;
        int T;
        char TorF[10];

        for (int i = 0; i < N; i++) {
            if (scanf(" %c %d %s", &letra, &T, TorF) != 3) {
                break;
            }

            int contadorL = letra - 'A';

            if (strcmp(TorF, "incorrect") == 0) {
                if (resolvido[contadorL] == 0) {
                    tempoAjuda[contadorL] += 20;
                }
            } else if (strcmp(TorF, "correct") == 0) {
                if (resolvido[contadorL] == 0) {
                    resolvido[contadorL] = 1;
                    tempo[contadorL] = T;
                }
            }
        }

        for (int i = 0; i < 26; i++) {
            if (resolvido[i] == 1) {
                S++;
                P += tempo[i] + tempoAjuda[i];
            }
        }

        printf("%d %d\n", S, P);
    }

    return 0;
}
