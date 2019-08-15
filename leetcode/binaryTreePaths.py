# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return None
        stack = [(root, [str(root.val)])]
        ans = []
        while stack:
            x = stack.pop()
            node, path = x[0], x[1]
            if node:
                #print(node.val, path)
                if not node.right and not node.left:
                    ans.append(path)
                    
                
                if node.right:
                    aux = path[:]
                    aux.append("->"+str(node.right.val))
                    stack.append((node.right, aux ))
                    
                if node.left:
                    aux = path[:]
                    aux.append("->"+str(node.left.val))
                    stack.append((node.left, aux))
                    
        return(["".join(x) for x in ans])


                    
            
        