#!/usr/bin/python
# -*- coding: utf-8 -*-

# test list
list = [23]
# list = [12, -30, 23, -43, 51]

# parameters
# listLength = 20  # array length
# create empty list:
# list = []
# adding values from input...
# for n in range(listLength):
#     y = input('Enter number #' + str(n + 1) + ': ')
#     list.append(y)

# show list
print "Enetered list:", list

max = None
min = None
max2 = None
min2 = None

# calculating negatives count & summ...
for value in list:
    if value > max or max is None:
        print "Max:", value, "Max Prev:", max
        max2 = max
        max = value
    elif value > max2 or max2 is None:
        print "Max2:", value, "Max2 Prev:", max2
        max2 = value
    if value < min or min is None:
        print "Max:", value, "Max Prev:", min
        min2 = min
        min = value
    elif value < min2 or min2 is None:
        print "Max2:", value, "Max2 Prev:", min2
        min2 = value

# u can also find second values by this way!!
# for value in list:
#     if (value > max2 or max2 is None) and value != max:
#         print "Saving new max:", value, "prev max:", max
#         max2 = value

print "Min Value:", min
print "Min Value2:", min2
print "Max Value:", max
print "Max Value2:", max2

if min is None:
    min = 0
if min2 is None:
    min2 = 0
if max is None:
    max = 0
if max2 is None:
    max2 = 0

minSumm = min + min2
maxSumm = max + max2

print "otvet 1:", maxSumm
print "otvet 2:", minSumm
