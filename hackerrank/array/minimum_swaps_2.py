#!/bin/python3
# Problem Statement: https://www.hackerrank.com/challenges/minimum-swaps-2/problem

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps=0
    H = {v:i for i,v in enumerate(arr)}
    for i, x in enumerate(arr):
        if x != i+1:
            t = arr[H[i+1]]
            arr[H[i+1]] = x
            arr[i] = t
            H[x] = H[i+1]
            swaps += 1
    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
