def cutrod(prices, longitud):
	if longitud==0:
		return 0
	for i in range(0,longitud):
		print(q)
		q=max(q, prices[i]+ cutrod(prices, longitud-i))

	return q


if __name__ == '__main__':
	arr=[1,5,8,9,10,11]
	cutrod(arr, 5)
