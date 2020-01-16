# USAR ITERTOOLS AND SET OPERATORS

from itertools import permutations
class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        a=set()
        for i in range(1,len(tiles)+1):
            a = a | set(permutations(tiles, i))
        return len(a)
        