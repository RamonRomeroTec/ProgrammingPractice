

if __name__ == '__main__':
    n=int(input())
    a = list(map(int,(input().split(' '))))
    pu = False;
    if(a[0]%2 == 0 or a[-1]%2 == 0):
        pu = True

    if(n%2 == 0 or pu):
        print("No")
    else:
        print("Yes")
