

def multArray(arr):
    r=1
    for i in arr:
        r=r*i
    return r
class Solution:
    def productExceptSelf(self, nums):
        a=[0]*len(nums)
        for i in range(len(nums)):
            left=multArray(nums[:i])
            right=multArray(nums[i+1:])
            a[i]=(left*right)
        return a
