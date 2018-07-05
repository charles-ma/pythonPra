def fibo(n):
    a, b = 0, 1
    for i in range(0, n):
        t = b
        b += a
        a = t
    return a 

print 'git'