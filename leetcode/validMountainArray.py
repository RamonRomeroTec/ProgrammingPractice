class Solution(object):
    def validMountainArray(self, A):
        if len(A)<3:
            return False
        i=0
        asc = 0
        des = 0
        up=True
        while i<len(A)-1:
            if up :
                if A[i]<A[i+1]:
                    i+=1
                    asc+=1
                elif A[i]==A[i+1]:
                    return False
                else:
                    up=False
            else:
                if A[i]>A[i+1]:
                    i+=1
                    des+=1
                else:
                    return False
        return asc > 0 and des > 0