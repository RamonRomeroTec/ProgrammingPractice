from collections import Counter
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        d={}
        for l in licensePlate:
            if l.isalpha():
                l=l.lower()
                if l in d:
                    d[l]+=1
                else:
                    d[l]=1
        ans=""               
        minlen=float('inf')
        words = [ w for w in sorted(words, key=lambda x:len(x)) if len(w) >= len(d) ]
        for word in words:
            l=len(word)
            c=Counter(word)
            status=True
            for k,v in d.items():
                if k not in c:
                    status=False
                    break
                else:
                    if c[k]<v:
                        status=False
                        break
            if status:
                return word
            
                    
        