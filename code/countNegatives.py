class Solution(object):
    def countNegatives(self, grid):
        c=0
        for row in grid:
            for cell in row:
                if cell<0:
                    c+=1
        return c
        