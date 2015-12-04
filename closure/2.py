# -*- coding:utf-8 -*-

def attribution(name):
   return lambda x: x + ' -- ' + name

pp = attribution('John')
print pp('Dinner is in the fridge')