"""
Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000
Result:[9, 1, 1, 0, 8, 4, 6, 7, 0, 0]
Runtime:0.009025335311889648
@author: Gravel
"""
def problem48():
    number = 0
    for i in range(1000):
        number += i**i
    number = list(map(int,str(sum)))
    return number[-10:]
