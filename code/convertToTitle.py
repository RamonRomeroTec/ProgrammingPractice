class Solution(object):
    def convertToTitle(self, n):
        ans=[]
        while n>0:
            n-=1
            ans.append(chr(65 + ((n) % 26))) 
            n//= 26
        return "".join(ans[::-1])
    
    