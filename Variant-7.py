#!/usr/bin/python
# -*- coding: utf-8 -*-

# Указываем максимальное кол-во эл-тов
maxCount = 100

# Получить кол-во элементов
print "Enter element's count"
count = input()

# Ограничиваем, если больше максимального...
if count > maxCount:
    count = maxCount

# Сумма
summ = 0

# Цикл...
for n in range(count):
    # Ввод числа...
    print "Enter a number", ( n + 1 ), 'of', count, '(0=break)'
    val = input()
    # Если введён нуль, то прекращаем выполнение
    if val == 0:
        print "Input breaked"
        break
    # Если число соответствует условию...
    if (val % 3) == 0 and (val % 10) == 9:
        # ...добавляем к сумме
        summ += val

# Результат
print "Summ:", summ
