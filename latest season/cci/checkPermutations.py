
class Solution:
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        a=set(s)
        b=set(t)
        
        if a|b != b:
            return False
        
        for i in a:
            if s.count(i) != t.count(i):
                return False
            
        return True
        