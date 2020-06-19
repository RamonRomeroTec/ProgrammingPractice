class SubrectangleQueries(object):

    def __init__(self, rectangle):
        self.matrix=rectangle
        

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        for r in range(row1, row2+1):
            for c in range(col1, col2+1):
                self.matrix[r][c]=newValue
        

    def getValue(self, row, col):
        return self.matrix[row][col]
        
