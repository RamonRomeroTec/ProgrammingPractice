from collections import Counter


class Solution:
    """
    @param x: an integer
    @param y: an integer
    @return: return an integer, denote the Hamming Distance between two integers
    """

    def hammingDistance(self, x, y):
        c= x^y
        s=Counter(format(c,'b'))

        return s['1']
        
