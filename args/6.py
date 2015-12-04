# -*- coding:utf-8 -*-

def help(object1, spacing=10, collapse=1):
    print object1
    print spacing
    print collapse
odbchelper = 'help(odbchelper)  # С одним аргументом, spacing и collapse получают значения по умолчанию, 10 и 1 соответственно.'
help(odbchelper)  # С одним аргументом, spacing и collapse получают значения по умолчанию, 10 и 1 соответственно.
odbchelper = 'С двумя аргументами, collapse получает значение по умолчанию 1.'
help(odbchelper, 12) # С двумя аргументами, collapse получает значение по умолчанию 1.
odbchelper = 'Здесь вы явно указываете имя аргумента, collapse, для которого передается значение. Аргумент spacing по-прежнему получает значение по умолчанию 10.'
help(odbchelper, collapse=0)  # Здесь вы явно указываете имя аргумента, collapse, для которого передается значение. Аргумент spacing по-прежнему получает значение по умолчанию 10.
odbchelper = 'Даже обязательные аргументы (в данном случае — object), которые не имеют значения по умолчанию, могут быть переданы по имени, и именованные аргументы могут быть указаны в произвольном порядке.'
help(spacing=15, object1=odbchelper) # Даже обязательные аргументы (в данном случае — object), которые не имеют значения по умолчанию, могут быть переданы по имени, и именованные аргументы могут быть указаны в произвольном порядке.


def func(a, b, c=2): # c - необязательный аргумент
    return a + b + c

func(1, 2)  # a = 1, b = 2, c = 2 (по умолчанию)

func(1, 2, 3)  # a = 1, b = 2, c = 3

func(a=1, b=3)  # a = 1, b = 3, c = 2

func(a=3, c=6)  # a = 3, c = 6, b не определен