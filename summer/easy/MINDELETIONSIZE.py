# PARA TRANSPONER DE COL -> ROW usar ZIP


class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        # c=0
        # for i in range(len(A[0])):
        #     for row in range(len(A)-1):
        #         if (A[row][i])>(A[row+1][i]):
        #             c+=1
        #             break
        # return c
        
        c = 0
        for i in zip(*A):
            if list(i) != sorted(i):
                c += 1
        return c