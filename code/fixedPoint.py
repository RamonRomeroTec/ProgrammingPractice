# BIN SEARCH NO FIND IF IT IS THE FIRST ELEMENT POSITIVE


class Solution(object):
    def fixedPoint(self, A):
        # for i, v in enumerate(A):
        #     if i == v:
        #         return i
        # return -1
    
        if len(A)==1:
            if A[0]==0:
                return 0
            else:
                return -1
        if not A:
            return -1
        def findFirstPositive(A, start, end):
            if A[start]>=0 and (start-1 < 0 or A[start-1]<=0):
                return start
            middle = (start+end) // 2
            if A[start]*A[end]<0:
                return findFirstPositive(A, middle+1, end)
            else:
                return findFirstPositive(A, end, middle-1 )
        start = findFirstPositive(A, 0, len(A)-1)
        print(start)
        for i in range(start, len(A)):
            if i == A[i]:
                return i
        return -1
            
        
       