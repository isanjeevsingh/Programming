#!/bin/python3
#Problem statement: https://www.hackerrank.com/challenges/repeated-string/problem

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def counta(s):
    cnt = 0
    for c in s:
        if c == 'a':
            cnt += 1
    return cnt
    
def repeatedString(s, n):
    lc = len(s)
    if n < lc:
        return counta(s[:n])
    else:
        return counta(s)*(n//lc) + counta(s[:n%lc])
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
