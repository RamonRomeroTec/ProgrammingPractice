def addBorder(picture):
    h=len(picture)+2
    w=len(picture[0])+2
    f=[]
    u="*"*w
    f.append(u)
    for i in range(len(picture)):
        picture[i]="*"+picture[i]+"*"
        f.append(picture[i])
    f.append(u)
    return f
