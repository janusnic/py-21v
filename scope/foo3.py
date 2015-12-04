x = 10
def foobar():
    global x
    print(x)
    x += 1
foobar()