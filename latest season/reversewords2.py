'''
Note: slice notation first then methods list and etc

'''


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = s.split(" ")
        a = []
        for i in n:
            i = i[::-1]
            a.append(i)
        return " ".join(a)
