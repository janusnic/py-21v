# -*- coding:utf-8 -*-
# 5.py глобальная переменная age

a_var = 10
b_var = 15
c_var = 25

def a_func(a_var):
    print "in a_func a_var = ", a_var
    b_var = 100 + a_var
    d_var = 2 * a_var
    print "in a_func b_var = ", b_var
    print "in a_func d_var = ", d_var
    print "in a_func c_var = ", c_var
    return b_var + 10

c_var = a_func(b_var)

print "a_var = ", a_var
print "b_var = ", b_var
print "c_var = ", c_var
print "d_var = ", d_var
