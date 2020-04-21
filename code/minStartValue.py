class Solution:
    def minStartValue(self, nums):
        m=float(1000000)
        s=0
        for n in nums:
            s+=n
            m=min(s,m)
        if m>=0:
            return 1
        else:
            return abs(m)+1
        