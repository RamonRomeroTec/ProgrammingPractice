'''



INdex out of bounts no aplica cuando se esta desarrollando sobre una estructura como listas, ya que
si se  ingresa un  -1 se devuelve el ultimo elemoentode la lsita y asui sucesisavente
'''




class Solution:

    def colinda(self, matriz, x, y):
        #abajo
        c=0

            if x>=0 and y>=0 and matriz[x][y+1]==1:
                c=c+1

            if x>=0 and y>=0 and matriz[x][y-1]==1:
                c=c+1

            if x>=0 and y>=0 and matriz[x+1][y]==1:
                c=c+1

            if x>=0 and y>=0 and matriz[x-1][y]==1:
                c=c+1
        except Exception as e:
            pass

        return c


    def islandPerimeter(self, grid):
        vertical= len(grid)
        horizontal= len(grid[0])
        s=Solution()
        x=0
        y=0
        for x in range(0, 1):
            for y in range(0,1):
                #print(grid[x][y])
                print (s.colinda(grid, x, y))




if __name__ == "__main__":

    mat = [[0,1,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [1,1,0,0]]

    s=Solution()

    print(str(s.islandPerimeter(mat)))
'''


'''
