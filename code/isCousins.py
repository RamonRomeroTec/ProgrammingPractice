from collections import deque
class Solution(object):
    def isCousins(self, root, x, y):
        q=deque([(root, None)])
        d={}
        curr_level=1
        while q:
            aux=len(q)
            for i in range(aux):
                n, p =q.popleft()
                if n:
                    d[n.val]=(curr_level, p)
                    if n.left:
                        q.append((n.left, n.val))
                    if n.right:
                        q.append((n.right, n.val))
            curr_level+=1
        try:
            if d[x][0]==d[y][0]:
                if d[x][1]!=d[y][1]:
                    return True
            return False
        except e:
            return False
        