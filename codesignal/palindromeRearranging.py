from collections import Counter
def palindromeRearranging(inputString):
    size=len(inputString)
    par=None
    if size%2==0:
        par=True
    else:
        par=False
    a=Counter(inputString)
    i=0
    for k,v in a.items():
        if v%2==1:
            i=i+1

    if par==True and i>0:
        return False
    elif par==False and i==1:
        return True
    elif par==True and i==0:
        return True
    else:
        return False
