# COMPARING LAST INDEXES AND EXISTENCE IN STACK

class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        s1=[]
        for l in S:
            if s1 and s1[-1]==l:
                s1.pop()
            else:
                s1.append(l)
        return "".join(s1)
    
            
            
            
            