def arrayMaximalAdjacentDifference(inputArray):
    ma=0
    for i in range(len(inputArray)-1):
        d=abs(inputArray[i]-inputArray[i+1])
        if d>ma:
            ma=d
    return ma
