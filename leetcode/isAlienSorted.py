class Solution(object):
    def isAlienSorted(self, words, order):
        d={}
        for i,v in enumerate(order):
            d[v]=i
        i=0
        j=1
        while j<len(words):
            word1 = words[i]
            word2 = words[j]
            if d[word1[0]] < d[word2[0]]:
                pass
            elif d[word1[0]] > d[word2[0]]:
                return False
            else:
                x=0
                while x<len(word1) and x<len(word2):
                    if d[word1[x]] <= d[word2[x]]:
                        x+=1
                    elif d[word1[x]] > d[word2[x]]:
                        return False
                if len(word1)>len(word2):
                    return False
            j+=1
            i+=1
        return True
                
                    
            
        