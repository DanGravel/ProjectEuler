import math
"""
Finds the largest divisible prime in a number
"""
def problem3(factor):
    prime = primeSeive(int(math.sqrt(factor)))
    largestfactor = 1
    tempfactor = factor    
    
    for i in range(0, len(prime)):
        if(tempfactor % prime[i] == 0):
            largestfactor = prime[i]
            #find the lowest divisible number from the prime
            while(tempfactor % prime[i] == 0):
                tempfactor /= prime[i]
        #if prime is larger then number you have gone to far        
        if(prime[i] > tempfactor): 
            return largestfactor
            
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
    
