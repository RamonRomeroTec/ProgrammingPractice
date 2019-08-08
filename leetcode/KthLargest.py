class Solution(object):
    def findKthLargest(self, nums, k):
        nums=sorted(nums)
        nums=nums[::-1]
        return nums[k-1]
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
