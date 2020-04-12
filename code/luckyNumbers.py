def column(matrix, i):
    return [row[i] for row in matrix]

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ap=[]
        for i in range(len(matrix)):
            a=min(matrix[i])
            for j in range(len(matrix[i])):
                if a == matrix[i][j]:
                    if a==max(column(matrix, j)):
                        ap.append(a)
        return(ap)
        