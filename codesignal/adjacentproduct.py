def adjacentElementsProduct(inputArray):
    mx=-99999
    for i in range(len(inputArray)-1):
        r=inputArray[i]*inputArray[i+1]
        if r>mx:
            mx=r

    return mx
