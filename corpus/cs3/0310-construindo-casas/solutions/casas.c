#include <math.h>
#include <stdio.h>

int main(){
  int l, c, perc;
  while(1) {
    scanf("%d", &l);
    if(l==0) break;

    scanf("%d", &c);
    if(c==0) break;

    scanf("%d", &perc);
    if(perc == 0) break;

    int area = l * c;

    double neededArea = (area * 100.0)/ perc;

    int lado = sqrt(neededArea);

    printf("%d\n", lado);
  }
  return 0;
}