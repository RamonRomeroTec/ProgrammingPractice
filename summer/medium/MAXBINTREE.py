# SIMPLIFICA A FUNCIONES 


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        
        """
        
  
        if not nums:
            return
        root = TreeNode(max(nums))
        left, right = spl(root.val, nums)
        root.left = self.constructMaximumBinaryTree(left)
        root.right = self.constructMaximumBinaryTree(right)
        return root

def spl( root,nums):
	if not nums:
		return ([],[])
	index = nums.index(root)
	return (nums[:index], nums[index+1:])
        

        
        