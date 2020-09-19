class Solution:
    def countOdds(self, low: int, high: int) -> int:
        base=(high-low)//2
        if high%2==0 and low%2==0:
            return base
        else:
            return base+1
        
        