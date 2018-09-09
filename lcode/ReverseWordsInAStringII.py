'''
class Solution:
    """
    @param str: a string
    @return: return a string
    """
    def reverseWords(self, strs):
        ns=strs[0].split(' ')
        return " ".join(ns[::-1])
        # write your code here

if __name__ == '__main__':
    l=["zpetg pufmmdf l onwmwpsyr qlke vuijr yrr sndp txvcv x hgkczoo cfuadsza prz e sucs"]
    s=Solution()
    print (s.reverseWords(l))
'''
class Solution:
    """
    @param str: a string
    @return: return a string
    """
    def reverseWords(self, strs):
        ns=strs.split(' ')
        return " ".join(ns[::-1])
        # write your code here
