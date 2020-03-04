import bisect 
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        a=nums[:]
        a=sorted(a)
        return [bisect.bisect_left(a, i) for i in nums]
        