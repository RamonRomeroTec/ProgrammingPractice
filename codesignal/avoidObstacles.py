def esdivisordeAny(l,n):
    for i in l:
        if i%n==0:
            return True
    return False



def avoidObstacles(inputArray):
    for i in range(2, max(inputArray)+2):
        if esdivisordeAny(inputArray,i)==False:
            return i
