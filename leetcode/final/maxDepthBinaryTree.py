# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxDepth(self, root):
        if root==None:
            return 0
        else:
            return 1+max(Solution().maxDepth(root.left), Solution().maxDepth(root.right))



        """
        :type root: TreeNode
        :rtype: int
        """
        
