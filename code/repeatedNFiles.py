
class Solution(object):
    def repeatedNTimes(self, A):
        s = set()
        for i in A:
            if i in s:
                return i
            else:
                s.add(i)
