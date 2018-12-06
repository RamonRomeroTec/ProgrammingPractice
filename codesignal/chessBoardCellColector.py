def chessBoardCellColor(cell1, cell2):
    p=list(cell1)
    q=list(cell2)

    d={}

    hor=['A', 'B', 'C','D','E', 'F', 'G','H']
    for i in range(0,len(hor),2):
        d[hor[i]]=0
    for i in range(1,len(hor),2):
        d[hor[i]]=1


    c1=-1
    c2=-1



    if d[p[0]]==0:
        if int(p[1])%2==1:
            c1=0
        else:
            c1=1

    else:
        if int(p[1])%2==1:
            c1=1
        else:
            c1=0


    if d[q[0]]==0:
        if int(q[1])%2==1:
            c2=0
        else:
            c2=1

    else:
        if int(q[1])%2==1:
            c2=1
        else:
            c2=0

    print(c1,c2)

    return c1==c2
