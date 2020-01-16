

class Solution:
    def titleToNumber(self, s):
        p=len(s)-1
        n=0
        for i in s:
            n=n+(ord(i)-ord('A')+1)*(26**p)
            p=p-1

        return n
        """
        :type s: str
        :rtype: int
        """
