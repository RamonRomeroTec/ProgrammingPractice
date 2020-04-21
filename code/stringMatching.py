class Solution:
    def stringMatching(self, words):
        if len(words)<=1:
            return []
        i=0
        s=set()
        while i<len(words)-1:
            j=i+1
            while j<len(words):
                if words[i] in words[j]:
                    s.add(words[i])
                elif words[j] in words[i]:
                    s.add(words[j])
                j+=1
            i+=1
                    
        return list(s)

            
        