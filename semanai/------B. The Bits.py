from itertools import permutations
s='01011'
a=list(permutations(s, len(s)))
u=set()
'''
5
01011
11001

'''
for i in range(0, len(a)):
    a[i]=''.join(map(str, a[i]))
    u.add(a[i])

for r in u:
    print (s)
    print (r)
    print ("\n")

'''
5
01011 ---> 01011 01011 01011 01011 el numero de 1's y 0s    14 23 34 35
11001       el numero de 0s

11011


'''
