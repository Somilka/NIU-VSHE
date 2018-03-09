#!/usr/bin/python
# -*- coding: utf-8 -*-

# ОГЭ: Вариант 2(второй)

# a = 5 % 2
# print a

# максимальное количество значений в массиве list = 1000
listLength = 1000

# list = [-20, 6, 1000, 100, -200] # 0

# заводим переменные
a = 0
b = 0
y = None

# создаём пустой список
list = []

# adding values from input...
for n in range(listLength):
    y = input('Enter number #' + str(n + 1) + ': ')
    if y != 0:
        n += 1
        list.append(y)
        # print y
        b += 1
        print b
    else:
            break
    if y <= 256 and y % 2 == 0 and y > 0:
        a += y


    # len(list)

# вывод ответов:
print "Summ:", a
print "Kol-vo:", b
