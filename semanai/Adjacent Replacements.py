'''
5
1 2 4 5 10

1 1 3 5 9

from sys import stdin

def update(s1, num):
    if num%2==0:
        for i in range (0,len(s1)):
            if s1[i]==num:
                s1[i]=num-1
        #subs ele -> ele-1
    else:
        for i in range (0,len(s1)):
            if s1[i]==num:
                s1[i]=num+1
        #subs ele -> ele+1


if __name__ == '__main__':
    n=int(stdin.readline())
    a=stdin.readline().split(' ')
    s1=list(map(int, a))
    for i in range(0, max(s1)):
        update(s1, i+1)
        #print(s1)

    r=""
    for i in s1:
        r=r+str(i)+" "

    print(r)

'''

from sys import stdin

def update(s1, num):
    if num%2==0:
        for i in range (0,len(s1)):
            if s1[i]==num:
                s1[i]=num-1
        #subs ele -> ele-1
    else:
        for i in range (0,len(s1)):
            if s1[i]==num:
                s1[i]=num+1
        #subs ele -> ele+1


if __name__ == '__main__':
    n=int(stdin.readline())
    a=stdin.readline().split(' ')
    s1=list(map(int, a))
    numbers=[]
    '''
    c=[]
    for i in range(0,1000):
        c.append(99999999-(2*i))
    s1=c
    '''


    for i in s1:
        numbers.append(i-1)
        numbers.append(i)
        numbers.append(i+1)


    for i in range(0, len(numbers)):
        update(s1, numbers[i])
        #print(s1)

    r=""
    for i in s1:
        r=r+str(i)+" "

    print(r)
