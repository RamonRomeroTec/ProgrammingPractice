# Transverse in order and form tree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def getl(root, l):
    if root:
        getl(root.left, l)
        l.append(root.val)
        getl(root.right, l)
    return l

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        nums= getl(root, [])
        nr = TreeNode(nums[0])
        head = nr
        if len(nums)>=1:
            for i in range(1,len(nums)):
                nr.right=TreeNode(nums[i])
                nr=nr.right
        nr.right = None
        return head
            
                
        