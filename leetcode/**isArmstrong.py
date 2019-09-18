#Slit and len
class Solution(object):
    def isArmstrong(self, N):
        init=N
        temp=N
        digits = []
        while(temp!=0):
            x = temp % 10
            digits.append(x)
            temp = temp // 10
        p=len(digits)
        s=0
        for d in digits:
            s+=(d**p)
            if s>init:
                return False
        return init==s
            
            
        