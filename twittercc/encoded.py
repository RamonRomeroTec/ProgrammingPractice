#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'decode' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY codes
#  2. STRING encoded
#

def decode(codes, encoded):
    a={}
    for i in codes:
        k,v=i.split('\t')
        if k=='[newline]':
            a[v]='\n'
        else:
            a[v]=k

    r=""
    n=len(encoded)
    i=0
    j=1
	#the prefix is the validation
    while i<n:
        if encoded[i:j] in a:
            r=r+a[encoded[i:j]]
            i=j
        else:
            j=j+1
    return r
'''
an access by using a dictionary, will reduce the iterations in the prefix, O(1)
it is only necessary to take in consideration the hashing time/ hashing function

def decode(codes, encoded):
    a={}
    for i in codes:
        k,v=i.split('\t')
        if k=='[newline]':
            a[v]='\n'
        else:
            a[v]=k
    l=0
    r=""
    while l<len(encoded):
        sli=encoded[l:l+6]
        #print(sli, l,size)
        r=r+a[sli]
        l=l+6

    return r


'''
if __name__ == '__main__':
