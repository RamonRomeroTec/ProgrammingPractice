from collections import deque

class Solution(object):
    def numIslands(self, grid):
        visited=set()
        c=0
        for i,row in enumerate(grid):
            for j,cell in enumerate(row):
                if cell=='1' and (i,j) not in visited:
                    c+=1
                    q=deque([(i,j)])
                    while q:
                        p=q.popleft()
                        if p not in visited:
                            visited.add(p)
                            if p[0]-1>=0 and grid[p[0]-1][p[1]]=='1' and (p[0]-1,p[1]) not in visited:
                                q.append((p[0]-1,p[1]))
                            if p[0]+1<len(grid) and grid[p[0]+1][p[1]]=='1' and (p[0]+1,p[1]) not in visited:
                                q.append((p[0]+1,p[1]))
                            if p[1]-1>=0 and grid[p[0]][p[1]-1]=='1' and (p[0],p[1]-1) not in visited:
                                q.append((p[0],p[1]-1))
                            if p[1]+1<len(grid[0]) and grid[p[0]][p[1]+1]=='1' and (p[0],p[1]+1) not in visited:
                                q.append((p[0],p[1]+1))
        return c
