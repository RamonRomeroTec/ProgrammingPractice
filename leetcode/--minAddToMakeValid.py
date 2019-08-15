class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        #if ok +2 else +1
        L=0
        
        c=0
        for i in S:
            #print(c, stack, i)
            if i == '(':
                L+=1
            else:
                if L>0:
                    L-=1
                else:
                    c+=1
        c+=L
        return c
        
        