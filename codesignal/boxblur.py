def magia(matrix, x, y):
    s=matrix[x][y]+matrix[x+1][y]+matrix[x-1][y]+matrix[x][y+1]+matrix[x+1][y+1]+matrix[x-1][y+1]+matrix[x][y-1]+matrix[x+1][y-1]+matrix[x-1][y-1]
    return s//9

def boxBlur(image):
    b=[]
    for i in range(1,len(image)-1):
        a=[]
        for j in range(1,len(image[0])-1):
            r=magia(image,i,j)
            a.append(r)
        b.append(a)
    return b
