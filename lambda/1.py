# -*- coding:utf-8 -*-

func = lambda x, y: x + y
print func(1, 2)

print func('a', 'b')

print (lambda x, y: x + y)(1, 2)

print (lambda x, y: x + y)('a', 'b')

