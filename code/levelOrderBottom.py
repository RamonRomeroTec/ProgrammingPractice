from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []
        q=deque([root])
        ans=[]
        while q:
            a=len(q)
            aux=[]
            for i in range(a):
                n=q.popleft()
                if n:
                    aux.append(n.val)
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
            ans.append(aux)
        return ans[::-1]

