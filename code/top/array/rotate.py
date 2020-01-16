class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        nums[:] = nums[n-k:] + nums[:n-k]
        