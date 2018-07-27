import math
from sys import argv
#write a program that calculates and prints the value according to a given formula
#Q = Square root of [(2 * C * D)/H]
#the fixed values of C and H: C = 50 and H = 30.
#d is the param whose values should be passed in as comma-separated sequence
#Ex: following comma separated input sequence is given to the program: 100,150,180
#The output of the program should be: 18,22,24


def calculate_sqrt(*d):
    """
    input: integers
    output: list of equation values
    """
    c = 50
    h = 30
    result = []
    
    for num in d:
        equation = math.sqrt((2 * num * c)/h)
        result.append(int(equation))
    
    print result


calculate_sqrt(100,150,180, 129, 234, 456, 12, 456)

