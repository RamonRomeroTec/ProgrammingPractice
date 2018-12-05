
def evalu(matrix, y, x):
    e=0

    if y-1 >= 0 and x-1 >=0 and matrix[y-1][x-1]==True:
        e=e+1

    if y-1 >= 0 and matrix[y-1][x]==True:
        e=e+1


    if x+1< len(matrix[0]) and y-1 >=0 and matrix[y-1][x+1]==True:
        e=e+1


    if  x-1 >= 0 and matrix[y][x-1]==True:
        e=e+1

    if  x+1 < len(matrix[0]) and matrix[y][x+1]==True:
        e=e+1


    if x-1 >= 0 and y+1 < len(matrix) and matrix[y+1][x-1]==True:
        e=e+1


    if y+1 < len(matrix) and matrix[y+1][x]==True:
        e=e+1


    if x+1< len(matrix[0]) and y+1 < len(matrix) and matrix[y+1][x+1]==True:
        e=e+1

    return e


def minesweeper(matrix):
    m=[]
    for i in range(len(matrix)):
        l=[]
        for j in range(len(matrix[0])):
            r=evalu(matrix,i,j)
            l.append(r)
        m.append(l)
    return m
