# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :type target: int
        :rtype: bool
        """
        s1=[root1]
        s2=[root2]
        a=set()
        b=set()
        while s1:
            n1=s1.pop()
            a.add(n1.val)
            if n1.left:
                s1.append(n1.left)
            if n1.right:
                s1.append(n1.right)
                
        while s2:
            n2=s2.pop()
            b.add(n2.val)
            if n2.left:
                s2.append(n2.left)
            if n2.right:
                s2.append(n2.right)
                
                
        for e in a:
            if target-e in b:
                return True
        return False
            
        