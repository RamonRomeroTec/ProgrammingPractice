class Solution:
    def isValidSudoku(self, board):
        block={0:set(),1:set(),
              2:set(),3:set(),
              4:set(),5:set(),
              6:set(),7:set(),
              8:set(),
             }
        cols={0:set(),1:set(),
              2:set(),3:set(),
              4:set(),5:set(),
              6:set(),7:set(),
              8:set(),
             }
        for y,row in enumerate(board):
            sd=set()
            for x,cell in enumerate(row):
                if cell in sd and cell != '.':
                    return False
                else:
                    sd.add(cell)
                    
                if cell in cols[x] and cell != '.':
                    return False
                else:
                    cols[x].add(cell)
                    
                if 0<=y and y<=2 and 0<=x and x<=2:
                    if cell in block[0] and cell != '.':
                        return False
                    else:
                        block[0].add(cell)
                elif 0<=y and y<=2 and 3<=x and x<=5:
                    if cell in block[1] and cell != '.':
                        return False
                    else:
                        block[1].add(cell)
                elif 0<=y and y<=2 and 6<=x and x<=8:
                    if cell in block[2] and cell != '.':
                        return False
                    else:
                        block[2].add(cell)
                
                elif 3<=y and y<=5 and 0<=x and x<=2:
                    if cell in block[3] and cell != '.':
                        return False
                    else:
                        block[3].add(cell)
                elif 3<=y and y<=5 and 3<=x and x<=5:
                    if cell in block[4] and cell != '.':
                        return False
                    else:
                        block[4].add(cell)
                elif 3<=y and y<=5 and 6<=x and x<=8:
                    if cell in block[5] and cell != '.':
                        return False
                    else:
                        block[5].add(cell)
                
                
                elif 6<=y and y<=8 and 0<=x and x<=2:
                    if cell in block[6] and cell != '.':
                        return False
                    else:
                        block[6].add(cell)
                elif 6<=y and y<=8 and 3<=x and x<=5:
                    if cell in block[7] and cell != '.':
                        return False
                    else:
                        block[7].add(cell)
                elif 6<=y and y<=8 and 6<=x and x<=8:
                    if cell in block[8] and cell != '.':
                        return False
                    else:
                        block[8].add(cell)
     
        return True
                
        
        
        
              
        
board = [   [".",".",".",".","5",".",".","1","."],
            [".","4",".","3",".",".",".",".","."],
            [".",".",".",".",".","3",".",".","1"],
            ["8",".",".",".",".",".",".","2","."],
            [".",".","2",".","7",".",".",".","."],
            [".","1","5",".",".",".",".",".","."],
            [".",".",".",".",".","2",".",".","."],
            [".","2",".","9",".",".",".",".","."],
            [".",".","4",".",".",".",".",".","."]]

print(Solution().isValidSudoku(board))