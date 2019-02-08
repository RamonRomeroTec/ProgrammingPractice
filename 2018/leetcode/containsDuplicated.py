class Solution:
    def containsDuplicate(self, nums):
        a=set()
        for i in nums:
            a.add(i)
        if len(a)==len(nums):
            return False
        return True

        """
        :type nums: List[int]
        :rtype: bool
        """
