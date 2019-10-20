class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def update(board, maxh, maxw, i,j):
            s=0
            if i-1>=0 and j-1 >=0 and (board[i-1][j-1]==1 or board[i-1][j-1]==-1):
                s+=1
            if i-1>=0  and (board[i-1][j]==1 or board[i-1][j]==-1 ):
                s+=1
            if i-1>=0 and j+1<maxw and (board[i-1][j+1]==1 or board[i-1][j+1]==-1) :
                s+=1
                
                
            if j-1>=0 and (board[i][j-1]==1 or board[i][j-1]==-1 ) :
                s+=1
            if j+1 < maxw  and (board[i][j+1]==1 or board[i][j+1]==-1):
                s+=1
                
            if i+1<maxh and  j-1>=0 and (board[i+1][j-1]==1 or board[i+1][j-1]==-1):
                s+=1
            if i+1<maxh and (board[i+1][j]==1 or board[i+1][j]==-1):
                s+=1
            if i+1<maxh and  j+1<maxw and (board[i+1][j+1]==1 or board[i+1][j+1]==-1):
                s+=1
               
            if board[i][j]==0 and s==3: #revive if 3 vecinos
                board[i][j]=-3
            elif s<2 and board[i][j]==1 : # vivo y muere
                board[i][j]=-1
            elif s>3 and board[i][j]==1:
                board[i][j]=-1
            else:
                pass
            
        mh=len(board)
        for i in range(mh):
            mw=len(board[i])
            for j in range(mw):
                update(board, mh,mw,i,j)
        mh=len(board)
        for i in range(mh):
            mw=len(board[i])
            for j in range(mw):
                if board[i][j] == -1:
                    board[i][j]=0
                elif board[i][j] == -3:
                    board[i][j]=1
                    

