def cutrod(prices, longitud):
	q=0
	if longitud==0:
		return 0

	for i in range(1,longitud):
		print(q)
		q=max(q, prices[i]+ cutrod(prices, longitud-i))

	return q


if __name__ == '__main__':
	arr=[0,1,5,8,9,10,11]
	cutrod(arr, 5)
