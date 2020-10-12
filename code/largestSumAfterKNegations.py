class Solution:
    def largestSumAfterKNegations(self, A, K):
        s=sum(A)
        A.sort()
        i=0
        while i<len(A) and K:
            if A[i]<0:
                K-=1
                s+=(A[i]*-2)
                A[i]*=-1
            elif A[i]==0:
                return s
            else:
                # 2 3 4
                if K%2!=0:#notpair
                    if i>0:
                        if A[i]>A[i-1]:
                            A[i-1]*=-1
                            return sum(A)
                        else:
                            A[i]*=-1
                            return sum(A)                        
                    else:
                        s-=(A[i]*2)
                        return s
                    
            i+=1

        return s