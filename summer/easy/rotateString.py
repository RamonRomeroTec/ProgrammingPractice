class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A)>len(B):
            return False
        A = A+A
        return B in A
        