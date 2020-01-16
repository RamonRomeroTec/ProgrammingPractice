class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        '''
        [[1,2],
         [3,4]]
        '''
        '''
        [[1,0],
         [0,2]]
        '''
        up=0
        r1=0
        for row, e1 in enumerate(grid):
            r1+=max(e1)
            for col, height in enumerate(e1):
                if height!=0:
                    up+=1
        r2=0
        print(up,r1)
        ng = zip(*grid)
        for row, e1 in enumerate(ng):
            r2+=max(e1)
        return (up+r1+r2)
        