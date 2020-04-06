class Solution:
    def sortByBits(self, arr):
        s = sorted([(x, format(x,'b')) for x in arr], key=lambda x:(x[1].count('1'), x[0]))
        return [x[0] for x in s]