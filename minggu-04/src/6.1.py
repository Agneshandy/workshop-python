# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

import fibo

fibo.fib(1000)
fibo.fib2(100)
fibo.__name__

fib = fibo.fib
fib(500)

from fibo import fib, fib2
fib(500)

from fibo import *
fib(500)

import fibo as fib
fib.fib(500)

from fibo import fib as fibonacci
fibonacci(500)

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
    
