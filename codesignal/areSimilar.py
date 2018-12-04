def areSimilar(a, b):
    if len(a) != len(b):
        return False
    else:
        c=0
        ix=[]
        for i in range(len(a)):
            if a[i]!=b[i]:
                c=c+1
                ix.append(i)


            if c>2:
                return False

        if len(ix)>0:
            aux=a[ix[0]]
            a[ix[0]]=a[ix[1]]
            a[ix[1]]=aux
            if a==b:
                return True
            else:
                return False
        return True
