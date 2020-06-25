class Solution(object):
    def isSubsequence(self, s, t):
        if s=="":
            return True
        if t=="":
            return False
        i=0
        j=0
        while j<len(s):
            while i<len(t):
                if s[j]==t[i]:
                    j+=1
                    if j==len(s):
                        return True
                i+=1
            if i==len(t):
                return False
        
            
        