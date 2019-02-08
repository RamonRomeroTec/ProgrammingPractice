

'''
Freddy has a very big elephant, Simon. He is flying to Gabon in order to let
Simon meet his brothers and sisters, however he is very big, which means he
doesn't really fit in the plane. In order to make him fit Freddy needs to minify
his size.


In order to do that he has N minifying guns (they make stuff smaller).
However, each gun can only be used once.

Each gun has a cost of using it c*w,
where c is unique per gun and w is the weight of the thing they are minifying.

Additionally each gun has a minify ratio called r,
which means that the size and weight get reduced to r percent of the original value.


Given that the initial weight of Simon is W and he is going to get shrunk b
each of the N guns exactly once, what is the minimum cost of doing this?


'''
if __name__ == '__main__':
    n, w= map(int, input().split(' '))
    cost=0
    magia=[]
    for i in range(n):
        c, r= map(float, input().split(' '))
        a=c*r
        magia.append([c,r,a])
    magia=sorted(magia, key= lambda t : t[2])
    for i in magia:
        cost=cost+i[0]*w
        w=w*i[1]
    print(cost)
