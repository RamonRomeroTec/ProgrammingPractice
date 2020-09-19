class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        s=0
        while numBottles>=numExchange:
            xchange=(numBottles//numExchange)
            s+=xchange*numExchange
            numBottles=(numBottles%numExchange)+xchange
        s+=numBottles
        return s
        