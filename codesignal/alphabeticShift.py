def alphabeticShift(inputString):
    inputString=list(inputString)
    for i in range(len(inputString)):
        if inputString[i] == 'Z':
            inputString[i]='A'
        elif inputString[i] == 'z':
            inputString[i]='a'
        else:
            inputString[i]=chr(ord(inputString[i])+1)
    return "".join(inputString)
