def add(x, y):
    return x + y

print add(1, 10)
print add('abc', 'def')

def hello():
    print "Hello"

def area(w, h):
    return w * h

def print_welcome(name):
    print "Welcome", name

hello()
hello()

print_welcome("Fred")
w = 4
h = 5
print "width =", w, "height =", h, "area =", area(w, h)

def func():
    pass

print(func())