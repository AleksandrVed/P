import math
Exit = 0
spisok =[]
maxS=0
minS=0
while Exit == 0:
    Shabl=str(input("Внести шаблон"))
    i = 0
    a = float(input("Ввести a"))
    x = float(input('Начальное значение х '))
    x1 = float(input('Конечное значение х'))
    Steps = int(input('Ввести кол-во шагов '))
    if x>x1:
        Step = -(x - x1)/Steps
    else:
        Step = (x1 - x)/Steps
    ch = int(input("Выбрать номер функции 1-3"))
    if ch == 1:
        while x != x1:
            g1 = (3*a*a-7*a*x+4*x*x)
            if g1 != 0:
                g=(-7)*(20*a*a+11*a*x+45*x*x)/(3*a*a-7*a*x+4*x*x)
                spisok.append(g)
                str = "\t".join([str(i) for i in spisok])
                print('Аргумент x = {:2f}\t Значение = {:2f}'.format(x, spisok[i]))
                i = i+1
                x = x + Step
                maxS = max(spisok)
                minS = min(spisok)
            else:
                print("Значения не принадлежат области определения функции.")
                x = x1-1
                continue

        sovpod = str.count(Shabl)
        print('Кол-во совпадений = ' '%d' %sovpod)


    elif ch == 2:
        while x != x1:
            f1 = (60 * (a**2) + 88* (a*x) +21 * (x**2))
            if f1 != 1 and f1 != 1:
                f = math.tan(60*a*a+88*a*x-21*x*x)
                spisok.append(f)
                str = "\t".join([str(i) for i in spisok])
                print('Аргумент x = {:2f}\t Значение = {:2f}'.format(x, spisok[i]))
                x = x + Step
                i = i+1
                maxS = max(spisok)
                minS = min(spisok)
            else:
                print("Значения не принадлежат области определения функции.")
                x=x1-1
                continue

        sovpod = str.count(Shabl)
        print('Кол-во совпадений = ' '%d' %sovpod)

    elif ch == 3:
        while x != x1:
            y1 = (-40) * a * a + 3 * a * x + x * x + 1
            if y1 >= 0:
                Y = math.log(y1)
                y=math.log((-40) * a * a + 3 * a * x + x * x + 1)/math.log(2)
                spisok.append(y)
                str = "\t".join([str(i) for i in spisok])
                print('Аргумент x = {:2f}\t Значение = {:2f}'.format(x, spisok[i]))
                x = x + Step
                i = i+1
                maxS = max(spisok)
                minS = min(spisok)
            else:
                print("Значения не принадлежат области определения функции.")
                x = x1-1
                continue
        sovpod = str.count(Shabl)
        print('Кол-во совпадений = ' '%d' %sovpod)

    else:
        print("Нет такой функции.")
    print('Максимум'+str(maxS))
    print('Минимум'+str(minS))
    print("Выйти из программы?(1-да, 0-нет)")
    Exit = int(input())
