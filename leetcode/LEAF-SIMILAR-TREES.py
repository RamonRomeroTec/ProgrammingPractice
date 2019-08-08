# DEPTH SEARCH


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def getArr(root1):
    stack = [root1]
    arr1=[]
    while stack:
        node = stack.pop()
        if node:
            if not node.right and not node.left:
                arr1.append(node.val)
            else:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
    return(arr1)
    
class Solution(object):

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        A = getArr(root1)
        B = getArr(root2)
        if len(A) != len(B):
            return False
        else:
            for i in range(len(A)):
                if A[i] != B[i]:
                    return False
            return True
        
            
        
        