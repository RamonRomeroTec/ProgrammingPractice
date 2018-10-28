from itertools import combinations

class Solution:
    def subsets(self, nums):
        r=[]
        for i in range(len(nums)+1):
            a=list(combinations(nums, i))
            r=r+a
        return r
