# -*- coding: utf-8 -*-
"""
Evaluate the sum of all the amicable numbers under 10000.
Result: 31626
Runtime: 0.22074365615844727
@author: Gravel
"""
import math


def problem21():
     total = 0
     for i in range(1,10000):
         first = sum(divisors(i))
         second = sum(divisors(first))
         if second == i and first != second:
             total += i
     return total

def divisors(num):
    divisors = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num%i == 0:
            if(i != num/i and num != num/i):
                divisors.append(i)
                divisors.append(int(num/i))
            else:
                divisors.append(i)
    return divisors

