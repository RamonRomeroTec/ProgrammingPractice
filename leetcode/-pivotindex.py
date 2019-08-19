class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
      
        l = 0
        r = sum(nums[1:])
        index = 0
        while index < len(nums):
            if l == r:
                return index
            else:
                l=l+nums[index]
                try:
            
                    r=r-nums[index+1]
                except:
                    return -1
            index+=1
            
        return -1
      