
# learn formula for mismatch
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = set()
        b=set([i for i in range(1, len(nums)+1)])
        for i in nums:
            if i not in a:
                a.add(i)
            else:
                sumx=sum(set(nums))
                ans= (len(nums)*(len(nums)+1)/2) - sumx
                return i,ans
                
            
        