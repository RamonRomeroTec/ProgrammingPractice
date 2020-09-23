class Solution:
    def imageSmoother(self, m):
        fm=[[0]*len(m[0]) for x in range(len(m))]
        for y, row in enumerate(m):
            for x, cell in enumerate(row):
                c=1
                sum1=m[y][x]
                if y+1<len(m):
                    c+=1
                    sum1+=m[y+1][x]
                if x+1 < len(m[y]):
                    c+=1
                    sum1+=m[y][x+1]
                if y+1<len(m) and x+1 < len(m[y]):
                    c+=1
                    sum1+=m[y+1][x+1]
                if y-1>=0:
                    c+=1
                    sum1+=m[y-1][x]
                if x-1>=0:
                    c+=1
                    sum1+=m[y][x-1]
                if y-1>=0 and x-1>=0:
                    c+=1
                    sum1+=m[y-1][x-1]
                if x+1 < len(m[y]) and y-1>=0:
                    c+=1
                    sum1+=m[y-1][x+1]
                if x-1>=0 and  y+1<len(m):
                    c+=1
                    sum1+=m[y+1][x-1]
                fm[y][x]=(sum1)//(c)
        return fm
