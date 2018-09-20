#inicializar arreglo
#iteracion en arreglo uno no cuenta...

def memoizedCutRod(prices, longitude):
    memo=[]
    for i in range(0, longitude+1):
        memo.append(-1)
    
    return memoizedCutRodAux(prices, longitude, memo)
    
def memoizedCutRodAux(prices, longitude, memo):
    if memo[longitude]>=0:
        return memo[longitude]
    if longitude==0:
        q=0
    else:
        
        q=-1
        for i in range(1, longitude+1):
            q=max(q, prices[i]+ memoizedCutRodAux(prices, longitude-i, memo))
            
    memo[longitude]=q
    print(memo)
    
    return q
    

if __name__ == '__main__':
	arr=[0,2,5,6,9,10,11]
	print(memoizedCutRod(arr, 3))
