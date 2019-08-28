class Solution(object):
    def countSegments(self, s):
        return len(s.split())
    
# class Solution(object):
#     def countSegments(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         count=0
        
#         for i in range(0,len(s)):
#             if s[i]!=" " and (s[i-1]==" " or i==0):
#                 count +=1
#         return count