


class Solution:
    """
    @param n: a postive Integer
    @return: if two adjacent bits will always have different values
    """
    def hasAlternatingBits(self, n):
        s=format(n, 'b')
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                return False
        return True

        # Write your code here
