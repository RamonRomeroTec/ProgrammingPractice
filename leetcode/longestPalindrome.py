from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = Counter(s)

        alones=False
        c=0
        l=0
        f=False
        for k,v in d.items():
            if v%2==0:
                l=l+v
            else:
                if v > 1:
                    l=l+v
                    c=c+1
                    f=True
                else:
                    alones=True
                    
        if f:
            return l-c+1
        else:
            if alones:
                return l+1
            else:
                return l
        