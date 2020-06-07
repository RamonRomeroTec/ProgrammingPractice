from collections import deque
class Solution(object):
    def getImportance(self, employees, id):
        d={}
        for i in employees:
            d[i.id]=(i.importance,i.subordinates)
        q=deque([d[id]])
        s=0
        while q:
            n=q.popleft()
            q+=[ d[i] for i in n[1]]
            s+=n[0]
        return s
        