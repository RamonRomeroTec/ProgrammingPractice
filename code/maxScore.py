class Solution(object):
    def maxScore(self, s):
        maxi=float('-inf')
        for i in range(1,len(s)):
            l=s[:i].count('0')
            r=s[i:].count('1')
            maxi=max(maxi,l+r)
        return maxi
            
        
        