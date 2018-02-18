#!/usr/bin/python
# -*- coding: utf-8 -*-

# ОГЭ: Вариант 4(четвёртый)

# Спрашиваем первое число ( длину списка ) и присваиваем его в listLength
print "Ukazhite dlinu spiska(pervoe chislo massiva)"
listLength = input()

# Устраняем возможность ошибки
if listLength > 1000:
    print ":::ERROR::: Po usloviu: Chislo dolzhno bit ne bolsche 1000"
    exit(1)

# Создаём пустой массив
list = []

# Заполняем массив числами
for b in range(listLength):
    y = input('Enter number #' + str(b + 1) + ': ')
    list.append(y)

# Заводим счётчик чисел, подходящих по условию
n = 0

# Проверяем все числа массива на выполнение условия
for value in list:
    if value % 3 == 0 and value % 10 == 2:
        n += 1

# Выводим ответ на экран
print "Summ:", n
