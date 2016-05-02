import math
"""
Finds the first triangular number that has 500 or more factors

@author: Gravel
"""

def problem12():
    for i in range(100000):
        triangle = int((i*(i + 1))/2)  #equation to get a tria 
        if divisors(triangle) > 500:
            return triangle
    
    
"""
Finds the number of divisors in a given number
"""
def divisors(num):
    factors = 0
    
    for i in range(1,int(math.sqrt(num) + 1)):
        if num % i == 0:
            factors += 2
        if i*i == num:
            factors -= 1
    return factors
   
