x = float(input('Введите '))
a = 1
a = a%x
b = 0
while b != (x**0.5):
    b = 0.5 * (a + x/a)
    a = b
print('Корень = ' + str(a))
