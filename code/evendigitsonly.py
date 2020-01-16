def evenDigitsOnly(n):
    while n/10>0:
        d=n%10
        if d%2==1:
            return False
        print(d)
        n=n//10
    return True
