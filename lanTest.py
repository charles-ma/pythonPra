# Some testing about try except block
try: 
    raise Exception, "I know python!", None
    pass
except (KeyboardInterrupt, SystemExit) as e:
    print str(e)
except Exception as e:
    print e
else:
    print "This is the else clause"
finally:
    print "This is the final clause"

# Context management protocol
try:
    with open("./newFile") as f:
        for eachLine in f:
            print eachLine    
except Exception as e:
    print e    

# Assertion related
assert 1 == 1

# Simple decorator
def simpleDec(func):
    def funcToReturn():
        print "hello simple decorator! "
        func()
    return funcToReturn

@simpleDec
def mySimpleFunc():
    print "mySimpleFunc called!"

mySimpleFunc()    

# Decorator with arguments
def myDec(x, y):
    def newFun(func):
        def yetFunc():
            print x + " : " + func(y)
        return yetFunc
    # Decorators have to return a function
    return newFun


@myDec("hello", "world")
def myPrint(x):
    return "<html>" + x + "</html>"

myPrint()
