class Solution:
    def numberOfMatches(self, n: int) -> int:
        return self.aux(n, 0)
    
    def aux(self, n, s):
        if n==1:
            return s
        if n%2 == 1:
            n=n//2
            s+=n
            n=n+1
            return self.aux(n, s)
        else:
            n=n//2
            s+=n
            return self.aux(n, s)
        