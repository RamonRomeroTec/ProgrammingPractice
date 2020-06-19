from collections import Counter
class Solution(object):
    def canBeEqual(self, target, arr):
        if len(target) != len(arr):
            return False
        return Counter(target) == Counter(arr)
        