class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        A=A+B
        A=sorted(A)
        f=len(A)
        if f%2==0:
            return (A[f//2]+A[(f//2)-1])/2
        return A[f//2]
        # write your code here
