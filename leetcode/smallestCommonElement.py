class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        a=set(mat[0])
        for row in mat:
            a=a&set(row)
        if len(a)==0:
            return -1
        else:
            return min(a)
        