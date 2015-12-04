# -*- coding:utf-8 -*-

squares = []
for x in range(5):
   squares.append(lambda n=x: n**2)
   
print squares[2]()

print squares[4]()
