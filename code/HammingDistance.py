class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return format(x^y, 'b').count('1')
        
        