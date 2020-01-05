#include  <stdio.h>
#include <math.h>

int main(void)
{
float a, x, g, f, y;
int var;
printf ("Vvedite x: ");
scanf ("%f", &x);
printf ("Vvedite a: ");
scanf ("%f" , &a);
printf ("Vvedite nomer: ");
scanf ("%int", &var);
if (var== 1)
    {
        if (3 * (a*a) - 7 * a * x + 4 * x * x == 0)
    {
        printf("Nevernoe zna4enie");
    }
        else
    {
        g = -((7) * (20 *(a*a) + 11 * a * x - ( 45 * (x*x)))) / (3 *(a*a) - 7 * a * x + 4*x*x);
        printf("g=%f\n",g);
    }
    }
if (var == 2)
    {
        if ((60 * (a*a) + 88* (a*x) +21 * (x*x))!=1) and ((60 * (a*a) + 88* (a*x) +21 * (x*x))!=-1)
    {
        f = (tan(60 * (a *a) + 88 * (a * x) + 21 * (x*x)));
        printf("f=%f\n",f);
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
        y = log((-40) * (a*a) + 3* a* x+ (x*x) +1)/log(2);
        printf("y=%f\n",y);
    }
        else
    {
        printf("Nevernoe zna4enie");
    }
    }
if (var > 3) or (var < 1)
    {
        printf("Nevernoe zna4enie");
    }
