def longest(s1, s2):
    a=set(s1)
    b=set(s2)
    u=a|b
    
    return "".join(sorted(u))
    # your code
