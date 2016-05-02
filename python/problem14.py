# -*- coding: utf-8 -*-
"""
Finds the starting number that produces the longest Collatz sequence
Result: 837799
Runtime: 53.66977643966675

@author: Gravel
"""

def problem14():
    longestChain = 0
    startingNumber = 2
    for i in range(2,1000000):
        temp = i
        chain = 0
        while temp != 1:
            if temp%2 == 0:  #even
                temp = int(temp/2)
                chain += 1
            else:            #odd
                temp = int(3*temp + 1)
                chain += 1
        chain += 1          #every sequence ends with 1 so add one at the end of every sequence
        if(chain > longestChain):
            longestChain = chain
            startingNumber = i
    return startingNumber
    