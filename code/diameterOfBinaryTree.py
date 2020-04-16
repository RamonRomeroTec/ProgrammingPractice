class Solution:
    def getmax(self, n):
        s=[(n,1)]
        mp=0
        while s:
            n,p=s.pop()
            mp=max(mp,p)
            if n:
                if n.right:
                    aux=p+1
                    s.append((n.right,aux))
                if n.left:
                    aux=p+1
                    s.append((n.left,aux))
        return mp
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        s=[root]
        mx=0
        while s:
            x=s.pop()
            if x:
                a=0
                b=0
                if x.right:
                    a=self.getmax(x.right)
                    s.append(x.right)
                if x.left:
                    b=self.getmax(x.left)
                    s.append(x.left)
                mx=max(mx,(a+b))
            
        return mx
