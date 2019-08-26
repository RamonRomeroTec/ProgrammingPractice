import re
class Solution(object):
    def isPalindrome(self, s):
        s = s.lower();
        s = re.sub('[^a-z0-9]','',s)
        if s == s[::-1]:
            return True
        return False
    
    
# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         s = [ x.lower() for x in s if x.isalpha() or x.isdigit()]
#         print(s)
#         return(s==s[::-1])
        