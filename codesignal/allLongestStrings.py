

def allLongestStrings(inputArray):
    ml=0
    r=[]
    for i in inputArray:
        if len(i)>=ml:
            ml=len(i)
    for i in inputArray:
        if len(i)==ml:
            r.append(i)
    return r
