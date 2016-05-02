# -*- coding: utf-8 -*-
"""
Finds all the possible latice paths in a 20x20 grid
The number of combinations is equal to the binomial coefficient (n + k / n) = n!/k!(n-k)!
Result:137846528820
Runtime:0.0001314848034257056
@author: Gravel
"""
import math
gridSize = [20,20] #height width
def problem15(gridSize):
    n = gridSize[0] + gridSize[1]
    k = gridSize[0]
    return int(math.factorial(n)/(math.factorial(k)*(math.factorial(n-k))))
    
    
