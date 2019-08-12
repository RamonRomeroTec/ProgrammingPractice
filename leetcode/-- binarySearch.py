
def magia(nums, begin, end, target):
    middle=(begin + end)//2
    if begin > end:
        return -1
    if target == nums[middle]:
        return middle
    elif nums[middle] > target: #move left
        return magia(nums, begin, middle-1, target)
    else: # move right
        return magia(nums, middle+1, end, target)
    
    
    
    
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return (magia(nums, 0, len(nums)-1, target))
        #try:
        #    return nums.index(target)
        #except:
        #    return -1
        
        