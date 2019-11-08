class Solution(object):
    def minDiffInBST(self, root):
        def inorder(root):
            a=[]
            if root!=None:
                a = inorder(root.left)
                a.append(root.val)
                a=a+inorder(root.right)
            return a
        a=inorder(root)
        mini=float('+inf')
        for e in range(len(a)-1):
            mini=min(mini,abs(a[e]-a[e+1]))
        return mini
            
            
        