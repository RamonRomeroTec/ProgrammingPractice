class Solution(object):
    def xorOperation(self, n, start):
        a=0
        for i in range(n):
            a=a^(start+2*i)
        return a
        
        