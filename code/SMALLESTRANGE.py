# FIND MIN MAX IN SINGLE RUN
class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
       
        
        minimum = 10001
        maximum = -1
        K = abs(K)
        for n in A:
          
            if n >maximum:
                maximum = n
            if n <= minimum:
                minimum = n
           
        k = (maximum-K)-(minimum+K)
        if  k <= 0:
            
            return 0
        else:
            return k
            
            
        
        