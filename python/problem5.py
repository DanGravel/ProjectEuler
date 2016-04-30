"""
Finds the smallest positive number that is evenly divisible by all numbers between 1 to 20
@author: Daniel Gravel
"""

def problem5():
    smallest = 20
    
    while True:
        if isMultiple(smallest):
            return smallest
        smallest += 20
            
def isMultiple(num):
    for i in range(1,20):
        if num%i != 0:
            return False
    return True
    
