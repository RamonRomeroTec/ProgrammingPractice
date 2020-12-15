class Solution:
    def countConsistentStrings(self, allowed, words):
        d1=set(allowed)
        c=0
        for i in words:
            sp= set(i) - d1
            if len(sp)==0:
                c+=1
        return c
        