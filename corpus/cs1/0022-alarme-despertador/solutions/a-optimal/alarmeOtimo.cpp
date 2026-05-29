#include <stdio.h>

int main()
{
	int h1,m1,h2,m2;
	
	scanf("%d",&h1);
	scanf("%d",&m1);	
	scanf("%d",&h2);
	scanf("%d",&m2);
	
	m1 += h1 * 60;
	m2 += h2 * 60;
	
	if(m1 < m2)
		printf("%d",m2 - m1);
	else
		printf("%d",(m2 + 1440) - m1);	
}
