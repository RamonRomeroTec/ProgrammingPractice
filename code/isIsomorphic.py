class Solution(object):
    def isIsomorphic(self, s, t):
        size = len(s)
        p=0
        d={}
        reviewed=set()
        while p<size:
            if s[p] in d:
                if t[p] != d[s[p]]:
                    return False
            else:
                if t[p] in reviewed:
                    return False
                else:
                    d[s[p]]=t[p]
                    reviewed.add(t[p])
            p+=1
        return True