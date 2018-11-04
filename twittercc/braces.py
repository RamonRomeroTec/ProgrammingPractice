#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the braces function below.
def braces(values):
	opens={'{', '[', '('}
	closes={'}':'{',']':'[', ')':'('}
	r=[]
	for t in values:
		s=[]
		u=[]
		for i in range(len(t)):
			if t[i] in opens:
				s.append(t[i])
			if t[i] in closes:
				try:
					if s[-1]==closes[t[i]]:
						s.pop()
				except Exception as e:
					u.append(t[i])
		if len(s)==0 and len(u)==0:
			r.append('YES')
		else:
			r.append('NO')


	return r

if __name__ == '__main__':
