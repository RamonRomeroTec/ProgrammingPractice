class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        c=0
        maxi=0
        for i in nums:
            if i==0:
                c=0
            else:
                c=c+1
                if c>maxi:
                    maxi=c
        return maxi
    
    
        """
        :type nums: List[int]
        :rtype: int
        """
        