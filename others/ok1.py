def calc(arr):

    b=sorted(set(arr))
    if len(b)==2:
        return abs(b[0]-b[1])
    x=b[-1]
    y=b[-2]
    u1=arr.index(y)
    u2=arr.index(x)
    #print(b,x,y,"-",u1,u2)


    r=0
    for i in range(min(u1, u2)+1, max(u1, u2)):
        r=r+min(x,y)-arr[i]
        #print(arr[i])


    return r

print(calc([8,5,2,7]))
a=[1,2,3,4,5,6,7]
print(a[3:])
print(a[:3])
