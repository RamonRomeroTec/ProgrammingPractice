class Solution(object):
    def finalPrices(self, prices):
        if len(prices)==1:
            return prices
        
        i=0
        while i< len(prices)-1:
            j=i+1
            while j < len(prices):
                if prices[i] >= prices[j]:
                    prices[i]-=prices[j]
                    break
                j+=1
            i+=1
                
                    
        return prices
        