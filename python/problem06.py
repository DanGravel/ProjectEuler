"""
Finds the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

@author: Daniel Gravel
"""
def problem6():
    sumSquare = 0
    squareSum = 0    
    for i in range(1,101):
        sumSquare += i**2
        squareSum += i
    squareSum = squareSum**2
    return squareSum - sumSquare
    