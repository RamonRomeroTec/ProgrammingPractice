from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m=Counter(magazine)
        r=Counter(ransomNote)
        return((r&m)==r)
        
        