class Solution(object):
    def kthSmallest(self, matrix, k):
        f=[]
        for i in matrix:
            for j in i:
                f.append(j)

        f=sorted((f))
        #print(f)
        return f[k-1]

        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
