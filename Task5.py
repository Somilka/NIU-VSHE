#!/usr/bin/python
# -*- coding: utf-8 -*-

# input
print "Enter number a(1;2 dflt)"
a = input()
print "Enter number h(3;2 dflt)"
h = input()
print "Enter number P(5;14 dflt)"
P = input()
# Go working...
s = 0
n = 0
while True:
    s = s + (a + n * h)
    print str(n) + ":" + str(s)
    if s > P:
        break
    n = n + 1
# result
print(n)
