'''
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
'''
from collections import defaultdict

def ok(strs):
    g=defaultdict(list)
    for i in strs:
        a=set(i)
        if len(g)>0:
            for e in list(g.keys()):
                c=set(e)
                #print(len(c-a), c, a, list(g.keys()))
                if len(c&a)==len(a):
                    g[e].append(i)
                    ad=True
                    break
                else:
                    ad=False
            if ad==False:
                g[i].append(i)
        else:
            g[i]=[i]
    r=[]
    print(g)
    for i in g.values():
        r.append(i)
    return r

print(ok(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(ok(["", "b"]))
