import math
import random
import time
begin = time.process_time()
c = 0
n = int(input('Количество точек = '))
r = float(input('Радиус = '))
ax = random.uniform(-5, 5)
ay = random.uniform(-5, 5)
for i in range(0, n):
    x = random.uniform(-5, 5)
    y = random.uniform(-5, 5)
    if (math.sqrt((x-ax)*(x-ax))+math.sqrt((y-ay)*(y-ay))<=r):
        c += 1
print('Точек в области: ', c)
time = (time.process_time()-begin)
f =  open('time.txt', 'a')
f.write(str(time)+'  секунд')
f.close
