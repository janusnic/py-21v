# -*- coding:utf-8 -*-
def fact(num):
    if num == 0: 
        return 1 # По договоренности факториал нуля равен единице
    else:
        return num * fact(num - 1) # возвращаем результат произведения num и результата возвращенного функцией fact(nu

print(fact(5))