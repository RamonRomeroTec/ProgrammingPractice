#String Compression: Implement a method to perform basic string compression using the counts

from collections import Counter
def fun(s):
    a=Counter(s)
    l=[]
    for k,v in a:
        l.append(k)
        l.append(v)

    if len(l)<=len(s):
        return len(l)
    else:
        return len(s)


    
