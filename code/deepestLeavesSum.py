from collections import deque
class Solution(object):
    def deepestLeavesSum(self, root):
        q=deque([root])
        while q:
            l=len(q)
            s=0
            for i in range(l):
                current=q.popleft()
                s+=current.val
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
        return (s)


                    
                
        