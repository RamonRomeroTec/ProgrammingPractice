


def check(matrix,x,y,val):

    while y<len(matrix) and x <len(matrix[0]):
        if matrix[y][x]!=val:
            return False
        y=y+1
        x=x+1

    return True





class Solution:
    """
    @param matrix: the given matrix
    @return: True if and only if the matrix is Toeplitz
    """


    def isToeplitzMatrix(self, matrix):
        for i in range(len(matrix[0])):
            if check(matrix,i,0,matrix[0][i])==False:
                return False


        for i in range(len(matrix)):
            if check(matrix,0,i,matrix[i][0])==False:
                return False

        return True


        # TODO: write code...
        # Write your code here
