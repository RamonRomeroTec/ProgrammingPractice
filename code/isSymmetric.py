# USE SEARCH BY LEVELS


from collections import deque
class Solution(object):
    def isSymmetric(self, root):
        q=deque([root])
        while q:
            aux=len(q)
            ev=[]
            for i in range(aux):
                node = q.popleft()
                if node:
                    ev.append(node.val)
                    if node.left:
                        q.append(node.left)
                    else:
                        q.append(None)
                    if node.right:
                        q.append(node.right)
                    else:
                        q.append(None)
                else:
                    ev.append('x')
            if len(ev)>1:
                if (ev[:len(ev)//2] != ev[len(ev)//2:][::-1]):
                    return False
        return True

