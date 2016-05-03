
"""
Calculates the sum of the digits in 100!
Result: 648
Runtime: 0.0005011558532714844

@author: Gravel
"""
import math

def problem20():
    factorial = math.factorial(100)
    factorial = list(map(int,list(str(factorial)))) #converts int to string array then maps each value in the number to an int in an array
    return sum(factorial)
    