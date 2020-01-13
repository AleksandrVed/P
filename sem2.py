import math

c = 0.0001

a = float(input())
b = float(input())
x1 = a + c
x1 = random.uniform(a, b)
x2 = x1 + c
if a < x1:
    x1 = a
    a = x1 + c
print(x1)
