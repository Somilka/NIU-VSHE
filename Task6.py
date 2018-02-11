#!/usr/bin/python
# -*- coding: utf-8 -*-

# parameters
listLength = 2  # array length

# input...

# test list
# list = [12, -30, 23, -43, 51]

# create empty list:
list = []

# adding values from input...
for n in range(listLength):
    y = input('Enter number #' + str(n + 1) + ': ')
    list.append(y)

# show list
print "Enetered list:", list

# initialize variables...
negCount = 0  # negative numbers count
negSumm = 0  # negative numbers summ

# calculating negatives count & summ...
for val in list:
    if val < 0:
        negSumm += val
        negCount += 1

# evaluating negatives negAverage
negAverage = 0
# if positive number...
if negCount > 0:
    # ...then get average
    negAverage = float(negSumm) / negCount

# modifiyng list...
for n in range(len(list)):
    list[n] -= negAverage

# results:
print "negCount:", negCount
print "negSumm:", negSumm
print "negAverage:", negAverage
print "Changed list:", list
