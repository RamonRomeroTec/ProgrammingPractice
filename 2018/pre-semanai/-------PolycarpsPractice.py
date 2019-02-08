'''
8 3
5 4 2 6 5 1 9 2
'''
from sys import stdin

if __name__ == '__main__':
    problems, days=map(int,(stdin.readline().split(' ')))
    dificultad = list(map(int,(input().split(' '))))

    s=sorted(dificultad)

    piv=[]
    for i in range(len(s)-days, len(s)):
        piv.append(int(s[i]))
    #print(piv)
    print(sum(piv))

    order=[]
    for i in piv:
        order.append(dificultad.index(i)+1)
    order.append(0)

    order.sort()



    suma=[]

    for i in range(0, len(order)-2):
        suma.append(abs(order[i]-order[i+1]))


    suma.append(len(dificultad)-(order[-2]))
    r = ' '.join(map(str, suma))
    #print(order)

    print (r) ## 17, 5, 11
