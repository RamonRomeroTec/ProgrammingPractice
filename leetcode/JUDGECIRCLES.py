# Count de string esta optimizado para correr mas rapido en strings que counter



# from collections import Counter
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # c = Counter(moves)
        # if ('U' in c and 'D' not in c ) or ('U' not in c and 'D'  in c):
        #     return False
        # if ('L' in c and 'R' not in c) or ('L' not in c and 'R'  in c):
        #     return False
        # if ('L' not in c and 'R' not in c) and ('U'  in c and 'D' in c  ):
        #     if abs(c['U']-c['D']) == 0:
        #         return True
            
        # if ('U' not in c and 'D' not in c) and ('L'  in c and 'R' in c  ):
        #     if abs(c['L']-c['R']) == 0:
        #         return True
            
        # if abs(c['U']-c['D']) == 0 and abs(c['L']-c['R']) == 0:
        #     return True
        # return False

        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
