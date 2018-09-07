'''
5
100 98 100 100
100 100 100 100
100 100 99 99
90 99 90 100
100 98 60 99

'''
from sys import stdin

if __name__ == '__main__':
    n=int(stdin.readline())
    s=0
    q=[]
    for i in range(1,n+1):
        a,b,c,d= map(int, input().split(' '))
        q.append(a+b+c+d)
    r=0
    for i in range(0,len(q)):
        if q[0]<q[i]:
            r=r+1

    print (r+1)
