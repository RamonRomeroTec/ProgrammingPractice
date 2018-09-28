


def fun(n,m):
    moves = 0
    if n > m :
    	print(abs(n - m))
    	exit()
    while n != m:
    	if m%2 == 0 and m > n:
    		m /= 2
    		moves += 1
    	else:
    		m += 1
    		moves += 1
    return(moves)


if __name__ == '__main__':
    n, t= map(int, str(input()).split(" "))
    print(fun(n,t))
