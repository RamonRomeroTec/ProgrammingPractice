def sumarsq(n):
    sum = 0

    while(n!=0):
            sum=sum+(n%10)**2
            n=n//10
    return sum


def fun(n):
    a=set()
    s=0
    while s!=1:
        s=sumarsq(n)
        if s not in a:
            a.add(s)
            print(s)
        else:
            return False
        n=s


    return True


print(fun(19))

def tolist(n):
    sum = 0
    a=[]

    while(n!=0):
            e=(n%10)
            a.append(e)
            n=n//10
    return a[::-1]


print(tolist(19))
