#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(void)
{
float a, x, g, f, y, step, x1, H, mini, maxi;
int var, exitt, n, steps;
char spisok[255];
char n1[255];
char n2[255];
char n3[255];
char n4[255];
char n5[255];
exitt = 0;
while (exitt == 0)
{
    n = 0;
    
    printf ("Vvedite a: ");
    scanf ("%s" , &n1);
    a = atof(n1);
    
    printf ("Vvedite nomer: ");
    scanf ("%s", &n2);
    n = atoi(n2);
    
    printf ("Vvedite na4al'noe x:  ");
    scanf ("%s", &n3);
    x = atof(n3);
    
    printf ("Vvedite kone4noe x:  ");
    scanf ("%s", &n4);
    x1 = atof(n4);
    
    printf ("Vvedite koli4estvo shagov  ");
    scanf ("%s", &n5);
    steps = atoi(n5);
    
    if (x>x1)
    {
        step = (-(x-x1)/steps);
    }
    else
    {
        step = ((x1-x)/steps);
    }
    if (var== 1)
    {
            if (3 * (a*a) - 7 * a * x + 4 * x * x == 0)
            {
                printf("Nevernoe zna4enie\n");
            }
            else
            {
                while (x != x1)
                    {
                        g = -((7) * (20 *(a*a) + 11 * a * x - ( 45 * (x*x)))) / (3 *(a*a) - 7 * a * x + 4*x*x);
                        printf("g=%f\n",g);
                        x = x+step;
                        spisok[n] =g;
                        n++;
                        if (mini > g)
                        {
                            mini = g;
                        }
                        if (maxi < g)
                        {
                            maxi = g;
                        }
                    }
            }
    }
    if (var == 2)
    {
            H = 60 * (a*a) + 88* (a*x) +21 * (x*x);
            if (H!=1 && H!=-1)
            {
                while (x != x1)
                {      
                f = (tan(60 * (a *a) + 88 * (a * x) + 21 * (x*x)));
                printf("f=%f\n",f);
                x = x + step;
                spisok[n] =g;
                n++;
                if (mini > g)
                {
                    mini = g;
                }
                if (maxi < g)
                {
                    maxi = g;
                }
                }
            }
            else
            {
                printf("Nevernoe zna4enie\n");
            }
        }
    if (var == 3)
    {
            if ((-40) * (a*a) + 3* a* x+ (x*x) +1 > 0)
            {
                while (x != x1)
                {
                y = log((-40) * (a*a) + 3* a* x+ (x*x) +1)/log(2);
                printf("y=%f\n",y);
                x = x+step;
                spisok[n] =g;
                n++;
                if (mini > g)
                {
                    mini = g;
                }
                if (maxi < g)
                {
                    maxi = g;
                }
                }
            }
            else
            {
                printf("Nevernoe zna4enie\n");
            }
        }
    printf("max = %f ", maxi);
    printf("min = %f\n ", mini);
    if (var > 3 || var < 1)
    {
        printf("Nevernoe zna4enie\n");
    }
    printf("Prodol)|(ut' raboty? (0-Yes, 1-Net)");
    scanf("%int", &exitt);
}
return 0;
}
