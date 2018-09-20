"""
OK
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of complete binary tree
    @return: the number of nodes
    """

    def countNodes(self, root):
        s=Solution()

        count = 1
        if root != None:
            if root.left != None:
                count += s.countNodes(root.left)
            if root.right != None:
                count += s.countNodes(root.right)
        return count
        '''
        s=Solution()
        if root==None:
            return 0
        if root.right!=None:
            return 1+ s.countNodes(root.right)
        if root.left!=None:
            return 1+ s.countNodes(root.left)
        '''
        # write your code here
