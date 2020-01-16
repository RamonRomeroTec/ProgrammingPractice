
from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        class Node():
            def __init__(self, xz,yz, maxw, maxh, empty):
                self.key = (xz,yz)
                self.sides = [t for t in [(xz+1, yz), 
                                          (xz-1, yz), (xz,yz+1),
                                          (xz,yz-1)]
                              if t[0]>=0 and t[0]<maxw and t[1]>=0 and t[1]<maxh 
                              and t not in empty]
        set_ok=set()
        set_rot=set()
        set_empty=set()
        mxh=len(grid)
        mxw=len(grid[0])
        for i, v in enumerate(grid):
            for j, e in enumerate(v):
                if e == 1:#fresh
                    set_ok.add((j,i))
                elif e == 0:#fresh
                    set_empty.add((j,i))
                elif e == 2:
                    set_rot.add((j,i))
        q=deque([])     
        for t in set_rot:
            a=Node(t[0],t[1], mxw, mxh, set_empty)
            q.append(a)
        c=0
        
        while q:
            if len(set_rot)==(mxh*mxw-len(set_empty)):
                return c
            currl=len(q)
            for i in range(currl):
                node = q.popleft()
                for child_t in node.sides:
                    if child_t not in set_rot:
                        s=Node(child_t[0],child_t[1], mxw, mxh, set_empty)
                        q.append(s)
                        set_rot.add(child_t)
            c+=1
                        
        if len(set_rot)==(mxh*mxw-len(set_empty)):
            return c
        else:
            return -1

    [[2,2,2],
     [0,2,2],
     [1,0,2]]

            
                              
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                
        