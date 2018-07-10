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
assert 1 == 2



