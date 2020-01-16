class Solution(object):
    def strStr(self, haystack, needle):

        if haystack==needle:
            return 0
        a=0
        while a<len(haystack)-len(needle)+1:
            if haystack[a:a+len(needle)]==needle:
                return a 
            a+=1
        return -1
        