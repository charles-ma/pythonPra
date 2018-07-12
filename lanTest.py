# Sample utilities
topicCounts = 0
def topicCount(func):
    '''Print out topic index and summary(docstring)'''
    def f():
        global topicCounts
        topicCounts += 1
        print "\nTopic " + str(topicCounts)
        print func.__doc__
        print "---------------------------"
        func()
    return f

# Some testing about try except block
@topicCount
def tryExceptTest():
    '''# Some testing about try except block'''
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

tryExceptTest()


# Context management protocol
@topicCount
def contextMgmtTest():
    '''# Context management protocol'''
    try:
        with open("./newFile") as f:
            for eachLine in f:
                print eachLine    
    except Exception as e:
        print e    

contextMgmtTest()        

# Assertion related
@topicCount
def assertionTest():
    '''# Assertion related'''
    assert 1 == 1

assertionTest()    

# Simple decorator
@topicCount
def simpleDecTest():
    '''# Simple decorator'''
    def simpleDec(func):
        def funcToReturn():
            print "hello simple decorator! "
            func()
        return funcToReturn

    @simpleDec
    def mySimpleFunc():
        print "mySimpleFunc called!"

    mySimpleFunc()    

simpleDecTest()

# Decorator with arguments
@topicCount
def decWithArgTest():
    '''# Decorator with arguments'''
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

decWithArgTest()

# Generator
# Simple Generator
@topicCount
def simpleGenTest():
    '''# Simple Generator'''
    def myGen():
        yield 1
        yield "hello world"

    for elem in myGen():
        print elem    

simpleGenTest()

# Random Selector -- Generator
@topicCount
def randomSelectTest():
    '''# Random Selector -- Generator'''
    from random import randint

    def randomSelect(aList):
        while len(aList) > 0:
            # randint params are inclusive!!!
            yield aList.pop(randint(0, len(aList) - 1))

    for e in randomSelect([1, 2, 3, 4, 5]):
        print e

randomSelectTest()        

# Counter -- Generator
@topicCount
def counterTest():
    '''# Counter -- Generator'''
    def myCounter():
        count = 0
        while(True):
            val = yield count
            if val is not None:
                count = val
            else:
                count += 1
    counter = myCounter()
    print counter.next()
    print counter.next()
    print counter.send(100)
    print counter.next()
    print counter.send(5)
    print counter.next()
    print counter.close()
    # print counter.next()
    '''
    try: 
        print counter.next()
    except SyntaxError as e: 
        print e
    '''

counterTest()

# Namespace
@topicCount
def namespaceTest():
    '''# Namespace'''
    class myClass(object):
        pass
    myInstance = myClass()
    myInstance.x = 1
    print myInstance.x

namespaceTest()
