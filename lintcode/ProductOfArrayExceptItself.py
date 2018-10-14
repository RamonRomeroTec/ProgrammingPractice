class Solution:
    """
    @param nums: an array of integers
    @return: the product of all the elements of nums except nums[i].
    """
    def productExceptSelf(self, nums):
        m=1
        r=[]
        for i in nums:
            m=m*i
        for i in nums:
            if i==0:
                r.append(0)
            else:
                r.append(int(m/i))
        return r
            
