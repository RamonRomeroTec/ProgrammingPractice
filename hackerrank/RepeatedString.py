#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    m1=s.count("a")
    m2=int(n/len(s))
    r=n%len(s)
    ans=m1*m2
    if r!=0:
        ans=ans+s[0:r].count("a")

    return ans






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
