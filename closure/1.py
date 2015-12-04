# -*- coding:utf-8 -*-
def newfunc(n):
    def myfunc(x):
        return x + n
    return myfunc

new = newfunc(100)  # new - это функция
print new(200)