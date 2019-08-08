'''
Note: return A.index(max(A)) -> N Complexity, 
Aplicar busqueda binaria para reducir la complejidad, basandonos en
asumir que el arreglo es triangular 

'''


class Solution(object):
    def peakIndexInMountainArray(self, A):

        # return A.index(max(A))
        f, l = 0, len(A)-1
        if l+1 < 3:
            return None
        if l+1 == 3:
            return A[1]

        while(1):
            mid = (l+f)/2
            # middle
            if A[mid-1] <= A[mid] and A[mid] >= A[mid+1]:
                return mid
            # desc
            elif A[mid-1] >= A[mid] and A[mid] >= A[mid+1]:
                l = mid
            # asc
            elif A[mid-1] <= A[mid] and A[mid] <= A[mid+1]:
                f = mid
