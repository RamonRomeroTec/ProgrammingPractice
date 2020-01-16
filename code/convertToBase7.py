class Solution(object):
    def convertToBase7(self, num):
        if num==0:
            return "0"
        ans=[]
        neg=False
        if num<0:
            num*=-1
            neg=True
        
        while num:
            ans.append(str(num%7))
            num//=7
        if neg:
            ans.append('-')
        return("".join(ans[::-1]))
        
     