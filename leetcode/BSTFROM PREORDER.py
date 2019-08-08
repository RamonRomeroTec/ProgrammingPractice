# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque


def splt(preorder, bp):
    if preorder:
        if len(preorder)==1:
            if preorder[0]>bp:
                return [], [preorder[0]]
            else:
                return [preorder[0]], []
        i=1
        while i < (len(preorder)):
            if preorder[i]>bp:
                break
            i+=1
        
        
        l, r = preorder[:i], preorder[i:]
      
        return l, r
    else:
        return [],[]
    
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        l, r = splt(preorder[1:], root.val)
        print(l,r)
        if len(l)==1:
            if l[0]>root.val:
                root.right = self.bstFromPreorder(l)
        if len(r)==1:
            if r[0]<root.val:
                root.left = self.bstFromPreorder(r)

        else:
            root.left = self.bstFromPreorder(l)
            root.right = self.bstFromPreorder(r)
        return root
        


# ujç= Solution().bstFromPreorder([8,5,1,7,10,12])

ujç= Solution().bstFromPreorder([1,2,3])

print('kkk')
        



     