def isLucky(n):
    n=str(n)
    m=len(n)//2
    a=n[:m]
    b=n[m:]
    print (a,b)
    a=list(map(int,a))

    b=list(map(int,b))

    return (sum(a)==sum(b))


    #return sum(map(int,a)==sum(map(int,b)
