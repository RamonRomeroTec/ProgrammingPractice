from sys import stdin

'''
6
abcdef
abfdce

3 5 4 5


'''

def stringed(n,a,b,s):
    pass

def moves(n,a,b):
    for i in range(0,n):
        if a[i]!=b[i]:


        pass



if __name__ == '__main__':
    n=int(stdin.readline())
    a=str(input())
    b=str(input())
    t1=''.join(sorted(a))
    t2=''.join(sorted(b))
    if t1!=t2:
        print ("-1")

    moves(n,a,b)





    print (str(len(a)), str(t2))
