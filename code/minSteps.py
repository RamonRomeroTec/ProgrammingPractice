from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        a1=Counter(s)
        a2=Counter(t)
        return sum((a2-a1).values())