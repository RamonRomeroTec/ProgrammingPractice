# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        stack =[root]
        s=0
        while stack:
            node = stack.pop()
            if node:
                if node.left and  not node.left.right and  not node.left.left:
                    #print('>',node.val,node.left.val)
                    s+=node.left.val
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return  s