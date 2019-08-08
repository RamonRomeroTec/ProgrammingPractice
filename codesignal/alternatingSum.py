def alternatingSums(a):
    a1=0

    b1=0

    for i in range(0, len(a), 2):
        a1=a1+a[i]
    for i in range(1, len(a), 2):
        b1=b1+a[i]
        
    return [a1, b1]
