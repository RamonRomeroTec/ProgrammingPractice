#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
from collections import Counter
def checkMagazine(magazine, note):
    m=Counter(magazine)
    for i in range(0, len(note)):
        if note[i] not in m:
            return "No"
        if note[i] in m and m[note[i]]<=0:
            return "No"
        elif note[i] in m and m[note[i]]>0:
            m[note[i]]=m[note[i]]-1


    return "Yes"


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(    checkMagazine(magazine, note))
