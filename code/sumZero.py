class Solution(object):
    def sumZero(self, n):
        ans=[]
        for i in range(1, (n//2)+1):
                ans.append(i*-1)
                ans.append(i)
        if n%2!=0:
            ans.append(0)
        return ans
                
        