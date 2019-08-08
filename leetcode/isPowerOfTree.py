class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n>1:
            if n%3 != 0:
                return False
            else:
                n=n/3
        return n==1

