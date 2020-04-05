from collections import Counter
def aux(n,visited):
    n=str(n)
    if n in visited:
        return False
    else:
        c=Counter(n)
        s=0
        for k,v in c.items():
            s+=(int(k)**2)*v
        if s==1:
            return True
        else:
            visited.add(n)
            return aux(s, visited)
    
class Solution(object):
    def isHappy(self, n):
        v=set()
        return aux(n,v)
        
                
                
        
