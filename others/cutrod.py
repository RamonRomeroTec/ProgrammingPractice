def cutrod(prices, longitud):
	q=0
	
	if longitud==0:
		return 0

	for i in range(1,longitud+1):
		print(q)
		q=max(q, prices[i]+ cutrod(prices, longitud-i))

	return q


if __name__ == '__main__':
	arr=[0,2,5,6,9,10,11]
	
	print(cutrod(arr, 3))
