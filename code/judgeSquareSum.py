import math
class Solution(object):
    def judgeSquareSum(self, c):
        if c==0:
            return True
        i=0
        while i < math.sqrt(c):
            b = c-(i*i)
            if math.sqrt(b) == int(math.sqrt(b)):
                return True
            i+=1
        return False
            
        