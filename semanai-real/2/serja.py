if __name__ == '__main__':
    n,m=map(int, str(input()).split(" "))
    s=[]
    e=[]
    for i in range(0,1000000):
        e.append(-999)
    a=[]
    for i in range(0,n):
        a.append(i)
    i=(n - 1)
    while (i>=0):
        if (s.index(a[i]) == len(s)-1):
            e[i] = len(s) + 1;
            s.append(a[i]);
        else:
            e[i] = len(s);

        i=i-1

    for i in range(0,m):
        a=int(input())
        print(e[nxt - 1])
