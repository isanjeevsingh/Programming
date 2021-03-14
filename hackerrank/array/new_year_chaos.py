#!/bin/python3
# Problem Statement: https://www.hackerrank.com/challenges/new-year-chaos/problem

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes=0
    for i in range(len(q)):
        if q[i] - i - 1 > 2:
            #print("Too chaotic")
            return "Too chaotic"
        for j in range(max(q[i]-2,0),i):
            if q[j]-1 > q[i]-1:
                bribes += 1            
    #print(bribes)
    return bribes

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
