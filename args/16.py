# -*- coding:utf-8 -*-
name = input('Имя...')
def print_name(name):  #В скобках - параметр, который получает функция
    print('Твое имя - ' + name)
a=input('Да?')
if a == 'да':
    print_name(name)  
elif a== 'нет':
    print_name('нет ') #Передаем "нет " как параметр 
#Еще какой-нибудь код, где мы вызываем эту функцию