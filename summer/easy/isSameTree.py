# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        q1 = deque([q])
        q2 = deque([p])
        l1=-23
        l2=-24
        while q1 and q2:
            n1 = q1.popleft()
            n2 = q2.popleft()
         
            
            if (n2 and n1==None) :
                return False
            elif (n1 and n2==None):
                return False
            elif (n1 and n2):
                if n1.val!= n2.val:
                    return False
            if n1:
                if n1.left:
                    q1.append(n1.left)
                else:
                    q1.append(None)

                if n1.right:
                    q1.append(n1.right)
                else:
                    q1.append(None)

            if n2:
                if n2.left:
                    q2.append(n2.left)
                else:
                    q2.append(None)
                if n2.right:
                    q2.append(n2.right)
                else:
                    q2.append(None)
        if len(q1) != len(q2):
            return False
        return True

        