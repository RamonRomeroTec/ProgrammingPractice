# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


        
def searchT(root, l, ):
    if root:
        if root.left:
            searchT(root.left, l)
        l.append(root.val)
        if root.right:
            searchT(root.right, l)
    return l

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        l = searchT(root, [])
        mini = 1000
        for i in range(1,len(l)):
            evaluate = abs(l[i]-l[i-1])
            if evaluate < mini:
                mini = evaluate
            
            
        return mini
        