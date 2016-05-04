"""
Calculates the total of all the name scores in a given file
Result: 871198282
Runtime: 0.014384031295776367
@author: Gravel
"""
OFFSET = ord('A') - 1
def problem22():
    file = open("p022_names.txt", "r")
    #reads file and splits at ',' and strips all double quotations then sorts the list alaphbetically
    names = sorted(file.read().replace('"', "").split(','))
    return sum(getNameScore(names[pos], pos + 1) for pos in range(len(names)))
"""
Returns the score of a name where each letter has a value ie A = 1 ...
The score is the sum of the letter values multiplied by the postion in the sorted list
"""
def getNameScore(name, position):
    return sum(ord(char) - OFFSET for char in list(name)) * position
