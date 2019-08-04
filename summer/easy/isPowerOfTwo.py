class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        while n > 1:
            if n % 2 !=0:
                return False
            else:
                n/=2
        
        return n==1
        