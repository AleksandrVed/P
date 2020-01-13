import math
import random
import time
begin = time.process_time()
t = 0
c = 0
n = int(input('Количество точек = '))
r = float(input('Радиус = '))
T = int(input('Измерение времении каждые...'))
ax = random.uniform(-5, 5)
ay = random.uniform(-5, 5)
for i in range(0, n):
    f =  open('time.txt', 'a')
    x = random.uniform(-5, 5)
    y = random.uniform(-5, 5)
    if (math.sqrt((x-ax)*(x-ax))+math.sqrt((y-ay)*(y-ay))<=r):
        c += 1
    t = t+ 1
    if t == T:
        time1 = (time.process_time() - begin)
        f.write(str(time1)+'  секунд\n')
        t = 0
print('Точек в области: ', c)
f.close
