class Solution(object):
    def queensAttacktheKing(self, queens, king):
        left_row=[float('+inf'), float('+inf')]
        right_row=[float('+inf'), float('+inf')]
        up_col=[float('+inf'), float('+inf')]
        down_col=[float('+inf'), float('+inf')]
        ul=[float('+inf'), float('+inf')]
        ur=[float('+inf'), float('+inf')]
        dl=[float('+inf'), float('+inf')]
        dr=[float('+inf'), float('+inf')]
        
        for q in queens:
            if q[0] == king[0]:
                #row
                if king[1]<q[1]:
                    #right
                    if (float('inf') in right_row):
                        right_row=q
                    else:
                        if (q[1]-king[1]) < (right_row[1]-king[1]):
                            right_row=q
                else:
                    #left 
                    if (float('inf') in left_row):
                        left_row=q
                    else:
                        if (king[1]-q[1]) < (king[1]-left_row[1]):
                            left_row=q
            elif q[1] == king[1]:
                #col
                if king[0]<q[0]:
                    #up
                    if (float('inf') in up_col):
                        up_col=q
                    else:
                        if (q[0]-king[0]) < (up_col[0]-king[0]):
                            up_col=q
                else:
                    #down 
                    if (float('inf') in down_col):
                        down_col=q
                    else:
                        if (king[0]-q[0]) < (king[0]-down_col[0]):
                            down_col=q
            elif abs(king[0]-q[0]) == abs(king[1]-q[1]) :
                if q[0]>king[0] and q[1]>king[1]: #ur

                    if (float('inf') in ur):
                        ur=q
                    else:
                        if (q[0]-king[0] < ur[0]-king[0]) and (q[1]-king[1]<ur[1]-king[1]):
                            ur=q
    
                elif q[0]<king[0] and q[1]<king[1]: #dl
                    if (float('inf') in dl):
                        dl=q
                    else:
                        if (king[0]-q[0] < king[0]-dl[0]) and (king[1]-q[1]< king[1]-dl[1]):
                            dl=q
                    
                elif q[0]>king[0] and q[1]<king[1]: #dr
                    if (float('inf') in dr):
                        dr=q
                    else:
                        if (q[0]-king[0] < dr[0]-king[0]) and (king[1]-q[1]< king[1]-dr[1]):
                            dr=q
                    
                elif q[0]<king[0] and q[1]>king[1]: #ul
                    if (float('inf') in ul):
                        ul=q
                    else:
                        if (king[0]-q[0] < king[0]-ul[0]) and (q[1]-king[1]< ul[1]-king[1]):
                            ul=q
        return [x for x in [left_row,right_row,up_col,down_col,ul,ur,dl,dr] if float('inf') not in x]

        
        