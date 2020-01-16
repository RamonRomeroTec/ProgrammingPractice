
def decode(encoded):
    r=encoded[::-1]
    a=[]
    i=0
    while i<len(r):
        n=int(r[i:i+2])
        if n<=12:
            n=int(r[i:i+3])
            i=i+3
        else:
            i=i+2
        a.append(chr(n))
    return ''.join(a)

t='701011792823411101701997927'
print(decode(t))
