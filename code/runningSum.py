class Solution(object):
    def runningSum(self, nums):
        a=sum(nums)
        r=[0]*len(nums)
        r[-1]=a
        for i in range(len(nums)-2, -1, -1):
            r[i]=r[i+1]-nums[i+1]
        return r
        