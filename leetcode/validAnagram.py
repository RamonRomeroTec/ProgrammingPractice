from collections import Counter

class Solution:
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        cs=Counter(s)
        ct=Counter(t)
        if len(cs)!=len(ct):
            return False
        for k,v in cs.items():
            if ct[k]!=cs[k]:
                return False
        return True
