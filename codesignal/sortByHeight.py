def sortByHeight(a):
    helper=a.copy()
    helper=sorted(helper, reverse=True)
    print(helper)
    c=0
    for i in reversed(range(len(a))):
        if a[i] != -1:
            a[i]=helper[c]
            c=c+1
    return a
           
