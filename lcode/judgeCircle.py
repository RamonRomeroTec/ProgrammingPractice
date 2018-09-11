'''
ok
'''
class Solution:

    def judgeCircle(self, moves):

        horizontal=0
        vertical=0


        for i in range(0,len(moves)):
            if moves[i]=='U':
                vertical=vertical+1
            elif moves[i] == 'D':
                vertical=vertical-1
            elif moves[i]=='L':
                horizontal=horizontal-1
            elif moves[i]=='R':
                horizontal=horizontal+1

        if (vertical==0 and horizontal==0):
            return True
        else:
            return False
