class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<=1 or len(set(s))==1:
            return s
        maxi=0
       
        for i in range(0, len(s)):
            for j in range(1, len(s)+1):
                if i+j <= len(s):
                    k = s[i:i+j]
                    if len(k)>maxi and k==k[::-1]  :
                        w=k
                        maxi=len(k)
                    #print(k, len(k))
        return w
        