# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#Output array
def inorder(root):
    a=[]
    if root!=None:
        a = inorder(root.left)
        a.append(root.val)
        a=a+inorder(root.right)
    return a



class Solution:
    def inorderTraversal(self, root):
        return inorder(root)

        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
