from collections import Counter

class Solution:
    """
    @param n: an unsigned integer
    @return: the number of ' bits
    """
    def hammingWeight(self, n):
        a= format(n, 'b')
        s=Counter(a)
        return s['1']
        # write your code here
