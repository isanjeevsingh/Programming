#!/bin/python3
#problem statement: https://www.hackerrank.com/challenges/counting-valleys/problem


import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    A, V = 0, 0
    for p in path:
        if p == 'U':
            A += 1
            if A == 0:
                V += 1
        else:
            A -= 1
    return V
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
