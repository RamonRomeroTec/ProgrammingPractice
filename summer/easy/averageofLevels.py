# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        init=0
        q = deque([(root,init)])
        ans=[]
        d={}
        while q:
            node, level = q.popleft()
            if node:
                if level not in d:
                    d[level] = [node.val]
                else:
                    d[level].append(node.val)
                if node.left:
                    q.append((node.left, level+1))
                if node.right:
                    q.append((node.right, level+1))
        return [float(sum(data)/float(len(data))) for data in d.values()]
                    