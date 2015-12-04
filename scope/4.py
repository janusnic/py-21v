# -*- coding:utf-8 -*-
# 4.py глобальная переменная age
age = 13
 
# функция изменяющая глобальную переменную
def get_older():
    global age
    age += 1
 
print age # напечатает 13
get_older() # увеличиваем age на 1
print age # напечатает 14