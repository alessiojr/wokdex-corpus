#include <stdio.h>
#include <stdlib.h>

int main()
{
    double H, P, avg;
    scanf("%lf %lf", &H, &P);
    avg = H/P;
    printf("%.2f\n", avg);
    return 0;
}