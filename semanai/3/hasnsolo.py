if __name__ == '__main__':
    n_troopers, xgun, ygun = [int(x) for x in input().split()]
    troopers = []
    for x in range(n_troopers):
    	xtroop, ytroop = [int(x) for x in input().split()]
    	try:
    		diff = ((ytroop - ygun)/(xtroop - xgun))
    	except:
    		diff = 9999999
    	troopers.append(diff)

    print(len(set(troopers)))
