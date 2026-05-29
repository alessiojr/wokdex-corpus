/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/
#include <stdio.h>
#include <string.h>
#include <math.h>

int main() {
    int N, L, C, paginas;

    while (scanf("%d %d %d", &N, &L, &C) == 3) {
        char palavra[71000];
        double linhas = 1;
        int caracteres_na_linha = 0;

        for (int i = 0; i < N; i++) {
            if(scanf("%s", palavra)!=1) break;
            int tamanho = strlen(palavra);

            if (caracteres_na_linha == 0) {
                caracteres_na_linha = tamanho;
            } else if (caracteres_na_linha + 1 + tamanho <= C) {
                caracteres_na_linha += 1 + tamanho;
            } else {
                linhas++;
                caracteres_na_linha = tamanho;
            }
        }
        paginas = ceil(linhas/L);
        printf("%d\n", paginas);
    }
    return 0;
}
