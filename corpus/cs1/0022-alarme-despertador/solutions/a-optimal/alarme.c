
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int h1,m1,h2,m2;
    scanf("%i %i %i %i", &h1, &m1, &h2, &m2);
    while (h1 != 0 || m1 != 0 || h2 != 0 || m2 != 0)
    {
        h2 -= h1;
        if(h2 == 0)
        {
            if(m1 >= m2)
            {
                h2 = 24;
            }
        }
        else if(h2 < 0)
        {
            h2 = 24 + h2;
        }
        h2 *= 60;
        m2 += h2;
        m2 -= m1;
        printf("%i\n", m2);
        scanf("%i %i %i %i", &h1, &m1, &h2, &m2);
    }
    
    return 0;
}