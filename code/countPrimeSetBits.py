class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        primes = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                     37, 41, 43, 47, 53, 59, 61, 67, 71])
        
        c=0
        for i in range(L, R+1):
            if (format(i,'b').count('1')) in primes:
                c+=1
        return c
        