"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        return self.aux(root, [])
    
    def aux(self, root, l):
        if root:
            if root.children:
                for i in root.children:
                    self.aux(i,l)
            l.append(root.val)
        return l
        