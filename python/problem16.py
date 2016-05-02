# -*- coding: utf-8 -*-
"""
Calculates the sume of the digits of the numer 2^1000
Result: 1366
Runtime: 0.0018122035951364523
@author: Gravel
"""

def problem16():
    num = 2**1000
    num = list(map(int, list(str(num))))
    return sum(num)
    
