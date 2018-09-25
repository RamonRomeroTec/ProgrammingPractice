#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    clouds=0
    i=0
    while i< len(c):
        print(i,(c[i]))
        if( i+2 < len(c) and c[i+2]==0):
            clouds=clouds+1
            i=i+2
        else:
            i=i+1
            clouds=clouds+1

    return clouds-1 #Ya estas contando un salto

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
