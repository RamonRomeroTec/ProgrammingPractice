# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
from collections import deque

class Solution:
    def levelOrder(self, root):
        q=deque([])
        r=[]
        if root == None:
            return r
        q.append(root)
        while(len(q)>0):
            size=len(q)
            l=[]
            for i in range(size):
                a=q.popleft()
                l.append(a.val)
                if a.left!=None:
                    q.append(a.left)
                if a.right!=None:
                    q.append(a.right)
            r.append(l)
        return r



        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
