def op(n, d):
    k=n
    c=0
    while n!=1:
        if n in d:
            return c+d[n]
        if n % 2==0:
            n = n//2
        else:
            n = 3 * n + 1
        c+=1
    d[k]=c
    return d[k]

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        aux={}
        return sorted(range(lo,hi+1), key=lambda x:op(x, aux))[k-1]
        