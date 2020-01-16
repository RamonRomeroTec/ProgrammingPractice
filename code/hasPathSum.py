# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            x = stack.pop()
            node, val =  x[0], x[1]
            if node:
                if not node.right and not node.left and val == sum:
                    return True
                if node.right:
                    stack.append((node.right, val+node.right.val))
                if node.left:
                    stack.append((node.left, val+node.left.val))
        return False
                
        