'''
Note: Slice notation and sum methods for lists. Such as 
        sort, sum, min, max

'''


class Solution(object):
    def arrayPairSum(self, nums):
        # nums=sorted(nums)
        # s=0
        # for i in range(0,len(nums), 2):
        #    s=s+nums[i]
        # return s
        nums.sort()
        return sum(nums[::2])
