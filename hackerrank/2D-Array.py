#!/bin/python3

import math
import os
import random
import re
import sys


def suma(arr,y,x):
    suma=arr[y-1][x-1]+arr[y-1][x]+arr[y-1][x+1]+arr[y+1][x-1]+arr[y+1][x]+arr[y+1][x+1]+arr[y][x]
    return suma

# Complete the hourglassSum function below.
def hourglassSum(arr):
    s=-99999
    for i in range(1,5):
        for j in range(1,5):
            s=max(s,suma(arr,i,j))
    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
