"""
Finds the largest palindrome made from the product of two 3-digit numbers.
"""

def problem4():
    largest = 0
    for i in reversed(range(100, 999)):
        for j in reversed(range(100, 999)):
            if palindrome(i*j) and i*j > largest:
                largest = i*j    
    return largest
                
def palindrome(num):
    return str(num) == str(num)[::-1]
    
