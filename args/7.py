# -*- coding:utf-8 -*-
def unknown(*args):
    for argument in args:
        print argument
 
unknown("hello","world") # напечатает оба слова, каждое с новой строки
unknown(1,2,3,4,5) # напечатает все числа, каждое с новой строки
unknown() # ничего не выведет