def flatten(list):
    return aflatten(list, [])

def aflatten(list, a):
    for i in list:
        print(i)
        try:
            if len(i)>1:
                a=aflatten(i,a)
        except:
            a.append(i)
    return a

print(flatten([[1,1],2,[1,1]]))
