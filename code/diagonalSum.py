class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = sum(mat[i][i]+mat[i][len(mat)-i-1]for i in range(len(mat)))
        if len(mat)%2 == 1:
            s-=mat[len(mat)//2][len(mat)//2] 
        return s