from collections import OrderedDict
class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        d=OrderedDict()
        maxi=0
        for i in tree:
            if i in d:
                d[i]+=1
            else:
                if len(d)==2:
                    c=sum(d.values())
                    maxi=max(maxi,c)
                    d.popitem(last=False)
                d[i]=1
            

print(Solution().totalFruit([3,3,3,1,2,1,1,2,3,3,4]))

[3,3,3,1,2,1,1,2,3,3,4]
11111111
