'''

ok

INdex out of bounts no aplica cuando se esta desarrollando sobre una estructura como listas, ya que
si se  ingresa un  -1 se devuelve el ultimo elemoentode la lsita y asui sucesisavente
'''




class Solution:

    def colinda(self, matriz, y, x):
        vertical= len(matriz)
        horizontal= len(matriz[0])
        #abajo
        c=0

        if x>=0 and y>=0 and x+1<horizontal and y < vertical and matriz[y][x+1]==1:
            #print("dere")
            c=c+1




        if x>=0 and y>=0 and x<horizontal and y+1 < vertical and  matriz[y+1][x]==1:
            #print("abajo")

            c=c+1



        if x-1>=0 and y>=0 and x<horizontal and y < vertical and matriz[y][x-1]==1:
            #print("izq")

            c=c+1



        if x>=0 and y-1>=0 and x<horizontal and y < vertical and matriz[y-1][x]==1:
            #print("arr")

            c=c+1


        return c


    def islandPerimeter(self, grid):
        vertical= len(grid)
        horizontal= len(grid[0])
        s=Solution()
        x=0
        y=0
        suma=0
        for y in range(0, vertical):
            for x in range(0,horizontal):

                if grid[y][x]==1:
                    #print(s.colinda(grid, y, x))
                    suma=suma+(4-s.colinda(grid, y, x))



        return suma



if __name__ == "__main__":

    mat = [[1,1,1]]

    s=Solution()

    print(str(s.islandPerimeter(mat)))
'''


'''
