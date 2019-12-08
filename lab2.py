from math import*
print('Введите x')
x = float(input())
print('Введите a')
a = float(input())
print('Введите значение')
var = int(input())
if var == 1:
    G = -((7) * (20 *(a**2) + 11 * a * x - ( 45 * (x**2)))) / (3 *(a**2) - 7 * a * x + 4*x*x)
    if (3 * (a**2) - 7 * a * x + 4 * x * x) == 0:
        print('Неверные данные')
    else:
        print(G)
elif var == 2:
    if (60 * (a**2) + 88* (a*x) +21 * (x**2))!=1 and (60 * (a**2) + 88* (a*x) +21 * (x**2))!=-1:
        F = (tan(60 * (a **2) + 88 * (a * x) + 21 * (x**2)))
        print(F)
    else:
        print('Неверные данные')
elif var == 3:
    if ((-40) * (a**2) + 3* a* x+ (x**2) +1) >= 0:
        Y = log((-40) * (a**2) + 3* a* x+ (x**2) +1)/log(2)
        print(Y)
    else:
        print('Неверные данные')
else:
    ('Неверное значение')
