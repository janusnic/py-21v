# -*- coding:utf-8 -*-
# 3.py глобальная переменная age
age = 44
 
def info():
    print age # Печатаем глобальную переменную age
 
def local_info():
    age = 22 # создаем локальную переменную age 
    print age
 
info() # напечатает 44
local_info() # напечатает 22