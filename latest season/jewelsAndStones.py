# @ramonromeroqro
# create a set, falidate if element exist

class Solution(object):
    def numJewelsInStones(self, J, S):
        s1=set(J)
        suma=0
        for i in S:
            if i in s1:
                suma=suma+1
        return suma
       
       
       