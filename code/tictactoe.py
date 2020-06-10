class Solution(object):
    def tictactoe(self, moves):
        res=[[None, None, None],
             [None, None, None],
             [None, None, None]]
        for i,p in enumerate(moves):
            if i%2==0:
                res[p[0]][p[1]]='A'
            else:
                res[p[0]][p[1]]='B'
        if res[0][0] and res[0][0] == res[0][1] and res[0][1] == res[0][2]:#1ren
            return res[0][0]
        elif res[1][0] and res[1][0] == res[1][1] and res[1][1] == res[1][2]:#2ren
            return res[1][0]
        elif res[2][0] and res[2][0] == res[2][1] and res[2][1] == res[2][2]:#2ren
            return res[2][0]
        elif res[0][0] and res[0][0] == res[1][0] and res[1][0]  == res[2][0]:#c1
            return res[0][0]
        elif res[0][1] and res[0][1] == res[1][1] and res[1][1]  == res[2][1]:#c1
            return res[0][1]
        elif res[0][2] and res[0][2] == res[1][2] and res[1][2]  == res[2][2]:#c1
            return res[0][2]
        elif res[0][0] and res[0][0] == res[1][1] and res[1][1]  == res[2][2]:#d1
            return res[0][0]
        elif res[2][0] and res[2][0] == res[1][1] and res[1][1]  == res[0][2]:#c2
            return res[2][0]
        if len(moves)==9:
            return 'Draw'
        return 'Pending'
    
        