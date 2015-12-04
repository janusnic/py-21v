# -*- coding:utf-8 -*-
a = 23
b = -24

if a < 0:
    a = -a
if b < 0:
    b = -b                         #Or use the command: elif (if+else)

if b == a:
    print "The absolute values of", a, "and", b, "are equal"
else:
    print "The absolute values of", a, "and", b, "are different"

def absolute_value(n):
    if n < 0:
        n = -n
    return n

if absolute_value(a) == absolute_value(b):
    print "The absolute values of", a, "and", b, "are equal"
else:
    print "The absolute values of", a, "and", b, "are different"

def bigger(a,b):
    if a > b:
        return a # Если a больше чем b, то возвращаем b и прекращаем выполнение функции
    return b # Незачем использовать else. Если мы дошли до этой строки, то b, точно не меньше чем a
 
# присваиваем результат функции bigger переменной num
num = bigger(23,42)