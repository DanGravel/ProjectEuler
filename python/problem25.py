# -*- coding: utf-8 -*-
"""
Returns the index of the first term in the fibonacci sequence that contains 1000 digits
Result: 4782
Runtime: 0.03286910057067871

@author: Gravel
"""
def problem25():
    f =  fib()
    index = 1    
    while True:
        fibonacciNum= next(f)
        if len(str(fibonacciNum)) >= 1000:
            return index
        index += 1
        
"""
Fibonacci number generator
"""   
def fib():
    a,b = 0,1
    while True:
        a,b = b, a+b
        yield a
