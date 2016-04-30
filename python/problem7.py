import math

"""
Finds the 10 001 st prime
"""
def problem7():
    primes = primeSeive(1000000) #finds all primes under a million
    return primes[10000]


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

