class Solution:
    def oddCells(self, n, m, indices) :
        a=[[0]*n,[0]*m]
        for p in indices:
            a[0][p[0]]+=1
            a[1][p[1]]+=1
        cont=0
        for r in a[0]:
            for c in a[1]:
                if (r+c)%2 == 1:
                    cont+=1
        return cont
        