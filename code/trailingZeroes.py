class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n>=5:
            aux=n//5
            count += aux
            n = aux
        return count
