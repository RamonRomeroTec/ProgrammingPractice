from collections import Counter
def commonCharacterCount(s1, s2):
    a=Counter(s1)
    b=Counter(s2)
    k=a&b
    r=0
    for v in k.values():
        r=r+v
    return r
        
