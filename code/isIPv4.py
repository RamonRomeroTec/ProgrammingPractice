def isIPv4Address(inputString):
    s=inputString.rstrip('.')
    s=inputString.split('.')
    try:
        s=list(map(int,s))
    except:
        return False
    print(s)
    if len(s)!=4:
        return False
    print (s)
    for i in s:
        if i <0 or i > 255:
            return False
    return True
