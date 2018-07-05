from fibo import fibo as f
from cmath import phase

def myDecorator(func):
    print 'decorated!'
    return func

class MyClass:
    def __init__(self):
        #self.name = name
        print 'This is the init method!'

    @myDecorator
    def myMethod(self):
        print 'My Method called!'

    name = 'Mary'    
    global G 
    G = 2

print f(10)
insta = MyClass()
insta.myMethod()

a = complex(1, 1)
b = complex(1, -1)

print a * b

print phase(a)