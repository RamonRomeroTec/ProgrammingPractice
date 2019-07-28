# Insertion sort may optimize this

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones.sort()
        print(stones)
        while stones:
            if len(stones)==1:
                return stones[0]
            
            if stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
            else:
                stones[-2]=stones[-1] - stones[-2]
                stones.pop()
                
            stones.sort()
            
            
        return 0
        