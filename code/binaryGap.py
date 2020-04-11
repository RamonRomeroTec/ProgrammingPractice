class Solution:
    def binaryGap(self, N: int) -> int:
        s=list(map(int,format(N, 'b')))
        a=0
        b=1
        comp=0
        while a<len(s)-1:
            while s[a]!=1:
                a+=1
                b=a+1
            c=1
            aux=True
            while s[b] != 1:
                if b>=len(s)-1:
                    aux=False
                    break
                c+=1
                b+=1
            if aux:   
                comp=max(c,comp)
            a=b
            b=a+1
        return comp
