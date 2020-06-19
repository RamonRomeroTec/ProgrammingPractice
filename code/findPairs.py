class Solution(object):
    def findPairs(self, nums, k):
        if k<0:
            return 0
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        ans=set()
        aux=0
        for i,c in d.items():
            if k == 0:
                if c>1:
                    aux+=1
                    
            else:
                if i+k in d:
                    ans.add((i, i+k))
                    ans.add((i+k, i))

                if i-k in d:
                    ans.add((i, i-k))
                    ans.add((i-k, i))
        return (len(ans)//2)+aux
            
        