import math
Exit = 0
spisokG =[]
spisokF =[]
spisokY =[]
maxS=0
minS=0
while Exit == 0:
    print("Внести шаблон")
    Shabl=str(input())
    strS=float(0)
    i = 0
    print("Ввести a")
    a = float(input())
    a1 = float(a)
    print("Ввести нижнюю границу - x")
    x1 = float(input())
    x11 = float(x1)
    print("Ввести вверхнюю границу - x")
    x2 = float(input())
    x22 = float(x2)
    print("Ввести x")
    x = float(input())
    xx = float(x)
    print('Ввести шаг изменения переменной x')
    Step = float(input())
    print("Функция 1")
    while x1 <= x and x <= x2:
        g1 = (3*a*a-7*a*x+4*x*x)
        if g1 != 0:
            g=(-7)*(20*a*a+11*a*x+45*x*x)/(3*a*a-7*a*x+4*x*x)
            spisokG.append(g)
            strS = "\t".join([str(i) for i in spisokG])
            print('Аргумент x = {:2f}\t Значение = {:2f}'.format(x, spisokG[i]))
            i = i+1
            x = x + Step
            maxS = max(spisokG)
            minS = min(spisokG)
            print('Максимум'+str(maxS))
            print('Минимум'+str(minS))
        else:
            print("Значения не принадлежат области определения функции.")
            x = x1-1
            continue

    fi = open('labG.txt','w')
    fi.write(str(spisokG) +'\n')
    fi.close()

    i = 0
    sovpod = strS.count(Shabl)
    print('Кол-во совпадений = ' '%d' %sovpod)
    print("Функция 2")
    a = a1
    x1 = x11
    x2 = x22
    x = xx
    while x1 <= x and x <= x2:
        f1 = (60 * (a**2) + 88* (a*x) +21 * (x**2))
        if f1 != 1 and f1 != 1:
            f = math.tan(60*a*a+88*a*x-21*x*x)
            spisokF.append(f)
            strS = "\t".join([str(i) for i in spisokF])
            print('Аргумент x = {:2f}\t Значение = {:2f}'.format(x, spisokF[i]))
            x = x + Step
            i = i+1
            maxS = max(spisokF)
            minS = min(spisokF)
            print('Максимум'+str(maxS))
            print('Минимум'+str(minS))
        else:
            print("Значения не принадлежат области определения функции.")
            x=x1-1
            continue

    fi = open('labF.txt','w')
    fi.write(str(spisokF) +'\n')
    fi.close()
    i = 0
    sovpod = strS.count(Shabl)
    print('Кол-во совпадений = ' '%d' %sovpod)
    a = a1
    x1 = x11
    x2 = x22
    x = xx
    print("Функция 3")
    while x1 <= x and x <= x2:
        y1 = (-40) * a * a + 3 * a * x + x * x + 1
        if y1 >= 0:
            Y = math.log(y1)
            y=math.log((-40) * a * a + 3 * a * x + x * x + 1)/math.log(2)
            spisokY.append(y)
            strS = "\t".join([str(i) for i in spisokY])
            print('Аргумент x = {:2f}\t Значение = {:2f}'.format(x, spisokY[i]))
            x = x + Step
            i = i+1
            maxS = max(spisokY)
            minS = min(spisokY)
            print('Максимум'+str(maxS))
            print('Минимум'+str(minS))
        else:
            print("Значения не принадлежат области определения функции.")
            x = x1-1
            continue

    fi = open('labY.txt','w')
    fi.write(str(spisokY) +'\n')
    fi.close()

    sovpod = strS.count(Shabl)
    print('Кол-во совпадений = ' '%d' %sovpod)

    print('Функция G')
    fi = open('labG.txt','r')
    data = fi.readline()
    fi.close()
    print(data)

    print('Функция F')
    fi = open('labF.txt','r')
    data = fi.readline()
    fi.close()
    print(data)

    print('Функция Y')
    fi = open('labY.txt','r')
    data = fi.readline()
    fi.close()
    print(data)

    print("Выйти из программы?(1-да, 0-нет)")
    Exit = int(input())
