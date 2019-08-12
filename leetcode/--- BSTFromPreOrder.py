
from collections import deque
def splt(preorder, bp):
    if preorder:
        i=0
        while i< len(preorder):
            if preorder[i] > bp:
                break
            i+=1
        l= preorder[:i]
        r= preorder[i:]
        return l,r
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
        root = TreeNode(preorder.pop(0))
        l, r = splt(preorder, root.val)
        root.left = self.bstFromPreorder(l)
        root.right = self.bstFromPreorder(r)
        return root