'''

Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column are set to O.



'''






def convert(arr, c,r):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i in r or j in c:

                arr[i][j]=0
    return arr





def zero(arr):
    col=set()
    ren=set()
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]==0:
                col.add(j)
                ren.add(i)

    return convert(arr, col,ren)




if __name__ == '__main__':
    m=[[1, 2 ,3,0],
    [4, 5 ,0,2],
    [7, 8 ,9,3]]

    print (zero(m))
