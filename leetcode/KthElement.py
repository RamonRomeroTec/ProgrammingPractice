# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def ior(root):
    a=[]
    if root!=None:
        a=ior(root.left)
        a.append(root.val)
        a=a+ior(root.right)
    return a



class Solution:
    def kthSmallest(self, root, k):
        print(ior(root))
        return ior(root)[k-1]
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
