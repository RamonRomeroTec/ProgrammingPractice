# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def removeLeafNodes(self, root,target) :
        
        chosen=[]
        q=deque([(root, None)])
        while q:
            node, father =q.popleft()
            if node.val==target:
                chosen.append((node, father))
            if node:
                if node.left:
                    q.append((node.left, node))
                if node.right:
                    q.append((node.right, node))
        for i in range(len(chosen)-1, -1, -1):
            nodex, parent = chosen[i][0], chosen[i][1]
            if not nodex.left and not nodex.right:
                if not parent:
                    return None
                if parent.left is nodex:
                    parent.left=None
                else:
                    parent.right=None
        return (root)
        