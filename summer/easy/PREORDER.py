

# the input access differs if the procedure is done by a manual stack or by recursive stack


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""



class Solution(object):
    
    
    
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
    
        return self.second(root, [])
    
    def second(self, root, l):
        if root:
            l.append(root.val)
            if root.children:
                for i in root.children:
                    self.second(i, l)
        return l