# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def conv(nums):
    if len(nums)==0:
            return None
    else:
        m=len(nums)//2
        a=TreeNode(nums[m])
        a.left=conv(nums[:m])
        a.right=conv(nums[m+1:])
        return a


class Solution:
    def sortedArrayToBST(self, nums):
        print(nums[:len(nums)//2])
        print(nums[len(nums)//2+1:])
        return conv(nums)



        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
