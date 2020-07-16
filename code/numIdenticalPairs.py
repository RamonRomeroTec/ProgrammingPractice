class Solution:
    def numIdenticalPairs(self, nums):
        d={}
        for e in nums:
            if e not in d:
                d[e]=1
            else:
                d[e]+=1
        s=0
        for v in d.values():
            s=s+(((v)*(v-1))//2)
        return s 
            