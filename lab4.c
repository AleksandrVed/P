#include <stdio.h>
#include <math.h>

int main(void)
{
float a, x, g, f, y, step, x1, x2, H, mini, maxi;
int var, exitt, n;
float spisok[100];
exitt = 0;
while (exitt == 0)
{
    n = 0;
    printf ("Vvedite a: \n");
    scanf ("%f" , &a);
    printf ("Vvedite nomer: \n");
    scanf ("%int", &var);
    printf ("nizhnaya granica  ");
    scanf ("%f", &x1);
    printf("verhnaya granica  ");
    scanf ("%f", &x2);
    printf ("Vvedite x: ");
    scanf ("%f", &x);
    printf ("Vvedite shag  ");
    scanf ("%f", &step);
    if (var== 1)
    {
            if (3 * (a*a) - 7 * a * x + 4 * x * x == 0)
            {
                printf("Nevernoe zna4enie");
            }
            else
            {
                while ((x1 <= x) && (x <= x2))
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
                while ((x1 <= x) && (x <= x2))
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
                printf("Nevernoe zna4enie");
            }
        }
    if (var == 3)
    {
            if ((-40) * (a*a) + 3* a* x+ (x*x) +1 > 0)
            {
                while ((x1 <= x) && (x <= x2))
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
                printf("Nevernoe zna4enie");
            }
        }
    printf("max = %f ", maxi);
    printf("min = %f\n ", mini);
    if (var > 3 || var < 1)
    {
        printf("Nevernoe zna4enie");
    }
    printf("Prodol)|(ut' raboty? (0-Yes, 1-Net)");
    scanf("%int", &exitt);
}
return 0;
}
