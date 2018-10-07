def firstDuplicate(a):
    s=set()
    for i in a:
        if i in s:
            return i
        else:
            s.add(i)
    return -1
