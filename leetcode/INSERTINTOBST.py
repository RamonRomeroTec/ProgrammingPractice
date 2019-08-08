# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.val<val:
                    if not node.right:
                        node.right = TreeNode(val)
                        break
                    else: 
                        stack.append(node.right)
                if node.val>val:
                    if not node.left:
                        node.left = TreeNode(val)
                        break
                    else:
                        stack.append(node.left)
        return root
                    
        