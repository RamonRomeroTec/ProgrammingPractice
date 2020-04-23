import bisect
class Solution:
    def arrayRankTransform(self, arr) :
        aux=sorted(set(arr))
        return [bisect.bisect_left(aux,x)+1 for x in arr]
        