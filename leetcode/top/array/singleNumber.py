class Solution(object):
    def singleNumber(self, nums):
        return (2*(sum(list(set(nums)))))-sum(nums)
        