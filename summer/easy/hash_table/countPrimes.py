# using erastoothenes sieve
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        bools= [True]*n

        c=0
        for i in range(2,n):
            if bools[i]==True:
                c+=1
                for j in range(i,n, i):
                    bools[j]=False
        return c