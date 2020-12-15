class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A==B:
            c=collections.Counter(A)
            return any([ x>1 for x in c.values()])

        A=list(A)
        B= list(B)
        s=[]
        for i in range(len(A)):
            if A[i]!=B[i]:
                s.append(i)
            if len(s) == 2:
                A[s[0]], A[s[1]] = A[s[1]], A[s[0]]
                return A == B
        return False
        
            