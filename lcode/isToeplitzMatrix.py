'''
ok

Divide y conquista, donde primero es necesarioo generar una funcion donde se determine si
si la diagonal es verdera y ejecutar para eje base x/  y



'''
def samediagonal (number,px,py,matrix):
    diag=True
    vertical= len(matrix)
    horizontal= len(matrix[0])
    x=px
    y=py
    while x<horizontal-1:
        while y<vertical-1:
            print (x,y)
            if matrix[x][y]==number:
                diag=diag and True
            else:
                diag=diag and False
                break
                break

            x=x+1
            y=y+1
            print (x,y)

        print("exe")


    return diag






def isToeplitzMatrix( matrix):
    vertical= len(matrix)
    horizontal= len(matrix[0])


    for i in range(0, horizontal):
       if samediagonal(matrix[0][i], 0, i, matrix)==False:
           return False

    for i in range(0, vertical):

        if samediagonal(matrix[i][0], i, 0, matrix)==False:
            return False

    return True


# Driver Code
if __name__ == "__main__":

    mat = [[6, 7, 8, 9],
          [4, 6, 7, 8],
          [1, 4, 6, 7],
          [0, 1, 4, 6],
          [2, 0, 1, 4]]

    print(str(isToeplitzMatrix(mat)))


        # Write your code here
