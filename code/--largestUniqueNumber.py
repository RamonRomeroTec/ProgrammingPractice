# absolute negative instead of sorted
from collections import Counter
class Solution(object):
    def largestUniqueNumber(self, A):
        d=Counter(A)
        maxi=-1
        for i in d.keys():
            if d[i]==1:
                maxi=max(i, maxi)
        return maxi