import math
from fractions import Fraction

if __name__ == '__main__':
    t=int(input())
    r=[]
    for i in (range(t)):

        f=float(input())

        if f==0:
            r.append(1)
        elif  f==1:
            r.append(1)
        else:
            i,l=map(str,str(f).split("."))
            g=1
            for i in range(len(l)):
                g=g*10

            if g%int(l)==0:
                r.append(int(1/f))
            else:
                r.append(g)



    for i in r:
        print(i)

'''

if int(l)-l != 0:
    r.append(10000)
else:

'''
