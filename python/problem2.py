"""
Finds the sum of all even fibonacci numbers up to the given limit
@author: Gravel
"""
def problem2(limit):
    sum = 0
    a,b = 1, 1
    while a <= limit:
        if a % 2 == 0:
            sum += a
        a, b = b, a+b
    print(sum)
    return(sum)
        
