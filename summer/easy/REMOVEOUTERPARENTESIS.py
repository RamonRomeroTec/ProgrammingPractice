# evaluate 0 status, no stack



class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        e=0
        ans=[]
        for c in S:
            if e!= 0:
        
                if c=='(':
                    e +=1
                else:
                    e -=1
                if e!= 0:
                    ans.append(c)
            else:
                e+=1
                
                
        return "".join(ans)
            
                
    
        

# class Solution(object):
#     def removeOuterParentheses(self, S):
#         """
#         :type S: str
#         :rtype: str
#         """
#         stack = []
#         ans = []
#         for c in S:
#             if c == '(':
#                 stack.append(c)
#                 if len(stack) > 1:
#                     ans.append(c)
#             else:
#                 stack.pop()
#                 if len(stack) != 0:
#                     ans.append(c)
#         return "".join(ans)
    
        
                
    
#     # (()(()))
#     #
#     #
        
                
            
            
        