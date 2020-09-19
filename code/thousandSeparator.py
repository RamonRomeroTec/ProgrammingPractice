class Solution:
    def thousandSeparator(self, n: int) -> str:
        n=str(n)
        i=0
        a=[]
        while True:
            if len(n)-(3*(i+1))<=0:
                a.append(n[0:len(n)-(3*i)])
                break
            a.append(n[len(n)-(3*(i+1)):len(n)-(3*i)])
            i+=1
       
        return ".".join(a[::-1])

