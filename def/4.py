# -*- coding:utf-8 -*-
def a(a,b):
    print a,b

a(5,6)

def bigger(a,b):
    if a > b:
        print a
    else:
       print b

def person(name, age):
    print name, "is", age, "years old"

person(age=23, name="John")

def a(b=4,c=5):
    print b,c
  
a()
a(12,13)
a(b=15,c=16)

def a(b=[1]):
    b[0] += 1
    b.append(1)
    print b
a()
a()
a()


