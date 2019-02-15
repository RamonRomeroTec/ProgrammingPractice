'''
Note: .sort .reverse ejecutan sobre lista, no return

'''

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in A:
            i=i.reverse()
        for k in range(len(A)):
            for j in range(len(A[k])) :
                if A[k][j]==0:
                    A[k][j]=1
                else:
                    A[k][j]=0
        return A
        