# Count and run according to it

from collections import Counter

class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        
        out = Counter(T)
        ans=[]
        for i in S:
            if i in out:
                ans.append((i*out[i]))
                del out[i]
        for key, value in out.items():
            ans.append(key*value)
        return("".join(ans))
            
       