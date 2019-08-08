class Solution:
    def missingNumber(self, nums):
        a=set(nums)
        for i in range(len(nums)+1):
            if i not in a:
                return i
        """
        :type nums: List[int]
        :rtype: int
        """
