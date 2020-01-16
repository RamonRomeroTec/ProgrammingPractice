class Solution(object):
    def generateMatrix(self, n):
        m = [[0]*n for i in range(n)]
        c=1
        izq = 0
        der = n
        up = 0
        down = n
        while c<=(n*n):
            # horizontal
            for i in range(izq,der):
                m[up][i]=c
                c+=1
            up+=1
            for i in range(up,down):
                m[i][der-1]=c
                c+=1
            der-=1
            for i in range(der-1, izq-1, -1):
                m[down-1][i]=c
                c+=1
            down-=1
            for i in range(down-1, up-1, -1):
                m[i][izq]=c
                c+=1
            izq+=1
        return m

