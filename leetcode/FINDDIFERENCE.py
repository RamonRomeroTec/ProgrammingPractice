# USE ABS SUM TO FIND DDIFFERENCE IN ARRAY

from collections import Counter

class Solution(object):
    def findTheDifference(self, s, t):
        # s=Counter(s)
        # t=Counter(t)
        # return list((t-s).elements())[0]
        a = sum(ord(i) for i in s)
        b = sum(ord(i) for i in t)
        return chr(abs(a-b))
        
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        