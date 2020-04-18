class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        a=set(A)
        b=set(B)
        if B in A:
            return 1
        if len(a-b) >=1 or len(b-a) >=1:
            return -1
        i=2
        s=A+A
        while B not in s:
            s+=A
            i+=1
            if len(s)>len(B)*3:
                return -1
        return i
        
        