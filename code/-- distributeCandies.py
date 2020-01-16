# return min(len(candies) / 2, len(set(candies))) simplify the problem to its rules

from collections import Counter
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        d = Counter(candies)
        magic = sorted([[key, value] for key, value in d.items()], key= lambda x : x[1])[::-1]
        girl = set()
        #while 1:
        spent = 0
        i=len(magic)-1
        while spent < len(candies)//2:
            if i<0:
                i=len(magic)-1

            if magic[i][1] != 0:
                magic[i][1]=magic[i][1]-1
                spent = spent+1
                girl.add(magic[i][0])
                i=i-1
            else:
                i=i-1
                continue
               
    
        return len(girl)
        # return min(len(candies) / 2, len(set(candies)))
    