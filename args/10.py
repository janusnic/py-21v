# -*- coding:utf-8 -*-
def a(*args):
     print args
 
a(1,2,3) # Переменное к-во аргументов
a([1,2,3]) # Список (передается как один аргумент)
a(*[1,2,3]) # Список со звездочкой (передается как переменное к-во аргументов)