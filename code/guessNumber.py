class Solution(object):
    def guessNumber(self, n):
        low=1
        ev=guess(n)
        high=n
        if ev == 0:
            return n
        elif guess(low)==0:
            return low
        elif guess(n)<0:
            high=n
        else:
            while guess(high)>1:
                high=n*10
            low=high//10  
        while True:
            mid=low+((high-low)//2)
            sev=guess(mid)
            if sev==0:
                return mid
            elif sev==1:
                low=mid
            elif sev==-1:
                high=mid

                    
    
        
        
        
        
        
        