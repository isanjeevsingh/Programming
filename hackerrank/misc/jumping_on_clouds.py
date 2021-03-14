#!/bin/python3
# Problem statement: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    current = 0
    while current < len(c)-1:
        jumps += 1
        if current + 2 <= len(c)-1 and c[current + 2] == 0:
            current += 2
        else:
            current += 1
    return jumps
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
