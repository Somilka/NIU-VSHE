#!/usr/bin/python
# -*- coding: utf-8 -*-

# Who is Kirill? v.1

# Спрашиваем пользователя, лох ли Кирилл
a = raw_input("Kirill loh?\n")

# Проверяем, что возвращает a
# print type(a), a

p = raw_input("Skolko procentov?\n")

# учитывая ответ, содержащийся в a, выясняем, кто такой Кирилл
if a == "da":
    print "Kirill loh", p, "%"
elif a == "net":
    print "Krill ne loh", p, "%"
elif a != "net":
    # print "Who is kirill?"
    # b = raw_input("Who is Kirill?\n")
    print a, p, "%"

# p = raw_input("Skolko procentov?\n")
# print a, p, "%"
# памагити, очень сложно((
