#!/usr/bin/python
# -*- coding: utf-8 -*-

a = 10
b = 6
print "#1", "a:", a, "b:", b
# --a  # decrement doesn't effect in python!!! WTF?
# a -= 1  # ???
print "#2", "a:", a
b = a % 4  # 10 % 4 = 2
print "#3", "b:", b
d = a - b  # 10 - 2 = 8
print "d:", d
