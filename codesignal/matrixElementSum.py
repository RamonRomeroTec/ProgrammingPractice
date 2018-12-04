def matrixElementsSum(matrix):
    r=0
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            if(matrix[i][j]==0):
                break
            else:
                r=r+matrix[i][j]
    return r
