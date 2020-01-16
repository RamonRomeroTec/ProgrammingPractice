
# remember pop left != pop

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root:
            q = deque([(root, 1)])
            current = 1
            r = []
            while q:

                x = q.popleft()
                node, level = x[0], x[1]
                if node:
                    if level == 1:
                        l=[node.val]
                    elif level > current:
                        current = level
                        r.append(l)
                        l=[node.val]
                    else:
                        l.append(node.val)
                    for i in node.children:
                        q.append((i,level+1))
            r.append(l)
            return r
        else:
            return None

        
        