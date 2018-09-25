#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    iambelow=False
    h=0
    v=0

    for i in range(0, len(s)):
        if s[i] == 'U':
            h=h+1
        if s[i] == 'D':
            h=h-1
        if iambelow==True and h>=0:
            v=v+1
            iambelow=False
        if h<0:
            iambelow=True
        else:
            iambelow=False



    return v

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
