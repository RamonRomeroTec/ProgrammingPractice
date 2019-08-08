"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        stack = [(root,1)]
        d=1
        while stack:
            node = stack.pop()
            element = node[0]
            deep = node[1]
            if deep and deep > d:
                d=deep
            if element:
                for n in element.children:
                    stack.append((n, deep+1))
        return d
        