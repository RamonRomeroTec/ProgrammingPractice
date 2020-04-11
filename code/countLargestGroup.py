class Solution:
    def countLargestGroup(self, n: int) -> int:
        d={}
        for i in range(1,n+1):
            s=0
            while i:
                s=s+(i%10)
                i=i//10
                
            if s in d:
                d[s]+=1
            else:
                d[s]=1
        aux=sorted([(k,v) for k,v in d.items()], key=lambda x:x[1], reverse=True )
        c=1
        va=aux[0][1]
        for i in range(1,len(aux)):
            if aux[i][1]!=va:
                break
            else:
                c+=1
        return c
            
        