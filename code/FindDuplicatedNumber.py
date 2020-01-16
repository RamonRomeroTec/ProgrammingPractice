from collections import Counter

class Solution:
    def findDuplicate(self, nums):
        a=Counter(nums)
        for k,v in a.items():
            if v>=2:
                return k


        """
        :type nums: List[int]
        :rtype: int
        """
