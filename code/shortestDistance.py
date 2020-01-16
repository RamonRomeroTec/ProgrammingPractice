class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        
        d={}
        for index, word in enumerate(words):
            if word==word1 or word==word2:
                if word in d:
                    d[word].append(index)
                else:
                    d[word]=[index]
        mini=float('+inf')
        for i in d[word1]:
            for j in d[word2]:
                mini=min(mini,abs(i-j))
        return mini
    
    