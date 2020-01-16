class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return len(nums)
        
        special=len(set(nums))
        a=0
        b=1
        breaker=nums[a]
        mini=nums[a]
        while a<len(nums)-1:
            while b<len(nums):
                if nums[b]>mini:
                    a=a+1
                    nums[a], nums[b] = nums[b], nums[a]
                    mini = nums[a]  
                else:
                    b=b+1
                if a+1==special:
                    return special
        