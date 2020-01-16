
def binarySearch(nums, begin, end , target):
    if begin - end == 1:
        return begin
    middle = (begin+end)//2
    if nums[middle] == target:
        return middle
    elif target < nums[middle] : #left
        return binarySearch(nums, begin, middle -1, target)
    else:
        return binarySearch(nums, middle +1, end, target)
        


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target <= nums[0]:
            return 0
        return binarySearch(nums, 0, len(nums)-1, target)
        
        