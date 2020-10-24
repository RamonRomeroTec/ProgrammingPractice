class Solution:
    def findSmallestSetOfVertices(self, n, edges):
        a=set()
        des=set(d for o,d in edges)
        for o,d in edges:
            if o not in des:
                a.add(o)
        return list(a)
    
        