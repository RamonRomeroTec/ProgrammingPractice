class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(map(str, list(s)))
        c = 0
        for i in range(0,len(s),k):
            if c % 2 == 0:
                s[:]= s[0:i]+s[i:i+k][::-1]+s[i+k:]
              
            c+=1
        return "".join(s)