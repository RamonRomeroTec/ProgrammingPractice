class Solution(object):
    def buildArray(self, target, n):
        i=0
        ans=[]
        while i<len(target):
            if i==0:
                d=target[i]-1
            else:
                d=target[i]-target[i-1]-1
            ans+=(['Push','Pop']*d)+['Push']
            i+=1
        return ans
        