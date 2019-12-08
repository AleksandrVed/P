#include  <stdio.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
float a, x, g, f, y;
printf ("Vvedite x: ");
scanf ("%f", &x);
printf ("Vvedite a: ");
scanf ("%f" , &a);
g = (-7)*(20*a*a+11*a*x+45*x*x)/(3*a*a-7*a*x+4*x*x);
printf  ("g=%f\n\n", g);

printf ("Vvedite x: ");
scanf ("%f", &x);
printf ("Vvedite a: ");
scanf ("%f", &a);
f = tan(60*a*a+88*a*x+21*x*x);
printf  ("f=%f\n\n", f);

printf ("Vvedite x:");
scanf ("%f", &x);
printf ("Vvedite a:");
scanf ("%f", &a);
y = log((-40)*a*a + 3*a*x + x*x + 1)/log(2);
printf  ("y=%f\n\n", y);
}
