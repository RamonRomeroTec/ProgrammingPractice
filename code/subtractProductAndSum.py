class Solution(object):
    def subtractProductAndSum(self, n):
        p=1
        s=0
        while n:
            d=n%10
            p*=d
            s+=d
            n=n//10
        return p-s
        