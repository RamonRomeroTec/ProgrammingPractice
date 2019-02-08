
import math

def splitText(n,p,q,string):



    a = max(p,q)
    b = min(p,q)


    repsA = math.floor(n/a)
    splitsA = n - repsA*a

    stop = 0

    while splitsA%b != 0 and stop < 1000:
        repsA -= 1
        splitsA = n - repsA*a
        stop += 1

    if stop >= 1000:
        print("-1")
        return

    repsB = math.floor(splitsA/b)

    subPalabras = []

    indexInicial = 0
    indexFinal = a


    for i in range(0,repsA):
        subPalabras.append(string[indexInicial:indexFinal])
        indexInicial = indexFinal
        indexFinal += a

    indexInicial = indexFinal - a
    indexFinal += b - a

    for i in range(0,repsB):
        subPalabras.append(string[indexInicial:indexFinal])
        indexInicial = indexFinal
        indexFinal += b

    lenSP = len(subPalabras)

    for i in range(0,lenSP):
        if len(subPalabras[i]) != p and len(subPalabras[i]) != q:
            print("-1")
            return

    print(lenSP)
    for i in range(0,lenSP):
        print(subPalabras[i])

if __name__ == '__main__':
    n,p,q=map(int,str(input()).split(" "))
    s=str(input())
    splitText(n,p,q,s)
