class Solution(object):
    def removeElement(self, nums, val):
        if not nums:
            return 0
        if len(nums)==1:
            if nums[0]==val:
                nums = []
                return 0
            else:
                return 1
        left = 0
        right = len(nums)-1
        while nums[right]==val:
            right-=1
            if right<0:
                nums=[]
                return 0
        while left < right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                left +=1
                while nums[right]==val:
                    right-=1
            else:
                left+=1
        nums=nums[:right+1]
        return right+1