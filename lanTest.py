# Sample utilities
topicCounts = 0
def newTopic(func):
    '''Form a new topic, print out topic index and summary(docstring)'''
    def f():
        global topicCounts
        topicCounts += 1
        print "\nTopic " + str(topicCounts)
        print func.__doc__
        print "---------------------------"
        func()
    return f

# Some testing about try except block
@newTopic
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
@newTopic
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
@newTopic
def assertionTest():
    '''# Assertion related'''
    assert 1 == 1

assertionTest()    

# Simple decorator
@newTopic
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
@newTopic
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
@newTopic
def simpleGenTest():
    '''# Simple Generator'''
    def myGen():
        yield 1
        yield "hello world"

    for elem in myGen():
        print elem    

simpleGenTest()

# Random Selector -- Generator
@newTopic
def randomSelectTest():
    '''# Random Selector -- Generator'''
    # import module using import clause
    # from random import randint

    # import module using __import__ function
    rand = __import__("random")
    
    def randomSelect(aList):
        while len(aList) > 0:
            # randint params are inclusive!!!
            yield aList.pop(rand.randint(0, len(aList) - 1))

    for e in randomSelect([1, 2, 3, 4, 5]):
        print e

randomSelectTest()        

# Counter -- Generator
@newTopic
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
@newTopic
def namespaceTest():
    '''# Namespace'''
    class MyClass(object):
        pass
    myInstance = MyClass()
    myInstance.x = 1
    print myInstance.x

namespaceTest()

# Class
@newTopic
def classTest():
    '''# Class'''
    class TestClass():
        # self can be renamed to something else
        def __init__(self, a):
            self.a = a
        
        def myPrint(self):
            print self.a

    testClass = TestClass("Hello Class!")
    # self passed in implicitly 
    testClass.myPrint()
    # self passed in explicitly
    TestClass.myPrint(testClass)

    print dir(TestClass)
    print TestClass.__dict__



classTest()
