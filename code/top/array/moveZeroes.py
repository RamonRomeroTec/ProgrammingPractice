class Solution(object):
    def moveZeroes(self, nums):

        current = 0
        for i in range(len(nums)):
            if nums[i]==0:
                for j in range(i, len(nums)):
                    if nums[j]!=0:
                        nums[i],nums[j] = nums[j],nums[i]
                        i=j
                        break
        return nums
                
        