class Solution(object):
    def anagramMappings(self, A, B):
        d={}
        for i,v in enumerate(B):
            d[v]=i
        return [d[x] for x in A]
            
        