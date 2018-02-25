#!/usr/bin/python
# -*- coding: utf-8 -*-

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

# Who is Kirill? v.1

# Спрашиваем пользователя, лох ли Кирилл
print("Is Kirill a Matthew?")
a = raw_input()
# a = "1"

# Проверяем, что возвращает a
# print type(a), a

# Спрашиваем пользователя, сколько процентов Кирилл лох/не лох/другое
print("How much percents for " + a + "?")
p = raw_input()

# учитывая ответ, содержащийся в a, выясняем, кто такой Кирилл
if a == "Yes":
    print "Kirill is Matvey", p + "%"
elif a == "No":
    print "Kirill is kake3000", p + "%"
elif a != "net":
    # print "Who is kirill?"
    # b = raw_input("Who is Kirill?\n")
    print a, p + "%"

# p = raw_input("Skolko procentov?\n")
# print a, p, "%"
# памагити, очень сложно((
