class Solution(object):
    def uniqueOccurrences(self, arr):
        a = collections.Counter(arr)
        return len(set(a.values()))==len(a)
        