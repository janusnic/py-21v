# -*- coding:utf-8 -*-

squares = []
for x in range(5):
   squares.append(lambda: x**2)

print squares[2]()

print squares[4]()
