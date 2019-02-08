# @ramonromeroqro
# zip, to reverse to cols


class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        43->
        """
        maxhor=[]
        for r in grid:
            maxhor.append(max(r))
        maxver=[]
        changed = zip(*grid)
        for i in changed:
            maxver.append(max(i))
        s=0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                s=s+min(abs(maxhor[i]-grid[i][j]),  
abs(maxver[j]-grid[i][j]))
        print(maxhor)

        print(maxver)

        return s
                
                
        
        
