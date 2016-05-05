
"""
Finds the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9
Result: 2783915460
Runtime: 0.14940142631530762
@author: Gravel
"""
import itertools

numbers = [0,1,2,3,4,5,6,7,8,9]
def problem24():
    combo = itertools.permutations(numbers)
    for i in range(0,1000000):
        permutation = next(combo)
    return permutation


     