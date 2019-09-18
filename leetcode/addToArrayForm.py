# Use indexes
class Solution(object):
    def addToArrayForm(self, A, K):
        #return list(str(int("".join( list(map(str,A))))+K))
        A=A[::-1]
        K = [ int(x) for x in list(str(K))][::-1]
        if len(A)<len(K):
            A,K=K,A
        carry=0
        for i in range(len(A)):
            try:
                summa1=A[i]+K[i]+carry
            except:
                summa1=A[i]+carry
            if summa1>9:
                carry=summa1//10
                summa1=summa1%10
            else:
                carry=0
            A[i]=summa1
            
        if carry:
            A.append(carry)
        return A[::-1]
                
            