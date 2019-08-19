def binSearch(nums, begin, end):
    mid = (begin+end)//2
    if mid -1 >= 0 and nums[mid-1] == nums[mid]:
        if mid % 2 == 1:
            return binSearch(nums, mid+1, end)
        else: 
            return binSearch(nums, begin, mid-1)
    elif mid+1 < len(nums) and  nums[mid+1] == nums[mid]:
        if mid%2 ==0:
            return binSearch(nums, mid+1, end)
        else: 
            return binSearch(nums, begin, mid-1)
    else:
        return nums[mid]



class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return binSearch(nums, 0 , len(nums))
        