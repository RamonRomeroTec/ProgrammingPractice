class Solution(object):
    def firstBadVersion(self, n):
        def binSearch(begin, end):
            middle=(begin+end)//2
            if(isBadVersion(middle)):
                if (not isBadVersion(middle-1)):
                    return middle
                else:
                    return binSearch(begin, middle-1)
            else:
                return binSearch(middle+1, end)
        return binSearch(0, n)