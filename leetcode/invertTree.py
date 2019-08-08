# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.right, node.left = node.left, node.right
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return root
        
        