import math
"""
Sum of all primes under 2 million
"""
def problem10():
    prime = primeSeive(2000000)  
    total = 0      #didnt use sum() as it kept giving a TypeError
    for i in prime:
        total += i
    return total
"""
Returns a list of primes using the sieve of Eratosthenes
"""
def primeSeive(sieveSize):
    sieve = [True]*sieveSize    
    sieve[0] = False #Zero and one are not prime
    sieve[1] = False
    
    for i in range(2, int(math.sqrt(sieveSize)) + 1):
        pointer = i * 2
        while pointer < sieveSize:
            sieve[pointer] = False
            pointer += i
    
    primes = []
    for i in range(sieveSize):
        if sieve[i] == True:
            primes.append(i)
    return primes

