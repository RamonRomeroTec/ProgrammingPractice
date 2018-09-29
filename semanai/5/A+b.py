
from fractions import Fraction

if __name__ == '__main__':
    t=int(input())
    r=[]
    for i in range(t):
        l=list(str(input()).split(" "))
        f=Fraction(0,1)
        for k in l:
            nk,dk= map(int,k.split("/"))
            f=f+Fraction(nk, dk)
        r.append(f)

    for i in r:
        if (i.denominator==1):
            print(str(i)+"/1")
        else:
            print(str(i))
