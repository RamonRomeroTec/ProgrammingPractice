class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi=0
        rel=0
        for i in gain:
            rel+=i
            maxi = max(rel, maxi)
        return maxi
        