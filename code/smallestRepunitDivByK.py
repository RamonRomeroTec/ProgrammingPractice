class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        a=[1]
        for i in range(K):
            a.append((a[-1]*10)+1)
        for i,v in enumerate(a):
            if v%K==0:
                return i+1
        return -1