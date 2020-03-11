class Solution:
    def findRelativeRanks(self, nums):
        s=sorted(nums[:], reverse=True)
        d={v:i for i,v in enumerate(s)}
        ans=[]
        for n in nums:
            if d[n]==0:
                ans.append("Gold Medal")
            elif d[n]==1:
                ans.append("Silver Medal")
            elif d[n]==2:
                ans.append("Bronze Medal")
            else:
                ans.append(str(d[n]+1))
        return ans
        