#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main()

{
	int h1,m1,h2,m2;
	int sh1,sm1,sh2,sm2;
	int is,fs,soma;
	
	scanf("%d",&h1);
	scanf("%d",&m1);
	scanf("%d",&h2);
	scanf("%d",&m2);
	
	while(h1 || m1 || h2 || m2 != 0)
	{
		if(h1 >= 0 && h1 <= 23)
		{
			if(m1 >= 0 && m1 <= 59)
			{
				if(h1 < h2)
				{
					sh1 = (23 - h1)*60;
					sm1 = (60 - m1);
					is = sh1 + sm1;
					sh2 = (23 - h2)*60;
					sm2 = (60 - m2);
					fs = sh2 + sm2;
					soma = is - fs;
				}
			}
		}
		if(h2 >= 0 && h2 <= 23)
		{
			if(m2 >= 0 && m2 <=59)
			{
				if(h1 >= h2)
				{
					sh1 = (23 - h1)*60;
					sm1 = (60 - m1);
					is = sh1 + sm1;
					sh2 = (23 - h2)*60;
					sm2 = (60 - m2);
					fs = sh2 + sm2;
					soma = ((fs - is)-1440)*-1;
				}
			}
		}
		printf("%d",soma);
		break;
	}
}
