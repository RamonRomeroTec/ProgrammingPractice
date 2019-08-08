'''
Implement an algorithm that will check whether the given grid
of numbers represents a valid Sudoku puzzle according to the
layout rules described above. Note that the puzzle represente
by grid does not have to be solvable.


'''

from collections import Counter
def evaluate(g,x,y):
        a=[]
        a.append(g[y-1][x-1])

        a.append(g[y-1][x])

        a.append(g[y-1][x+1])

        a.append(g[y][x-1])

        a.append(g[y][x])

        a.append(g[y][x+1])

        a.append(g[y+1][x-1])

        a.append(g[y+1][x])

        a.append(g[y+1][x+1])

        s=Counter(a)
        print(s)
        for k,v in s.items():
                if k!='.' and v>1:
                        return False
        return True









def sudoku2(grid):
        for i in grid:
                s=Counter(i)
                for k,v in s.items():
                        if k!='.' and v>1:
                                return False

        for i in range(9):
                p=[]
                for j in range(9):
                        p.append(grid[j][i])
                s=Counter(p)
                for k,v in s.items():
                        if k!='.' and v>1:
                                return False



        for i in range(1,9,3):
                for j in range(1,9,3):
                        if evaluate(grid,i,j)==False:
                                return False

        return True
