'''

Given a string s, find and return the first
instance of a non-repeating character in it.
If there is no such character, return '_'.
'''

from collections import Counter
def firstNotRepeatingCharacter(s):
    a=Counter(s)
    n=[]
    for k,v in a.items():
        if v==1:
            n.append(s.find(k))
    if len(n)==0:
        return '_'
    else:
        return (s[sorted(n)[0]])

   
