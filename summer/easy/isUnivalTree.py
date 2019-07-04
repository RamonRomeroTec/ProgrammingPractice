# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = [root]
        s={root.val,None}
        while stack:
            node = stack.pop()
            if node:
                if node.val not in s:
                    return False
                stack.append(node.right)

                stack.append(node.left)

        return True
        