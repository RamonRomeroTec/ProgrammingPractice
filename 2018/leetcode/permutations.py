from itertools import permutations


class Solution:
    def permute(self, nums):
        a=list(permutations(nums, len(nums)))
        return sorted(a )
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
