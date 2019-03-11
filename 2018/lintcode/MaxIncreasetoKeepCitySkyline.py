'''
ok
'''
class Solution:
    """
    @param grid: a 2D array
    @return: the maximum total sum that the height of the buildings can be increased
    """
    def getver(self,grid):
        a=[]
        for  i in grid:
            a.append(max(i))

        return a

    def gethor(self,grid):
        a=[]
        for  i in range(0,len(grid[0])):
            max=0
            for j in grid:
                if j[i]>=max:
                    max=j[i]
            a.append(max)

        return a

    def increase(self,grid, hor, ver):
        s=0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                s=s+((min(hor[j],ver[i]))-grid[i][j])
        return s





    def maxIncreaseKeepingSkyline(self, grid):
        s=Solution()
        return s.increase(grid, s.gethor(grid), s.getver(grid))


        # Write your code here


if __name__ == '__main__':
    a=[[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
    s=Solution()
    print(s.maxIncreaseKeepingSkyline(a))


