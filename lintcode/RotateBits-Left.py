class Solution:
    """
    @param n: a number
    @param d: digit needed to be rorated
    @return: a number
    """
    def leftRotate(self, n, d):

        return (n << d)|(n >> (32 - d))
        # write code here
