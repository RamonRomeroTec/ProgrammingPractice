class Solution:
    def reverseBits(self, n: int) -> int:
        x=format(n,'b')[::-1]
        return int((x+("0"*(32-len(x)))), 2)
        