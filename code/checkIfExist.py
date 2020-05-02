class Solution(object):
    def checkIfExist(self, arr):
        d={}
        for v in (arr):
            if (v%2==0 and v//2 in d) or v*2 in d:
                return True
            d[v]=True
        return False
        