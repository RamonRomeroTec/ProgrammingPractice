# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return self.val

def trimBST( root, L, R):
    """
    :type root: TreeNode
    :type L: int
    :type R: int
    :rtype: TreeNode
    """
    stack = [(root, None)]
    while stack:
        node, parent = stack.pop()
        if node:
            if node.val == L: 
                node.left  = None
            elif node.val < L: 
                if node.right:
                    parent.left = node.right 
            if node.val == R:
                node.right = None
            elif node.val > R:
                if node.left:
                    parent.right = node.left 
            if node.left:
                stack.append((node.left, node))
            if node.right:
                stack.append((node.right, node))
    return root
    
    
    '''
    # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
def trimBST(self, root, L, R):
    """
    :type root: TreeNode
    :type L: int
    :type R: int
    :rtype: TreeNode
    """
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            print(node.val)
            if node.val < L: 
                if node.right:
                    node, node.right = node.right, node
            elif node.val == L:
                node.right  = None
                
                
            if node.val > R:
                if node.left:
                    node, node.left = node.left, node
            elif node.val == R: 
                node.left  = None
            print(root)
                
                
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
    print(root,'ss')
    return root
    '''


root = TreeNode(3)
root.left=TreeNode(0)
root.right=(TreeNode(4))
a=root
a=root.left
a.right=(TreeNode(2))
a=a.right
a.left=(TreeNode(1))
trimBST(root, 1,3)
