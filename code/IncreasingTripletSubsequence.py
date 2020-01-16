class Solution:
    """
    @param nums: a list of integers
    @return: return a boolean
    """
    def increasingTriplet(self, nums):
        a=[]
        for i in range(len(nums)):
            if nums[i] not in a:
                a.append(nums[i])


        for i in range(len(a)-2):
            if a[i]<a[i+1] and a[i+1]< a[i+2]:
                return True
        return False

        # write your code
