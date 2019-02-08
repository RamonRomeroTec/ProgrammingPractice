def solve(a,b,i):
    if a==0 or b==0:
        return [a,b]
    else:
        if a>=2*b:
            a=a%(2*b)
            return solve(a,b,i)
        else:
            if b>=2*a:
                b=b%(2*a)
                return solve(a,b,i)
            else:
                return [a, b]






if __name__ == '__main__':
    m, n = map(int,(input().split(' ')))
    print(" ".join(map(str,solve(m,n,False))))
