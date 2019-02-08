from collections import Counter
def dif(a,b):


    for  i  in b:

        a.remove(i)
    return a


if __name__ == '__main__':
    a=[1,0,1,1,0,1]
    b=[1,0,1,0,1]
    print(dif(a,b))
