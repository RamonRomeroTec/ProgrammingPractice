'''

'''
def combinations(n,s):

    r=0
    if s<=n:
        r= int((s-1)/2)

    else:
            if (s%2)==0:
                r= int(n-(s/2))
            else:
                r= int(n-((s-1)/2))
    if r<=0:
        return 0
    else:
        return r

if __name__ == '__main__':
    n, s = map(int, input().split(' '))
    print (combinations(n,s))


'''

    print(combinations(8, 5))
    print(combinations(8, 15))
    print(combinations(7, 20))
    print(combinations(1000000000000,1000000000001))
    print(combinations(10, 9))
    print(combinations(9, 10))
    print(combinations(10, 10))

    1 2 3 4 5 6 7 8 9 10

    2
1
0
500000000000
4
4
5
'''
