#!/bin/python3
# Problem statement: https://www.hackerrank.com/challenges/sock-merchant/problem

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    prev, pairs = None, 0
    for a in ar:
        if a == prev:
            pairs+=1
            prev = None
        else:
            prev = a
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
