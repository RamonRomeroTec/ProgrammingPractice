def binS1(nums, left, right, target):
    middle=(left+right)//2
    if left>right:
        return -1
    if middle+1 == len(nums) or nums[middle]==target:
        if nums[middle-1]<target:
            return middle
        else:
            return binS1(nums,left,middle-1, target)
    elif nums[middle]<target: #right
        return binS1(nums,middle+1,right, target)
    elif target<nums[middle]: #left
        return binS1(nums,left,middle-1, target)
def binS2(nums, left, right, target):
    middle=(left+right)//2
    if left>right:
        return -1
    if nums[middle]==target:
        if middle+1 == len(nums) or nums[middle+1]>target:
            return middle+1
        else:
            return binS2(nums,middle+1,right, target)
    elif nums[middle]<target: #right
        return binS2(nums,middle+1,right, target)
    elif target<nums[middle]: #left
        return binS2(nums,left,middle-1, target)
            
class Solution(object):
    def isMajorityElement(self, nums, target):
        return len(nums)//2 < (binS2(nums, 0, len(nums)-1, target)-binS1(nums, 0, len(nums)-1, target))

