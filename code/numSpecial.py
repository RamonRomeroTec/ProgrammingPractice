class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        col = list(zip(*mat))
        s=0
        for i,row in enumerate(mat):
            for j,c in enumerate(row):
                if c == 1:
                    if sum(row) == 1 and sum(col[j])==1:
                        s+=1
        return s
        
