class Solution(object):
    def findNumbers(self, nums):
        c=0
        for num in nums:
            if len(str(num))%2==0:
                c+=1
        return c
        