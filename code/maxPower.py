class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 1:
            return 1
        i = 0
        maxi = 0
        while i < len(s) - 1:
            j = i + 1
            c = 1
            while j < len(s) and s[i] == s[j]:
                j += 1
                c += 1
            maxi = max(c, maxi)
            i = j
        return maxi

