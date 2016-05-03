# -*- coding: utf-8 -*-
"""
Counts the number of letters in the numbers from 1 to 1000
@author: Gravel
"""

S = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen",]
D = ["","teen","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
Hundred = 7
Thousand = 8

def problem17():
    total = 0    
   
    for i in range(1,1000):
        ones = S[i%10] if i % 100 > 20 else S[0]
        tens = S[int(i%100)] if i % 100 < 20  else D[int((i%100)/10)]
        hundreds = S[int(i/100)] if int(i/100) != 0 else S[0]
        
        if i < 10:
            total += len(tens)
            #print(tens)
        elif i < 20:
            total += len(tens)
            #print(tens)
        elif i < 100:
            total += len(tens) + len(ones)
            #print("%s %s" % (tens, ones))
            
        elif i < 1000:
            total += len(hundreds) + len(tens) + len(ones) + Hundred + 3
            #print("%s hundred %s %s" % (hundreds ,tens, ones))
    print(total)
    
problem17()